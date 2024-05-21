import argparse
import logging
import source_infuser as psi

def main():
    psi.logs.setup_logging('DEBUG')

    parser = argparse.ArgumentParser(description='Generate a markdown report of the project structure and file contents.')
    parser.add_argument('-r', '--root', type=str, default='.', help='Root directory of the project')
    parser.add_argument('-o', '--output', type=str, default=None, help='Output markdown file')
    args = parser.parse_args()

    report = psi.generate_report(args.root)
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(report)
        logging.info(f"Report generated and saved to {args.output}")
    else:
        logging.info(report)

if __name__ == "__main__":
    main()
