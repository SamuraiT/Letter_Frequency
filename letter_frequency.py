#frequency of a letter
import string

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def most_frequent(st):
	"""
	make a list of (frequency, letter) of a strint:st
	st:a string you will examine each letter frequency 
	return list of tuple(freq,letter)
	"""
	alpha = zip(alphabet,[0]*26)
	d = dict(alpha)
	t = []
	count = 0.0
	for letter in st:
		if letter not in alphabet: continue
		d[letter] = d.setdefault(letter,0)+1
		count += 1
	for letter,freq in d.items():
		t.append( (freq*100/count,letter,))
	t.sort(reverse = True)
	return t

def most_frequent_fromfile(filename ='sample.txt'):
	"""
	examine frequency of each letter of the file you pass
	this func only allows an alphabet letter

	filename:the file you will examine
	return list of tuple(freq,letter)
	"""
	fin = open(filename)
	alpha = zip(alphabet,[0]*26)
	d = dict(alpha)
	t = []
	count = 0.0
	for line in fin:
		line = line.strip().lower()
		for letter in line:
			if letter not in alphabet :continue
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

def compare_list(sample,stats):
	"""
	compare the each frequency of letter from sample you'd like to examine
	and stats( statistic data) 
	and print the result in descending order
	"""
	#if not len(sample) >= len(stats):raise TypeError,'the length of sample and stats are different'
	for i in range( len(sample) ):
		print sample[i][1],'%0.2f' % sample[i][0],stats[i][0],stats[i][1],(' <- bingo' if sample[i][1] == stats[i][0] else '')

def compare(sample_file,stats_file = 'frequency_of_letter.txt'):
	"""comare the letter frequency of the sample_file with 
	stats_file.
	then print them in descending order
	"""
	stats = make_frequency_list(stats_file)
	sample = most_frequent_fromfile(sample_file)
	compare_list(sample,stats)

def compare_string(message,stats_file = 'frequency_of_letter.txt'):
	"""
	compare the letter frequency of the message with 
	stats_file.
	then print them in descending order
	"""
	stats = make_frequency_list(stats_file)
	sample = most_frequent(message)
	compare_list(sample,stats)


		
if __name__ == '__main__':
	sample = most_frequent_fromfile()
	stats = make_frequency_list()
	compare_list(sample,stats)
	print
	sample_file = 'sample.txt'
	compare( sample_file )
	print 
	message = 'hello, thank you for trying to run this module. if you have a problem, suggestion, comment,or question,feel free to ask me ! thank you'
	compare_string(message)

	
