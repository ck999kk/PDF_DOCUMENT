import unittest
import os
import sys

# Add the scripts directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../scripts')))

from check_filenames import is_valid

class TestCheckFilenames(unittest.TestCase):

    def test_valid_filenames(self):
        self.assertTrue(is_valid("20230101-Document-001.pdf"))
        self.assertTrue(is_valid("20231231-Another_Document_Title-999.pdf"))
        self.assertTrue(is_valid("20230515-Short-123.pdf"))

    def test_invalid_date_format(self):
        self.assertFalse(is_valid("230101-Document-001.pdf")) # Too short
        self.assertFalse(is_valid("2023010-Document-001.pdf")) # Too short
        self.assertFalse(is_valid("202301011-Document-001.pdf")) # Too long
        self.assertFalse(is_valid("YYYYMMDD-Document-001.pdf")) # Not digits

    def test_invalid_seq_number(self):
        self.assertFalse(is_valid("20230101-Document-ABC.pdf")) # Not digits
        self.assertFalse(is_valid("20230101-Document-1.pdf")) # Too short (should be 001)

    def test_missing_parts(self):
        self.assertFalse(is_valid("20230101-Document.pdf")) # Missing seq part
        self.assertFalse(is_valid("Document.pdf")) # Missing date and seq part

    def test_non_pdf_files(self):
        self.assertTrue(is_valid("image.jpg")) # Should ignore non-pdf files
        self.assertTrue(is_valid("document.txt")) # Should ignore non-pdf files

if __name__ == '__main__':
    unittest.main()
