"""Installation file."""

from setuptools import setup, find_packages

setup(
    name="rootme",
    author="sagittarius-a",
    packages=find_packages(),
    version="1.0.3",
    description="api.www.root-me.org cli simple client",
    entry_points={"console_scripts": ["rootme=rootme.__main__:main"]},
    install_requires=["requests", "colorama", "typing-extensions",],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Natural Language :: English",
        "Intended Audience :: Developers",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Bug Tracking",
        "Topic :: Utilities",
        "Typing :: Typed",
    ],
)
