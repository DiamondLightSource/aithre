![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg) <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/co2e14/aithre"> <img alt="GitHub top language" src="https://img.shields.io/github/languages/top/co2e14/aithre">


Controls for I23 laser shaping project

At Diamond:
module load python/3.11
Use python -m venv .venv to install python env (python3.11)

If using Linux ver. need to install the local version of rtc6-fastcs in order to use bluesky to control excelliSCAN
pip install ../path/to/rtc6-fastcs

If it doesn't launch the GUI, need to uninstall and reinstall pyqt5 and opencv in specific order. 

pip uninstall opencv-python opencv-python-headless

pip uninstall PyQt5 PyQt5-sip

pip install --upgrade pip

pip install opencv-python-headless

pip install PyQt5


![icon](https://user-images.githubusercontent.com/45949926/161590407-25c165b3-38b9-4906-93d2-ac9a1d5d4eb9.png)
