# JSON Policy Document Validator

This Python script (`main.py`) provides a utility to validate JSON files containing AWS IAM policy documents. It checks if the required fields are present and verifies the resource argument in the policy.

## Prerequisites

- Python 3.x installed on your system.

## Usage

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/patryk03/remitly
    ```

2. Run the script with the desired JSON file as an argument (json files should be located in the __data__ project directory):

    ```bash
    python main.py one_astericks_correct.json
    ```

## Running tests

1. Run the following command:

    ```bash
    python -m unittest tests.test_main
    ```

This command will execute the unit tests defined in 'test_main.py' and display the results.

## Test Cases

The provided unit tests cover various scenarios including:

- Valid JSON files with different resource arguments.
- Handling of missing files.
- Handling of empty JSON files.
- Handling of invalid JSON format.
- Handling of JSON files with missing required fields.