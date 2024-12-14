from setuptools import setup, find_packages

setup(
    name="my_tool",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "mytool = my_tool.cli:main",  # Command `mytool` will run `main()` from `cli.py`
        ],
    },
    install_requires=[],
    description="A simple command-line tool",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourname/my_tool",
)
