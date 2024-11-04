def split_file(input_file, max_lines=400):
    try:
        # Open the input file in read mode
        with open(input_file, 'r') as infile:
            lines = infile.readlines()

        # Split lines into chunks of max_lines
        total_parts = (len(lines) + max_lines - 1) // max_lines
        base_name = input_file.rsplit('.', 1)[0]

        for i in range(total_parts):
            part_lines = lines[i * max_lines : (i + 1) * max_lines]
            output_file = f"{base_name}_part{i + 1}.txt"

            # Write each part to a new file
            with open(output_file, 'w') as outfile:
                outfile.writelines(part_lines)

            print(f"Part {i + 1} written to {output_file}")
        
        print("File splitting complete.")
    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Prompt the user for input filename
input_file = input("Enter the name of the input text file (with .txt extension): ")

# Call the function to split the file
split_file(input_file)
