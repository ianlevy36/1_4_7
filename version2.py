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

def convertimg(original_image):
    
    original_image = original_image.convert("RGBA")
    height = len(original_image)
    width = len(original_image[0])
    for row in range(0,420):
        for column in range(0,500):
             original_image[row][column][3] = 127
    im1 = original_image
    im1.save(original_image)

def resize(original_image):
    
   
    im = original_image
    im = im.convert("RGBA")
    width = 500
    height = 420
    im2 = im.resize((width, height), Image.NEAREST)
    im2.save(im2)

def overlay(original_image,directory = None):
    if directory == None:
       directory = os.getcwd() 
    image_list, file_list = get_imgs(directory)
    
    for n in range(len(image_list)):
        im = Image.blend(image_list[1],image_list[n],.5)
        image_list[1]= im
   
def finishimg(directory = None):
    
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
    
    #go through the images and save modified versions
    for n in range(len(image_list)):
        # Parse the filename
        filename, filetype = file_list[n].split('.')
        resize(image_list[n])
        # Round the corners with radius = 30% of short side
        new_image = overlay(image_list[n])
        #save the altered image, suing PNG to retain transparency
        new_image_filename = os.path.join(new_directory, filename + '.png')
        new_image.save(new_image_filename) 
    
   
    
     

    