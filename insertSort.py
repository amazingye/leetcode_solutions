#插入排序
def insertSort(L,first,last):
	for i in range(first+1,last):
		temp = L[i]
		j = i-1
		while j>=0 and L[j]>temp:
			L[j+1] = L[j]
			j-=1
		if(j!=i-1):
			L[j+1] = temp


#test
L = [4,2,5,6,1,7]
insertSort(L,0,len(L)-1)
print(L)
			
