
def doesFileExist(fileadress):
	try:
		with open(fileadress) as f:
			for line in f:
				pairs = line.split(" - ")
				meaningpair = pairs[1].split(", ")
				print (pairs[0])
				for pair in meaningpair:
					print pair
	except IOError:
		print ("File does not exist")


def main():
	doesFileExist('dict.txt')

if __name__ == '__main__':
	main()
