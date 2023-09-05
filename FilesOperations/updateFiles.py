def update_file_at_end(file_name, content_to_append):
    try:
        with open(file_name, "a", encoding="utf-8") as file:
            file.write(content_to_append)
            print(f"Appended to {file_name} at the end.")
    except Exception as error:
        print(f"An error occurred: {error}")

def update_file_at_beginning(file_name, content_to_prepend):
    try:
        with open(file_name, "r+", encoding="utf-8") as file:
            content = file.read()
            content = content_to_prepend + "\n" + content
            file.seek(0)
            file.write(content)
            print(f"Prepended to {file_name} at the beginning.")
    except Exception as error:
        print(f"An error occurred: {error}")

def update_file_at_middle(file_name, content_to_insert, line_number):
    try:
        with open(file_name, "r+", encoding="utf-8") as file:
            lines = file.readlines()
            lines.insert(line_number - 1, content_to_insert + "\n")
            file.seek(0)
            file.writelines(lines)
            print(f"Inserted into {file_name} at line {line_number}.")
    except Exception as error:
        print(f"An error occurred: {error}")

def read_file(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            print(file.read())
    except Exception as error:
        print(f"An error occurred: {error}")

# Example usage:
update_file_at_end("newfile.txt", "Dries Mertens\n")
update_file_at_beginning("newfile.txt", "Hi <3")
update_file_at_middle("newfile.txt", "Lucas Torreira", 2)
read_file("newfile.txt")
