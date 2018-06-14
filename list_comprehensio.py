x = int ( raw_input())
y = int ( raw_input())
n = int ( raw_input())
print [ [ i, j] for i in range( x + 1) for j in range( y + 1) if ( ( i + j ) != n )]



'''x = int(raw_input("Enter first number"))
y = int(raw_input("Eneter second number"))
n = int(raw_input("Enter value of N"))
ar = []
p = 0
for i in range ( x + 1 ) :
    for j in range( y + 1):
         if i+j != n:

             ar.append([])
             ar[p] = [i , j]
             p+=1           
print ar
'''
