# Import library
# Lists all files with .py, .csv, .json and .dbc extensions.
from pathlib import Path

path = Path.cwd()
files = { p.resolve() for p in Path(path).glob("**/*") 
    if p.suffix in ['.py', '.csv', '.json', '.dbc'] }

for file in files:
    print(file.parts[-1])