#! python3

import os


__spanish_html_escape_map__ = {
	"Á": "&Aacute;",
	"á": "&aacute;",
	"É": "&Eacute;",
	"é": "&eacute;",
	"Í": "&Iacute;",
	"í": "&iacute;",
	"Ñ": "&Ntilde;",
	"ñ": "&ntilde;",
	"Ó": "&Oacute;",
	"ó": "&oacute;",
	"Ú": "&Uacute;",
	"ú": "&uacute;",
	"Ü": "&Uuml;",
	"ü": "&uuml;",
	"«": "&laquo;",
	"»": "&raquo;",
	"¿": "&iquest;",
	"¡": "&iexcl;",
}

__spanish_unicode_escape_map__ = {
	"Á": "\\u00C1",
	"á": "\\u00E1",
	"É": "\\u00C9",
	"é": "\\u00E9",
	"Í": "\\u00CD",
	"í": "\\u00ED",
	"Ñ": "\\u00D1",
	"ñ": "\\u00F1",
	"Ó": "\\u00D3",
	"ó": "\\u00F3",
	"Ú": "\\u00DA",
	"ú": "\\u00FA",
	"Ü": "\\u00DC",
	"ü": "\\u00FC",
	"«": "\\u00AB",
	"»": "\\u00BB",
	"¿": "\\u00BF",
	"¡": "\\u00A1"
}


def escape_characters(infile_path, outfile_path,
	escape_map=__spanish_unicode_escape_map__
):
	"""Takes the path to the original file, the path for the
	output file (including the file extension) and a dictionary
	mapping from characters to escape characters (defaults to
	__spanish_unicode_escape_map__).
	Reads the input file, escapes its characters and writes the
	result in the output file path.
	NOTE: If you are trying to escape the characters for a HTML file
	that will be imported via 'include' in the 'html' option of a
	Message or Form Ibexfarm controller you should use
	__spanish_html_escape_map__ in escape_map.
	""" 

	# Read input file
	with open(infile_path, 'r', encoding='utf8') as infile:
		result = infile.read()
	# Replace characters with escape characters
	for char, html_entity in escape_map.items():
		result = result.replace(char, html_entity)
	# Write output file
	with open(outfile_path, 'w', encoding='utf8') as outfile:
		outfile.write(result)
