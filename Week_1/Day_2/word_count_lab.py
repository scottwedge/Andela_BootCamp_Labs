# Counts the occurence of words in a sentence
def words(sentence):
	count_dict = {}
	for word in sentence.split():
		# if key is a integer
		if word.isdigit():
			count_dict.setdefault(int(word),0)
			count_dict[int(word)] += 1
		# otherwise treated as a string
		else:
			count_dict.setdefault(word,0)
			count_dict[word] += 1

	return count_dict

