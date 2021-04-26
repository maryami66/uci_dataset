from setuptools import setup
from os import path


current_dir = path.abspath(path.dirname(__file__))


with open("README.md", "r") as fh:
    long_description = fh.read()

with open(path.join(current_dir, 'requirements.txt'), 'r') as f:
    install_requires = f.read().split('\n')


setup(
    name='uci_dataset',
    version='0.0.4',
    author='Maryam Bahrami',
    author_email='maryami_66@yahoo.com',
    packages=['uci_dataset'],
    url='https://github.com/maryami66/uci-dataset',
    license='MIT',
    description='Read UCI dataset without the need to download any file from an external website.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    setup_requires='numpy',
    install_requires=install_requires,
    keywords='uci dataset, toy dataset, public dataset',
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.6'
)