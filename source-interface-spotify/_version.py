from pathlib import Path
import toml


def get_version():
    # Load the version from pyproject.toml
    pyproject = toml.load(Path(__file__).parent.parent / 'pyproject.toml')
    return pyproject['tool']['poetry']['version']


__version__ = get_version()
