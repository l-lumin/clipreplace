# Welcome to Clip Replace

ClipReplace is a simple command-line tool to replace a section of text in a file with clipboard content.

## Features

- Replaces a sections of text in a file with content from your clipboard.
- Supports creating backups of the file before making changes.
- Provides a dry-run feature for previewing changes without modifying the file.
- Can override clipboard content with custom input.

## Installation

To install **ClipReplace**, use `pipx` to ensure isolation from your system:

```sh
pipx install clipreplace
```

## Usage

### Basic Usage

1. Copy the text you want to replace with to your clipboard.
2. Run the follow command:

```sh
clipreplace --file <file_path>
```

This will search for the first matching line in the file and replace that section with the content from your clipboard.

### Options

| Option                        | Description                                             |
| ----------------------------- | ------------------------------------------------------- |
| `--file` or `-f`              | Path to the file you want to modify                     |
| `--dry-run`                   | Preview the changes without modifying the file          |
| `--clipboard-content` or `-c` | Specify custom content to replace the clipboard content |
| `--no-backup`                 | Do not create a backup of the file                      |
