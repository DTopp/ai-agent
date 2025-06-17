import os

def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(abs_working_dir, file_path))
    
    if abs_file_path.startswith(abs_working_dir + os.sep):
        try:
            os.makedirs(os.path.dirname(abs_file_path), exist_ok=True)
        except:
            return f'Error: Cannot create {os.path.dirname(abs_file_path)}'
        try:
            with open(abs_file_path, "w") as f:
                f.write(content)
                return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        except:
                return f'Error: Cannot write to "{abs_file_path}"'
    else:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    