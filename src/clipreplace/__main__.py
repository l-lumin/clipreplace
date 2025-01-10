import argparse
import pyperclip
from pathlib import Path


def clipreplace(file_path: str):
    file_path = Path(file_path)
    if not file_path.exists():
        print("File not found.")
        return

    try:
        with file_path.open("r") as file:
            content = file.readlines()
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    clipboard_content = pyperclip.paste().strip().splitlines()
    if not clipboard_content:
        print("Clipboard is empty.")
        return

    start_idx = end_idx = -1
    for i, line in enumerate(content):
        if line.strip() == clipboard_content[0]:
            start_idx = i
            end_idx = i + len(clipboard_content)

    if start_idx == -1:
        print("Clipboard content not found in file.")
        return

    new_section = "\n".join(clipboard_content) + "\n"
    content = content[:start_idx] + [new_section] + content[end_idx:]
    try:
        with file_path.open("w") as file:
            file.writelines(content)
    except Exception as e:
        print(f"Error writing file: {e}")
        return
    else:
        print("Content replaced.")

def main():
    parser = argparse.ArgumentParser(
        description="ClipReplace: Replace a section of text in a file with clipboard content."
    )
    parser.add_argument(
        "--file", "-f", required=True, help="Path to the file to modify."
    )
    args = parser.parse_args()
    clipreplace(args.file)
