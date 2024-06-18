import subprocess
import os
import shutil

def run_bash_command(command, cwd=None):
    try:
        result = subprocess.run(command, cwd=cwd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(result.stdout.decode())
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e.stderr.decode()}")
        raise

def build_cpp_project(project_path):
    # Expand the ~ to the full path
    project_path = os.path.expanduser(project_path)

    if not os.path.isdir(project_path):
        raise FileNotFoundError(f"The directory '{project_path}' does not exist.")

    commands = [
        'autoreconf -i',            # Generate configuration scripts, if necessary
        './configure',              # Configure the project
        'make clean',               # Clean the build
        'make',                     # Build the project
    ]

    for command in commands:
        print(f"Running: {command}")
        run_bash_command(command, cwd=project_path)
    
    # Move compiled C/C++ program to home folder
    home_dir = os.path.expanduser("~")
    compiled_program_path = os.path.join(project_path, "shc.1")
    destination_path = os.path.join(home_dir, "shc.1")
    if (os.path.isfile(compiled_program_path)):
        shutil.copy(compiled_program_path, destination_path)
        print(f"Move {compiled_program_path} to {destination_path}")
    else:
        print(f"{compiled_program_path} is not found")

if __name__ == "__main__":
    project_path = os.path.expanduser("~/study_workspace/temp/shc-4.0.3/")
    build_cpp_project(project_path)

# python3 -m compileall test.py
# cd ./__pycache__
# chmod +x test.cpython-310.pyc
# ./test.cpython-310.pyc