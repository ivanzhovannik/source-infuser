import logging
import os
from pathlib import Path
import fnmatch

with open('test/.psi-ignore', 'r') as f:
    IGNORE_PATTERNS = f.read().split('\n')

logging.getLogger(__name__)
logging.info("\n\t".join(["Ignored Patterns:", *IGNORE_PATTERNS]))

def generate_report(root_dir):
    report = []

    # Add project name (directory name)
    project_name = Path(root_dir).name
    report.append(f"project: {project_name}\n")

    # Generate the tree structure
    tree_structure = generate_tree(root_dir)
    report.append("```tree")
    report.append(tree_structure)
    report.append("```\n")

    # List files and their content
    report.append("file_content:")
    for file_path in Path(root_dir).rglob('*'):
        if file_path.is_file() and not ignore_path(file_path, root_dir):
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                report.append(f"```{file_path.relative_to(root_dir)}")
                report.append(content)
                report.append("```")
            except Exception as e:
                print(f"Failed to process {file_path} due to: {e}")

    return "\n".join(report)

def ignore_path(path, root_dir) -> bool:
    relative_path = path.relative_to(root_dir).as_posix()
    for pattern in IGNORE_PATTERNS:
        if fnmatch.fnmatch(relative_path, pattern) or fnmatch.fnmatch(path.name, pattern):
            return True
    return False

def generate_tree(root_dir):
    tree_lines = []

    for root, dirs, files in os.walk(root_dir):
        # Filter out ignored directories
        dirs[:] = [d for d in dirs if not ignore_path(Path(root) / d, root_dir)]
        
        level = root.replace(root_dir, '').count(os.sep)
        indent = ' ' * 4 * (level)
        tree_lines.append(f"{indent}├── {os.path.basename(root)}/")
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            file_path = Path(root) / f
            if not ignore_path(file_path, root_dir):
                tree_lines.append(f"{subindent}└── {f}")

    return "\n".join(tree_lines)

