import cv2
import os

# define
file_path = '{VIDEO_PATH}'
dest_path = '{DESTINATION_PATH}'

vidcap = cv2.VideoCapture(file_path)
success, image = vidcap.read()

count = 0
step = 600

# check numbers
# length = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
length = vidcap.get(cv2.CAP_PROP_FRAME_COUNT)
print( 'length:', length, 'exported:', length/step )

# loop
while success:
  vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*step))    # skip to step value
  success,image = vidcap.read()

  cv2.imwrite(dest_path+"/f%d.jpg" % count, image)

  print('frame: %d', success)
  count += 1


print('finished:', count)
