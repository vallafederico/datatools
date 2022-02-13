# --------- --------- Check GPU

# GPU -- V100 -- Excellent / P100 -- Very Good / T4 -- Good / K80 -- Meh / P4 -- (Not Recommended)
!nvidia-smi

# --------- --------- Download Assets

# @title **Download Stuffs**
from google.colab import files

max = 8#@param {type:"number"}
prefix = "out_" #@param {type:"string"}

for i in range(max):
  filename = f"{prefix}{i}.png"
  files.download(filename)

