# ClipReplace
[![Test](https://github.com/l-lumin/clipreplace/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/l-lumin/clipreplace/actions/workflows/test.yml)

**ClipReplace** is a simple command-line tool to replace a section of text in a file with clipboard content.

## Installation

Install `clipreplace` using `pipx`:

```sh
pipx install clipreplace
```

## Usage

1. Copy text to your clipboard
2. Run the command:

```sh
clipreplace --file <file_path>
```

3. If the first line of the clipboard matches a line in the file, the match section will be replaced with the clipboard content.

## License

This project is licensed under the MIT License.
