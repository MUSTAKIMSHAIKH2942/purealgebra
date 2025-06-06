
from setuptools import setup, find_packages

setup(
    name="purealgebra",
    version="0.1",
    packages=find_packages(),
    author="Mustakim Shaikh",
    author_email="mustakim.shaikh.prof@gmail.com",
    description="Pure Python Algebra Library",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/MUSTAKIMSHAIKH2942/purealgebra",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.6',
)
