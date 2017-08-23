import argparse


class NegatableStoreTrueAction(argparse.Action):
  """Like 'store_true', but for an option '--foo', also handles '--no-foo'.
  """

  def __init__(
      self, option_strings, dest, default=False, required=False, help=None):
    option_strings += [
        option_string.replace('--', '--no-', 1)
        for option_string in option_strings
        if option_string.startswith('--')]
    super(NegatableStoreTrueAction, self).__init__(
        option_strings=option_strings,
        dest=dest,
        nargs=0,
        const=True,
        default=default,
        required=required,
        help=help)

  def __call__(self, parser, namespace, values, option_string=None):
    negated = option_string.startswith('--no-')
    setattr(namespace, self.dest, not negated)
