# 🗂️ File Metadata Inspector

A simple yet powerful Python script to **inspect metadata** of files in any directory using **generators**, **destructuring**, and `yield`. Ideal for developers, analysts, or sysadmins who need a quick way to explore file details in a clean and memory-efficient way.

---

## 🚀 Features

- ✅ Uses **generators** for efficient, lazy iteration over file metadata
- ✅ Extracts key metadata: name, size, created and modified timestamps
- ✅ **Destructures** metadata neatly for cleaner code
- ✅ Human-readable output
- ✅ Handles missing or invalid directories gracefully

---

## 🧠 How It Works

The script uses `os.scandir()` to traverse a directory and `yield`s file metadata one item at a time. This makes it memory-efficient and scalable for large directories.

```python
for metadata in file_metadata_generator(directory):
    filename, size, created, modified = (
        metadata['filename'],
        metadata['size_bytes'],
        metadata['created'],
        metadata['modified']
    )
```

---

## 📦 Requirements

- Python 3.6 or higher
- No external libraries required

---

## 📂 Usage

1. **Clone or Download** this repository:
    ```bash
    git clone https://github.com/yourusername/file-metadata-inspector.git
    cd file_metadata_inspector
    ```

2. **Run the script**:
    ```bash
    python main.py --file /path/to/your/folder
    ```

---

## 🧪 Sample Output

```
Inspecting files in: /Users/you/Documents

File: resume.pdf
Size: 48976 bytes
Created: Mon May  1 14:23:12 2025
Modified: Wed May  3 11:08:34 2025

File: notes.txt
Size: 1024 bytes
Created: Tue Apr 25 09:12:10 2025
Modified: Tue Apr 25 09:12:10 2025
```

---

## 🛠️ Customization Ideas

- Add **recursive directory traversal**
- Filter by file extension (e.g., only `.txt` or `.csv`)
- Export metadata to CSV or JSON
- Add support for symbolic links or hidden files

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---


