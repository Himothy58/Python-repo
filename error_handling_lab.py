def error_handling_lab():
    try:
        # Ask the user for a filename
        filename = input("Enter the filename: ")

        # Open and read the file
        with open(filename, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)

    except FileNotFoundError:
        print(f"Error: File '{filename}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied to access '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

error_handling_lab()
