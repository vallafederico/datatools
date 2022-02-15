# --------- --------- Check GPU

# GPU -- V100 -- Excellent / P100 -- Very Good / T4 -- Good / K80 -- Meh / P4 -- (Not Recommended)
gpu_info = !nvidia-smi
gpu_info = '\n'.join(gpu_info)
if gpu_info.find('failed') >= 0:
  print('Not connected to a GPU')
else:
  print(gpu_info)

# --------- --------- Download Assets

# @title **Download Stuffs**
from google.colab import files

max = 8#@param {type:"number"}
prefix = "out_" #@param {type:"string"}

for i in range(max):
  filename = f"{prefix}{i}.png"
  files.download(filename)

