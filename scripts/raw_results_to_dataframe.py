#! python3

import pandas as pd
import json
import os
from functools import reduce

def raw_results_to_dataframe(infile_path, outdir_path,
	per_subject=False):
	"""Takes the path to a raw_results files from an Ibexfarm
	experiment and the path to the directory where the output file(s)
	will be written.
	Writes a CSV file with all the data from the raw_results file.
	If per_subject is set to True it also writes a separate CSV file
	for each subject.
	"""

	# Open raw results file
	with open(infile_path, 'r', encoding='utf8') as infile:
		file_content = infile.readlines()

	subjects = {}
	counter = 1
	# Iterate lines in the file searchig for JSON lines
	for line in file_content:
		# Check if the line is a line containing data in JSON format
		if line.startswith('['):
			# Create an entry in the subjects dictionary for the
			# current subject and add column names and row data
			# to it
			subjects['subject ' + str(counter)] = {}
			curr_subject = subjects['subject ' + str(counter)]
			curr_subject['cols'] = json.loads(line)[2]
			curr_subject['rows'] = json.loads(line)[3]
			curr_subject['id'] = counter
			counter += 1

	# Create a dataframe for each subject and add them to a dictionary
	subject_dfs = {}
	for subject_key, subject in subjects.items():
		# Make a dictionary for each data row and add them to a list
		list_for_dataframe = []
		for row in subject['rows']:
			row_dict = {}
			for col, value in row:
				# Store each value in the correct column
				row_dict[subject['cols'][col]] = value
			list_for_dataframe.append(row_dict)
		# Create the dataframe
		subject_dfs[subject_key] = pd.DataFrame(list_for_dataframe)
		# Add the 'Subject ID' column to the dataframe
		subject_dfs[subject_key]['Subject ID'] = subject['id']

	# If the optional argument 'per_subject' is set to True, create a
	# different file for each subject
	if per_subject == True:
		for dataframe_name, dataframe in subject_dfs.items():
			dataframe.to_csv(
				os.path.join(outdir_path, dataframe_name + '.csv'),
				encoding='utf8'
				)

	# Create a dataframe with the data from all subjects
	all_subjects_df = reduce(
		lambda df1, df2: pd.concat([df1, df2]), subject_dfs.values()
		)
	# Write CSV file with the dataframe with the data from all subjects
	all_subjects_df.to_csv(
		os.path.join(outdir_path, 'all_subjects.csv'),
		encoding='utf8'
		)
