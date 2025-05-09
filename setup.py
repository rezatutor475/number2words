from setuptools import setup, find_packages
import os


def get_version():
    version_file = os.path.join("number2words", "__init__.py")
    with open(version_file, encoding="utf-8") as f:
        for line in f:
            if line.startswith("__version__"):
                delim = '"' if '"' in line else "'"
                return line.split(delim)[1]
    raise RuntimeError("Unable to find version string.")


# Load the README file for the long description
try:
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()
except FileNotFoundError:
    long_description = "A Python package to convert numbers to words in English and Persian."

# Read requirements from requirements.txt if available
requirements = []
if os.path.isfile("requirements.txt"):
    with open("requirements.txt", "r", encoding="utf-8") as req_file:
        requirements = [line.strip() for line in req_file if line.strip() and not line.startswith("#")]

setup(
    name="number2words",
    version=get_version(),
    author="Your Name",
    author_email="your.email@example.com",
    description="Convert numbers to words in English and Persian",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/number2words",
    packages=find_packages(exclude=["tests*", "examples"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Natural Language :: English",
        "Natural Language :: Persian"
    ],
    python_requires='>=3.7',
    include_package_data=True,
    install_requires=requirements,
    extras_require={
        "dev": ["pytest", "flake8", "mypy"],
    },
    entry_points={
        "console_scripts": [
            "number2words=number2words.cli:main"
        ]
    },
    keywords=["number", "words", "farsi", "persian", "english", "conversion", "text", "language"]
)
