

# Writing to the file
with open("example.txt", "w") as file:
    file.write("Hello, this is a test file!\n")
    file.write("This is the second line of the file.\n")

# Define the function to handle errors and read the file
def open_file_and_handle_errors():
    filename = input("Please enter the filename: ")

    try:
        # Try to open the file for reading
        with open(filename, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except IOError:
        print(f"Error: An unexpected error occurred while trying to read '{filename}'.")

# Call the function after creating the file
open_file_and_handle_errors()
