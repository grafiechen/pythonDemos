# This is a sample Python script.

import os
import urllib.parse

from PIL import Image
import time

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# filename = "template/test.png"
# baseImg = Image.open('template/test.png')
# name = '坠夜流金'
# pillowUtil.write_text(baseImg, name)
#
# name, ext = os.path.splitext(filename+"header")
# baseImg.save(f"{name}-header.png")

imgUrl = 'https://dl.pvp.xoyo.com/prod/icons/handbook/image/%E5%9D%A0%E5%A4%9C%E6%B5%81%E9%87%91%E7%A4%BC%E7%9B%92-%E8%AF%A6%E6%83%85-1.png'
imgName = urllib.parse.unquote(imgUrl)
itemName = imgName.split('/')
print('截取字符串', len(itemName), itemName[len(itemName) - 1])
realNameAll = itemName[len(itemName) - 1]
realNameAll = realNameAll.split('-')
print(realNameAll, realNameAll[0])
testPng = Image.open('template/test.png').convert("RGBA")
aPng = Image.open('template/base-pic.png').convert("RGBA")
final2 = Image.new("RGBA", testPng.size)

final2 = Image.alpha_composite(final2, testPng)
final2 = final2.resize(aPng.size)
final2 = Image.alpha_composite(final2, aPng)

testPng.paste(final2, (0, 20))
# imagedata = requests.get(imgUrl)
# img1 = Image.open(BytesIO(imagedata.content))
# img1.save("download")
# baseImg.paste(img1, (0, 0))
# remark = '售价xxxxxxxx套，xxxxxxxxxx通宝'
filenameTime = time.strftime('%Y%m%d%H%M%S', time.localtime())
testPng.save(f"out/out-{filenameTime}.png")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
