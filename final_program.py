import PIL
import matplotlib.pyplot as plt
import os.path  
import PIL.ImageDraw            
from PIL import Image

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


def convertimg():
    im1 = Image.open("bluefire.jpg")
    im2 = Image.open("redlighting.jpg")
    im3 = Image.open("city.jpg")
    im4 = Image.open("Geopattern.jpg")
    
    im3 = im3.convert("RGBA")
    im1 = im1.convert("RGBA")
    im4 = im4.convert("RGBA")
    im2 = im2.convert("RGBA")
    
    im5 = Image.blend(im2, im3, 0.4)
    im5.save("step1.png","PNG")
    im6 = Image.blend(im4, im1, 0.6)
    im6.save("step2.png","PNG")
    im7 = Image.blend(im6, im5, 0.7)
    im7.save("final.png","PNG")
    
def resize(directory = None):
    if directory == None:
       directory = os.getcwd() 
        
    # Create a new directory 'modified'
    new_directory = os.path.join(directory, 'modified')
    try:
        os.mkdir(new_directory)
    except OSError:
        pass # if the directory already exists, proceed  
    
    #load all the images
    image_list, file_list = get_imgs(directory)
    
    if directory == None:
       directory = os.getcwd() 
    image_list, file_list = get_imgs(directory)
    
    for n in range(len(image_list)):
        im = image_list[n]
        im = im.convert("RGBA")
        width = 650
        height = 500
        new_image = im.resize((width, height), Image.NEAREST)
        # Parse the filename
        filename, filetype = file_list[n].split('.')
       
       
       
        #save the altered image, suing PNG to retain transparency
        new_image_filename = os.path.join(new_directory, filename + '.png')
        new_image.save(new_image_filename)   
   
   
def finishimg():
    resize()
    convertimg()