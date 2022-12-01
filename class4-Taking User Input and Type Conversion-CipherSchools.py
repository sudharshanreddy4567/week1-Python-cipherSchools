imrazzaditya
/
week1-Python-CipherSchools
Public
Code
Issues
Pull requests
Actions
Projects
Security
Insights
week1-Python-CipherSchools/class4-Taking User Input and Type Conversion-CipherSchools.py
@imrazzaditya
imrazzaditya Add files via upload
 1 contributor
32 lines (26 sloc)  673 Bytes
###########################Taking User Input################################
#Delimiter is \n character
a=input()
print(a)
print(type(a))
#Sample python code
a=input()
b=input()
print(a)
print(b)
#Input in python is delimited using \n by default

###########################Type Casting#####################################
a=65
bin(65)


###########################Typecoercion#####################################
#To do type concersion we use coersioning
a=15
print(str(a))
print(int('12345'))
print(float('1.5'))


#Python doesn't have type casting
a=65
isinstance(a,object)
a='A'
isinstance(a,object)
#In python the above is different
