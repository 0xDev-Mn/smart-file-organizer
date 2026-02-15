# Smart File Organizer (Python)

A simple and beginner-friendly Python script that automatically organizes files in your **Downloads** folder into neatly categorized subfolders such as Documents, Images, Videos, and Archives.

This tool is designed to help everyday users keep their system clean without manually sorting files.

---

## ✨ Features
- 📁 Automatically organizes files by type
- 🧠 Uses clear, customizable rules
- 🔁 Safe to run multiple times
- ⚡ Lightweight and fast
- 🐍 Uses only Python standard library modules

---

## 📂 Example

### Before
Downloads/
├── resume.pdf
├── photo.png
├── movie.mp4
├── archive.zip


### After
Downloads/
├── Documents/
│ └── resume.pdf
├── Images/
│ └── photo.png
├── Videos/
│ └── movie.mp4
├── Archives/
│ └── archive.zip


---

## 🛠 How It Works
- Scans the Downloads folder
- Detects file extensions
- Creates category folders if needed
- Moves files into the correct folder

---

## 🧰 Technologies Used
- Python 3
- pathlib (standard library)
- shutil (standard library)

No external dependencies are required.

---

## ▶️ How to Run

```bash
python organizer.py
