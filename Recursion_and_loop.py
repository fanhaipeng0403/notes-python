def sum_recursion(n):
	if n==1:
		return 1
	else:
		retur n+sum_recursion(n-1)
   

def sum_loop(n):
	total=0
	for i in range(n+1):
		total=total+i
	return total 