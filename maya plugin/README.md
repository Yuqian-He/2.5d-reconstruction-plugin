# Maya Plugin of 2.5D Models Based on Monocular Images

## Build
[main script](https://github.com/Yuqian-He/2.5d-reconstruction-plugin/blob/main/maya%20plugin/main%20script.py): This is the script runing on maya scripts editor.

[2.5D Models Based on Monocular Images](https://github.com/XChengCode/Synthesis-of-2.5D-Models-Based-on-Monocular-Images/tree/main): This is the AI model I used in this project. You can also download it [here]()

[Virtual env](): This virual env was created based on which can run the ai model. You can download my virtual env as I installed everything already. As for people try to build by themselves, here is the steps:

```c++
//I use macOS Ventura 13.4

//create a virtual env, I use python 3.11.3
python3 -m venv myenv
//active this virtual env
source myenv/bin/activate
//Here is a list of libraries contained within my environment.
/*
distlib==0.3.6
eos-py==1.4.0.post0
filelock==3.12.0
h5py==3.8.0
imageio==2.28.0
Jinja2==3.1.2
lazy_loader==0.2
MarkupSafe==2.1.2
mpmath==1.3.0
networkx==3.1
numpy==1.24.3
packaging==23.1
Pillow==9.5.0
platformdirs==3.5.1
protobuf==4.21.12
PyWavelets==1.4.1
PyYAML==3.12
scikit-image==0.20.0
scipy==1.10.1
sympy==1.11.1
TBB==0.2
tifffile==2023.4.12
torch==2.0.0
typing_extensions==4.5.0
virtualenv==20.23.0
*/

```
> Please ensure that your virtual environment and AI model are placed in root directory of your Maya installation. You can find the installation path by typing the following code in your Maya script editor using Python:(Mine is /Users/naname/Library/Preferences/Autodesk/maya/)

```python
import maya.cmds as cmds

path = cmds.internalVar(userAppDir=True)
print(path)
```

