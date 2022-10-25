"""Pip configuration."""
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="badchars",
    version="0.5.0",
    description="A hex badchar generator for different programming languages.",
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="cytopia",
    author_email="cytopia@everythingcli.org",
    url="https://github.com/cytopia/badchars",
    install_requires=[],
    scripts=[
        "badchars"
    ],
    project_urls={
        'Source Code': 'https://github.com/cytopia/badchars',
        'Documentation': 'https://github.com/cytopia/badchars',
        'Bug Tracker': 'https://github.com/cytopia/badchars/issues',
    },
    classifiers=[
        # https://pypi.org/classifiers/
        #
        # How mature is this project
        'Development Status :: 5 - Production/Stable',
        # Indicate who your project is intended for
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "Intended Audience :: System Administrators",
        # Project topics
        "Topic :: Internet",
        "Topic :: Security",
        "Topic :: System :: Shells",
        "Topic :: System :: Systems Administration",
        "Topic :: Utilities",
        # License
        "License :: OSI Approved :: MIT License",
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        # How does it run
        "Environment :: Console",
        # Where does it rnu
        "Operating System :: OS Independent",
    ],
 )
