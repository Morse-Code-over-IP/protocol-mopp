# TODO - create by chatgpt


   




# SigBit Python Utility Functions

This package provides common utility functions for the SigBit project.

## Functions

### `ditlen(wpm: int) -> float`

Returns the length of a dit in seconds for a given words-per-minute.

- **Parameters:**
  - `wpm` (int): Words per minute.

- **Returns:**
  - `float`: Length of a dit in seconds.

### `encode(text: str) -> List[str]`

Takes a string of characters and returns a word buffer.

- **Parameters:**
  - `text` (str): Input string.

- **Returns:**
  - `List[str]`: Word buffer.

### `decode(buffer: List[str]) -> str`

Takes a word buffer and returns a string of characters.

- **Parameters:**
  - `buffer` (List[str]): Input word buffer.

- **Returns:**
  - `str`: Decoded string.

### `zfill(string: str, digits: int) -> str`

Implementation of `zfill` for MicroPython.

- **Parameters:**
  - `string` (str): Input string.
  - `digits` (int): Desired length.

- **Returns:**
  - `str`: Padded string.

### `ljust(string: str, width: int, fillchar: str = ' ') -> str`

Implementation of `ljust` for MicroPython.

- **Parameters:**
  - `string` (str): Input string.
  - `width` (int): Desired width.
  - `fillchar` (str, optional): Fill character. Defaults to space (' ').

- **Returns:**
  - `str`: Left-justified string.

## Morse Code Lookup Table

A lookup table (`morse`) is provided for Morse code encoding and decoding.

## License

This code is part of the SigBit project and is released under the [GNU GENERAL PUBLIC LICENSE Version 3](https://www.gnu.org/licenses/gpl-3.0.html).

## Author

- **Sebastian Stetter, DJ5SE**
- GitHub: [tuxintrouble](https://github.com/tuxintrouble)

For more information, visit the [SigBit project on GitHub](https://github.com/tuxintrouble/sigbit).