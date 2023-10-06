import os
import time
import sys

os.system("clear")

file = str(input(f"Target Zip File : ").lower())
passlist = str(input(f"Password List : ").lower())

os.system(f"sudo fcrackzip -u -D -p {passlist} {file}")

()
