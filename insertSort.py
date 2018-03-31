#插入排序
def insertSort(L):
	for i in range(len(L)):
		temp = L[i]
		j = i-1
		while j>=0 and L[j]>temp:
			L[j+1] = L[j]
			j-=1
		if(j!=i-1):
			L[j+1] = temp


#test
L = [4,2,5,6,1,7,3,6,1,2]
insertSort(L)
print(L)
