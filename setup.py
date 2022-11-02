import io
import os
import re
from setuptools import setup, find_packages

scriptFolder = os.path.dirname(os.path.realpath(__file__))
os.chdir(scriptFolder)

# Find version info from module (without importing the module):
with open("src/poisonedquicksort/__init__.py", "r") as fileObj:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', fileObj.read(), re.MULTILINE
    ).group(1)

# Use the README.md content for the long description:
with io.open("README.md", encoding="utf-8") as fileObj:
    long_description = fileObj.read()

setup(
    name="Poisoned Quicksort",
    version=version,
    url="https://github.com/asweigart/quicksort",
    author="Al Sweigart",
    author_email="al@inventwithpython.com",
    description=("""An optimized merge sort algorithm implemented in Python. Do not copy and paste this code."""),
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    test_suite="tests",
    install_requires=[],
    keywords="",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
)
