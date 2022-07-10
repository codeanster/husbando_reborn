# Husbando Reborn #

## Next Steps ##
* ~~Set up Danbooru API and get .env file setup~~ Turns out we don't need API
* Run danbooru_image_dowloader.py until until there are ~10000 images
* ~~refactor anime_face_detection.ipynb to work as a script to process all the images~~
* Resize all the cropped images to be the same (let's try 256 for now)
* Use Danbooru API to search by image id for tags and save them to a csv for a id and tags grouping
* Think of ways we can display data with the tags and categorize them(?)
* Improve performance of facial detection and cropping algorithm by increasing number of images being cropped and measuring how good of a "match" they are.

### Data Storage ###
I expect the images (20,000 in total) to be about ~16GB in total, so will need to think of a way to store it on the cloud but also be easily accessible for training on google colab since we will need a GPU for it. For right now, using google drive is the best solution. If we get ~50,000 images, then we can consider that but it still wouldn't be neccessary in my opinion. 

### Data Cleaning ###
* Work on improving our selection process (picking the right tags). Maybe our metric for tracking this can be "how many images do we throw out when manually searching a random sample of 100 images?
* Crop images around the face, resize images

### Model Training ###
We're not here yet, but we will be using [stylegan2](https://github.com/NVlabs/stylegan2) with tensorflow. I think pyTorch would be more efficient, but I'm more comfortable with tensorflow. We will also be using GPU's for training because we won't have to pay $100 a month for cloud services lmao.

Some things to consider
* Having the tags will be immensely useful once we figure out how to use it. I think it would help us navigate the GAN's [latent space](https://towardsdatascience.com/understanding-latent-space-in-machine-learning-de5a7c687d8d)
