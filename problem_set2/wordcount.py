#!/usr/bin/python

import sys
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
import csv
import string

if __name__ == '__main__':
	f = open(sys.argv[1], 'r', encoding='utf-8')
	s = f.read().lower()
	s = s.translate({ord(i):None for i in string.punctuation})
	s = s.split()
	total_words = len(s)
	wc = Counter(s)
	fo = open(sys.argv[1]+'.freq','w')

	distribution = []

	for word in wc.most_common():
		# if word[1] < 3:
		# 	break
		distribution.append((word[0], word[1]))
		fo.write(word[0]+"\t"+str(word[1])+'\n')
	fo.close()

	labels, values = zip(*distribution)
	indexes = np.arange(len(labels))

	plt.scatter(indexes, values, s=10)
	plt.title("word freq distribution\n"+sys.argv[1]+"\ntotal words: "+str(total_words))
	plt.xlabel('words')
	plt.ylabel('freq')

	plt.savefig(sys.argv[1]+".png")
	plt.show()