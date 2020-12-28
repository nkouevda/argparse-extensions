# argparse-extensions

[`argparse`](https://docs.python.org/3/library/argparse.html) extensions.

## Installation

    pip install argparse-extensions

## Usage

### NegatableStoreTrueAction

:warning: Deprecated: Python 3.9 introduced `argparse.BooleanOptionalAction`

`action=argparse_extensions.NegatableStoreTrueAction` is a drop-in replacement
for `action='store_true'`:

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--foo',
        action=argparse_extensions.NegatableStoreTrueAction)

This will handle `--no-foo` in addition to `--foo`.

## License

[MIT License](LICENSE.txt)
