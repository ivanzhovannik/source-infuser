import argparse
import logging
import source_infuser as psi

# Set up logging before any logging calls
logger = logging.getLogger(__name__)
psi.logs.setup_logging('DEBUG')
logger.debug("Logging setup called")

def main():

    parser = argparse.ArgumentParser(description='Generate a markdown report of the project structure and file contents.')
    parser.add_argument('-r', '--root', type=str, default='.', help='Root directory of the project')
    parser.add_argument('-o', '--output', type=str, default=None, help='Output markdown file')
    args = parser.parse_args()

    report = psi.generate_report(args.root)
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(report)
        logger.info(f"Report generated and saved to {args.output}")
    else:
        logger.info(report)

if __name__ == "__main__":
    main()
