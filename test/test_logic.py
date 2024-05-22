import unittest
from source_infuser.logic import generate_report
from pathlib import Path

class TestGenerateReport(unittest.TestCase):
    def test_generate_report(self):
        report = generate_report('.')
        self.assertIn('project:', report)
        self.assertIn('file_content:', report)

if __name__ == '__main__':
    unittest.main()
