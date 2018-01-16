from timeit import Timer
def t1():
	li = []
	for i in range(1000):
		li = li + [i]
def t2():
	li = []
	for i in range(1000):
		li.extend([i])
def t3():
	li = []
	for i in range(1000):
		li.append(i)
def t4():
	li = [i for i in range(1000)]
def t5():
	li = list(range(1000))

timer1 = Timer("t1()","from __main__ import t1")
print(timer1.timeit(1000))
timer2 = Timer("t2()","from __main__ import t2")
print(timer2.timeit(1000))
timer3 = Timer("t3()","from __main__ import t3")
print(timer3.timeit(1000))
timer4 = Timer("t4()","from __main__ import t4")
print(timer4.timeit(1000))
timer5 = Timer("t5()","from __main__ import t5")
print(timer5.timeit(1000))