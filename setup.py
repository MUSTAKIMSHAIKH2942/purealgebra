
from setuptools import setup, find_packages

setup(
    name="purealgebra",
    version="0.1",
    packages=find_packages(),
    author="Your Name",
    author_email="your.email@example.com",
    description="Pure Python Algebra Library",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/purealgebra",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.6',
)
