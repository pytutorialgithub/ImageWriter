

# β Write "Hello World" onΒ MyImage.png

from PIL import Image, ImageDraw, ImageFont # ποΈ Import modules from PIL


my_text = "Hello World" # ποΈ Text to add to Image

font_path = "font/AgentOrange.ttf" # ποΈ Font .ttf Path

font_size = 100 # ποΈ Font Size

x, y = 50, 30 # ποΈ top left corner of the text

img = Image.open(f'images/MyImage.png') # ποΈ Open Image

dr = ImageDraw.Draw(img) # ποΈ Create New Image

my_font = ImageFont.truetype(font_path, font_size) # ποΈ Initialize Font

dr.text((x, y), my_text, font=my_font) # ποΈ Add text to image

img.save("dest/new_img.png") # ποΈ save Image


# --------------------------------




# β Center "Hello World" onΒ MyImage.png

from PIL import Image, ImageDraw, ImageFont # ποΈ Import modules from PIL


my_text = "Hello World" # ποΈ Text to add to Image

font_path = "font/AgentOrange.ttf" # ποΈ Font .ttf Path

font_size = 100 # ποΈ Font Size

x, y = 250, 250 # ποΈ top left corner of the text

img = Image.open(f'images/MyImage.png') # ποΈ Open Image

dr = ImageDraw.Draw(img) # ποΈ Create New Image

my_font = ImageFont.truetype(font_path, font_size) # ποΈ Initialize Font

dr.text((x, y), my_text, font=my_font) # ποΈ Add text to image

img.save("dest/img_text_center.png") # ποΈ save Image


# --------------------------------




# β Set Color to "Hello World" onΒ MyImage.png

from PIL import Image, ImageDraw, ImageFont # ποΈ Import modules from PIL


my_text = "Hello World" # ποΈ Text to add to Image

font_path = "font/AgentOrange.ttf" # ποΈ Font .ttf Path

font_size = 100 # ποΈ Font Size

x, y = 250, 250 # ποΈ top left corner of the text

color = "yellow" # ποΈ Color

img = Image.open(f'images/MyImage.png') # ποΈ Open Image

dr = ImageDraw.Draw(img) # ποΈ Create New Image

my_font = ImageFont.truetype(font_path, font_size) # ποΈ Initialize Font

dr.text((x, y), my_text, font=my_font, fill=color) # ποΈ Add text to image

img.save("dest/img_text_color.png") # ποΈ save Image


# --------------------------------



# β Set RGB Color to "Hello World" onΒ MyImage.png

from PIL import Image, ImageDraw, ImageFont # ποΈ Import modules from PIL


my_text = "Hello World" # ποΈ Text to add to Image

font_path = "font/AgentOrange.ttf" # ποΈ Font .ttf Path

font_size = 100 # ποΈ Font Size

x, y = 250, 250 # ποΈ top left corner of the text

rgb_color = (255,0,0,255) # ποΈ Rgb Color

img = Image.open(f'images/MyImage.png') # ποΈ Open Image

dr = ImageDraw.Draw(img) # ποΈ Create New Image

my_font = ImageFont.truetype(font_path, font_size) # ποΈ Initialize Font

dr.text((x, y), my_text, font=my_font, fill=color) # ποΈ Add text to image

img.save("dest/img_text_color_rgb.png") # ποΈ save Image


# --------------------------------




# β Set Color to "Hello" and "World" onΒ MyImage.png

from PIL import Image, ImageDraw, ImageFont # ποΈ Import modules from PIL


my_text = "Hello World" # ποΈ Text to add to Image

font_path = "font/AgentOrange.ttf" # ποΈ Font .ttf Path

font_size = 100 # ποΈ Font Size

x, y = 250, 250 # ποΈ top left corner of the text

colors = ["red", "yellow"] # Multi Colors

img = Image.open(f'images/MyImage.png') # ποΈ Open Image

dr = ImageDraw.Draw(img) # ποΈ Create New Image

my_font = ImageFont.truetype(font_path, font_size) # ποΈ Initialize Font

for color, word in zip(colors, my_text.split()): # ποΈ Loop over the colors and text split

    dr.text((x, y), word, font=my_font, fill=color) # ποΈ Add text to image
    x += x * 2 

img.save("dest/img_two_words.png") # ποΈ save Image



