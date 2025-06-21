import unittest
from utils.transform import transform_data

class TestTransformData(unittest.TestCase):
    def test_transform_valid_data(self):
        sample = [{
            "Title": "Jacket 6",
            "Price": 2453920.0,
            "Rating": "3.8",
            "Color": 3,
            "Size": "XL",
            "Gender": "Women",
            "Timestamp": "2024-01-01T00:00:00"
        }]
        df = transform_data(sample)
        self.assertEqual(len(df), 1)
        self.assertEqual(df.iloc[0]["Title"], "Jacket 6")
        self.assertIsInstance(df.iloc[0]["Price"], float)
        self.assertIsInstance(df.iloc[0]["Rating"], float)

    def test_transform_invalid_rating(self):
        sample = [{
            "Title": "Invalid Product",
            "Price": "$15.00",
            "Rating": "Not Rated",
            "Color": 3,
            "Size": "S",
            "Gender": "Female",
            "Timestamp": "2024-01-01T00:00:00"
        }]
        df = transform_data(sample)
        self.assertEqual(len(df), 0)

if __name__ == "__main__":
    unittest.main()