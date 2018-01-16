import time

start_time = time.time()
for a in range(0,1001):
	for b in range(0,1001-a):
		c = 1000-a-b
		if a*a+b*b==c*c:
			print(a,b,c)
end_time = time.time()
print('Take time:',end_time-start_time)

start_time = time.time()
for a in range(0,1001):
	for b in range(0,1001-a):
		c = 1000-a-b
		if c>=a and c>=b: # important sentence
			if a*a+b*b==c*c:
				print(a,b,c)
end_time = time.time()
print('Take time:',end_time-start_time)

start_time = time.time()
for a in range(0,1001):
	for b in range(0,1001-a):
		c = 1000-a-b
		if c<a or c<b: 
			break  # important sentence
		if a*a+b*b==c*c:
			print(a,b,c)
end_time = time.time()
print('Take time:',end_time-start_time)