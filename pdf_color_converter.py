# pip install pdf2image pillow

import os
import numpy as np
from pdf2image import convert_from_path
from PIL import Image

pdf_path = "/Users/eric/Downloads/L16_Mar7_Logistic.pdf"

images = convert_from_path(pdf_path)

converted_images = []

for img in images:
    arr = np.array(img)

    arr_original = arr.copy()

    white_mask = np.all(arr_original == [255, 255, 255], axis=-1)
    black_mask = np.all(arr_original == [0, 0, 0], axis=-1)

    arr[white_mask] = [0, 0, 0]
    arr[black_mask] = [255, 255, 255]

    converted_img = Image.fromarray(arr)
    converted_images.append(converted_img)

dirname = os.path.dirname(pdf_path)
filename, ext = os.path.splitext(os.path.basename(pdf_path))
output_pdf_path = os.path.join(dirname, f"{filename}_converted.pdf")

if converted_images:
    converted_images[0].save(
        output_pdf_path, 
        "PDF", 
        resolution=100.0,
        save_all=True, 
        append_images=converted_images[1:]
    )

print(f"Converted PDF saved to: {output_pdf_path}")


