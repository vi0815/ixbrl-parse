from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="ixbrlparse",
    packages=find_packages(),
    version="0.1",
    author="David Kane",
    author_email="david@dkane.net",
    description="A python module for getting useful data out of ixbrl files.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/drkane/ixbrl-parse",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
