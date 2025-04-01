def file_read_write():
    try:
        # Read the input file
        with open('input.txt', 'r') as infile:
            content = infile.read()

        # Modify the content (e.g., convert to uppercase)
        modified_content = content.upper()

        # Write the modified content to a new file
        with open('output.txt', 'w') as outfile:
            outfile.write(modified_content)

        print("File has been successfully modified and written to 'output.txt'!")
    except FileNotFoundError:
        print("Error: 'input.txt' not found. Please ensure the file exists.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

file_read_write()
