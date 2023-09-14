import busio
import board
from digitalio import DigitalInOut

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from adafruit_epd.ssd1680 import Adafruit_SSD1680  

# create the spi device and pins we will need
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
ecs = DigitalInOut(board.D8)
dc = DigitalInOut(board.D22)
srcs = None
rst = DigitalInOut(board.D27)
busy = DigitalInOut(board.D17)

# give them all to our driver
display = Adafruit_SSD1680(122, 250,        # 2.13" HD Tri-color or mono display
    spi,
    cs_pin=ecs,
    dc_pin=dc,
    sramcs_pin=srcs,
    rst_pin=rst,
    busy_pin=busy,
)
display.rotation = 1

# Create blank image for drawing.
width = display.width
height = display.height
image = Image.new("RGB", (width, height))

WHITE = (0xFF, 0xFF, 0xFF)
BLACK = (0x00, 0x00, 0x00)

# Get drawing object to draw on image. Also text is drawn.
draw = ImageDraw.Draw(image)
# empty it
draw.rectangle((0, 0, width, height), fill=WHITE)

# Load default font.
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)

# Alternatively load a TTF font.  Make sure the .ttf font
# file is in the same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
# font = ImageFont.truetype('Minecraftia.ttf', 8)

def makeText(t1, t2, t3, t4):

    draw.text((20, 5), t1, font=font, fill=BLACK)
    draw.text((20, 35), t2, font=font, fill=BLACK)
    draw.text((20, 65), t3, font=font, fill=BLACK)
    draw.text((20, 95), t4, font=font, fill=BLACK)

    display.image(image)
    display.display()

    return "...display ready..."
