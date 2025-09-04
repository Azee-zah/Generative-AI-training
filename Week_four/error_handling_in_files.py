# to handle error while working with files
from pathlib import Path


workspace = Path("workspace_files")
workspace.mkdir(exist_ok=True)

try:
    with open(workspace / "missing_file.txt", "r") as f:
        content = f.read()
        print("File content:", content)
except FileNotFoundError:
    print("Oops! That file does not exist yet.")
    print("Let us create it!")


    with open(workspace / "missing_file.txt", "w") as f:
        f.write("Now I exist!")
    print("File created successfully!")


# to check if a file exist 
workspace = Path("workspace_files")
file_path = workspace / "notes.txt"

if file_path.exists:
    print(f"Found the file:", {file_path.name})  # to check if a file existed

    file_size = file_path.stat().st_size        #to get extra info about the file
    print(f"File Size: {file_size} bytes")

    with open(file_path, "r", encoding="utf-8") as f:   # read and show content of file
        content = f.read()
        print("Content preview:", content[:50],"...")

else:
    print(f"File {file_path.name} does not exist!")
    print("You might have to create it")
