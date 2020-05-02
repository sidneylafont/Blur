from PIL import Image
import numpy as np
import sys


def main():
    picName = sys.argv[1]

    img = Image.open(picName)
    ary = np.array(img)
    imageLength = len(ary)

    newImage = []

    for x in range(0, imageLength):
        newRow = []
        for y in range(0, imageLength):
            surroundingCells = surrounding(x, y, imageLength - 1)
            surroundingCellsRGB = []
            for sc in surroundingCells:
                if sc is None:
                    surroundingCellsRGB.append(None)
                else:
                    surroundingCellsRGB.append(ary[sc[0]][sc[1]])
            newRGB = gaussianAvg(surroundingCellsRGB)
            newRow.append(newRGB)
        newImage.append(newRow)

    finalImage = np.array(newImage)
    for x in range(0, imageLength):
        for y in range(0, imageLength):
            ary[x][y][0] = finalImage[x][y][0]
            ary[x][y][1] = finalImage[x][y][1]
            ary[x][y][2] = finalImage[x][y][2]


    postImage = Image.fromarray(ary, 'RGB')
    postImage.save("images/" + picName[7:-4] + "blurred.jpg")
    print("done")


def surrounding(x, y, l):
    cellCords = [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1), (x, y - 1), (x, y),
                 (x, y + 1), (x + 1, y - 1), (x + 1, y), (x + 1, y + 1)]

    for c in range(0, len(cellCords)):
        if cellCords[c][0] == -1 or cellCords[c][1] == -1 or cellCords[c][0] == l + 1 or cellCords[c][1] == l + 1:
            cellCords[c] = None

    return cellCords


def gaussianAvg(rgb):
    gMultipliers = [1, 2, 1, 2, 4, 2, 1, 2, 1]
    denominator = 0
    numeratorR = 0
    numeratorB = 0
    numeratorG = 0

    for c in range(0, len(gMultipliers)):
        if not (rgb[c] is None):
            denominator += gMultipliers[c]
            numeratorR = numeratorR + (gMultipliers[c] * rgb[c][0])
            numeratorG = numeratorG + (gMultipliers[c] * rgb[c][1])
            numeratorB = numeratorB + (gMultipliers[c] * rgb[c][2])

    newPixel = [numeratorR // denominator, numeratorG // denominator, numeratorB // denominator]
    return newPixel


main()
