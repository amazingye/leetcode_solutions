#快速排序
def quickSort(L,low,high):
	i = low
	j = high
	if i>= j:
		return L
	key = L[i]
	while i<j:
		while i<j and L[j]>=key:
			j-=1
		L[i] = L[j]
		while i<j and L[i]<=key:
			i+=1
		L[j] = L[i]
	L[i] = key
	quickSort(L,low,i-1)
	quickSort(L,j+1,high)


#test
a = [7,4,6,9,9,8,5,10,2]
low = 0
high = len(a)-1
quickSort(a,low,high)
print(a)
