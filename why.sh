#!/bin/bash
#https://raw.githubusercontent.com/NinjaAung/hangingSpaceMan/master/why.sh

red='\x1b[38;5;9m'
has?() { hash $1 2>/dev/null; }


echo -e "${red}THIS AIN'T NO GAME"

afplay youThought.mp3

python3 test.py