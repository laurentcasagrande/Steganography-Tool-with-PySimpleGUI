# Steganography Tool with PySimpleGUI

## Overview

This Python-based Steganography Tool, developed using PySimpleGUI, allows users to encode and decode messages within images. The tool utilizes the Least Significant Bit (LSB) approach, embedding and extracting information in the least significant bit of each color channel of the image.

## Features

- **Encode**: Embed text messages into images using the LSB approach.
- **Decode**: Extract hidden messages from images using the LSB approach.
- **User-Friendly Interface**: Built using PySimpleGUI for an easy and intuitive experience.

## Least Significant Bit (LSB) Approach

The LSB approach involves manipulating the least significant bit of each pixel in the image without significantly altering the visual appearance. In this tool, the LSB of each color channel (Red, Green, and Blue) is used to store binary information. This approach ensures that the modifications are subtle and imperceptible to the human eye. The first 8 bits signify the lenght of the encoded message which results in a max char lenghth of 2^8 = 256.

### Encoding Process

1. **Text to Binary Conversion**: The plaintext message is converted into binary form, including the length of the message.
2. **Binary Embedding**: Each bit of the binary message is embedded into the least significant bit of the corresponding color channel of each pixel in the image.
3. **Image Output**: The modified image is saved with the embedded message.

### Decoding Process

1. **Binary Extraction**: The least significant bit of each color channel in the encoded image is extracted.
2. **Binary to Text Conversion**: The extracted binary message is converted back into the original plaintext using the stored message length.
3. **Message Retrieval**: The decoded message is presented to the user.

## Screenshots

![Encode Tab](screenshots/encode_tab.png)
![Decode Tab](screenshots/decode_tab.png)

## Getting Started

### Prerequisites

- Python 3.x
- Required Python packages (PySimpleGUI, OpenCV, NumPy, Pillow)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repository.git
