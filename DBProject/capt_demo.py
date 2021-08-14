# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 08:23:39 2020

@author: hp
"""



from captcha.image import ImageCaptcha
import random

# The number list, lower case character list and upper case character list are used to generate captcha text.
number_list = ['0','1','2','3','4','5','6','7','8','9']

alphabet_lowercase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

alphabet_uppercase = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

base_char = alphabet_lowercase + alphabet_uppercase + number_list

# This function will create a random captcha string text based on above three list.
# The input parameter is the captcha text length.
def create_random_captcha_text(captcha_string_size=4):

    captcha_string_list = []

   
    for i in range(captcha_string_size):

        # Select one character randomly.
        char = random.choice(base_char)

        # Append the character to the list.
        captcha_string_list.append(char)

    captcha_string = ''

    # Change the character list to string.    
    for item in captcha_string_list:
        captcha_string += str(item)

    return captcha_string

def create_image_captcha(captcha_text):
    image_captcha = ImageCaptcha()
    # Create the captcha image.
    image = image_captcha.generate_image(captcha_text)

    # Add noise curve for the image.
    image_captcha.create_noise_curve(image, image.getcolors())

    # Add noise dots for the image.
    image_captcha.create_noise_dots(image, image.getcolors())
    
    # Save the image to a png file.
    image_file = "./captcha_"+captcha_text + ".png"
    image_captcha.write(captcha_text, image_file)
    # Display the image in a matplotlib viewer.
    #plt.imshow(image)
    #plt.show() 
    
    
    #print(image_file + " has been created.")
    return image_file
# Create an audio captcha file.    

#captcha_text=create_random_captcha_text(10)
#create_image_captcha(captcha_text)

