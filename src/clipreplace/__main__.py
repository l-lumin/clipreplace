import argparse
import pyperclip
from pathlib import Path


def clipreplace(
    file_path: str, dry_run: bool = False, clipboard_content_override: list = None
):
    file_path = Path(file_path)
    if not file_path.exists():
        print("File not found.")
        return

    try:
        with file_path.open("r") as file:
            content = file.readlines()
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    clipboard_content = (
        clipboard_content_override or pyperclip.paste().strip().splitlines()
    )
    if not clipboard_content:
        print("Clipboard is empty.")
        return

    start_idx = end_idx = -1
    for i, line in enumerate(content):
        if line.strip() == clipboard_content[0].strip():
            start_idx = i
            end_idx = i + len(clipboard_content)
            break

    if start_idx == -1:
        print("Clipboard content not found in file.")
        return

    new_section = "\n".join(clipboard_content) + "\n"
    updated_content = content[:start_idx] + [new_section] + content[end_idx:]

    if dry_run:
        print("Dry run enabled. Preview of changes:")
        print("".join(updated_content))
        return

    backup_path = file_path.with_suffix(file_path.suffix + ".bak")
    try:
        backup_path.write_text("".join(updated_content))
        print(f"Backup file created: {backup_path}")
    except Exception as e:
        print(f"Error creating backup file: {e}")
        return

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
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview the changes without modifying the file.",
    )
    parser.add_argument(
        "--clipboard-content",
        "-c",
        help="Specify the content to replace with instead of clipboard content.",
    )
    args = parser.parse_args()

    clipboard_content_override = (
        args.clipboard_content.strip().splitlines() if args.clipboard_content else None
    )
    clipreplace(
        args.file,
        dry_run=args.dry_run,
        clipboard_content_override=clipboard_content_override,
    )


if __name__ == "__main__":
    main()
