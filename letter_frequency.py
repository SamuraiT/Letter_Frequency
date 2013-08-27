#frequency of a letter

def most_frequent(st):
	"""
	make a list of (frequency, letter) of a strint:st
	st:a string you will examine each letter frequency 
	return list of tuple(freq,letter)
	"""
	d = dict()
	t = []
	count = 0.0
	for letter in st:
		if letter in string.punctuation or letter in ' ': continue
		d[letter] = d.setdefault(letter,0)+1
		count += 1
	for letter,freq in d.items():
		t.append( (freq*100/count,letter,))
	t.sort(reverse = True)
	return t

def most_frequent_fromfile(filename ='sample_story.txt'):
	"""
	examine frequency of each letter of the file you pass
	this func only allows an alphabet letter

	filename:the file you will examine
	return list of tuple(freq,letter)
	"""
	fin = open(filename)
	d = dict()
	t = []
	count = 0.0
	for line in fin:
		line = line.strip().lower()
		for letter in line:
			if not letter in 'abcdefghijklmnopqrstuvwxyz':continue
			d[letter] = d.setdefault(letter,0)+1
			count += 1
	for letter,freq in d.items():
		t.append( (freq*100/count,letter,))
	t.sort(reverse = True)
	return t


def make_frequency_list(filename = 'frequency_of_letter.txt'):
	"""
	make a list of english letter frequency from the file.
	If you would like to make list from other source, you can 
	change the file name
	
	return: a list of (letter,freq) 
	"""
	fin = open(filename)
	t =[]
	for line in fin:
		line = line.strip().lower()
		if line[0] == '#':continue
		t.append( tuple( line.split() ) )
	return t

def compare(sample,stats):
	"""
	compare the each frequency of letter from sample you'd like to examine
	and stats( statistic data) 
	and print the result in descending order
	"""
	if not len(sample) == len(stats):raise TypeError,'the length of sample and stats are different'
	for i in range( len(sample) ):
		print sample[i][1],'%0.2f' % sample[i][0],stats[i][0],stats[i][1]

		
if __name__ == '__main__':
	sample = most_frequent_fromfile()
	stats = make_frequency_list()
	compare(sample,stats)
	
