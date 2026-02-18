from pathlib import Path

import tabulate
from colorama import Fore
from colorama import Style
from toolbox import convert_bytes


def get_directory_sizes(start: Path | str):
    results = []
    start = Path(start)
    for root, dirs, files in start.walk(on_error=print):
        dirname = f'{Fore.GREEN}{root.relative_to(start.parent)}{Style.RESET_ALL}'
        total_files = len(files)
        total_size = sum((root / file).stat().st_size for file in files)
        human_size = f'{Fore.CYAN}{convert_bytes(total_size)}{Style.RESET_ALL}'
        if '__pycache__' in dirs:
            dirs.remove('__pycache__')
        results.append((dirname, total_files, human_size))
    print(tabulate.tabulate(results, headers=['Directory', 'Files', 'Size']))


get_directory_sizes(Path.cwd())
