#!pip3 install Pybooru
from pybooru import Danbooru
import os
import urllib.request
import time

#works only on my colab right now, will need to get it to work with .env files

# https://pybooru.readthedocs.io/en/stable/api_danbooru.html#pybooru.api_danbooru.DanbooruApi_Mixin.post_list

booru = Danbooru('danbooru',os.getenv('USER'), os.getenv('KEY'))
posts = booru.post_list(limit = 100,random=True)

#let's search through tag_string for 'boy'

#let's do a while loop while our designated image file has less than 10,000 images

dir_path = '/content'
number_of_images = len([entry for entry in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, entry))])

# I should figure out how to search for a list of strings in a string... hmm that explanation doesn't sound write

total_images = 10000 #total images we want
while number_of_images < total_images:
  posts = booru.post_list(limit = 100,random=True)
  for post in posts:
    #lazy way of searching... we can do better (actually maybe this is something you can try to optimize)
    if ('1boy' in (post['tag_string'])) and \
    ('male_focus' in (post['tag_string'])) and \
    ('1girl' not in post['tag_string']) and \
    ('2girl' not in post['tag_string']) and \
    ('3girl' not in post['tag_string']) and \
    ('groin' not in post['tag_string']) and \
    ('bulge' not in post['tag_string']) and \
    ('4girl' not in post['tag_string']):
      try:
        #download image
        urllib.request.urlretrieve(post['file_url'],filename= f"/content/{post['id']}.png")
        # print(post['tag_string'])
        print(f'Image saved to /content/{post["id"]}.png')
      except Exception as e:
        print(e)
  print('Done searching... Waiting')
  #re-search after 30 seconds
  time.sleep(30)
  print('Searching....')
