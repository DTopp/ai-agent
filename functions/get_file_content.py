import os

def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(abs_working_dir, file_path))
    
    if abs_file_path.startswith(abs_working_dir + os.sep):
        if os.path.isfile(abs_file_path) is False:
            return f'Error: File not found or is not a regular file: "{file_path}"'
        else:
            MAX_CHARS = 10000
            try:
                with open(abs_file_path, "r") as f:
                    file_content_string = f.read(MAX_CHARS)
                    more_chars = f.read(1)
                    if more_chars != '':
                        file_content_string += '[...File "{file_path}" truncated at 10000 characters]'
                    return file_content_string
            except:
                return f'Error: Cannot access "{abs_file_path}"'
    else:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    