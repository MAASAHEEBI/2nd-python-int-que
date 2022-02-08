'''Write a Python Program for Sum of squares of first n natural numbers
Examples:
Input : N = 4
Output :1 + 4 + 9 + 16 = 30'''

n=int(input('Enter the num till what you want to square and add: '))
sm = 0
for i in range(1, n+1) : 
 sm = sm + (i * i)
print(sm)

