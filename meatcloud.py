import numpy as np
import random
import os
import sys
from PIL import Image, ImageFont, ImageDraw
from wordcloud import WordCloud, STOPWORDS

WIDTH = int(os.environ.get('WIDTH', 640 * 3))
HEIGHT = int(os.environ.get('HEIGHT', 320 * 3))

names = [m for m in open('/opt/in/words').read().split("\n") if m]
name_len = len(names)
names = " ".join(names)

font_file = "/opt/in/font.ttf"
mask = np.array(Image.open("/opt/in/mask.png"))


class MeatCloud(WordCloud):
    def generate_from_frequencies(self, frequencies):
        super(MeatCloud, self).generate_from_frequencies(frequencies)
        print len(self.layout_)

wc = MeatCloud(
    font_path=font_file,
    background_color=(0, 0, 0),
    mask=mask,
    max_words=name_len,
    prefer_horizontal=float(os.environ.get('HORIZ', 0.9)),
    max_font_size=int(os.environ.get('MAX_SIZE', 300)),
    min_font_size=int(os.environ.get('MIN_SIZE', 4)),
    relative_scaling=float(os.environ.get('REL_SCALE', 0.5)),
)


def color_func(*args, **kwargs):
    return 255, 255, 255

wc.generate_from_text(names)
wc.recolor(color_func=color_func)
out = "/opt/out/meat_txt.png"
wc.to_file(out)
os.chmod(out, 0666)
