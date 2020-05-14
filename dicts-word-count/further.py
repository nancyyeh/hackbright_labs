
# import sys
import string
from collections import Counter

def word_count(file_name):

	file = open(file_name)

	entire_doc = file.read()
	entire_doc = entire_doc.replace("\n", " ")
	words = entire_doc.split(" ")

	clean_list = []

	for word in words:
		word = word.lower()
		word = word.strip(string.punctuation)
		clean_list.append(word)

	word_counts = Counter(clean_list)

	print(word_counts)

	# count_dic = {}

	# for line in open(file_name):
	# 	line = line.rstrip()
	# 	words = line.split(" ")
	# 	for word in words:
	# 		word = word.lower()
	# 		word = word.strip(string.punctuation)
	# 		count_dic[word] = count_dic.get(word, 0) + 1

	# #return count_dic

	# for key, value in count_dic.items():
	# 	print(f"{key} {value}")

# file = sys.argv[1]
# word_count(file)