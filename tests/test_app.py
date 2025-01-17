import unittest
from utils.date_utils import parse_relative_date
from config.settings import get_default_dates
from utils.response_formatter import build_json_output

class TestMetricsApp(unittest.TestCase):
    def test_get_default_dates(self):
        start, end = get_default_dates()
        self.assertIsNotNone(start)
        self.assertIsNotNone(end)

    def test_parse_relative_date(self):
        start, end = parse_relative_date("last year")
        self.assertTrue(start.startswith("2023"))
        self.assertTrue(end.startswith("2023"))

    def test_build_json_output(self):
        data = [{"Entity": "Amazon", "Parameter": "Revenue"}]
        result = build_json_output(data, "2023-01-01", "2023-12-31")
        self.assertEqual(result[0]["Entity"], "Amazon")
        self.assertEqual(result[0]["Start Date"], "2023-01-01")

if __name__ == "__main__":
    unittest.main()
