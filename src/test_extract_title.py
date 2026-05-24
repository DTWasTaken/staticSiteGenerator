import unittest

from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        md = "# Test Title"
        title = extract_title(md)
        self.assertEqual(title, "Test Title")

    def test_extract_title_no_title(self):
        md = "###### Not A Title"
        with self.assertRaises(ValueError) as cm:
            title = extract_title(md)
        self.assertEqual(
            str(cm.exception),
            "No title found in markdown document"
        )

    def test_extract_title_multiline(self):
        md = """
# Multiline Title
Some other non-title text
"""
        title = extract_title(md)
        self.assertEqual(title, "Multiline Title")

    def test_extract_title_with_punctuation(self):
        md = """
# Multiline Title, a Love Story (for Robots)...
Some other non-title text
"""
        title = extract_title(md)
        self.assertEqual(title, "Multiline Title, a Love Story (for Robots)...")

    def test_extract_title_not_on_first_line(self):
        md = """
Some other non-title text
# Multiline Title
"""
        title = extract_title(md)
        self.assertEqual(title, "Multiline Title")


if __name__ == "__main__":
    unittest.main()
