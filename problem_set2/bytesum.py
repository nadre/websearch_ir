#!/usr/bin/python

import sys

if __name__ == '__main__':
	bytesum = 0
	f = open(sys.argv[1], "rb")
	try:
		byte = f.read(1)
		while byte != "":
			byte = f.read(1)
			try:
				# print byte.encode("hex")
				bytesum += int(byte.encode("hex"), 16)
			except Exception, e:
				pass
	finally:
		f.close()
	print bytesum