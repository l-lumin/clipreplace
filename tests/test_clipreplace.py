import pytest

from clipreplace.__main__ import clipreplace


# Setup temporary file
@pytest.fixture
def temp_file(tmp_path):
    file = tmp_path / "test.txt"
    yield file


@pytest.fixture
def mock_clip(mocker):
    def _mock_clipboard(content):
        mocker.patch("pyperclip.paste", return_value=content)

    return _mock_clipboard


def test_file_not_exist(mocker):
    clipreplace("nonexistent.txt")


def text_clipboard_match(temp_file, mock_clip):
    initial_content = "Line 1\nLine 2\nLine 3\n"
    temp_file.write_text(initial_content)

    mock_clip("Line 2\nHello, World!\n")

    clipreplace(str(temp_file))
    expected_content = "Line 1\nLine2\nHello, World\n"
    assert temp_file.read_text() == expected_content


def test_clipboard_not_match(temp_file, mock_clip):
    initial_content = "Line 1\nLine 2\nLine 3\n"
    temp_file.write_text(initial_content)

    mock_clip("Line 4\nHello, World!\n")

    clipreplace(str(temp_file))
    assert temp_file.read_text() == initial_content


def test_empty_clipboard(temp_file, mock_clip):
    initial_content = "Line 1\nLine 2\nLine 3\n"
    temp_file.write_text(initial_content)

    mock_clip("")

    clipreplace(str(temp_file))
    assert temp_file.read_text() == initial_content


def test_empty_file(temp_file, mock_clip):
    temp_file.write_text("")

    mock_clip("Line 2\nHello, World!\n")

    clipreplace(str(temp_file))
    assert temp_file.read_text() == ""
