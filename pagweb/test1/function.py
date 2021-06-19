from io import BytesIO
from django.core.files import File
from PIL import Image
import os
import copy

def new_name(imagen, extra):
    if extra in imagen.name:
        return None
    else:
        no_folder = imagen.name.split('/')[-1]
        nuevo_name = no_folder.split('.')[0] + extra + '.' + no_folder.split('.')[1]
        return nuevo_name


def make_small_image(image, extra=None):
    """Makes small image for the news"""

    image_aux = copy.copy(image) # Here we copy the image to access it later
    im = Image.open(image)
    width, height = im.size
    ratio_size = width/height
    ratio_ideal = 1
    if ratio_size==ratio_ideal:
        left = 0
        right = width
        top = 0
        bottom = height
    elif ratio_size>ratio_ideal: #Imagen ancha
        left = (width/ratio_size)*(ratio_size-ratio_ideal)/2
        right = (width/ratio_size)*(ratio_ideal+ (ratio_size-ratio_ideal)/2)
        top = 0
        bottom = height
    elif ratio_size<ratio_ideal: #Imagen alta
        left = 0
        right = width
        top = (height/ratio_ideal)*(ratio_ideal-ratio_size)/2
        bottom = (height/ratio_ideal)*(ratio_size + (ratio_ideal-ratio_size)/2)
    im = im.crop((left, top, right, bottom))

    image_io = BytesIO() # create a BytesIO object

    image_filename2, image_extension2 = os.path.splitext(image_aux.name)#HERE WE TAKE THE EXTENSION, example : '.jpg'
    image_extension3 = image_extension2.split('.') #Here we separate the extension as a list of : ['', 'jpg']
    if image_extension3[1] == 'jpg':
        im.save(image_io, 'jpeg',quality=85) # save image to BytesIO object
    else:
        im.save(image_io, image_extension3[1],quality=85) # save image to BytesIO object

    if extra == None:
        small_image = File(image_io, name=image.name) # create a django friendly File object
    elif extra != None:
        small_image = File(image_io, name=new_name(image, extra))

    if extra in small_image: 
        return None
    else:
        return small_image

def make_wide_image(image, extra=None):
    """Makes wide image for blogs"""

    image_aux = copy.copy(image) # Here we copy the image to access it later
    im = Image.open(image)
    width, height = im.size
    print(f"Width: {width} and Height: {height}")
    ratio_size = width/height
    ratio_ideal = 4
    if ratio_size==ratio_ideal:
        print("Imagen Perfecta")
        left = 0
        right = width
        top = 0
        bottom = height
    elif ratio_size>ratio_ideal: #Imagen ancha
        left = (width/ratio_size)*(ratio_size-ratio_ideal)/2
        right = (width/ratio_size)*(ratio_ideal+ (ratio_size-ratio_ideal)/2)
        top = 0
        bottom = height
    elif ratio_size<ratio_ideal: #Imagen alta
        left = 0
        right = width
        top = (height/ratio_ideal)*(ratio_ideal-ratio_size)/2
        bottom = (height/ratio_ideal)*(ratio_size + (ratio_ideal-ratio_size)/2)
    im = im.crop((left, top, right, bottom))

    image_io = BytesIO() # create a BytesIO object

    image_filename2, image_extension2 = os.path.splitext(image_aux.name)
    image_extension3 = image_extension2.split('.')
    if image_extension3[1] == 'jpg':
        im.save(image_io, 'jpeg',quality=85) # save image to BytesIO object
    else:
        im.save(image_io, image_extension3[1],quality=85) # save image to BytesIO object

    if extra == None:
        wide_image = File(image_io, name=image.name) # create a django friendly File object
    elif extra != None:
        wide_image = File(image_io, name=new_name(image, extra))

    if extra in wide_image: 
        return None
    else:
        return wide_image

def make_round_image(image, extra=None):
    """Makes small image for the news"""

    image_aux = copy.copy(image) # Here we copy the image to access it later
    im = Image.open(image)
    width, height = im.size
    ratio_size = width/height
    ratio_ideal = 1.5

    if ratio_size==ratio_ideal:
        left = 0
        right = width
        top = 0
        bottom = height
    elif ratio_size>ratio_ideal: #Imagen ancha
        left = (width/ratio_size)*(ratio_size-ratio_ideal)/2
        right = (width/ratio_size)*(ratio_ideal+ (ratio_size-ratio_ideal)/2)
        top = 0
        bottom = height
    elif ratio_size<ratio_ideal: #Imagen alta
        left = 0
        right = width
        top = (height/ratio_ideal)*(ratio_ideal-ratio_size)/2
        bottom = (height/ratio_ideal)*(ratio_size + (ratio_ideal-ratio_size)/2)
    im = im.crop((left, top, right, bottom))

    image_io = BytesIO() # create a BytesIO object

    image_filename2, image_extension2 = os.path.splitext(image_aux.name)
    image_extension3 = image_extension2.split('.')
    if image_extension3[1] == 'jpg':
        im.save(image_io, 'jpeg',quality=85) # save image to BytesIO object
    else:
        im.save(image_io, image_extension3[1],quality=85) # save image to BytesIO object

    if extra == None:
        round_image = File(image_io, name=image.name) # create a django friendly File object
    elif extra != None:
        round_image = File(image_io, name=new_name(image, extra))

    if extra in round_image: 
        return None
    else:
        return round_image

def make_tall_image(image, extra=None):
    """Makes small image for the news"""
    image_aux = copy.copy(image) # Here we copy the image to access it later
    im = Image.open(image)
    width, height = im.size
    ratio_size = width/height
    ratio_ideal = 60/83

    if ratio_size==ratio_ideal:
        left = 0
        right = width
        top = 0
        bottom = height
    elif ratio_size>ratio_ideal: #Imagen ancha
        left = (width/ratio_size)*(ratio_size-ratio_ideal)/2
        right = (width/ratio_size)*(ratio_ideal+ (ratio_size-ratio_ideal)/2)
        top = 0
        bottom = height
    elif ratio_size<ratio_ideal: #Imagen alta
        left = 0
        right = width
        top = (height/ratio_ideal)*(ratio_ideal-ratio_size)/2
        bottom = (height/ratio_ideal)*(ratio_size + (ratio_ideal-ratio_size)/2)
    im = im.crop((left, top, right, bottom))

    image_io = BytesIO() # create a BytesIO object

    image_filename2, image_extension2 = os.path.splitext(image_aux.name)
    image_extension3 = image_extension2.split('.')
    if image_extension3[1] == 'jpg':
        im.save(image_io, 'jpeg',quality=85) # save image to BytesIO object
    else:
        im.save(image_io, image_extension3[1],quality=85) # save image to BytesIO object
        
    if extra == None:
        tall_image = File(image_io, name=image.name) # create a django friendly File object
    elif extra != None:
        tall_image = File(image_io, name=new_name(image, extra))
    
    if extra in tall_image: 
        return None
    else:
        return tall_image
