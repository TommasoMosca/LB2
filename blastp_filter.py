import sys

def filter(input_file):
	for line in input_file:
		line= line.rstrip().split()
		block = line[1]+' '+line[2]
		block = block.split()
		block[1] = float(block[1])
		if block[1] <= 30:
			print(block)



if __name__ == '__main__':
	blastp_file=sys.argv[1]
	with open(blastp_file) as filein:
		filter(filein)
