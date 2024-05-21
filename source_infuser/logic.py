import logging
import os
from pathlib import Path
from .ignore import IgnoreRules

logger = logging.getLogger(__name__)

ignore_rules = IgnoreRules('.psi-ignore')

def generate_report(root_dir):
    logger.info("\n\t".join(["Ignored Patterns:", *ignore_rules.ignore_patterns]))
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
        if file_path.is_file() and not ignore_rules.should_ignore(file_path, root_dir):
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                report.append(f"```{file_path.relative_to(root_dir)}")
                report.append(content)
                report.append("```")
            except Exception as e:
                logger.error(f"Failed to process {file_path} due to: {e}")

    return "\n".join(report)

def generate_tree(root_dir):
    tree_lines = []

    for root, dirs, files in os.walk(root_dir):
        # Filter out ignored directories
        dirs[:] = [d for d in dirs if not ignore_rules.should_ignore(Path(root) / d, root_dir)]
        
        level = root.replace(root_dir, '').count(os.sep)
        indent = ' ' * 4 * (level)
        tree_lines.append(f"{indent}├── {os.path.basename(root)}/")
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            file_path = Path(root) / f
            if not ignore_rules.should_ignore(file_path, root_dir):
                tree_lines.append(f"{subindent}└── {f}")

    return "\n".join(tree_lines)
