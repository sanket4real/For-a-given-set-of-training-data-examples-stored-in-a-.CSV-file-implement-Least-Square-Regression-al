# Function to calculate b
def calculateB(x, y, n):

	# sum of array x
	sx = sum(x)

	# sum of array y
	sy = sum(y)
	
	# for sum of product of x and y
	sxsy = 0

	# sum of square of x
	sx2 = 0

	for i in range(n):
		sxsy += x[i] * y[i]
		sx2 += x[i] * x[i]
	b = (n * sxsy - sx * sy)/(n * sx2 - sx * sx)
	return b

# Function to find the
# least regression line
def leastRegLine(X,Y,n):
	
	# Finding b
	b = calculateB(X, Y, n)
	meanX = int(sum(X)/n)
	meanY = int(sum(Y)/n)

	# Calculating a
	a = meanY - b * meanX

	# Printing regression line
	print("Regression line:")
	print("Y = ", '%.3f'%a, " + ", '%.3f'%b, "*X", sep="")

# Driver code

# Statistical data
import pandas as pd
# Step 1 :Import libraries and dataset
datas = pd.read_csv('data.csv')
print(datas )
X = datas.TEMPERATURE

Y = datas.PRESSURE
n = len(X)
leastRegLine(X, Y, n)
