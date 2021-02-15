from cv2 import cv2
from PIL import Image
from numpy import asarray

url = './wafer_image_$.png'
url_destination = './img_$_gray.jpg';
image = []
image_gray = []

for i in range (0, 5) :

    current_url = url.replace('$', str(i + 1))
    image.append(cv2.imread(current_url))
    image_gray.append(cv2.cvtColor(image[i], cv2.COLOR_BGR2GRAY))

for i in range (0, 5) :

    current_url = url_destination.replace('$', str(i + 1))
    cv2.imwrite(current_url, image_gray[i])


for i in range(0, 5) :

    current_url = url.replace('$', str(i + 1))
    data = asarray(image[i])
    print(type(data))
    print(data.shape)

    new_image = Image.fromarray(data)
    print(type(new_image))
    print(new_image.mode)
    print(new_image.size)
    print(data)
    image2 = Image.fromarray(data)
    row = len(data)
    col = len(data[0])
    for i in range(row):
        for j in range(col):
            if (data_1[i][j] != data_2[i][j]):
                print(str(i) + " " + str(j))
