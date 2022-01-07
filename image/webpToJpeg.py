from PIL import Image
import glob

# paths
testpath = '/Users/federicovalla/Documents/Work/cllla/resarch/scraping/ff/00/ff/11878628_8826132_480.webp'
dir_origin = '/Users/federicovalla/Documents/Work/cllla/resarch/scraping/ff/00/ff'
dir_target = '/Users/federicovalla/Documents/Work/cllla/resarch/py/target'

# indexes
index = 0


# convert : WEBP to JPEG
def webpToJpeg(img):
  i = Image.open(img)
  i.convert('RGB')
  print(index)

  destination = dir_target+'/im_'+str(index)+'.jpeg'
  i.save(destination, 'jpeg')


# loop
for img_webp in glob.glob(dir_origin+'/*.webp'):
    webpToJpeg(img_webp)
    index +=1
