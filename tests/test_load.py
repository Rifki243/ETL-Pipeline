import unittest
from unittest.mock import mock_open, patch
from utils.load import save_to_csv

class TestSaveToCSV(unittest.TestCase):
    @patch("builtins.open", new_callable=mock_open)
    @patch("os.makedirs")
    def test_save_to_csv_success(self, mock_makedirs, mock_file):
        sample_data = [{
            "Title": "Hoodie 3",
            "Price": 7950080.0,
            "Rating": 4.8,
            "Color": 3,
            "Size": "L",
            "Gender": "Unisex",
            "Timestamp": "2024-01-01T00:00:00"
        }]
        save_to_csv(sample_data, filename="output.csv")
        mock_file.assert_called_once_with("output.csv", mode='w', newline='', encoding='utf-8')

    def test_save_to_csv_empty_data(self):
        with self.assertRaises(ValueError):
            save_to_csv([])

if __name__ == "__main__":
    unittest.main()