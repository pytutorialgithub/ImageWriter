

# ✅ Write "Hello World" on MyImage.png

from PIL import Image, ImageDraw, ImageFont # 👉️ Import modules from PIL


my_text = "Hello World" # 👉️ Text to add to Image

font_path = "font/AgentOrange.ttf" # 👉️ Font .ttf Path

font_size = 100 # 👉️ Font Size

x, y = 50, 30 # 👉️ top left corner of the text

img = Image.open(f'images/MyImage.png') # 👉️ Open Image

dr = ImageDraw.Draw(img) # 👉️ Create New Image

my_font = ImageFont.truetype(font_path, font_size) # 👉️ Initialize Font

dr.text((x, y), my_text, font=my_font) # 👉️ Add text to image

img.save("dest/new_img.png") # 👉️ save Image


# --------------------------------




# ✅ Center "Hello World" on MyImage.png

from PIL import Image, ImageDraw, ImageFont # 👉️ Import modules from PIL


my_text = "Hello World" # 👉️ Text to add to Image

font_path = "font/AgentOrange.ttf" # 👉️ Font .ttf Path

font_size = 100 # 👉️ Font Size

x, y = 250, 250 # 👉️ top left corner of the text

img = Image.open(f'images/MyImage.png') # 👉️ Open Image

dr = ImageDraw.Draw(img) # 👉️ Create New Image

my_font = ImageFont.truetype(font_path, font_size) # 👉️ Initialize Font

dr.text((x, y), my_text, font=my_font) # 👉️ Add text to image

img.save("dest/img_text_center.png") # 👉️ save Image


# --------------------------------




# ✅ Set Color to "Hello World" on MyImage.png

from PIL import Image, ImageDraw, ImageFont # 👉️ Import modules from PIL


my_text = "Hello World" # 👉️ Text to add to Image

font_path = "font/AgentOrange.ttf" # 👉️ Font .ttf Path

font_size = 100 # 👉️ Font Size

x, y = 250, 250 # 👉️ top left corner of the text

color = "yellow" # 👉️ Color

img = Image.open(f'images/MyImage.png') # 👉️ Open Image

dr = ImageDraw.Draw(img) # 👉️ Create New Image

my_font = ImageFont.truetype(font_path, font_size) # 👉️ Initialize Font

dr.text((x, y), my_text, font=my_font, fill=color) # 👉️ Add text to image

img.save("dest/img_text_color.png") # 👉️ save Image


# --------------------------------



# ✅ Set RGB Color to "Hello World" on MyImage.png

from PIL import Image, ImageDraw, ImageFont # 👉️ Import modules from PIL


my_text = "Hello World" # 👉️ Text to add to Image

font_path = "font/AgentOrange.ttf" # 👉️ Font .ttf Path

font_size = 100 # 👉️ Font Size

x, y = 250, 250 # 👉️ top left corner of the text

rgb_color = (255,0,0,255) # 👉️ Rgb Color

img = Image.open(f'images/MyImage.png') # 👉️ Open Image

dr = ImageDraw.Draw(img) # 👉️ Create New Image

my_font = ImageFont.truetype(font_path, font_size) # 👉️ Initialize Font

dr.text((x, y), my_text, font=my_font, fill=color) # 👉️ Add text to image

img.save("dest/img_text_color_rgb.png") # 👉️ save Image


# --------------------------------




# ✅ Set Color to "Hello" and "World" on MyImage.png

from PIL import Image, ImageDraw, ImageFont # 👉️ Import modules from PIL


my_text = "Hello World" # 👉️ Text to add to Image

font_path = "font/AgentOrange.ttf" # 👉️ Font .ttf Path

font_size = 100 # 👉️ Font Size

x, y = 250, 250 # 👉️ top left corner of the text

colors = ["red", "yellow"] # Multi Colors

img = Image.open(f'images/MyImage.png') # 👉️ Open Image

dr = ImageDraw.Draw(img) # 👉️ Create New Image

my_font = ImageFont.truetype(font_path, font_size) # 👉️ Initialize Font

for color, word in zip(colors, my_text.split()): # 👉️ Loop over the colors and text split

    dr.text((x, y), word, font=my_font, fill=color) # 👉️ Add text to image
    x += x * 2 

img.save("dest/img_two_words.png") # 👉️ save Image



