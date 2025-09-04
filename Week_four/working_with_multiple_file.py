# to read a file and write another at the same time
from pathlib import Path


workspace = Path("workspace_files")
input_file = workspace / "original.txt"
output_file = workspace / "processed.txt"

#create input file
sample_text = '''hello world
python programming
file handling tutorial
learning is fun'''

with open(input_file, "w", encoding="utf-8") as f:
    f.write(sample_text)

print("Created input file")


with open(input_file, "r", encoding="utf-8") as infile, \
open(output_file, "w", encoding="utf-8") as outfile:
    
    line_number = 1
    for line in infile:
        processed_line = f"Line {line_number}: {line.strip().upper()}\n"  #processing
        outfile.write(processed_line)
        line_number += 1

print("File processing complete")

print("\nOriginal file:")
with open(output_file, "r", encoding="utf-8") as f:
    print(f.read())


print("\nProcessed file:")
with open(output_file, "r", encoding="utf-8") as f:
    print(f.read())



