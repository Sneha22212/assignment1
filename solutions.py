#Q1 sum of two numbers
a=int(input("enter first number ")) #take first num as input
b=int(input("enter second number"))  #take second num as input
c=a+b                                #calculate sum
print(c)                             #printing the sum


#Q2 even or odd 
num=int(input("enter a number"))    #take num as input
if(num%2==0):                       #check if num is completely divided by two
    print(f"{num}is an even number")
else:
    print(f"{num} is an odd number")


#Q3 factorial
num=int(input("enter  number"))    
fact=1
for i in range (1,num+1):
    fact*=i
print(fact) 


#Q4 greeting with name
name=input("enter name")
print(f"Good evening{name}")


#Q5 writing in a text file
string=input("enter string")
samplefile=open('abc.txt','w')
print(string,file=samplefile) 


#Q6 reading from a file
samplefile=open('abc.txt','r')
content=samplefile.read()
print(content)


#Q7 length of a string
s=input("enter a string")
print(f"length of {s} is " + str(len(s)))

#Q8 concate two strings
str1="hello"
str2="all"
print(str1+" "+str2)

#Q9 substring present or not in a string
str1="hello all , how are you"
print('hello' in str1)  #true
print('each' in str1)   #false


#Q10 convert string to uppercase
str1='hello all'
print(str1.upper()) 


#Q11 first n numbers of fibonacci series
n=int(input("enter value for n "))
a=0
b=1
i=1
while (i in range (n+1)):
    print(a)
    next=a+b
    a=b
    b=next
    i+=1  


#Q12 sum of digits of a given number
num=int(input("enter number")) #taking a number as input
sum= 0
while num > 0:
    digit = num % 10
    sum+= digit
    num//= 10
print(f"Sum of digits: {sum}")  #printing the sum


#Q13 calculate age by birthyear
year=int(input("enter your birth year"))
current=2024
age=current-year
print(age) 


#Q14 multiple line input from user till they enter empty line
lines = []
print("Enter multiple lines of text ")
while True:
    line = input()
    if line == "":
        break
    lines.append(line)

print("You entered:")
for line in lines:
    print(line)



#Q15 reading and printing from csv file
file=open("xyz.csv",'r')
content=file.read()
print(content)


#Q16 frequency of characters in string 
string = input("Enter a string: ")
char_freq= {}

for char in string:
    if char in char_freq:
        char_freq[char] += 1
    else:
        char_freq[char] = 1

print("Character frequencies:")
for char, freq in char_freq.items():
    print(f"{char}: {freq}") 


#Q17 converting string to title case
string = input("Enter a string: ")# Input string
title_case = string.title()
print("String in title case:", title_case)


#Q18 check if two strings are anagrams
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

char_count1 = {}
char_count2 = {}

for char in str1:
    if char in char_count1:
        char_count1[char] += 1
    else:
        char_count1[char] = 1
for char in str2:
    if char in char_count2:
        char_count2[char] += 1
    else:
        char_count2[char] = 1

if char_count1 == char_count2:
    print(f"{str1} and {str2} are anagrams.")
else:
    print(f"{str1} and {str2} are not anagrams.")


#Q19 remove all punctuations from a given string 
string = input("Enter a string: ")
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

s= ""    # empty string to store string without punctuations
for char in string:
    if char not in punctuations:
        s += char  

print("String without punctuation:", s)

#Q20 sum of list of numbers
numbers = [10, 20, 30, 40, 50]
sum = 0
for num in numbers:
    sum += num  
print("Sum of the numbers:", sum)

#Q21 number of occurences of an element in a list
numbers = [1, 2, 3, 4, 2, 2, 5, 2]
element_to_count = int(input("enter number to count"))
count = 0

for i in numbers:
    if i == element_to_count:
        count += 1  # Increment count whenever element_to_count is found

# Print the count of occurrences
print(f"Count of {element_to_count} in the list:", count)



#Q22 minimum and maximum number in a list
numbers = [5, 10, 3, 8, 15, 2]

# Initialize mim and max to first number of list
min_num = numbers[0]  
max_num = numbers[0]  

for num in numbers:
    if num < min_num:
        min_num = num  # Update min_num if a smaller number is found
    if num > max_num:
        max_num = num  # Update max_num if a larger number is found

print("Minimum number:", min_num)
print("Maximum number:", max_num)



#Q23 converting celcius to fahrenheit and vice-versa
# celcius to fahrenheit

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius} Celsius is equal to {fahrenheit} Fahrenheit")

#fahrenheit to celcius

fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print(f"{fahrenheit} Fahrenheit is equal to {celsius} Celsius")



#Q24 calculator
num1=float(input("enter first number"))
num2=float(input("enter second number"))
operator=input("enter operator")
result=0
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        print("Error: Division by zero")
else:
    print("Error: Invalid operator")

print(f"Result: {num1} {operator} {num2} = {result}")



#Q25 copy content of one text file to other
source=open("abc.txt",'r')
content=source.read()

destination=open("pqr.txt",'w')
destination.write(content)
print("content written successfully") 



#Q26 to check if a string start with a given prefix or end with a given suffux

string="hello everyone , how are you"
prefix=input("enter prefix to check") 
if (string.startswith(prefix)):
    print(f"The string '{string}' starts with the prefix '{prefix}'")
else:
    print(f"The string '{string}' does not start with the prefix '{prefix}'") 

suffix=input("enter suffix to check ")
if (string.endswith(suffix)):
    print(f"The string '{string}' ends with the suffix '{suffix}'")
else:
    print(f"The string '{string}' does not ends with the suffix '{suffix}'") 



#Q27 convert string to list of its characters
string=input("enter string")  #input a string
char_list = []                #empty list to store the characters 

for i in string:
    char_list.append(i)      # adding all characters to the list
print("List of characters:", char_list) 









