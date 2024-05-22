# Source Infuser

<img src="docs/source_infuser_logo.png" alt="Source Infuser Logo" width="200" height="200">

Source Infuser helps keep your AI assistant updated with the changes you perform in your software project. It generates detailed reports of your project's structure, which can be continuously infused into your AI assistant.

## Features

- Generate markdown reports of your project structure.
- Supports customizable ignore patterns similar to `.gitignore` in `.psi-ignore`.
- Easy integration with your existing CI/CD pipelines.

## Installation

### From Source

You can install the package directly from the GitHub repository:

```shell
git clone https://github.com/ivanzhovannik/source-infuser.git
cd source-infuser
pip install .
```

### From PyPi (Feature Under Development)

```shell
pip install source_infuser
```

## Usage

To generate a report of the current directory and write it into `report.md`:

```shell
psi -o report.md
```

or alternatevely

```shell
source_infuser -r . -o report.md
```

**Command-line Options**: 
* -r, --root: Root directory of the project (default: current directory).
* -o, --output: Output markdown file (optional).

**Ignore some elements of your project**: 

In case you want to ignore parts of your root using `.gitignore` patters, just add `.psi-ignore` file to your current directory.

## Contributions
We welcome contributions! Please follow these steps:

1. Go to [source-infuser/issues](https://github.com/ivanzhovannik/source-infuser/issues).
2. If there is no issue similar to the one you encountered, create a new issue.
3. Describe your case in detail to help us better reproduce and understand the problem.
4. If you solved the problem yourself, please go ahead and create a pull-request, tag @ivanzhovannik to review.

## License
This package is free to use for research or commercial purposes. Any part can be reproduced; just mention the source.

## Acknowledgements
Thanks to all users and contributors who made this project better!