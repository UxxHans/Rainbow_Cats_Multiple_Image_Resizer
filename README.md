# Rainbow_Cats_Multiple_Image_Resizer
Automatically resize and rearrange multiple images to keep the proportion and the position. For transparent image, it will detect and adjust the final position if the image is sticking on any side of the canvas.

<b>Guide:</b>

- Enter the target size and target extension name (if needed) in main.py.

- Throw image folders (without files other than images) or images into the "Input" folder.

- Run main.py and get results from "Output" folder.

<b>For Gray Scale and RGB (Not Transparent):</b>

- Resize the picture and keep the proportion.

- Center the picture in the canvas.

- Maximize the picture and fit it in the canvas.

<b>For RGBA (Transparent):</b>

- Resize the picture and keep the proportion.

- Find if the picture is sticking on any side in the canvas and keep that position.

- Maximize the picture according to it original size, transparent space is also counted.

![Image](https://github.com/UxxHans/Rainbow_Cats_Multiple_Image_Resizer/blob/main/Guide/BeforeAfter.jpg)
