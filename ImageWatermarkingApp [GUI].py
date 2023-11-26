# GUI
from tkinter import *

root = Tk()
root.title("WATERMARKING APP")
root.geometry("1000x1000")







root.mainloop()


# # TEXT ON THE IMAGE (WATERMARK)
# from PIL import Image, ImageDraw, ImageFont

# # get an image
# with Image.open("Default.jpg").convert("RGBA") as base:

#     # make a blank image for the text, initialized to transparent text color
#     txt = Image.new("RGBA", base.size, (255, 255, 255, 0))

#     # get a font
#     fnt = ImageFont.truetype("C:/Windows.old/Windows/Fonts/times.ttf", size=80)
#     # fnt = ImageFont.load_default()
    
#     # get a drawing context
#     d = ImageDraw.Draw(txt)

#     # # draw text, half opacity
#     # d.text((10, 10), "Hello", font=fnt, fill=(255, 255, 255, 128))
#     # # draw text, full opacity
#     # d.text((10, 80), "World", font=fnt, fill=(255, 255, 255, 255))
    
    
#     # draw multiline text
#     d.multiline_text((10, 10), "Hello\nWorld", font=fnt, fill=(250, 250, 250, 128))

#     out = Image.alpha_composite(base, txt)

#     out.show()








# BASIC LINE DRAW ON THE IMAGE
# # import sys
# from PIL import Image, ImageDraw, ImageShow

# with Image.open("Default.jpg") as im:

#     draw = ImageDraw.Draw(im)
#     draw.line((0, 0) + im.size, fill=128)
#     draw.line((0, im.size[1], im.size[0], 0), fill=128)

#     # write to stdout
#     # im.save(sys.stdout, "PNG")
    
#     # show image
#     ImageShow.show(im, title=None)