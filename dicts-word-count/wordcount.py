
import sys
import string

def word_count(file_name):

	count_dic = {}

	for line in open(file_name):
		line = line.rstrip()
		words = line.split(" ")
		for word in words:
			word = word.lower()
			word = word.strip(string.punctuation)
			count_dic[word] = count_dic.get(word, 0) + 1

	#return count_dic

	for key, value in count_dic.items():
		print(f"{key} {value}")

file = sys.argv[1]
word_count(file)