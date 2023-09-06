from PIL import Image
from PIL import ImageEnhance as ie
import glob, os
import random, numpy, multiprocessing



def morph(file, im):
    h_scale = random.uniform(0.8, 1.2)
    w_scale = random.uniform(0.8, 1.2)
    rot = random.randint(0, 359)
    flipit = random.randint(0, 1)
    col = random.uniform(0.8, 1.2)
    con = random.uniform(0.8, 1.2)
    bri = random.uniform(0.8, 1.2)
    sharp = random.uniform(0.8, 1.2)
    longer_side = max(im.size)
    new_size = 256
    im.thumbnail((new_size, new_size), Image.ANTIALIAS)
    w = im.size[0]
    h = im.size[1]
    im = im.resize((int(round(w_scale*w)), int(round(h_scale*h))), Image.ANTIALIAS)
    im = im.rotate(rot)
    if flipit:
        im = im.transpose(Image.FLIP_LEFT_RIGHT)
    en = ie.Color(im)
    im = en.enhance(col)
    en = ie.Brightness(im)
    im = en.enhance(bri)
    en = ie.Contrast(im)
    im = en.enhance(con)
    en = ie.Sharpness(im)
    im = en.enhance(sharp)
    horizontal_pad = (longer_side - im.size[0]) / 2
    vert_pad = (longer_side - im.size[1]) / 2
    im = im.crop((-horizontal_pad, -vert_pad, im.size[0] + horizontal_pad, im.size[1] + vert_pad)) 
    nm = "_rot" + str(rot) + "_flip_" + str(flipit) + "_h" + str(h_scale) + "_w" + str(w_scale) + "_col" + str(col) + "_bri" + str(bri) + "_con" + str(con) + "_sharp" + str(sharp) + ".jpg" 
    im.save(file + nm, "JPEG")	

def run(in_file):
    file, ext = os.path.splitext(in_file)
    im = Image.open(in_file)
    for i in range(1, 20):
        morph(file, im)

pool = multiprocessing.Pool(8)

pool.map(run, glob.glob("*.jpg"))


