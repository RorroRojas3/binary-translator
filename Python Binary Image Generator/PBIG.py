from random import *
import sys
from PIL import Image
import binascii
def string2bits(s=''):
    return [bin(ord(x))[2:].zfill(8) for x in s]

def bits2string(b=None):
    return ''.join([chr(int(x, 2)) for x in b])

s = sys.argv[1]

b = string2bits(s)

z = 0
while(z < 30):

    imageOrder = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    # print('String:')
    # print(s)
    #
    # print('\nList of Bits:')
    # for x in b:
    #     print(x)
    #
    # print('\nString:')
    # print(s2)
    BinDigits = ['', '', '', '', '', '', '', '']
    n = 0
    print(b)
    while(n < 8):

        a = int(b[0][n])

        BinDigits[n] = 'Zero.jpg'
        if(a == 1):
            BinDigits[n] = 'One.jpg'


        n += 1
    Spaces = ['', '', '', '', '','','','','']
    Empty = 0
    while(Empty < 9):
        Spaces[Empty] = "Space.jpg"
        Empty += 1


    x = 0
    images = map(Image.open, BinDigits)
    # widths, heights = zip(*(i.size for i in images))
    total_width = (430)*9
    max_height = (430)*9

    new_im = Image.new('RGB', (total_width, max_height), (150, 155, 155, 0))

    Rand = randint(0, 8)
    imageOrder[Rand] = 1
    f = 1
    for i in imageOrder:
        if(i == 1):
            images = map(Image.open, BinDigits)
            x_offset = 0

            y_offset = ((f)*400)
            f+=1

            for im in images:
                new_im.paste(im, (x_offset,y_offset))
                x_offset += 400
        if(i == 0):
            images = map(Image.open, Spaces)
            x_offset = 0

            y_offset = ((f)*400)
            f+=1
            for im in images:
                new_im.paste(im, (x_offset,y_offset))
                x_offset += 400
    num = str(z)
    new_im.save(s+num+'.jpg')
    z += 1
