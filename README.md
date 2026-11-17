# Image to Sketch Converter 🎨

A Python-based Image to Sketch Converter that transforms ordinary images into pencil sketch-style artwork using **OpenCV** and image processing techniques. The application also supports capturing images directly through a webcam and converting them into sketches.

## ✨ Features

- **Image to Sketch Conversion:** Convert existing images into pencil sketches.
- **Webcam Capture:** Capture images directly using your computer's webcam.
- **Grayscale Conversion:** Convert input images into grayscale.
- **Image Inversion:** Generate inverted versions of grayscale images.
- **Gaussian Blur:** Apply Gaussian blur to create the pencil sketch effect.
- **Multiple Output Images:** Save intermediate processing stages along with the final sketch.
- **Automatic Folder Management:** Organise generated images into separate folders.
- **Input Validation:** Handle invalid image paths and unsupported image files.
- **Error Handling:** Handle webcam, image-reading and file-saving errors.

## 🛠️ Technologies Used

- **Python** – Core programming language
- **OpenCV** – Image processing and webcam access
- **NumPy** – Numerical operations on image data
- **Pathlib** – File and directory management

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/RaavanHrishi07/Image-to-Sketch-Converter.git
```

### 2. Navigate to the Project Directory

```bash
cd Image-to-Sketch-Converter
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

Alternatively, install the required packages directly:

```bash
python -m pip install opencv-python numpy
```

## 🚀 How to Run

Start the application using:

```bash
python sketchScript.py
```

The application displays the following menu:

```text
========================================
       IMAGE TO SKETCH CONVERTER
========================================

1 - Capture image using webcam
2 - Convert an existing image
3 - Exit
```

### Option 1: Capture an Image Using Webcam

1. Select option `1`.
2. Allow webcam access if prompted.
3. The application captures an image.
4. Enter a name for the output folder.
5. The captured image is converted into a pencil sketch.

### Option 2: Convert an Existing Image

1. Select option `2`.
2. Enter the path of the image.
3. Enter a name for the output folder.
4. The application processes the image and generates the sketch.

Example:

```text
Enter the input image path: images-trial/hulk.jpg

Enter a name for the output folder: hulk
```

### Option 3: Exit

Select option `3` to close the application.

## 🔬 How Image Processing Works

The application uses a pencil sketch conversion technique based on grayscale conversion, image inversion, Gaussian blur and image division.

**Processing Workflow:**

1. **Grayscale Conversion:** The original image is converted into grayscale.
2. **Image Inversion:** The grayscale image is inverted.
3. **Gaussian Blur:** A Gaussian blur is applied to the inverted image.
4. **Second Inversion:** The blurred image is inverted again.
5. **Image Division:** The grayscale image is divided by the inverted blurred image to produce the pencil sketch effect.

### Processing Formula

```python
pencil_sketch = cv2.divide(
    gray,
    inverted_blurred,
    scale=256.0
)
```

## 📂 Project Structure

```text
Image-to-Sketch-Converter/
│
├── sketchScript.py
├── requirements.txt
├── README.md
├── haarcascade_frontalface_default.xml
│
├── images-trial/
│   └── Sample input images
│
├── sketches/
│   └── Generated sketch outputs
│
└── webcam/
    └── data/
        └── Captured webcam images
```

*Note: Generated images and local test images are excluded from version control.*

## 🖼️ Output Files

For every successful conversion, the application generates four images:

| Output File | Description |
|---|---|
| `(gray).png` | Grayscale version of the input |
| `(inverted).png` | Inverted grayscale image |
| `(blurred).png` | Blurred image |
| `(final).png` | Final pencil sketch |

The generated files are saved inside:

```text
sketches/<output-folder-name>/
```

## 📦 Requirements

- Python 3.10 or later
- OpenCV (`opencv-python`)
- NumPy
- A webcam (only required for webcam capture)

## 🧰 Troubleshooting

**1. OpenCV Module Not Found**

Install OpenCV using:

```bash
python -m pip install opencv-python
```

**2. NumPy Module Not Found**

```bash
python -m pip install numpy
```

**3. Webcam Not Opening**

- Check whether your webcam is connected.
- Allow camera permissions.
- Close other applications that may be using the webcam.

**4. Image File Not Found**

- Verify the image path.
- Make sure the file exists.
- Use the correct file extension and path.

## 🔮 Future Improvements

- Graphical User Interface (GUI).
- Adjustable sketch intensity and blur settings.
- Support for additional image-processing effects.
- Face detection integration.
- Batch image conversion.

## 👨‍💻 Author

**Hrishikesh Sharma**

GitHub: [@RaavanHrishi07](https://github.com/RaavanHrishi07)

## ⭐ Support

If you find this project useful, consider giving the repository a star on GitHub!

---

*Built with Python and OpenCV.*