# Steganography Tool with PySimpleGUI

A simple Python-based Steganography Tool that allows encoding and decoding messages to and from an image in a UI. The tool utilizes the Least Significant Bit (LSB) approach, embedding and extracting information in the least significant bit of each color channel of the image.

## Least Significant Bit (LSB) Approach

The LSB approach used involves manipulating the least significant bit of each pixel in the image without significantly altering the visual appearance. In this tool, the LSB of each color channel (Red, Green, and Blue) is used to store binary information. This approach ensures that the modifications are subtle and imperceptible to the human eye. The first 8 bits signify the lenght of the encoded message which results in a max char lenghth of 2^8 = 256.

## How to Run

### Prerequisites

- Python 3.x
- Required Python packages (PySimpleGUI, OpenCV, NumPy, Pillow)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/laurentcasagrande/Steganography-Tool-with-PySimpleGUI.git

2. Install dependencies:
   
   ```bash
   pip install -r requirements.txt

3. Run the main.py script

OR

use the underlying functions directly

```bash
result_file_path = encode("path/to/input/image.png", "Your secret message")
decoded_message = decode("path/to/encoded/image.png")
