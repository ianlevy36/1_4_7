import PIL
import matplotlib.pyplot as plt
import os.path  
import PIL.ImageDraw            
from PIL import Image

def convertimg():
    im1 = Image.open("bluefire.jpg")
    im2 = Image.open("redlighting.jpg")
    im3 = Image.open("city.jpg")
    im4 = Image.open("Geopattern.jpg")
    
    im3 = im3.convert("RGBA")
    im1 = im1.convert("RGBA")
    im4 = im4.convert("RGBA")
    im2 = im2.convert("RGBA")
    
    im5 = Image.blend(im2, im3, 0.6)
    im5.save("step1.png","PNG")
    im6 = Image.blend(im4, im1, .8)
    im6.save("step2.png","PNG")
    im7 = Image.blend(im6, im5, 0.8)
    im7.save("final.png","PNG")
    

   
def resize():
    imageFile = "bluefire.jpg"
    im1 = Image.open(imageFile)
    
    width = 500
    height = 420
    im2 = im1.resize((width, height), Image.NEAREST)
    ext = ".png"
    im2.save("bluefire" + ext)
   
   
   
def finishimg():
    resize()
    convertimg()
    
     
def get_imgs(directory=None):
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    image_list = [] # Initialize aggregaotrs
    file_list = []
    
    directory_list = os.listdir(directory) # Get list of files
    for entry in directory_list:
        absolute_filename = os.path.join(directory, entry)
        try:
            image = PIL.Image.open(absolute_filename)
            file_list += [entry]
            image_list += [image]
        except IOError:
            pass # do nothing with errors tying to open non-images
    return image_list, file_list
    