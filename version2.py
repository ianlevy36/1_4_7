import PIL
import matplotlib.pyplot as plt
import os.path  
import PIL.ImageDraw            
from PIL import Image

def im_overlay():
    
    
    
    
    background = Image.open("test1.png")
    foreground = Image.open("test2.png")

    background.composite(foreground, background, )
    background.show()
def resize():
    imageFile = "bluefire.jpg"
    im1 = Image.open(imageFile)
    
    width = 500
    height = 420
    im2 = im1.resize((width, height), Image.NEAREST)
    ext = ".jpg"
    im2.save("redlightning" + ext)
   
    imageFile = "redlightning.jpg"
    im1 = Image.open(imageFile)
    
    width = 500
    height = 420
    im2 = im1.resize((width, height), Image.NEAREST)
    ext = ".jpg"
    im2.save("redlightning" + ext)
    
    imageFile = "city.jpg"
    im1 = Image.open(imageFile)
    
    width = 500
    height = 420
    im2 = im1.resize((width, height), Image.NEAREST)
    ext = ".jpg"
    im2.save("city" + ext)
    
    imageFile = "GreatGorgeLake.jpg"
    im1 = Image.open(imageFile)
    
    width = 500
    height = 420
    im2 = im1.resize((width, height), Image.NEAREST)
    ext = ".jpg"
    im2.save("GreatGorgeLake" + ext)
   
    imageFile = "Geopattern.jpg"
    im1 = Image.open(imageFile)
    
    width = 500
    height = 420
    im2 = im1.resize((width, height), Image.NEAREST)
    ext = ".jpg"
    im2.save("Geopattern" + ext)
    