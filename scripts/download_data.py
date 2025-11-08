import kagglehub
import shutil
from pathlib import Path

# Kaggle dataset: https://www.kaggle.com/datasets/mohamedbakhet/amazon-books-reviews
DATASET = "mohamedbakhet/amazon-books-reviews"

def main():
    print(f"[INFO] Downloading dataset: {DATASET}")
    path = kagglehub.dataset_download(DATASET)
    print("Downloaded to:", path)

    # Copy data to local ./data directory for consistency
    target_dir = Path("data")
    target_dir.mkdir(exist_ok=True)

    print(f"[INFO] Copying files to {target_dir}/")
    for item in Path(path).iterdir():
        dest = target_dir / item.name
        if item.is_file():
            shutil.copy(item, dest)
        elif item.is_dir():
            shutil.copytree(item, target_dir / item.name, dirs_exist_ok=True)

    print("\n[✔] Done. Dataset files are now available in ./data")

if __name__ == "__main__":
    main()
