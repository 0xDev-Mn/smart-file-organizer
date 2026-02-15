from pathlib import Path
import shutil

BASE_DIR = "/home/bat-man/Downloads"

CATEGORIES = {
    "Documents": [".pdf", ".txt", ".docx"],
    "Images": [".jpg", ".png", ".jpeg"],
    "Videos": [".mp4", ".mkv"],
    "Archives": [".zip", ".tar", ".gz"],
}

def organize():
    for item in BASE_DIR.iterdir():
        if item.is_file():
            for folder, extensions in CATEGORIES.items():
                if item.suffix.lower() in extensions:
                    target_dir = BASE_DIR / folder
                    target_dir.mkdir(exist_ok=True)
                    shutil.move(str(item), target_dir / item.name)
                    break

if __name__ == "__main__":
    organize()
