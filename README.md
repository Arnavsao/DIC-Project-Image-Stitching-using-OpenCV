# Image Stitching Project

## Overview
This project automates the creation of panoramic images by stitching together multiple input images using Python and OpenCV. It seamlessly merges overlapping fields of view to produce high-quality panoramic views.

## Features
- **Automatic Stitching**: Effortlessly stitches multiple images into panoramic views.
- **Image Preprocessing**: Enhances image quality with grayscale conversion, thresholding, and contour detection before stitching.
- **Contour Analysis**: Identifies the largest contour in the stitched image to extract the region of interest.
- **User Interface**: Provides a simple command-line interface for specifying input image directories and viewing stitched results.

## Technologies Used
- **Python**: Primary programming language.
- **OpenCV**: Core library for image processing and stitching.
- **NumPy**: Facilitates efficient numerical computing and array operations.
- **imutils**: Offers utility functions for image processing tasks.
- **glob**: Enables file handling and path manipulation.

## Usage
1. Clone the repository.
2. Ensure Python and dependencies are installed.
3. Run the script, providing the input image directory.
4. View the resulting stitched output image.

## Contributions
Contributions are welcome! Feel free to submit pull requests for suggestions, bug fixes, or new features.

## License
This project is licensed under the MIT License.

## Acknowledgments
This project is inspired by the contributions of researchers and developers in computer vision and image processing.
