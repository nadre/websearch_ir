#!/usr/bin/python

import hashlib
import re
import distance
from simhash import Simhash, SimhashIndex

# inspiration: https://leons.im/posts/a-python-implementation-of-simhash-algorithm/

duplicate_texts_path = "duplicate-texts.txt"
correct_matches_path = "correct-matches.txt"

def find_near_duplicates(tuples, thres):
	dups = []
	l = len(tuples)
	for i in range(0, l):
		x = tuples[i]
		for j in range(i, l):
			y = tuples[j]
			if x[0] == y[0]:
				continue
			i = 0
			h1 = x[1]
			h2 = y[1]
			while(len(h1) != len(h2)):
				if len(h1) < len(h2):
				 	h1 = h1+"0"
				else:
					h2 = h2+"0"
			d = distance.hamming(h1, h2)
			if d < thres:
				dups.append((x[0], y[0]))
	return dups

def find_duplicates_with_same_hash(hash_fn):
	hmap = {}
	with open(duplicate_texts_path, "r", encoding='utf-8') as f:
		duplicate_texts = f.readlines()
		idx = 1
		for text in duplicate_texts:
			h = hash_fn(text)
			if h in hmap:
				hmap[h].append(idx)
			else:
				hmap[h] = [idx]
			idx += 1

	return [x for x in hmap.values() if len(x) > 1]

def get_tuples(hash_fn):
	tuples = []
	with open(duplicate_texts_path, "r", encoding='utf-8') as f:
		duplicate_texts = f.readlines()
		idx = 1
		for text in duplicate_texts:
			tuples.append((str(idx), str(hash_fn(text))))
			idx += 1
	return tuples

def get_features(x, width):
    x = x.lower()
    x = re.sub(r'[^\w]+', '', x)
    return [x[i:i + width] for i in range(max(len(x) - width + 1, 1))]

def md5_sum(x):
	return hashlib.md5(x.encode('utf-8')).hexdigest()

def simhash3(x, width = 3):
	return Simhash(get_features(x, width)).value

if __name__ == '__main__':
	print(find_duplicates_with_same_hash(md5_sum))
	print(find_duplicates_with_same_hash(simhash3))

	tuples = get_tuples(simhash3)
	print(find_near_duplicates(tuples, 13))

	matches = []
	with open(correct_matches_path) as f:
		correct_matches = f.readlines()
		for match in correct_matches:
			match = match.split()
			matches.append((match[0], match[1]))
			