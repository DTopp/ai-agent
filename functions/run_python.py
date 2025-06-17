import os
import subprocess

def run_python_file(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(abs_working_dir, file_path))
    if abs_file_path.startswith(abs_working_dir + os.sep):
        if os.path.isfile(abs_file_path):
            if abs_file_path[-3:].lower() == '.py':
                try:
                    result = subprocess.run(['python3', abs_file_path], cwd=abs_working_dir, capture_output=True, text=True, timeout=30)
                    formatted_result = ''
                    formatted_result += f'STDOUT: {result.stdout}\n'
                    formatted_result += f'STDERR: {result.stderr}\n'
                    if result.returncode != 0:
                        formatted_result += f'Process exited with code {result.returncode}'
                    if result.stderr == '' and result.stdout == '':
                        return 'No output produced'
                    return formatted_result
                except Exception as e:
                    return f"Error: executing Python file: {e}"
            else:
                return f'Error: "{file_path}" is not a Python file.'
        else:
            return f'Error: File "{file_path}" not found.'
    else:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'