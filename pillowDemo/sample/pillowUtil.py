import time
import urllib.parse
from typing import List

from PIL import Image
from PIL import ImageDraw, ImageFont

basicMode = {
    'url': 'template/test.png'
}
headerMode = {
    'url': 'template/header_base.png',
    'frame_width': 710,
    'frame_height': 400,
}

frontMode = {
    "color": (0, 0, 0),
    "size": 20,
    "ttf": 'simkai.ttf',
}
descMode = {
    'color': (0, 0, 0),
    'size': 10,
    'ttf': 'simkai.ttf',
}
defaultTextMode = {
    'color': (0, 0, 0),
    'size': 10,
    'ttf': 'simkai.ttf',
}


def get_file_name(fileName):
    return '测试'


def save_img(path, png):
    filenameTime = time.strftime('%Y%m%d%H%M%S', time.localtime())
    png.save(f"out/{path}/Img-{filenameTime}.png")


def write_text(img: Image, text: List[str], frontFormat):  # 写文本
    box = img.getbbox()
    print(box[0], box[1], box[2], box[3])
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(frontFormat["ttf"], size=frontFormat["size"])
    # 重新计算x轴，需要剔除字符 一半 的长度，用于居中
    width, height = font.getsize(text[0])
    beginY = 2
    # 参数：位置、文本、填充、字体
    # 给单个文本框填充数据
    index = 0
    for textItem in text:
        widthItem, heightItem = font.getsize(textItem)
        realX = (box[2] - widthItem) / 2
        realY = beginY
        if index > 0:
            realY += height * index
        index += 1
        draw.multiline_text((realX, realY), textItem, frontFormat["color"], font=font)
    return img


def save_file_demo():
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

    filenameTime = time.strftime('%Y%m%d%H%M%S', time.localtime())
    final2.save(f"out/headerImg-{filenameTime}.png")
    testPng.paste(final2, (0, 20))
    # imagedata = requests.get(imgUrl)
    # img1 = Image.open(BytesIO(imagedata.content))
    # img1.save("download")
    # baseImg.paste(img1, (0, 0))
    # remark = '售价xxxxxxxx套，xxxxxxxxxx通宝'
    testPng.save(f"out/out-{filenameTime}.png")


def save_file_header_img():
    basePng = Image.open('template/really_item_background.png').convert("RGBA")
    wantedPng = Image.open('template/base-pic.png').convert("RGBA")
    final2 = Image.new("RGBA", basePng.size)

    final2 = Image.alpha_composite(final2, basePng)
    final2 = final2.resize(wantedPng.size)
    final2 = Image.alpha_composite(final2, wantedPng)
    filenameTime = time.strftime('%Y%m%d%H%M%S', time.localtime())
    final2.save(f"out/header/headerImg-{filenameTime}.png")
    return final2


def save_file_header_txt():
    basePng = Image.open('template/header_text_base.png')
    img = write_text(basePng, ["金发·璨月蝶心"], frontMode)
    filenameTime = time.strftime('%Y%m%d%H%M%S', time.localtime())
    img.save(f"out/header/headerText-{filenameTime}.png")
    return img


def save_file_desc_txt():
    basePng = Image.open('template/header_text_base.png')
    img = write_text(basePng, ["不绑定限时3周。售价280。"], frontMode)
    filenameTime = time.strftime('%Y%m%d%H%M%S', time.localtime())
    img.save(f"out/header/headerDesc-{filenameTime}.png")
    return img


def save_file_head():
    headerTextPng = save_file_header_txt()
    headerImgPng = save_file_header_img()
    headerDescPng = save_file_desc_txt()
    testPng = Image.open('template/test.png').convert("RGBA")
    headerTextSize = headerTextPng.size
    headerImgSize2 = headerImgPng.size
    testPng.paste(headerImgPng, (0, 0))
    testPng.paste(headerTextPng, (0, headerImgSize2[1]))
    testPng.paste(headerDescPng, (0, headerImgSize2[1] + headerTextSize[1]))
    filenameTime = time.strftime('%Y%m%d%H%M%S', time.localtime())
    testPng.save(f"out/out-{filenameTime}.png")


def create_real_base():
    basePng = Image.open('template/header_base.png').convert("RGBA")
    basePng2 = Image.open('template/header_second_base_img.png').convert('RGBA')
    final2 = Image.new("RGBA", basePng2.size)
    png1 = basePng.resize(final2.size)
    png1 = Image.alpha_composite(png1, basePng2)
    basePng2Size = png1.size
    basePngSize = basePng.size
    basePng.paste(png1, (int((basePngSize[0] - basePng2Size[0]) / 2), 0))
    filenameTime = time.strftime('%Y%m%d%H%M%S', time.localtime())
    basePng.save(f"out/header/headerImg-{filenameTime}.png")


def save_price_img():
    img_base_path = 'template/price/'
    # 时间戳
    base_date_img_path = img_base_path + 'price_base_date.png'
    dateImg = Image.open(base_date_img_path)
    dateImg = write_text(dateImg, ['2023-03-02'], defaultTextMode)
    save_img('price/date', dateImg)
    # 服务器
    base_server_name_img_path = img_base_path + 'price_base_service_name.png'
    server_name_img = Image.open(base_server_name_img_path)
    server_name_img = write_text(server_name_img, ['斗转星移'], defaultTextMode)
    save_img('price/server_name', server_name_img)
    # 金额
    base_price_img_path = img_base_path + 'price_base_service_price.png'
    price_img = Image.open(base_price_img_path)
    price_img = write_text(price_img, ['269888'], defaultTextMode)
    save_img('price/price', price_img)
    # 售卖状态
    state_img_path = img_base_path + 'price_base_service_state.png'
    state_img = Image.open(state_img_path)
    state_img = write_text(state_img, ['在售'], defaultTextMode)
    save_img('price/state', state_img)
    # 把所有图片都拼起来
    base_img_path = img_base_path + 'price_base.png'
    base_img = Image.open(base_img_path)
    widthIndex = 0
    # 时间
    base_img.paste(dateImg, (widthIndex, 0))
    # 服务器
    dateImgSize = dateImg.size
    widthIndex += dateImgSize[0]
    base_img.paste(server_name_img, (widthIndex, 0))
    # 金额
    server_name_img_size = server_name_img.size
    widthIndex += server_name_img_size[0]
    base_img.paste(price_img, (widthIndex, 0))
    # 售卖状态
    price_img_size = price_img.size
    widthIndex += price_img_size[0]
    base_img.paste(state_img, (widthIndex, 0))
    save_img('price', base_img)
    # basePng = Image.open(img_base_path + 'price_base.png').convert("RGBA")
