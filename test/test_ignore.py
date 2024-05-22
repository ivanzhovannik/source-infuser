import unittest
from source_infuser.ignore import IgnoreRules
from pathlib import Path

class TestIgnoreRules(unittest.TestCase):
    def setUp(self):
        self.ignore_rules = IgnoreRules('.psi-ignore')

    def test_ignore(self):
        ignored_path = Path('report.md')
        not_ignored_path = Path('some_file.py')
        self.assertTrue(self.ignore_rules.should_ignore(ignored_path, Path('.')))
        self.assertFalse(self.ignore_rules.should_ignore(not_ignored_path, Path('.')))

if __name__ == '__main__':
    unittest.main()
