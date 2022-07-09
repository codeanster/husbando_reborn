#!pip3 install Pybooru
from pybooru import Danbooru
import os
import urllib.request
import time
from csv import writer

#helper funciton to write data to csv
def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)
        
# https://pybooru.readthedocs.io/en/stable/api_danbooru.html#pybooru.api_danbooru.DanbooruApi_Mixin.post_list
booru = Danbooru('danbooru')
posts = booru.post_list(limit = 100,random=True)

#let's do a while loop while our designated image file has less than 10,000 images

#directory we want to save images
dir_path = 'data/uncropped/'
number_of_images = len([entry for entry in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, entry))])

# I should figure out how to search for a list of strings in a string... hmm that explanation doesn't sound write

total_images = 10000 #total images we want
while number_of_images < total_images:
  print(f'There are {number_of_images} images')
  posts = booru.post_list(limit = 100,random=True)
  for post in posts:
    #lazy way of searching... we can do better (actually maybe this is something Jess optimize so it's only 1 line of code, maybe like  (for word in words not in post['tag_string']) or something, I'm not sure)
    if ('1boy' in (post['tag_string'])) and \
    ('male_focus' in (post['tag_string'])) and \
    ('1girl' not in post['tag_string']) and \
    ('2girl' not in post['tag_string']) and \
    ('3girl' not in post['tag_string']) and \
    ('groin' not in post['tag_string']) and \
    ('bulge' not in post['tag_string']) and \
    ('upskirt' not in post['tag_string']) and \
    ('panties' not in post['tag_string']) and \
    ('skirt' not in post['tag_string']) and \
    ('grabbing' not in post['tag_string']) and \
    ('4girl' not in post['tag_string']):
      try:
        #download image
        urllib.request.urlretrieve(post['file_url'],filename= f"{dir_path}/{post['id']}.png")
        # print(post['id'],post['tag_string'])
        print(f'Image saved to {dir_path}{post["id"]}.png')
        
        #save tag and id to csv
        row_contents = [post['id'],post['tag_string']]
        append_list_as_row('meta.csv',row_contents)  
      except Exception as e:
        print(e)
  print('Finished Downloading and Saving...')
    
  #re-search after 5 seconds
  time.sleep(5)
  print('Searching....')
  
  #get number of images in directory
  number_of_images = len([entry for entry in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, entry))])