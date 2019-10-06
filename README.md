# Ibexfarm Scripts

Useful scripts when working with Ibexfarm.

## `escape_characters(infile_path, outfile_path, escape_map=__spanish_unicode_escape_map__)`

Takes the path to the original file, the path for the output file (including the file extension) and a dictionary mapping from characters to escape characters (defaults to `__spanish_unicode_escape_map__`).

Reads the input file, escapes its characters and writes the result in the output file path.

NOTE: If you are trying to escape the characters for a HTML file that will be imported via `'include'` in the `'html'` option of a `Message` or `Form` Ibexfarm controller you should use `__spanish_html_escape_map__` in `escape_map`.

## `raw_results_to_dataframe(infile_path, outdir_path, per_subject=False)`

Takes the path to a `raw_results` files from an Ibexfarm experiment and the path to the directory where the output file(s) will be written.

Writes a CSV file with all the data from the `raw_results` file.
If `per_subject` is set to `True` it also writes a separate CSV file for each subject.
