# Source Infuser

How to keep your AI assistant updated with the changes you performed? This package prepares your software project for continuous infusion into your AI assistant in a rather simplistic manner.

## Installation

### From Source

You can install the package directly from the GitHub repository:

```shell
git clone https://github.com/ivanzhovannik/source-infuser.git
cd source-infuser
pip install .
```

### From PyPi (Feature under development)

```shell
pip install source_infuser
```

## Usage
To generate a report of the current directory and write it into `report.md`:

```shell
source_infuser -r . -o report.md
```

