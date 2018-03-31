#希尔排序
def shellSort(L):
	d = len(L)
	while True:
		d = d//2
		for x in range(d):
			for i in range(x,len(L),d):
				temp = L[i]
				j = i-d
				while j>=0 and L[j]>temp:
					L[j+d] = L[j]
					j-=d
				if j != i-d:
					L[j+d] = temp
		if d == 1:
			return


l = [49,38,65,97,76,13,27,49,78,34,12,64,1]
shellSort(l)
print(l)
