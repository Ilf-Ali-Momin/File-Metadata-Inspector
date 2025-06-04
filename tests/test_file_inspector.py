import pytest
from src.file_inspector import FileInspector, CombinedFileInspector

import os

@pytest.fixture
def sample_files(tmp_path):
    f1 = tmp_path / "file1.txt"
    f2 = tmp_path / "file2.txt"
    f1.write_text("Hello\nWorld")
    f2.write_text("Another\nFile")
    return str(f1), str(f2)

def test_metadata(sample_files):
    f1, _ = sample_files
    fi = FileInspector(f1)
    metadata = fi.get_metadata()
    assert "Size:" in metadata

def test_combined_inspector(sample_files):
    f1, f2 = sample_files
    fi1 = FileInspector(f1)
    fi2 = FileInspector(f2)
    combined = fi1 + fi2
    assert isinstance(combined, CombinedFileInspector)
