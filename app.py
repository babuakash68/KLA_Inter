from PIL import Image, ImageChops

img =   Image.open('Level_1_data/wafer_image_1.png')
img2=   Image.open('Level_1_data/wafer_image_2.png')
img3=   Image.open('Level_1_data/wafer_image_3.png')
img4=   Image.open('Level_1_data/wafer_image_4.png')

diff = ImageChops.difference(img, img2)

print(diff.getbbox())