import unittest
from unittest.mock import patch, Mock
from utils.extract import extract_data

class TestExtractData(unittest.TestCase):
    @patch("utils.extract.requests.get")
    def test_extract_data_returns_list(self, mock_get):
        mock_html = """
        <div class='collection-card'>
            <div class='product-details'>
                <h3>Crewneck 73</h3>
                <span class='price'>$10.99</span>
                <p>Rating: 4.5 / 5 ⭐</p>
                <p>Color: Blue</p>
                <p>Size: M</p>
                <p>Gender: Unisex</p>
            </div>
        </div>
        """
        mock_get.return_value = Mock(status_code=200, text=mock_html)

        result = extract_data(max_items=1, max_pages=1)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 1)
        self.assertIn("Title", result[0])
        self.assertEqual(result[0]["Title"], "Crewneck 73")

if __name__ == "__main__":
    unittest.main()