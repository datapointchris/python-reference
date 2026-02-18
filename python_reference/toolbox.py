import itertools
import sys
from pathlib import Path


def convert_bytes(num: int | float) -> str:
    """Convert bytes to human readable format"""
    for unit in ('B', 'KB', 'MB', 'GB', 'TB', 'PB'):
        if num < 1024.0 or unit == 'PB':
            break
        num /= 1024.0
    else:
        raise ValueError(f'Value {num} is too large to convert to human readable format')
    return f'{num:.2f} {unit}'


def human_readable_size(obj: object) -> str:
    """Get human readable size of any python object"""
    size = sys.getsizeof(obj)
    return convert_bytes(size)


def glob_multiple_patterns(path: Path, patterns: str | list[str]):
    patterns = [patterns] if isinstance(patterns, str) else patterns
    return list(itertools.chain.from_iterable(Path(path).glob(p) for p in patterns))


def tree(
    dir_path: Path,
    prefix: str = '',
    include_glob: str | list[str] = '**/*',
    exclude_glob: str | list[str] | None = None,
):
    """Create tree structure for path

    Args:
        dir_path (Path): _description_
        prefix (str, optional): _description_. Defaults to ''.
        include_glob (str, optional): _description_. Defaults to '*'.
        exclude_glob (_type_, optional): _description_. Defaults to None.

    Yields:
        _type_: _description_
    """

    # prefix components:
    SPACE = '    '
    BRANCH = '│   '
    # pointers:
    TEE = '├── '
    LAST = '└── '

    contents = glob_multiple_patterns(dir_path, include_glob)
    if exclude_glob:
        exclude = glob_multiple_patterns(dir_path, exclude_glob)
        contents = list(set(contents) - set(exclude))
    # contents each get pointers that are ├── with a final └── :
    pointers = [TEE] * (len(contents) - 1) + [LAST]
    for pointer, path in zip(pointers, contents, strict=True):
        yield prefix + pointer + path.name
        if path.is_dir():  # extend the prefix and recurse:
            extension = BRANCH if pointer == TEE else SPACE
            # i.e. SPACE because last, └── , above so no more |
            yield from tree(path, prefix=prefix + extension)
