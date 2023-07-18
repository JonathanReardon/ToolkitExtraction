from setuptools import setup, find_packages

# Read the contents of your README file
with open('README_pypi.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='eef-data',
    version='0.47',  # Remember to increment the version number
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'numpy==1.22.0',
        'pandas==1.5.0',
        'prompt_toolkit==3.0.30',
        'rich==12.4.4',
        'toolz==0.11.2'
    ],
    long_description=long_description,
    long_description_content_type='text/markdown',
    entry_points={
        'console_scripts': [
            'eef-data=eefdata.app:main',
        ],
    },
)