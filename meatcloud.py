import numpy as np
import random
import os
from PIL import Image, ImageFont, ImageDraw
from wordcloud import WordCloud, STOPWORDS


TEXT = os.environ.get('TEXT', 'NO TEXT')
WIDTH = int(os.environ.get('WIDTH', 640 * 3))
HEIGHT = int(os.environ.get('HEIGHT', 320 * 3))
OUTER_FONT_SIZE = int(os.environ.get('OUTER_FONT_SIZE', 48))

inner_font = "/opt/in/inner.ttf"
outer_font = "/opt/in/outer.ttf"

mask = Image.new("RGBA", (WIDTH, HEIGHT), (255, 255, 255))
draw = ImageDraw.Draw(mask)
outer_font = ImageFont.truetype(outer_font, OUTER_FONT_SIZE)

print TEXT
draw.text(
    (0, 0),
    TEXT,
    (0, 0, 0),
    font=outer_font
)

mask.save('/opt/out/mask.png')

names = [m for m in open('/opt/in/words').read().split("\n") if m]
random.shuffle(names)
names = " ".join(names)

mask = np.array(Image.open("/opt/out/mask.png"))


class MeatCloud(WordCloud):
    def generate_from_frequencies(self, frequencies):
        super(MeatCloud, self).generate_from_frequencies(frequencies)
        print len(self.layout_)


wc = MeatCloud(
    font_path=inner_font,
    background_color=(10, 10, 10),
    mask=mask,
    max_words=500,
    prefer_horizontal=float(os.environ.get('HORIZ', 0.9)),
    max_font_size=int(os.environ.get('MAX_SIZE', 300)),
    min_font_size=int(os.environ.get('MIN_SIZE', 4)),
)


def color_func(*args, **kwargs):
    return 255, 255, 255

wc.generate_from_text(names)
wc.recolor(color_func=color_func)
out = "/opt/out/meat.png"
wc.to_file(out)
os.chmod(out, 0666)