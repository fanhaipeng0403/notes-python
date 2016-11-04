# def sum_self1(n):
# 	if n==1:
# 		return 1
# 	else:
# 		toatl=n+sum_self1(n-1) 
#     return n

def sum_self2(n):
	total=0
	for i in xrange(n+1):
		total=total+i
	    print(total) 