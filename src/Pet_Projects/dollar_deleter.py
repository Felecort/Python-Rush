
output_file_path = r"D:\Projects\PythonProjects\Python-rush\src\tmp_files\liza_text_out.txt"
path_to_file = r"D:\Projects\PythonProjects\Python-rush\src\tmp_files\liza_text.txt"

with open(path_to_file, "r", encoding="utf-8") as data:
    text = data.read()
    output_text = []
    append_output_text = output_text.append
    for char in text:
        if char != "$":
            append_output_text(char)
    output_text = "".join(output_text)


with open(output_file_path, "w", encoding="utf-8") as out_file:
    out_file.write(output_text)
