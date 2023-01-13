#!/usr/bin/env python3

# convert fixed width 
import sys

def convert_fixed_with(rawfile, basefile, tday):
""" Convert fixed width file to delimited """

	
	list = [5, 55, 45, 72, 23, 43,
	        123, 145, 187, 199,
	        230, 54]
	
	filename = ''.join(['{}'.format(basefile),'_',
		                 '{}'.format(tday), '.txt'])
	f = open(filename, 'w')
	with open(rawfile, 'r') as infile:
		for line in infile:
			iter = 0 
			prev_position = 0 
			position = list[iter]
			temp = []
			while position < len(line) and iter + 1 < len(list):
				iter += 1
				temp.append(line[prev_position:position])
				prev_position = position
				position = list[iter]
			temp.append(line[prev_position:])

			temp_str = '|'.join(x for x in temp)

			f.write(temp_str)

	f.close()

if __name__ == '__main__':
	rawfile = sys.argv[1]
	basefile = sys.argv[2]
	tday = sys.argv[3]
	convert_fixed_with(rawfile, basefile, tday)




