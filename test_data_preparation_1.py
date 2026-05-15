import unittest
import time
import sys
from data_preparation import (
    load_data,
    preprocess_data,
    split_data,
    validate_data
)


class TestDataPreparation(unittest.TestCase):
    """Unit tests for data_preparation.py covering positive, negative,
    boundary, and non-functional scenarios."""

    def test_load_data_positive(self):
        """Test loading data from a valid file path."""
        try:
            data = load_data("tests/sample_data.csv")
            self.assertIsNotNone(data)
            self.assertGreater(len(data), 0)
        except Exception as e:
            self.fail(f"Unexpected exception occurred: {e}")

    def test_load_data_negative(self):
        """Test loading data from an invalid file path."""
        try:
            with self.assertRaises(FileNotFoundError):
                load_data("invalid/path/to/data.csv")
        except Exception as e:
            self.fail(f"Unexpected exception occurred: {e}")

    def test_load_data_boundary_empty_file(self):
        """Test loading data from an empty file."""
        try:
            data = load_data("tests/empty_data.csv")
            self.assertEqual(len(data), 0)
        except Exception as e:
            self.fail(f"Unexpected exception occurred: {e}")

    def test_preprocess_data_positive(self):
        """Test preprocessing valid data."""
        try:
            raw_data = load_data("tests/sample_data.csv")
            processed_data = preprocess_data(raw_data)
            self.assertIsNotNone(processed_data)
            self.assertGreater(len(processed_data), 0)
        except Exception as e:
            self.fail(f"Unexpected exception occurred: {e}")

    def test_preprocess_data_negative(self):
        """Test preprocessing with invalid data format."""
        try:
            with self.assertRaises(ValueError):
                preprocess_data("invalid_data_format")
        except Exception as e:
            self.fail(f"Unexpected exception occurred: {e}")

    def test_split_data_positive(self):
        """Test splitting valid processed data."""
        try:
            raw_data = load_data("tests/sample_data.csv")
            processed_data = preprocess_data(raw_data)
            train, test = split_data(processed_data, 0.8)
            self.assertGreater(len(train), 0)
            self.assertGreater(len(test), 0)
        except Exception as e:
            self.fail(f"Unexpected exception occurred: {e}")

    def test_split_data_boundary_ratio(self):
        """Test splitting data with boundary ratio values."""
        try:
            raw_data = load_data("tests/sample_data.csv")
            processed_data = preprocess_data(raw_data)
            train, test = split_data(processed_data, 1.0)
            self.assertGreater(len(train), 0)
            self.assertEqual(len(test), 0)
        except Exception as e:
            self.fail(f"Unexpected exception occurred: {e}")

    def test_validate_data_positive(self):
        """Test validating correct data."""
        try:
            raw_data = load_data("tests/sample_data.csv")
            processed_data = preprocess_data(raw_data)
            is_valid = validate_data(processed_data)
            self.assertTrue(is_valid)
        except Exception as e:
            self.fail(f"Unexpected exception occurred: {e}")

    def test_validate_data_negative(self):
        """Test validating incorrect data."""
        try:
            with self.assertRaises(ValueError):
                validate_data("invalid_data")
        except Exception as e:
            self.fail(f"Unexpected exception occurred: {e}")

    def test_load_data_performance(self):
        """Performance test for loading data."""
        try:
            start_time = time.time()
            load_data("tests/sample_data.csv")
            duration = time.time() - start_time
            self.assertLess(duration, 2.0)
        except Exception as e:
            self.fail(f"Unexpected exception occurred: {e}")

    def test_preprocess_data_security(self):
        """Security test to ensure preprocessing does not execute code."""
        try:
            malicious_data = ["__import__('os').system('rm -rf /')"]
            with self.assertRaises(Exception):
                preprocess_data(malicious_data)
        except Exception as e:
            self.fail(f"Unexpected exception occurred: {e}")

    def test_usability_split_data(self):
        """Usability test for split_data with user-friendly ratio."""
        try:
            raw_data = load_data("tests/sample_data.csv")
            processed_data = preprocess_data(raw_data)
            train, test = split_data(processed_data, 0.75)
            self.assertAlmostEqual(len(train) / len(processed_data), 0.75, places=2)
        except Exception as e:
            self.fail(f"Unexpected exception occurred: {e}")


if __name__ == "__main__":
    unittest.main()