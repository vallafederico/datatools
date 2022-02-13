# SRCNN Image Super Resolution

#@title **Install SRCNN** 
!git clone https://github.com/Mirwaisse/SRCNN.git
!curl https://raw.githubusercontent.com/justinjohn0306/SRCNN/master/models/model_2x.pth -o model_2x.pth
!curl https://raw.githubusercontent.com/justinjohn0306/SRCNN/master/models/model_3x.pth -o model_3x.pth
!curl https://raw.githubusercontent.com/justinjohn0306/SRCNN/master/models/model_4x.pth -o model_4x.pth
  
# @title **Increase Resolution SINGLE**
import subprocess

zoomfac = 4#@param {type:"number"}
index = 15#@param {type:"number"}

filename = f"out_{index}.png"

cmd = [
    'python',
    '/content/SRCNN/run.py',
    '--zoom_factor',
    str(zoomfac), 
    '--model',
    f"/content/model_{zoomfac}x.pth",  
    '--image',
    filename,
    '--cuda'
]
print(f'upscale {index} /', filename)

subprocess.run(cmd, cwd=f'/content/')
