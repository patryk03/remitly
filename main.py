import json
import sys

# Read the data from the file
def read(file_name):
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
            # Check if file is empty
            if not data:
                raise ValueError("Empty file")
            # Check if the required fields are present
            if 'PolicyDocument' not in data or 'Statement' not in data['PolicyDocument']:
                raise ValueError("Missing required fields in JSON file")
            # Return the resource argument from the data
            return data['PolicyDocument']['Statement'][0]['Resource']
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_name}")
    except json.decoder.JSONDecodeError:
        raise ValueError(f"Invalid JSON format in file: {file_name}")

# Verify the data
def verify(file_name):
    # Extract the resource argument from the data
    resource_arg = read(file_name)
    # Check if the resource argument is not equal to '*'
    return resource_arg != '*'

if __name__ == '__main__':
    # Check if the file name is provided and file is located in the data directory
    if len(sys.argv) != 2:
        print("Usage: python main.py file.json (located in data directory)")
        sys.exit(1)

    # Get the file name from the command line argument and verify the file
    json_file = sys.argv[1]
    try:
        result = verify(f'data/{json_file}')
        if result:
            print("Resource argument isn't equal to: *")
        else:
            print("Resource argument is equal to: *")
    except (FileNotFoundError, ValueError) as e:
        print("Error:", e)
        sys.exit(1)