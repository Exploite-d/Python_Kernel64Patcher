#!/usr/bin/env python3
import sys
import argparse
from os import system

Pink = '\33[95m'
CEND = '\033[0m'

argv = sys.argv

print (Pink + "Python Kernel64Patcher by @exploit3dguy on Twitter." + CEND)
arguments = argparse.ArgumentParser()
arguments.add_argument("-i", "--input", help="Input file")
arguments.add_argument("-o", "--output", help="Output file")
arguments.add_argument("-a11", "--amfi11", help="Applies AMFI_11 patch to kernel. (For iOS 11 kernels)")
arguments.add_argument("-a12", "--amfi12", help="Applies AMFI_12 patch to kernel. (For iOS 12 kernels)")
arguments.add_argument("-a13", "--amfi13", help="Applies AMFI_13 patch to kernel. (For iOS 13 kernels)")
args = arguments.parse_args()


if len(argv) == 1:
		arguments.print_help(sys.stderr)
		sys.exit(1)
input_file = str(args.input)
if args.input:
   print("Processing input file...")
   system("cp " + input_file + " ./kernel.inprogress")
else:
	print("Input file not specified. Exiting...")
	sys.exit(1)
if args.amfi11:
	print("Applying AMFI_11 patch")
	kernel_file = open("./kernel.inprogress", "r+b")
	fh = kernel_file
	file = fh.read()
	hex_value = hex(file.index(b"\xF8\x5F\xBC\xA9\xF6\x57\x01\xA9\xF4\x4F\x02\xA9\xFD\x7B\x03\xA9\xFD\xC3\x00\x91\xF3\x03\x00\xAA\x15\x00\x80\x52")) #Finding pattern
	hex_value = int(hex_value, 0)
	fh.seek(hex_value, 0)
	fh.write(b"\xE0\x03\x00\x32\xC0\x03\x5F\xD6") #Applying AMFI patch
	fh.close()   
if args.amfi12:
	print("Applying AMFI_12 patch")
	kernel_file = open("./kernel.inprogress", "r+b")
	fh = kernel_file
	file = fh.read()
	hex_value = hex(file.index(b"\xFD\x7B\xBF\xA9\xFD\x03\x00\x91\x02\x9B\xE6\x97\x1F\x00\x00\x71\xE0\x07\x9F\x1A\xFD\x7B\xC1\xA8\xC0\x03\x5F\xD6")) #Finding pattern
	hex_value = int(hex_value, 0)
	fh.seek(hex_value, 0)
	fh.write(b"\xE0\x03\x00\x32\xC0\x03\x5F\xD6") #Applying AMFI patch
	fh.close()
if args.amfi13:
	print("Applying AMFI_13 patch")
	kernel_file = open("./kernel.inprogress", "r+b")
	fh = kernel_file
	file = fh.read()
	hex_value = hex(file.index(b"\xFD\x7B\xBF\xA9\xFD\x03\x00\x91\xD9\x15\x00\x94\xFD\x7B\xC1\xA8\xC0\x03\x5F\xD6\xFF\xC3\x00\xD1\xF4\x4F\x01\xA9")) #Finding pattern
	hex_value = int(hex_value, 0)
	fh.seek(hex_value, 0)
	fh.write(b"\xE0\x03\x00\x32\xC0\x03\x5F\xD6") #Applying AMFI patch
	fh.close()	
if args.output:
	output = str(args.output)
	system("mv " + "./kernel.inprogress " + output)
	print("Writing out patched file to " + output)
else:
	print("Output file not specified. Exiting...")
	system("rm -rf ./kernel.inprogress")
	sys.exit(1)
