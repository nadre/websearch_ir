#!/usr/bin/python

import hashlib
import re
import distance
import itertools
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
	
	return list_of_dups_to_dict(dups)

def find_duplicates_with_same_hash(hash_fn):
	hmap = {}
	with open(duplicate_texts_path, "r", encoding='utf-8') as f:
		duplicate_texts = f.readlines()
		idx = 1
		for text in duplicate_texts:
			h = hash_fn(text)
			if h in hmap:
				hmap[h].append(str(idx))
			else:
				hmap[h] = [str(idx)]
			idx += 1

	dups_list = [x for x in hmap.values() if len(x) > 1]

	return list_of_dups_to_dict(dups_list)

def list_of_dups_to_dict(dups_list):
	dups = []
	for entry in dups_list:
		dups.extend(list(itertools.combinations(entry, 2)))

	return dict(dups)


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

def simhash5(x, width = 5):
	return Simhash(get_features(x, width)).value

def simhash7(x, width = 7):
	return Simhash(get_features(x, width)).value

def get_matches():
	matches = {}
	with open(correct_matches_path) as f:
		correct_matches = f.readlines()
		for match in correct_matches:
			match = match.split()
			matches[match[0]] = match[1]
	return matches

def evaluate(matches, dups_dict):
	true_pos = 0
	false_neg = 0
	false_pos = 0
	for key in matches:
		if(str(key) in dups_dict):
			if matches[key] == dups_dict[key]:
				true_pos += 1
			else:
				false_pos += 1
		else:
			false_neg += 1

	print('precision: {:2f} recall: {:2f}'
		.format(
			true_pos/(true_pos+false_pos)*100,
			true_pos/(true_pos+false_neg)*100))	

if __name__ == '__main__':

	matches = get_matches()

	md5_sum_dups = find_duplicates_with_same_hash(md5_sum)
	print('md5_sum dups')
	evaluate(matches, md5_sum_dups)

	simhash3_dups = find_duplicates_with_same_hash(simhash3)
	print('simhash3 dups')
	evaluate(matches, simhash3_dups)

	tuples = get_tuples(simhash3)
	simhash3_near_dups = find_near_duplicates(tuples, 11)
	print('simhash3 near dups with hamming distance thres 11')
	evaluate(matches, simhash3_near_dups)

	tuples = get_tuples(simhash5)
	simhash5_near_dups = find_near_duplicates(tuples, 11)
	print('simhash5 near dups with hamming distance thres 11')
	evaluate(matches, simhash5_near_dups)

	tuples = get_tuples(simhash7)
	simhash7_near_dups = find_near_duplicates(tuples, 11)
	print('simhash7 near dups with hamming distance thres 11')
	evaluate(matches, simhash7_near_dups)