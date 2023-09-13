#!/usr/bin/python
# img_to_pdf.py
# Code for combining images all in the same dir to a single PDF
# (C) Brice Turner, 2023
import os
import numpy as np
import imageio
from PIL import Image, ImageDraw, ImageFont

def convert_to_rgb(image_path):
    # load images as 16-bit np array
    img_array = imageio.v2.imread(image_path)

    # if already 8-bit or RGB, use Pillow
    if img_array.dtype == np.uint8:
        return Image.open(image_path).convert('RGB')
    
    # rescale 16-bit to 8-bit
    scaled_array = ((img_array - img_array.min()) / (img_array.max() - img_array.min()) * 255).astype(np.uint8)
    
    # convert the 8-bit data back to  image
    img = Image.fromarray(scaled_array)
    
    return img.convert('RGB')

def draw_header_footer(img, filename):
    """Draw text on top and bottom of the image."""
    draw = ImageDraw.Draw(img)
    width, height = img.size
    font = ImageFont.truetype("arial.ttf", 100)  # Adjust font size as required
    bbox = draw.textbbox((0, 0), "Footer text", font=font)
    text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
    
    # Top text
    x = (width - text_width) // 2
    y = 100  # 100 pixels from the top
    draw.text((x, y), "header text", fill="green", font=font)
    
    # Bottom text
    y = height - text_height - 100  # 100 pixels from the bottom
    draw.text((x, y), "Footer text", fill="green", font=font)

    # Add filename text
    font_filename = ImageFont.truetype("arial.ttf", 75)  # Adjust font size as required
    x_filename = width - 10  # 10 pixels from the right side
    y_filename = 10  # 10 pixels from the top
    draw.text((x_filename, y_filename), filename, fill="yellow", font=font_filename, anchor="rt")
    
    return img

def images_to_pdf(directory, output_filename, extension=".tif"):
    # take all files within given dir with given extension
    files = [f for f in os.listdir(directory) if f.endswith(extension)]
    files.sort()  # sort files

    # catch-all if nothing found
    if not files:
        print(f"No images with extension {extension} found in {directory}.")
        return

    # open the first image, convert it to RGB
    first_img = draw_header_footer(convert_to_rgb(os.path.join(directory, files[0])), files[0])
    # convert all to RGB and add to list
    imgs = [draw_header_footer(convert_to_rgb(os.path.join(directory, f)), f) for f in files[1:]]

    # safe to PDF
    first_img.save(output_filename, save_all=True, append_images=imgs)
    print(f"Saved {len(files)} images to {output_filename}.")

if __name__ == "__main__":
    dir_path = "C:\\path\\to\\files"
    # output file name
    base_name = "output_pdf_name"
    # keep this as PDF
    extension = ".pdf"

    # index ensures files don't get replaced when repeatedly running
    index = 0 
    output_pdf = f"{base_name}{index}{extension}"
    while os.path.exists(output_pdf):
        index += 1
        output_pdf = f"{base_name}{index}{extension}"

    # change if needed. default is tif
    ext = ".tif" 

    # run it
    images_to_pdf(dir_path, output_pdf, ext)