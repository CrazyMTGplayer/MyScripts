#countnsay.py
#Sequence of 1, 11, 21, 1211, 111221, 312211, 13112221
#prints nth element of sequence

def main():
	print "1, 11, 21, 1211... prints nth number"
	inputstring = raw_input('Nth number : ')
	print "Input is ",  inputstring
	print "Output is ", process(int(inputstring))

def process(target):
	if (target == 0):
		return ""

	seq = '1'
	for i in range(1,target):
		lastseq = seq
		seq = []
		count, seqCh = 1, lastseq[0]
		for j in range(1, len(lastseq)):
			if seqCh == lastseq[j]:
				count += 1
			else:
				seq.append(str(count))
				seq.append(seqCh)
				seqCh = lastseq[j]
				count = 1
		seq.append(str(count))
		seq.append(seqCh)

	return ''.join(seq)

def countseq(seq):
	num = len(seq)
	digit = seq[0]
	return str(num) + digit

if __name__ == "__main__":
	main()

