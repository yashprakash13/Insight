import random
import string
from stop_words import get_stop_words
import stylecloud
import os

from constants import *


def get_styled_cloud(comments, extra_stop_words = None, icon_selected = 'fas fa-cloud'):
    stop_words = get_stop_words('en')
    if extra_stop_words:
        stop_words += extra_stop_words

    cloud_name = ''.join(random.choices(string.ascii_uppercase +
                                        string.digits, k = 7)) + '.png'
    # cloud_name = str(random.randint(1, 100)) + '.png'
    file_path = os.path.join(PRETTY_LITTLE_WORD_CLOUD_PATH, cloud_name)

    

    text = ' '.join(comments)
    stylecloud.gen_stylecloud(text = text,
                                size = 1024,
                                icon_name = icon_selected,
                                palette = 'colorbrewer.diverging.Spectral_11',
                                background_color = 'black',
                                gradient = 'horizontal',
                                custom_stopwords = stop_words,
                                output_name = file_path
                            )

    return cloud_name

    


