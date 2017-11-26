#! /usr/bin/env python

from skimage.io import imread, imsave, imshow, show
from matplotlib.pyplot import subplots
import pynder
from helpers import get_access_token, get_login_credentials
from io_helpers import save_image, init as init_io

email, password, FBID = get_login_credentials()
FBTOKEN = get_access_token(email, password)
session = pynder.Session(facebook_id=FBID, facebook_token=FBTOKEN)
print("Session started..")

while True:
    users = session.nearby_users()
    init_io()
    for user in users:
        photos = user.get_photos()
        print("Fetched user photos..")
        for photo in photos:
            image = imread(photo)
            fig, ax = subplots(figsize=(10, 10))
            imshow(image)
            show()

            input_string = "Write 1 to like. Write 2 to dislike"
            ans = input(input_string).lower()

            if ans == "1":
                save_image(image, photo, True)
            else:
                save_image(image, photo, False)
