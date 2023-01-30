import sys
n = int(sys.argv[1])
for i in range(n+1):
	with open('lambdas', 'a') as the_file:
		the_file.write('{}\n'.format(i/n))

