import os
from google.genai import types

def get_files_info(working_directory, directory=None):
    
    working_directory = os.path.abspath(working_directory)
    if directory is None:
        directory = working_directory
    else:
        directory = os.path.abspath(os.path.join(working_directory, directory))
    if directory == working_directory or directory.startswith(working_directory + os.sep):
        pass
    else:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if os.path.isdir(directory) is False:
        return f'Error: "{directory}" is not a directory'
    else:
        directory_info = ''
        try:
            items = os.listdir(directory)
        except:
            return f'Error: Cannot access "{directory}"'
        for item in items:
            try:
                file_size = os.path.getsize(os.path.join(directory, item))
                is_dir = os.path.isdir(os.path.join(directory, item))
            except:
                directory_info += f'- {item}: Error accessing file\n'
                continue
            directory_info += f'- {item}: file_size={file_size} bytes, is_dir={is_dir}\n'
        return directory_info
    
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

    
