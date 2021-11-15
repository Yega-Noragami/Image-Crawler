import os
import json 
import requests
import selenium
from selenium import webdriver 
from os import path as PATH
from selenium.webdriver.chrome.service import Service
import base64
import time
import urllib.request


DRIVER_PATH = './chromedriver'


# Scroll to the end of the page
def scroll_to_end(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    print('scroll done')

# Setup Driver 
def setUpDriver():
    DRIVER_PATH = './chromedriver'
    driver = webdriver.Chrome(DRIVER_PATH)
    # downloadImagesFromChrome(driver)
    CURRENT_PATH= os.getcwd()
    
    try:
        os.mkdir("Images")
    except:
        print("Pass")
        
    IMAGE_PATH= os.path.join(CURRENT_PATH , "Images")

    # Call downloadFromChrome for each set of images and links 
    POSES_NAME = ["Name-1" , "Name-2" , "Name-3"]
    GOOGLE_IMAGES = ["GoogleSearchLink-1", "GoogleSearchLink-1", "GoogleSearchLink-3"]

    print("Image Directory and path : ", IMAGE_PATH)

    for i in range(len(POSES_NAME)):
        downloadImagesFromChrome(driver , POSES_NAME[i], GOOGLE_IMAGES[i] , IMAGE_PATH)

# Function which is responsible for downloading images from the provided hyperlink 
def downloadImagesFromChrome(driver , POSES_NAME , GOOGLE_IMAGES , IMAGE_PATH):

    # Change to current directory for 
    os.chdir(IMAGE_PATH)

    try:
        os.mkdir(str(POSES_NAME))
    except:
        print("Images exist")

    os.chdir(str(POSES_NAME))

    for i in range(len(POSES_NAME)):

        driver.get(GOOGLE_IMAGES)
        counter = 0
        for j in range(1,10):     
            scroll_to_end(driver)
            image_elements = driver.find_elements_by_class_name('rg_i')

            print("image_elements:",image_elements)

            for image in image_elements: 
                if (image.get_attribute('src') is not None):
                    try:
                        my_image = image.get_attribute('src').split('data:image/jpeg;base64,')
                        filename = POSES_NAME+str(counter)+'.jpeg'
                        print("filename:", filename)
                        if(len(my_image) >1): 
                            with open(filename, 'wb') as f: 
                                f.write(base64.b64decode(my_image[1]))
                        else: 
                            print(image.get_attribute('src'))
                            urllib.request.urlretrieve(image.get_attribute('src'), POSES_NAME + str(counter)+'.jpeg')
                        counter += 1

                        if counter ==50:
                            return 
                    except:
                        print("Pass")
        


def main():
    # This function is responsible for downloading downloading all images in link to specific location 
    while True: 
        print("1. Download images ")
        print("6. Exit program ")
        choice = input("Enter your choice: ")
        if choice == '6':
            print("Exiting ... ")
            break 
        else : 
            print(" Your choice is :", choice)

        if choice =='1':
            setUpDriver()

 

if __name__ == '__main__':
 main()