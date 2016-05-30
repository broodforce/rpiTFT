% initialisation
% Start X with DPMS disabled and no screensaver
X -dpms -s 0 &
% Define default display to use
export DISPLAY=0:0
% Execute Clock - might need sudo
python code1.0.1.py
