# Handbrake Automatic Video Converter

An automatic video converter using HandBrake CLI. All videos found on a given folder, and subsequent folders, will be
converted on original location while original file will be transferred to another folder for easy removal.

### HandBrake

This is a video converter and the HandBrake GUI can be found [here](https://handbrake.fr), which also has a HandBrake
CLI.

For more information, follow [this](https://handbrake.fr/docs/en/latest/table-of-contents.html) link.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Support](#support)
- [License](#license)
- [Status](#status)

<a name="description"></a>

## Description

Given a specific folder, all video files found with user-given extensions will be converted to a target extension also
provided by the user.

The converted video file will stay in the original folder while the original file will be transferred to another folder.
This has the benefit of easy removal of the original files, as well as if a file does not encode successfully the
original file still exists and can be converted again.

The program also accepts a user custom command which must have placeholders to be replaced by the original file path and
converted file path.

In a first use of the program, all given arguments will be saved in a storage file so the user does not have to always
write the same repeated command.

In the end, an output file will be created containing:

- all the files' information, files' original size and converted size;
- if the file was successfully encoded;
- the size difference between all files.

Initially, this project has the aim of reducing files size to ocupy the least amount of space in the disk and comparing
between original size and converted size, but since a user can input a custom command, this can also be used just to
convert a lot of files in a folder for other purposes.

<a name="features"></a>

## Features

| Status | Feature                                                              |
|:-------|:---------------------------------------------------------------------|
| ✅      | convert a lot of files in their corresponding folders                |
| ✅      | convert files with multiple different extensions at the same time    |
| ✅      | transfer of original files in an external folder for easy removal    |
| ✅      | configurations will be saved in an external file                     |
| ✅      | use of an automatic basic command aimed to reduce file size          |
| ✅      | a custom HandBrake command with placeholders can also be inserted    |
| ✅      | output file containing converted files information and their success |

Any new features are **very** welcome!

<a name="prerequisites"></a>

## Prerequisites

[Python 3](https://www.python.org/downloads/) must also be installed.

To use this project, the HandBrake command line version must be installed. This installation can be found
in [this link](https://handbrake.fr/downloads.php) under 'Downloads->Other->Command Line Version'

<a name="installation"></a>

## Installation

```
pip --no-cache-dir install havc
```

or,

```
pip3 --no-cache-dir install havc
```

<a name="usage"></a>

## Usage

| Command | Required | Description                                                      |
|:--------|:---------|:-----------------------------------------------------------------|
| -r      | ✅        | absolute path folder to the HandBrake.exe (command line version) |
| -c      | ✅        | absolute path folder containing the files to convert             |
| -e      | ✅        | multiple file extensions to find and convert                     |
| -t      | ✅        | file extension the converted file will have                      |
| -d      | ❌        | folder's name containing original files                          |
| -cc     | ❌        | custom handbrake command with placeholders                       |

#### Notes

- Initial command must have all required arguments except if these arguments already are configured in the config.txt
  file.
- Non-required arguments will also be saved in the config.txt file if specified.
- The folder containing original filed has the default name of 'TO-DELETE'.
- The dot '.' before each extension is completely optional.

---

Any additional help can be provided if the following command is run:

```
havc --help
```

Example of the initial command:

```
havc -r "C:\path\to\Desktop" -c "C:\path\to\Desktop\folder to convert" -e mp4 mkv -t m4v
```

After this, the config.txt file will be configured and then the following command becomes valid (always using the previous configurations):

```
havc
```

If any argument have to be modified just run the command with the necessary argument, for instance, if the extensions
have to be modified, we simply run:

```
havc -e mov .avi mp4
```

<a name="support"></a>

## Support

The following links contain documentation about how to make a HandBrake command:

- [Command Line Reference](https://handbrake.fr/docs/en/latest/cli/command-line-reference.html)

- [CLI Options](https://handbrake.fr/docs/en/latest/cli/cli-options.html)

<a name="license"></a>

## License

[MIT](https://choosealicense.com/licenses/mit/)

<a name="status"></a>

## Status

This project started as a simple one file script, but then I saw the opportunity to make a program more complex that could also not only help the community, but also help my development. With that said, this project was also developed for educational purposes, so any bugs, suggestions, new features, improvements, etc, don't hesitate to ask, open an issue or a pull request.