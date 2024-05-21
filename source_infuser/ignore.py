import fnmatch
from pathlib import Path

class IgnoreRules:
    def __init__(self, ignore_file: str):
        self.ignore_patterns = []
        self.load_ignore_patterns(ignore_file)

    def load_ignore_patterns(self, ignore_file: str):
        with open(ignore_file, 'r') as file:
            self.ignore_patterns = [line.strip() for line in file if line.strip() and not line.startswith('#')]

    def is_ignored(self, path: Path) -> bool:
        relative_path = path.as_posix()
        for pattern in self.ignore_patterns:
            if fnmatch.fnmatch(relative_path, pattern):
                return True
        return False

    def should_ignore(self, path: Path, root_dir: Path) -> bool:
        relative_path = path.relative_to(root_dir).as_posix()
        for pattern in self.ignore_patterns:
            if fnmatch.fnmatch(relative_path, pattern):
                return True
        return False
