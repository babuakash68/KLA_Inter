import PIL
from PIL import Image, ImageChops

import json
from numpy import asarray

import json

with open('input.json') as f:
      jason_data = json.load(f)

list1 = []
print(jason_data)
for i in range(5):
    s1=("./wafer_image_"+str((i+1))+".png")
    img =   asarray(Image.open(s1).convert('LA'))
    list1.append([img])
s1=("./wafer_image_"+str((i+1))+".png")
img = asarray(Image.open(s1).convert('LA'))
row = len(img)
col = len(img[0])
s1=("./wafer_image_"+str((i+1))+".png")
img = asarray(Image.open(s1).convert('LA'))
row = len(img)
col = len(img[0])
res = []

for i in range(4):
    for j in range(row):
        for k in range(col):
            equal = 0
            not_equal = 0
            l=i+1
            for l in range(4-i):
               # print(list1[i + l + 1][j][k] - list1[i + l + 1][j][k])
                # print(list1[i][0][j][k][1])
                # print("t2", list1[i + l + 1][0][j][k][1])
                if (list1[i][0][j][k][0] != list1[i + l + 1][0][j][k][0]) or (list1[i][0][j][k][1] != list1[i + l + 1][0][j][k][1]):
                    # print("ano")
                    not_equal += 1
                else:
                    # print("check")
                    equal += 1
            # print(not_equal, "---", equal)        
            if(not_equal > equal):
                # print('hello')
                res.append([j , k , i + 1])
print(res)
res = []

for i in range(5):
    for j in range(row):
        for k in range(col):
            equal = 0
            not_equal = 0
            l=i+1
            for l in range(4 - i):
               # print(list1[i + l + 1][j][k] - list1[i + l + 1][j][k])
                # print(list1[i][0][j][k][1])
                # print("t2", list1[i + l + 1][0][j][k][1])
                if (list1[i][0][j][k][0] != list1[i + l + 1][0][j][k][0]) or (list1[i][0][j][k][1] != list1[i + l + 1][0][j][k][1]):
                    # print("ano")
                    not_equal += 1
                else:
                    # print("check")
                    equal += 1
            # print(not_equal, "---", equal)        
            if(not_equal > equal):
                # print('hello')
                res.append([j , k , i + 1])
    for j in range(row):
        for k in range(col):
            equal = 0
            not_equal = 0
            for l in range(4):
               # print(list1[i + l + 1][j][k] - list1[i + l + 1][j][k])
                # print(list1[i][0][j][k][1])
                # print("t2", list1[i + l + 1][0][j][k][1])
                if (list1[4][0][j][k][0] != list1[l][0][j][k][0]) or (list1[4][0][j][k][1] != list1[l][0][j][k][1]):
                    # print("ano")
                    not_equal += 1
                else:
                    # print("check")
                    equal += 1
            # print(not_equal, "---", equal)        
            if(not_equal > equal):
                # print('hello')
                res.append([j , k , i + 1])
 
s=open("output.csv",)
s.write(str(res))