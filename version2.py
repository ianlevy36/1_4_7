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

def convertimg(directory = None):
    
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
        
       
        image_list[n] = image_list[n].convert("RGBA")
        for row in range(image_list[n].size[1]):
            for column in range(image_list[n].size[0]):
               image_list[n][row][column][3] = 127
        new_image =image_list[n]
        filename, filetype = file_list[n].split('.')
        #save the altered image, suing PNG to retain transparency
        new_image_filename = os.path.join(new_directory, filename + '.png')
        new_image.save(new_image_filename) 





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
        width = 500
        height = 420
        new_image = im.resize((width, height), Image.NEAREST)
        # Parse the filename
        filename, filetype = file_list[n].split('.')
       
       
       
        #save the altered image, suing PNG to retain transparency
        new_image_filename = os.path.join(new_directory, filename + '.png')
        new_image.save(new_image_filename) 
    

    
def finishimg(directory = None):
    resize()
    convertimg()
    
    
   
    
     

    