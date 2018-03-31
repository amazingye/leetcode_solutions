def selectSort(L):
	for i in range(len(L)):
		small = L[i]
		postition = i
		for j in range(i+1,len(L)):
			if L[j]<small:
				small = L[j]
				postion = j
		L[postion] = L[i]
		L[i] = small


l = [4,6,3,7,9,1,0,3,23,41,2]
selectSort(l)
print(l)
