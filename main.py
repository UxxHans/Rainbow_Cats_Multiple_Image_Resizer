import os
import math
from PIL import Image

# Set image size here: (Width, Height)
resize_size = [500, 1000]

# Set the only type of extension you want to resize, eg. ".png" or set ".*" to resize every file
extension_name = ".*"


def main():

    # Set the counter
    counter = 0

    # Resize every image found in all folders and sub-folders in "Input Images"
    for root, dirs, files in os.walk("Input"):
        for file in files:
            # If the file has certain extension name
            if file.endswith(extension_name) or extension_name == ".*":
                # Resize and save the image
                resize_image(os.path.join(root, file),
                             "Output/" + "Resized_" + str(counter) + "_" + file,
                             resize_size[0], resize_size[1])
                # Add up the counter
                counter += 1


def resize_image(source_image_path, save_image_path, resize_width, resize_height):

    # Create pillow image
    final_image = Image.open(source_image_path)
    print("Before Resizing:", final_image.size)

    # Process image
    width = final_image.width
    height = final_image.height
    resize_aspect = resize_width/resize_height
    source_aspect = width/height

    # Find the best fit position in the canvas
    if source_aspect < resize_aspect:
        final_image = resize_canvas(final_image, math.floor(height * resize_aspect), height)
    elif source_aspect > resize_aspect:
        final_image = resize_canvas(final_image, width, math.floor(width / resize_aspect))

    # Resize the image
    final_image = final_image.resize((resize_width, resize_height))

    # Output image
    final_image.save(save_image_path)
    print("After resizing:", final_image.size)


def resize_canvas(source_image, canvas_width, canvas_height):

    # Declare the variables
    x1_position, y1_position, x2_position, y2_position, background = 0, 0, 0, 0, 0

    # Load the image
    image_pixels = source_image.load()
    image_width, image_height = source_image.size

    # Set the canvas background color
    mode = source_image.mode
    if len(mode) == 1:  # L, 1
        # Center the image
        x1_position = math.floor((canvas_width - image_width) / 2)
        y1_position = math.floor((canvas_height - image_height) / 2)
        x2_position = x1_position + image_width
        y2_position = y1_position + image_height

        # Fill background with white
        background = 255

    if len(mode) == 3:  # RGB
        # Center the image
        x1_position = math.floor((canvas_width - image_width) / 2)
        y1_position = math.floor((canvas_height - image_height) / 2)
        x2_position = x1_position + image_width
        y2_position = y1_position + image_height

        # Fill background with white
        background = (255, 255, 255)

    if len(mode) == 4:  # RGBA
        # Find position of the image in canvas
        top = False
        left = False
        bottom = False
        right = False

        # If there is pixel on the edge, stick the image on it in the canvas
        for y in range(image_height):
            for x in range(image_width):
                if x == 0:
                    if image_pixels[x, y][3] != 0:
                        left = True
                        continue
                elif x == image_width - 1:
                    if image_pixels[x, y][3] != 0:
                        right = True
                        continue
                elif y == 0:
                    if image_pixels[x, y][3] != 0:
                        bottom = True
                        continue
                elif y == image_height - 1:
                    if image_pixels[x, y][3] != 0:
                        top = True
                        continue

        # Top image
        if top:
            if left:
                x1_position = 0
                y1_position = canvas_height - image_height
                x2_position = x1_position + image_width
                y2_position = y1_position + image_height
            elif right:
                x1_position = canvas_width - image_width
                y1_position = canvas_height - image_height
                x2_position = x1_position + image_width
                y2_position = y1_position + image_height
            else:
                x1_position = math.floor((canvas_width - image_width) / 2)
                y1_position = canvas_height - image_height
                x2_position = x1_position + image_width
                y2_position = y1_position + image_height

        # Bottom image
        elif bottom:
            if left:
                x1_position = 0
                y1_position = 0
                x2_position = x1_position + image_width
                y2_position = y1_position + image_height
            elif right:
                x1_position = math.floor((canvas_width - image_width))
                y1_position = 0
                x2_position = x1_position + image_width
                y2_position = y1_position + image_height
            else:
                x1_position = math.floor((canvas_width - image_width) / 2)
                y1_position = 0
                x2_position = x1_position + image_width
                y2_position = y1_position + image_height

        # Left image
        elif left:
            x1_position = 0
            y1_position = math.floor((canvas_height - image_height) / 2)
            x2_position = x1_position + image_width
            y2_position = y1_position + image_height

        # Right image
        elif right:
            x1_position = canvas_width - image_width
            y1_position = math.floor((canvas_height - image_height) / 2)
            x2_position = x1_position + image_width
            y2_position = y1_position + image_height

        # Center the image
        else:
            x1_position = math.floor((canvas_width - image_width) / 2)
            y1_position = math.floor((canvas_height - image_height) / 2)
            x2_position = x1_position + image_width
            y2_position = y1_position + image_height

        # Set background to transparent
        background = (255, 255, 255, 0)

    # Create empty canvas
    output_image = Image.new(mode, (canvas_width, canvas_height), background)
    # Paste the image in canvas
    output_image.paste(source_image, (x1_position, y1_position, x2_position, y2_position))
    # Return image
    return output_image


main()
