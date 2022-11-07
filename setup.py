from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="havc",
    version="1.0.7",
    description="An automatic video converter using HandBrake CLI.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zaytiri/handbrake-automatic-video-converter",
    author="zaytiri",
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
    ],
    keywords="handbrake, cli, console, video, converter, encoder",
    packages=["src", "src.configurations", "src.entities", "src.services", "src.utils"],
    python_requires=">=3.10.6",
    entry_points={
        "console_scripts": [
            "havc=src:main",
        ],
    }
)