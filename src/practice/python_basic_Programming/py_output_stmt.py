# Python Print stmt

a,b,c=10,20,30
print('Values of::',a,b,c) # -> Values of:: 10 20 30

# sep attribute

# withpout separtor
print(a,b,c)

# using sepearator
print(a,b,c,sep='*') # adding own separater * 

# output stmt with end attribut

print('Hello Pradeep',end='\t')
print('Cool',end='\t')
print('Default')

# {} replacemet operator

name='Prdeep'
age=29
nature='Silent'

# use Replacement operator

print('Hi {} you age may be {} and you are in {} only'.format(name,age,nature))
