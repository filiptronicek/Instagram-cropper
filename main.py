from PIL import Image
import urllib.request
from io import BytesIO
import os


photoPath = input("your desired photo URL")

print(photoPath)

file = BytesIO(urllib.request.urlopen(photoPath).read())
img = Image.open(file)
width, height = img.size

for i in range(6):
    realIndex = i + 1
    if realIndex <= 3:
        leftUp = (width/3)*i
        rightDown = (width/3)*realIndex
        b=(leftUp,0,rightDown,height/2)
    else:
        leftUp = (width/3)*(i-3)
        rightDown = (width/3)*(realIndex-3)
        b=(leftUp,height/2,rightDown,height)
    print(b)
    c_i=img.crop(box=b)
    c_i.save(os.path.dirname(os.path.realpath(__file__))+"/images/"+str(realIndex)+".png")