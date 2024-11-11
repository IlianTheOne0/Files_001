# Generated by Qodo Gen
from func import _write
import unittest

class Test_Write(unittest.TestCase):

    # Count words containing a specific symbol in a file
    def test_count_words_with_symbol(self):
        with open('assets/original_file.txt', 'w') as f:
            f.write("apple banana cherry\n")
            f.write("date elderberry fig\n")
            f.write("grape apple\n")
    
        result = _write('a')
        self.assertEqual(result, 5)

    # Handle empty file gracefully
    def test_empty_file(self):
        with open('assets/original_file.txt', 'w') as f:
            pass
    
        result = _write('a')
        self.assertEqual(result, 0)

    # Handle file with no matching words
    def test_no_matching_words(self):
        with open('assets/original_file.txt', 'w') as f:
            f.write("apple banana cherry\n")
            f.write("date elderberry fig\n")
    
        result = _write('z')
        self.assertEqual(result, 0)