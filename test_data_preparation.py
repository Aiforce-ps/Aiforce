import os
import pytest
from data_preparation import precheck_datageneration


def test_valid_inputs():
    """Test precheck_datageneration with valid inputs."""
    try:
        model_file = "model.pkl"
        row_numbers = 10
        data_type = "SingleTable"
        open(model_file, 'w').close()
        result = precheck_datageneration(model_file, row_numbers, data_type)
        assert result is True
    except Exception as e:
        pytest.fail(f"Unexpected exception occurred: {e}")
    finally:
        if os.path.exists(model_file):
            os.remove(model_file)


def test_invalid_file_extension():
    """Test precheck_datageneration with invalid file extension."""
    try:
        model_file = "model.txt"
        row_numbers = 10
        data_type = "SingleTable"
        open(model_file, 'w').close()
        with pytest.raises(ValueError):
            precheck_datageneration(model_file, row_numbers, data_type)
    except Exception as e:
        pytest.fail(f"Unexpected exception occurred: {e}")
    finally:
        if os.path.exists(model_file):
            os.remove(model_file)


def test_negative_row_numbers():
    """Test precheck_datageneration with negative row numbers."""
    try:
        model_file = "model.pkl"
        row_numbers = -5
        data_type = "SingleTable"
        open(model_file, 'w').close()
        with pytest.raises(ValueError):
            precheck_datageneration(model_file, row_numbers, data_type)
    except Exception as e:
        pytest.fail(f"Unexpected exception occurred: {e}")
    finally:
        if os.path.exists(model_file):
            os.remove(model_file)


def test_invalid_data_type():
    """Test precheck_datageneration with invalid data type."""
    try:
        model_file = "model.pkl"
        row_numbers = 10
        data_type = "InvalidType"
        open(model_file, 'w').close()
        with pytest.raises(ValueError):
            precheck_datageneration(model_file, row_numbers, data_type)
    except Exception as e:
        pytest.fail(f"Unexpected exception occurred: {e}")
    finally:
        if os.path.exists(model_file):
            os.remove(model_file)


def test_missing_file():
    """Test precheck_datageneration when the model file does not exist."""
    try:
        model_file = "missing.pkl"
        row_numbers = 10
        data_type = "SingleTable"
        if os.path.exists(model_file):
            os.remove(model_file)
        with pytest.raises(FileNotFoundError):
            precheck_datageneration(model_file, row_numbers, data_type)
    except Exception as e:
        pytest.fail(f"Unexpected exception occurred: {e}")


def test_boundary_row_number():
    """Test precheck_datageneration with boundary row number value."""
    try:
        model_file = "model.pkl"
        row_numbers = 1
        data_type = "MultiTable"
        open(model_file, 'w').close()
        result = precheck_datageneration(model_file, row_numbers, data_type)
        assert result is True
    except Exception as e:
        pytest.fail(f"Unexpected exception occurred: {e}")
    finally:
        if os.path.exists(model_file):
            os.remove(model_file)


def main():
    """Main function to execute all unit tests."""
    pytest.main([__file__])


if __name__ == "__main__":
    main()
