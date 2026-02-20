import json
import math
a = int(input("first number"))
b = int(input("second number"))
r=1
while(True):
	if a or b == 0:
		r = 0;
	x = int(a/b)
	r = a- (b*x)
	if r == 0:
		print(b)
		exit()
	a=b
	b=r
print(b)

