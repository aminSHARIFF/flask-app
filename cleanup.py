import os
import shutil
from pathlib import Path

ROOT = Path(__file__).parent

def remove_pycache():
    for path in ROOT.rglob("__pycache__"):
        shutil.rmtree(path, ignore_errors=True)
    print("Removed __pycache__ folders")

def remove_pyc():
    for path in ROOT.rglob("*.pyc"):
        path.unlink(missing_ok=True)
    print("Removed .pyc files")

def remove_db():
    for path in ROOT.rglob("*.sqlite3"):
        path.unlink(missing_ok=True)
    print("Removed .sqlite3 files")

def remove_migrations():
    migrations_path = ROOT / "migrations"
    if migrations_path.exists():
        shutil.rmtree(migrations_path, ignore_errors=True)
        print("Removed migrations folder")

if __name__ == "__main__":
    print("Starting cleanup...\n")

    remove_pycache()
    remove_pyc()
    remove_db()

    # ⚠️ optional (uncomment if you REALLY want reset)
    # remove_migrations()

    print("\nCleanup complete.")