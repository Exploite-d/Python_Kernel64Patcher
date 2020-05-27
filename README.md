# Python_Kernel64Patcher
64-bit Kernel patcher that currently supports iOS 11-13 written in Python. This patcher requires only 3 basic dependencies so it's not big nightmare with compiling it like liboffsetfinder64.

# Disclaimer 

I saw that patcher doesnt work on some devices and I wil try to fix this issue soon. As of now 6s , 5s devices are confirmed t work


# Requirements

Homebrew - https://brew.sh/index_pl

Python3 - brew install python3

argparse - pip install argparse-utils

# Why did I make this?
I made this to have working kernel patcher that I can use on any computer without having problems with compiling.
# Usage
Before using kernel with my tool you need to decompress it with img4lib: ./img4 -i input -o output

Patch iOS 11 kernel - ./Kernel64Patcher.py -i input -o output -a11 AMFI

Patch iOS 12 kernel - ./Kernel64Patcher.py -i input -o output -a12 AMFI

Patch iOS 13 kernel - ./Kernel64Patcher.py -i input -o output -a13 AMFI

# Credits
@L0W_P1X3L , @mcg29_ , @Ralph0045 - for sharing kernel patches in past so I was able to add them automatically to my tool.

# Upcoming features

- iOS 10 AMFI patch

- Maybe more kernel patches

# Screenshot of tool
![](photo.png)

