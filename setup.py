import os
import sys
from setuptools import setup
import pathlib
import yaml

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

def get_version():
    if getattr(sys, 'frozen', False):
        path = os.path.join(sys._MEIPASS, "files/progsettings.yaml")
    else:
        path = os.path.join(os.path.dirname(__file__), 'havc', 'progsettings.yaml')

    with open(path, 'r') as settings_file:
        settings = yaml.safe_load(settings_file)['prog'.upper()]
        return settings['version'.upper()]
    
setup(
    name="havc",
    version=get_version(),
    description="An automatic video converter using HandBrake CLI.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zaytiri/handbrake-automatic-video-converter",
    project_urls={
        'GitHub': 'https://github.com/zaytiri/handbrake-automatic-video-converter',
        'Changelog': 'https://github.com/zaytiri/handbrake-automatic-video-converter/blob/main/CHANGELOG.md',
    },
    author="zaytiri",
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
    ],
    keywords="handbrake, cli, console, video, converter, encoder",
    package_data={'havc': ['progsettings.yaml']},
    packages=["havc", "havc.configurations", "havc.entities", "havc.services", "havc.utils"],
    python_requires=">=3.10.6",
    install_requires=[
      "PyYAML~=6.0",
    ],
    entry_points={
        "console_scripts": [
            "havc=havc:app.main",
        ],
    }
)