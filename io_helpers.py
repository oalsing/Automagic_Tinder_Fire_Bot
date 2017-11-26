import errno
import os
from skimage.io import imsave

base_folder = os.path.dirname(os.path.abspath(__file__)) + "/data"

LIKE_FOLDER = base_folder + "/likes/"
DISLIKE_FOLDER = base_folder + "/dislikes/"

def save_image(image, name, liked):

    filename = LIKE_FOLDER if liked else DISLIKE_FOLDER
    file_url_list = name.split("/")
    filename += file_url_list[-1]

    print(filename)

    imsave(filename, image)

def init():
    mkdir_p(LIKE_FOLDER)
    mkdir_p(DISLIKE_FOLDER)

def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise
