from pathlib import Path


#moving around inside a file
workspace = Path("workspace_files")
file_path = workspace / "story.txt"

story = """Once upon a time, there was a lady who was curious and inquisitive,
she is just trying to find out how things work behind the curtains.
Eventually, she was oppurtuned to get into the programming language world.
She began her journey in python and spends her evry day writing codes.
one day, she discovered file handling.
This opened her to the world of greater oppurtunities.
The end."""


with open(file_path, "w", encoding="utf-8") as u:
    u.write(story)

print("Created the story file")

#moving around
with open(file_path, "r", encoding="utf-8") as u:
    print("\nFile Positioning Demo:")

    first_part = u.read(20)
    print(f"First 20 characters: '{first_part}'")


    current_position = u.tell()
    print("Current position in file:", current_position)


    #jump to beginning
    u.seek(0)
    print(f"After seeking beginning: position{u.tell()}")


    #go to position 50 and read
    u.seek(50)
    rest_of_the_line = u.readline()
    print(f"Reading from position 50: '{rest_of_the_line.strip()}")

    #go to beginning and read from there
    u.seek(0)
    read_from_beginning = u.readline()
    print(f"First line: {read_from_beginning.strip()}")


