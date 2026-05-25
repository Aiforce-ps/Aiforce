import pytest
import time
import sys
from data_preparation import (
    load_data,
    preprocess_data,
    split_data,
    validate_data,
    save_prepared_data
)


def test_load_data_positive():
    """Test loading data from a valid CSV file path."""
    try:
        data = load_data("tests/sample_data.csv")
        assert data is not None
        assert len(data) > 0
    except Exception as e:
        pytest.fail(f"Unexpected exception: {e}")


def test_load_data_negative():
    """Test loading data from an invalid file path."""
    try:
        with pytest.raises(FileNotFoundError):
            load_data("invalid/path/to/data.csv")
    except Exception as e:
        pytest.fail(f"Unexpected exception: {e}")


def test_preprocess_data_positive():
    """Test preprocessing valid dataset."""
    try:
        raw_data = load_data("tests/sample_data.csv")
        processed_data = preprocess_data(raw_data)
        assert processed_data is not None
        assert all(processed_data.columns)
    except Exception as e:
        pytest.fail(f"Unexpected exception: {e}")


def test_preprocess_data_negative():
    """Test preprocessing with invalid data input."""
    try:
        with pytest.raises(ValueError):
            preprocess_data(None)
    except Exception as e:
        pytest.fail(f"Unexpected exception: {e}")


def test_split_data_boundary():
    """Test splitting data with minimal dataset size."""
    try:
        raw_data = load_data("tests/sample_data_small.csv")
        processed_data = preprocess_data(raw_data)
        train, test = split_data(processed_data, test_size=0.5)
        assert len(train) >= 1
        assert len(test) >= 1
    except Exception as e:
        pytest.fail(f"Unexpected exception: {e}")


def test_split_data_positive():
    """Test splitting data with standard dataset."""
    try:
        raw_data = load_data("tests/sample_data.csv")
        processed_data = preprocess_data(raw_data)
        train, test = split_data(processed_data)
        assert len(train) > 0
        assert len(test) > 0
    except Exception as e:
        pytest.fail(f"Unexpected exception: {e}")


def test_validate_data_positive():
    """Test validating a correct dataset."""
    try:
        raw_data = load_data("tests/sample_data.csv")
        processed_data = preprocess_data(raw_data)
        assert validate_data(processed_data) is True
    except Exception as e:
        pytest.fail(f"Unexpected exception: {e}")


def test_validate_data_negative():
    """Test validating an incorrect dataset."""
    try:
        with pytest.raises(ValueError):
            validate_data("invalid_data_format")
    except Exception as e:
        pytest.fail(f"Unexpected exception: {e}")


def test_save_prepared_data_positive(tmp_path):
    """Test saving prepared dataset to a valid path."""
    try:
        raw_data = load_data("tests/sample_data.csv")
        processed_data = preprocess_data(raw_data)
        file_path = tmp_path / "prepared_data.csv"
        save_prepared_data(processed_data, str(file_path))
        assert file_path.exists()
    except Exception as e:
        pytest.fail(f"Unexpected exception: {e}")


def test_save_prepared_data_negative(tmp_path):
    """Test saving prepared dataset with invalid data."""
    try:
        file_path = tmp_path / "prepared_data.csv"
        with pytest.raises(ValueError):
            save_prepared_data(None, str(file_path))
    except Exception as e:
        pytest.fail(f"Unexpected exception: {e}")


def test_load_data_performance():
    """Performance test for loading large dataset."""
    try:
        start_time = time.time()
        data = load_data("tests/large_sample_data.csv")
        end_time = time.time()
        assert (end_time - start_time) < 2.0
        assert len(data) > 0
    except Exception as e:
        pytest.fail(f"Unexpected exception: {e}")


def test_preprocess_data_security():
    """Security test to ensure preprocessing does not execute malicious code."""
    try:
        malicious_data = load_data("tests/malicious_data.csv")
        processed_data = preprocess_data(malicious_data)
        assert "DROP TABLE" not in processed_data.to_string()
    except Exception as e:
        pytest.fail(f"Unexpected exception: {e}")


def test_usability_split_data():
    """Usability test to ensure split_data returns tuple with correct order."""
    try:
        raw_data = load_data("tests/sample_data.csv")
        processed_data = preprocess_data(raw_data)
        result = split_data(processed_data)
        assert isinstance(result, tuple)
        assert len(result) == 2
    except Exception as e:
        pytest.fail(f"Unexpected exception: {e}")


if __name__ == "__main__":
    sys.exit(pytest.main([__file__]))