# Working on absolute paths
from pathlib import Path

print(Path('test/pytest_code.py').resolve())
