from typing import List

import setuptools


def read_multiline_as_list(file_path: str) -> List[str]:
    with open(file_path) as req_file:
        contents = req_file.read().split("\n")
        if contents[-1] == "":
            contents.pop()
        return contents


with open("README.md", "r") as readme_file:
    long_description = readme_file.read()


setuptools.setup(
    name="timed_dict",
    version="0.2.0",
    author="Teialabs",
    author_email="contato@teialabs.com",
    description="Dictionary with expirable keys ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TeiaLabs/TimedDict",
    packages=setuptools.find_packages(),
    keywords='cache dictionary time expirable ',
    python_requires=">=3.6",
)
