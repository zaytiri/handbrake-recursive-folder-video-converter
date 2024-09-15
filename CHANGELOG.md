# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

### Status
- Added
- Changed
- Fixed
- Removed

## [1.3.0] - 2024-09-15

### Added
- support for Linux users.

## [1.2.1] - 2023-03-06

### Fixed
- fixed issue where intermediate folders were not being created.
- fixed issue where sub-folders with the same name as parent folders were not being created.

## [1.2.0] - 2023-03-04

### Fixed
- fixed errors.
### Changed
- the 'delete folder' argument can now be only a folder name or an absolute path, while before it needed to be only a name and the default path was the same directory as 'to convert' folder.
- the output file will now only be created after the encoding.
### Added
- program will skip duplicate files (with the same name and target extension) if one already exists. The skipped file will not be touched. This information will be added to the output file summary.


## [1.1.2] - 2023-02-28

### Fixed
- fixed issue where a video file did not have the correct path when inside sub folders.
- fixed issue where 'to delete' directory was not creating the same structure as the original to convert folder.

## [1.1.1] - 2022-11-10

### Changed
- README.md file was updated

## [1.1.0] - 2022-11-10

### Added
- new argument regarding shutting down the computer when the program is done
- removal of output file, if no files were found during searching

### Fixed
- fixed bug where video searching was being done two times in a row

## [1.0.0] - 2022-11-09

### Added
- First release on PyPI