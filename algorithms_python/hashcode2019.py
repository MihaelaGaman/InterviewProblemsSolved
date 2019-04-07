import os
import operator
from operator import itemgetter

def read_from_file(fname):
	f = open(fname, 'r')
	str_l = f.readlines()
	f.close()

	N = int(str_l[0])

	d_tags_h = {}
	d_tags_v = {}

	for i in range(1, N+1):
		img_info = str_l[i].split()

		orient = img_info[0]
		no_tags = int(img_info[1])

		tags = []

		for j in range(2, no_tags + 2):
			tags.append(img_info[j])

		if orient == 'H':
			d_tags_h[i-1] = tags
		else:
			d_tags_v[i-1] = tags

	return N, d_tags_h, d_tags_v

def generate_all_verticals(d_tags_v, d_tags_h):
	pairs = [(id_img, d_tags_v[id_img]) for id_img in d_tags_v]
	
	n = len(pairs)

	for i in range(n):
		for j in range(i+1, n):
			d_tags_h[(pairs[i][0], pairs[j][0])] = list(set(pairs[i][1] + pairs[j][1]))	

	return d_tags_h

def intersection(lst1, lst2): 
    lst3 = [list(filter(lambda x: x in lst1, sublist)) for sublist in lst2] 
    return lst3

def compute_score(s1, s2):
	nc = len(intersection(s1, s2))
	n1 = len(set(s1) - set(s2))
	n2 = len(set(s2) - set(s1))

	return min([nc, n1, n2])

def convert(d_tags_h):
	return [(idx, d_tags_h[idx]) for idx in d_tags_h]

def build_ids_scores_list(l_id_tags):
	ids_scores = []

	n = len(l_id_tags)
	for i in range(n):
		(idx_1, tags_1) = l_id_tags[i]
		for j in range(i+1, n):
			(idx_2, tags_2) = l_id_tags[j]
			s = compute_score(tags_1, tags_2)
			ids_scores.append((s, idx_1, idx_2))

	return ids_scores


def remove_duplicate_verticals(ids_scores, id1, id2):
	res = []

	for (_, idx_1, idx_2) in ids_scores:
		if type(idx_1) is tuple and (idx_1[0] in [id1, id2] or idx_1[1] in [id1, id2]):
			continue
		if type(idx_2) is tuple and (idx_2[0] in [id1, id2] or idx_2[1] in [id1, id2]):
			continue

		res.append((_, idx_1, idx_2))

	return res


def build_slideshow(l_id_tags):
	# n = len(l_id_tags)
	S = []
	
	ids_scores = build_ids_scores_list(l_id_tags)

	ids_scores.sort(key = operator.itemgetter(0), reverse=True)

	n = len(ids_scores) - 2
	# i = 1

	last_index = ids_scores[0][2]
	first = ids_scores[0][1]
	S.append(first)
	S.append(ids_scores[0][2])

	all_s = [elem for elem in ids_scores if elem[1] == first or elem[2] == first]

	ids_scores = list(set(ids_scores) - set(all_s))
	if type(first) is tuple:
		ids_scores = remove_duplicate_verticals(ids_scores, first[0], first[1])

	while n > 0:
		all_s = [elem for elem in ids_scores if elem[1] == last_index or elem[2] == last_index]
		max_pair = max(all_s,key=itemgetter(0))
		elem = max_pair[1] if max_pair[2] == last_index else max_pair[2]
		
		S.append(elem)
		ids_scores.remove(max_pair)
		ids_scores = list(set(ids_scores) - set(all_s))

		if type(last_index) is tuple:
			ids_scores = remove_duplicate_verticals(ids_scores, last_index[0], last_index[1])

		last_index = elem

		n = len(ids_scores)
		#i += 1

	return S


def build_output(S, fname):
	f = open(fname, 'w')

	f.write(str(len(S)) + "\n")

	for elem in S:
		if type(elem) is tuple:
			f.write(str(elem[0]) + " " + str(elem[1]) + "\n")

		else:
			f.write(str(elem) + "\n")

	f.close()


fname = str(raw_input())
N, d_tags_h, d_tags_v = read_from_file(fname)

generate_all_verticals(d_tags_v, d_tags_h)

l_id_tags = convert(d_tags_h)

S = build_slideshow(l_id_tags)

build_output(S, fname + ".out")


