from PIL import Image, ImageDraw, ImageFont

backMode = {  # 背景图属性，我的背景图上需要添加一个二维码和多个文本框
    "back_url": "timg.jpg",
    "size": (550, 363),
    "QR": {  # 二维码属性
        "frame": (130, 130),  # 大小
        "position": (380, 200),  # 位置
    },
    "name": {  # 文本框属性
        "size": 25,  # 字号
        "ttf": "FZXBSJW.TTF",  # 字体
        "color": "",  # 颜色
        "position": (20, 40),
        "frame": (300, 20),
    },
    "remark": {
        "size": 25,  # 字号
        "ttf": "FZXBSJW.TTF",  # 字体
        "color": "",  # 颜色
        "position": (20, 40),
        "frame": (300, 20),
    }
}


def write_line(img, text, x, y):
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font='simkai.ttf', size=20)
    # 参数：位置、文本、填充、字体
    # 给单个文本框填充数据
    draw.multiline_text((x, y), text, (255, 0, 0), font=font)


def write_text(img: Image, text):  # 写文本
    box = img.getbbox()
    print(box[0], box[1], box[2], box[3])
    # 取中间的位置 高就去 box[1],宽去 box[2]的一半
    write_line(img, text, x=box[2] / 2 , y=box[0] )
    return img
