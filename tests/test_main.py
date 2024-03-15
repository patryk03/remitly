import unittest
from main import verify

class TestVerifyFunction(unittest.TestCase):
    def test_verify_with_one_astericks_correct(self):
        result = verify("data/one_astericks_correct.json")
        self.assertFalse(result)

    def test_verify_with_more_astericks_correct(self):
        result = verify("data/more_astericks_correct.json")
        self.assertTrue(result)

    def test_verify_with_different_values_correct(self):
        result = verify("data/more_astericks_correct.json")
        self.assertTrue(result)

class TestVerifyFunctionWithErrors(unittest.TestCase):
    def test_verify_missing_file(self):
        file_name = "data/missing_file.json"
        try:
            verify(file_name)
        except FileNotFoundError as e:
            self.assertEqual(str(e), f'File not found: {file_name}')
            print("\nCaught error:", e)
            
    def test_verify_with_empty_file(self):
        try:
            verify("data/empty_file.json")
        except ValueError as e:
            self.assertEqual(str(e), "Empty file")
            print("\nCaught error:", e)

    def test_verify_with_invalid_json_format(self):
        file_name = "data/invalid_json_format.json"
        try:
            verify(file_name)
        except ValueError as e:
            self.assertEqual(str(e), f'Invalid JSON format in file: {file_name}')
            print("\nCaught error:", e)

    def test_verify_with_missing_fields(self):
        try:
            verify("data/missing_fields.json")
        except ValueError as e:
            self.assertEqual(str(e), "Missing required fields in JSON file")
            print("\nCaught error:", e)
    

if __name__ == '__main__':
    unittest.main()