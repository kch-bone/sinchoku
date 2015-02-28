# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont, ImageFilter

import sys

param = sys.argv

# 背景画像を開く
if param[1] == None:
    print "srcfile none"
src = Image.open(param[1])

sx = src.size[0]
sy = src.size[1]

#resizeを行う
if sx > sy :
    length = src.size[0]
else:
    length = src.size[1]

if length > 600:
    while length > 600:
        length = int(length*0.9)
        sx = int(sx*0.9)
        sy = int(sy*0.9)

else:
    while length < 600:
        length = int(length*1.1)
        sx = int(sx*1.1)
        sy = int(sy*1.1)


    
src.show()
img = src.resize((sx, sy), Image.ANTIALIAS)

# フォントセット
textFont = ImageFont.truetype("/System/Library/Fonts/ヒラギノ角ゴ ProN W6.otf", 40)
# テキストを貼り付ける Image を生成
textImg = Image.new("RGBA", (300, 100), (0, 0, 0, 0))
tmpDraw = ImageDraw.Draw(textImg)
# 貼り付けるテキスト

if int(param[2]) == 1:
    text = u"頑張りました！"
else:
    text = u""
# 影分を先に貼り付ける
tmpDraw.text((12, 2), text, font=textFont, fill="rgb(176, 196, 222)")
# 本体文字を貼り付ける
tmpDraw.text((10, 0), text, font=textFont, fill="black")
# 5 度傾ける
textImg = textImg.rotate(5)
# 背景画像に貼り付ける
img.paste(textImg, (sx-300, sy-100), textImg)
# 画像保存
img.show()
img.save("./output.png")