from setuptools import find_packages, setup

setup(
    name="mcqgenerator",
    version="0.0.1",
    author="Prince Chothani",
    author_email="princechothani53@gmail.com",
    install_requires=["langchain", "streamlilt", "python-dotenv", "PyPDF2"],
    packages=find_packages() # this help to consider src folder as package because of __init__
)
