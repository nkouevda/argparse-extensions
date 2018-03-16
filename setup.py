from setuptools import setup

version = {}

with open('argparse_extensions/__version__.py', 'r') as f:
  exec(f.read(), version)

with open('README.md', 'r') as f:
  readme = f.read()

setup(
    name='argparse-extensions',
    version=version['__version__'],
    description='argparse extensions',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/nkouevda/argparse-extensions',
    author='Nikita Kouevda',
    author_email='nkouevda@gmail.com',
    license='MIT',
    packages=['argparse_extensions'],
)
