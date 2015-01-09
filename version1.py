import PIL
import matplotlib.pyplot as plt
import os.path  
import PIL.ImageDraw            

def get_images(directory=None):
    if directory == None:
        directory = os.getcwd()      
    image_list = [] 
    file_list = []
    directory_list = os.listdir(directory) 
    for entry in directory_list:
        absolute_filename = os.path.join(directory, entry)
        try:
            image = PIL.Image.open(absolute_filename)
            file_list += [entry]
            image_list += [image]
        except IOError:
            pass 
    return image_list, file_list
def edit_all_images(directory=None):
    
    if directory == None:
        directory = os.getcwd() 
    new_directory = os.path.join(directory, 'new')
    try:
        os.mkdir(new_directory)
    except OSError:
        pass 
    image_list, file_list = get_images(directory) 
    for n in range(len(image_list)):
        filename, filetype = file_list[n].split('.') 
        #######new_image = round_corners(image_list[n],.30)
      
        new_image_filename = os.path.join(new_directory, filename + '.png')
        new_image.save(new_image_filename) 
def round_corners(original_image, percent_of_side):
   
    
    
    #set the radius of the rounded corners
    width, height = original_image.size
    radius = int(percent_of_side * min(width, height)) # radius in pixels
    rounded_mask = PIL.Image.new('RGBA', (width, height), (127,0,127,0))
    drawing_layer = PIL.ImageDraw.Draw(rounded_mask)
    
   
    # Make the new image, starting with all transparent
    result = PIL.Image.new('RGBA', original_image.size, (0,0,0,0))
    result.paste(original_image, (0,0), mask=rounded_mask)
    return result
    