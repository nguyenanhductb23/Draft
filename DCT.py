import math
 
# Function to find discrete cosine transform and print it
def dctTransform(matrix, m, n):
 
    # dct will store the discrete cosine transform
    dct = []
    for i in range(m):
        dct.append([None for _ in range(n)])
 
    for i in range(m):
        for j in range(n):
 
            # ci and cj depends on frequency as well as
            # number of row and columns of specified matrix
            if (i == 0):
                ci = 1 / (m ** 0.5)
            else:
                ci = (2 / m) ** 0.5
            if (j == 0):
                cj = 1 / (n ** 0.5)
            else:
                cj = (2 / n) ** 0.5
 
            # sum will temporarily store the sum of
            # cosine signals
            sum = 0
            for k in range(m):
                for l in range(n):
 
                    dct1 = matrix[k][l] * math.cos((2 * k + 1) * i * math.pi / (
                        2 * m)) * math.cos((2 * l + 1) * j * math.pi / (2 * n))
                    sum = sum + dct1
 
            dct[i][j] = ci * cj * sum
 
    for i in range(m):
        for j in range(n):
            print(dct[i][j], end="\t")
        print()
        
    
def idctTransform(dct, m, n):    
    # f will store the inverse discrete cosine transform
	f = []
	for i in range(m):
	    f.append([None for _ in range(n)])

	for i in range(m):
	    for j in range(n):

			# ci and cj depends on frequency as well as
			# number of row and columns of specified matrix
		    if (i == 0):
			    ci = 1 / (m ** 0.5)
		    else:
		    	ci = (2 / m) ** 0.5
		    if (j == 0):
		    	cj = 1 / (n ** 0.5)
		    else:
		    	cj = (2 / n) ** 0.5

			# sum will temporarily store the sum of
			# cosine signals
		    sum = 0
		    for k in range(m):
		    	for l in range(n):
				    idct1 = ci * cj * dct[k][l] * math.cos((2 * i + 1) * k * math.pi / (
				        2 * m)) * math.cos((2 * j + 1) * l * math.pi / (2 * n))
				    sum = sum + idct1

		    f[i][j] = sum

	for i in range(m):
	    for j in range(n):
	        print(f[i][j], end="\t")
	        print()
 
# Driver code
matrix = [[255, 255, 255, 255, 255, 255, 255, 255],
          [255, 255, 255, 255, 255, 255, 255, 255],
          [255, 255, 255, 255, 255, 255, 255, 255],
          [255, 255, 255, 255, 255, 255, 255, 255],
          [255, 255, 255, 255, 255, 255, 255, 255],
          [255, 255, 255, 255, 255, 255, 255, 255],
          [255, 255, 255, 255, 255, 255, 255, 255],
          [255, 255, 255, 255, 255, 255, 255, 255]]
 
dctTransform(matrix, 8, 8)



dct = [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]

idctTransform(dct, 8, 8)
