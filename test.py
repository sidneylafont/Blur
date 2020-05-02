from PIL import Image
import numpy as np

picName = 'images/pre1.jpg'

img = Image.open(picName)
ary = np.array(img)

print(len(ary))

for x in ary:
    print(len(x) == len(ary))