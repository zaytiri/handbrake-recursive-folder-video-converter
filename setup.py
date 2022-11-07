from setuptools import setup
import pathlib
from havc.utils.version import get_version

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

version = get_version()

setup(
    name="havc",
    version=version,
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
    packages=["havc", "havc.configurations", "havc.entities", "havc.services", "havc.utils"],
    python_requires=">=3.10.6",
    entry_points={
        "console_scripts": [
            "havc=havc:app.main",
        ],
    }
)