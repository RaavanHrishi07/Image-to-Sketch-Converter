
"""
Image to Sketch Converter using OpenCV.

Features:
1. Capture an image using a webcam.
2. Convert an existing image into a pencil sketch.
3. Save grayscale, inverted, blurred and final sketch images.
"""

from datetime import datetime
from pathlib import Path
import re

import cv2
import numpy as np


# Project directories
BASE_DIR = Path(__file__).resolve().parent
SKETCHES_DIR = BASE_DIR / "sketches"
WEBCAM_DIR = BASE_DIR / "webcam" / "data"


def safe_folder_name(name: str) -> str:
    """Create a safe folder name for saving output images."""

    cleaned = re.sub(r'[<>:"/\\|?*]', "_", name.strip())
    cleaned = cleaned.rstrip(". ")

    return cleaned or f"sketch_{datetime.now():%Y%m%d_%H%M%S}"


def read_image(image_path: str | Path):
    """Read an image from the given path."""

    path = Path(image_path).expanduser()

    if not path.is_absolute():
        path = Path.cwd() / path

    if not path.is_file():
        print(f"\nError: Image file not found: {path}")
        return None

    try:
        image_data = path.read_bytes()

        image = cv2.imdecode(
            np.frombuffer(image_data, dtype=np.uint8),
            cv2.IMREAD_COLOR
        )

    except OSError as error:
        print(f"\nError: Could not read image: {error}")
        return None

    if image is None:
        print("\nError: Unsupported or corrupted image file.")
        return None

    return image


def save_image(image, destination: Path) -> bool:
    """Save an image to the specified destination."""

    try:
        success, encoded = cv2.imencode(
            destination.suffix or ".png",
            image
        )

        if not success:
            print(f"Error: Could not encode {destination.name}")
            return False

        destination.write_bytes(encoded.tobytes())
        return True

    except OSError as error:
        print(f"Error: Could not save image: {error}")
        return False


def convert(image_path: str | Path, output_name: str | None = None):
    """Convert an image into a pencil sketch."""

    image = read_image(image_path)

    if image is None:
        return None

    print()

    if output_name is None:
        output_name = input(
            "Enter a name for the output folder: "
        ).strip()

    folder_name = safe_folder_name(output_name)

    output_dir = SKETCHES_DIR / folder_name

    # Avoid overwriting previous conversions.
    if output_dir.exists():
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_dir = SKETCHES_DIR / f"{folder_name}_{timestamp}"

    output_dir.mkdir(parents=True, exist_ok=True)

    # Step 1: Convert image to grayscale.
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Step 2: Invert grayscale image.
    inverted = cv2.bitwise_not(gray)

    # Step 3: Apply Gaussian blur.
    blurred = cv2.GaussianBlur(
        inverted,
        (21, 21),
        0
    )

    # Step 4: Invert the blurred image.
    inverted_blurred = cv2.bitwise_not(blurred)

    # Step 5: Create the final pencil sketch.
    pencil_sketch = cv2.divide(
        gray,
        inverted_blurred,
        scale=256.0
    )

    # Save all processing stages.
    outputs = {
        f"{folder_name}(gray).png": gray,
        f"{folder_name}(inverted).png": inverted,
        f"{folder_name}(blurred).png": blurred,
        f"{folder_name}(final).png": pencil_sketch
    }

    for filename, processed_image in outputs.items():

        destination = output_dir / filename

        if not save_image(processed_image, destination):
            print("\nConversion stopped due to a saving error.")
            return None

    final_path = output_dir / f"{folder_name}(final).png"

    print("\nImage converted successfully!")
    print(f"Output folder: {output_dir}")
    print(f"Final sketch: {final_path}")

    return final_path


def open_cam():
    """Capture an image using the default webcam."""

    WEBCAM_DIR.mkdir(parents=True, exist_ok=True)

    camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    # Try the default backend if DirectShow is unavailable.
    if not camera.isOpened():
        camera.release()
        camera = cv2.VideoCapture(0)

    try:

        if not camera.isOpened():
            print(
                "\nError: Could not open webcam. "
                "Check camera connection and permissions."
            )
            return

        print("\nWebcam opened. Capturing image...")

        success, frame = camera.read()

        if not success or frame is None:
            print("\nError: Could not capture image from webcam.")
            return

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S_%f"
        )

        captured_path = WEBCAM_DIR / f"{timestamp}.png"

        if not save_image(frame, captured_path):
            return

        print(f"\nCaptured image saved: {captured_path}")

    finally:
        camera.release()

    # Convert captured image after releasing the camera.
    convert(captured_path)


def start():
    """Display the main application menu."""

    while True:

        print("\n========================================")
        print("       IMAGE TO SKETCH CONVERTER")
        print("========================================")

        print("1 - Capture image using webcam")
        print("2 - Convert an existing image")
        print("3 - Exit")

        choice = input("\nEnter your choice (1-3): ").strip()

        if choice == "1":
            open_cam()

        elif choice == "2":

            image_path = input(
                "\nEnter the input image path: "
            ).strip().strip('"')

            convert(image_path)

        elif choice == "3":

            print("\nThank you for using Image to Sketch Converter!")
            break

        else:

            print("\nInvalid choice. Please enter 1, 2 or 3.")


if __name__ == "__main__":
    start()
