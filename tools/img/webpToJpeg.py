from PIL import Image
import glob

# paths
dir_origin = '{ORIGIN_DIRECTORY}'
dir_target = '{TARGET_DIRECTORY}'

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
