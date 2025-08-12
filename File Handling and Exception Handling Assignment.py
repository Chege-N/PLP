def modify_and_write_file(input_filename, output_filename):
    try:
        # Read the input file
        with open(input_filename, 'r') as input_file:
            content = input_file.read()

        # Modify the content (e.g., convert to uppercase and add a prefix)
        modified_content = "Modified Content:\n" + content.upper()

        # Write to a new output file
        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)

        print(f"Successfully read '{input_filename}' and wrote modified content to '{output_filename}'")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied when accessing '{input_filename}' or writing to '{output_filename}'.")
    except IOError as e:
        print(f"Error: An I/O error occurred: {e}")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")


# Prompt user for input filename
input_filename = input("Enter the input filename (e.g., input.txt): ")
output_filename = "modified_" + input_filename

# Call the function to process the file
modify_and_write_file(input_filename, output_filename)