from numba import jit
import math
import time



def start(start,end):
	is_prime=True
	index=start
	a=time.clock()
	print("Start")
	while(index<end):
		
		is_prime=True
		for j in range(2,int(math.sqrt(index))):
			if(index%j==0):
				is_prime=False
				index=index+1
				break
		if(is_prime):
			print(index)
			# print(time.clock()-a)
			# a=time.clock()
			index=index+2
			pass
@jit
def start_jit(start,end):
	is_prime=True
	index=start
	a=time.clock()
	print("Start")
	while(index<end):
		
		is_prime=True
		for j in range(2,int(math.sqrt(index))):
			if(index%j==0):
				is_prime=False
				index=index+1
				break
		if(is_prime):
			print(index)
			# print(time.clock()-a)
			# a=time.clock()
			index=index+2
			pass



# for i in range(40):
# 	a=time.clock()
# 	start_jit(2,21474836400)
# 	print(2**i,time.clock()-a)

start_index=2**46

print(start_index)
a=time.clock()
start(start_index,start_index+140)
print(time.clock()-a)
# print(2**40,2**40+2)
a=time.clock()
start_jit(start_index,start_index+300)
print(time.clock()-a)
