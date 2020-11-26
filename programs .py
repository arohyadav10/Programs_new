#%% basic core programs 

# 1st question User Input and Replace String Template “Hello <<UserName>>, How are you?” 

a=input("Enter Username: ")
if len(a)<3:
   print('enter a longer name')
else:
   print('Hello ,how are you?'+a)

#%%   #2nd question flip coin with head and tail percentage 

import random

def flipCoin():
    heads = 0 
    tails = 0 
    headspercent = 0 
    tailspercent = 0 

    for i in range(1000): 
      coin=random.randint(1,2) 

      if coin==1: 
          heads+=1 
      else: # 
          tails+=1 

    headspercent = heads / 10.0 
    tailspercent = 100.0 - headspercent 

    print("Heads percent: " + str(headspercent)) 
    print("Tails percent: " + str(tailspercent)) 



flipCoin() 
#%% 3.leap year 
# Python program to check if year is a leap year or not

year = 2012

if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))

#%% 4. power of 2
# Display the powers of 2 using anonymous function

terms = 10

# Uncomment code below to take input from the user
# terms = int(input("How many terms? "))

# use anonymous function
result = list(map(lambda x: 2 ** x, range(terms)))

print("The total terms are:",terms)
for i in range(terms):
   print("2 raised to power",i,"is",result[i])

#%% 5.harmonic numbers 

def nthHarmonic(N) : 
	# H1 = 1 
	harmonic = 2
    
	# Hn = H1 + H2 + H3 ... + 
	# Hn-1 + Hn-1 + 1/n 
	for i in range(2, N + 1) : 
		harmonic += 1 / i 

	return harmonic 
	 
if __name__ == "__main__" : 

	N = 10
	print(round(nthHarmonic(N),5)) 


#%% 6. Factors .. program to print prime factors 

import math 

def primeFactors(n): 
	
	while n % 2 == 0: 
		print 2, 
		n = n / 2
		
	for i in range(3,int(math.sqrt(n))+1,2): 
		

		while n % i== 0: 
			print i, 
			n = n / i 
			

	if n > 2: 
		print n 

n = 315
primeFactors(n) 

#%% Functional programs 

# 1. 2D array

n_rows= int(input("Number of rows:"))

n_cols = int(input("Number of columns:"))

matrix = [ ]

print("Enter the entries row-wise:")


for i in range(n_rows):          

    a =[ ]

    for j in range(n_cols):      

         a.append(int(input()))

    matrix.append(a)

for i in range(n_rows):

    for j in range(n_cols):

        print(matrix[i][j], end = " ")

    print( )

#%% 2.Sum of three integers add to zero

def findTriplets(arr, n): 

	found = True
	for i in range(0, n-2): 
	
		for j in range(i+1, n-1): 
		
			for k in range(j+1, n): 
			
				if (arr[i] + arr[j] + arr[k] == 0): 
					print(arr[i], arr[j], arr[k]) 
					found = True
	
	if (found == False): 
		print(" not exist ") 

arr = [0, -1, 2, -3, 1] 
n = len(arr) 
findTriplets(arr, n) 

#%% 3. Euclidean  Distance
import math 

def distance(x1 , y1 , x2 , y2): 

	return math.sqrt(math.pow(x2 - x1, 2) +
				math.pow(y2 - y1, 2) * 1.0) 

print("%.6f"%distance(0, 0, 4, 3)) 

#%% 4. Quadratic equation 
# Solve the quadratic equation ax**2 + bx + c = 0

import cmath

a = 1
b = 5
c = 6

d = (b**2) - (4*a*c)

sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))

#%% 5. Windchill 

import math
v = float(input("Input wind speed in kilometers/hour: "))
t = float(input("Input air temperature in degrees Celsius: "))

Fahrenheit = (t * 9/5) + 32
t= Fahrenheit
print("Temperature in Fahrenheit is ",+t)
wci = 13.12 + 0.6215*t -  11.37*math.pow(v, 0.16) + 0.3965*t*math.pow(v, 0.16)
print("The wind chill index is", int(round(wci, 0)))


#%%  Logical programs

# 1.Gambler

import random
import time
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import style

style.use("ggplot")

broke_count = 0

totalFunded = 0
totalEnding = 0

wins = 0
losses = 0

def Labouchere():
    global broke_count
    global totalFunded
    global totalEnding
    global wins
    global losses

    
    starting_funds = 50

    totalFunded += starting_funds

    
    goal = 10
    system = [1,1,1,1,1,1,1,1,1,1]
    #system = [1,2,2,3,2]

    profit = 0

    current_funds = starting_funds

    wagerSizes = []
    plot_funds = []

    not_broke = True

    wins = 0
    losses = 0

    while profit < goal and not_broke:
        if len(system) > 1:
            size = system[0]+system[-1]
            wagerSizes.append(size)
            plot_funds.append(current_funds)

        else:
            size = system[0]
            wagerSizes.append(size)
            plot_funds.append(current_funds)


        if current_funds <= 0:
            not_broke = False
            broke_count += 1
            losses += 1

        elif current_funds - size <= 0:
            size = current_funds
            not_broke = False
            broke_count += 1

        dice = random.randrange(1,101)

        if dice < 51:
            losses += 1
            system.append(size)
            current_funds -= size
            profit = current_funds - starting_funds

        else:
            wins += 1
            current_funds += size
            profit = current_funds - starting_funds

            if profit != goal:
                try:
                    del system[0]
                    del system[-1]
                except:
                    pass

    wagerSizes.append(size)
    plot_funds.append(current_funds)

    totalEnding += current_funds

    s1.plot(wagerSizes)
    s2.plot(plot_funds)

    


f = plt.figure()
s1 = f.add_subplot(211)
s2 = f.add_subplot(212)

sample_size = 10000

for x in range(sample_size):
    Labouchere()

#print("Winners:",wins,"losers:",losses)
print(totalFunded, totalEnding)
print("Broke Percentage:", ((float(broke_count)/sample_size))*100.0)

plt.show()

#%% 2. coupon numbers

import random

coupon = open("coupons.txt", "a")

def generate(amount):

    for x in range(0, amount):

        a = random.randint(1000, 9999)
        a = str(a)
        b = random.randint(1000, 9999)
        b = str(b)
        c = random.randint(1000, 9999)
        c = str(c)

        total = ""
        total = str(total)
        total = a + " " + b + " " + c

        coupon.write(total)
        coupon.write("\n")


amount = int(input("How many coupons do you want to generate: "))

generate(amount)

coupon.close()

print("\nCode's have been generated!")

 
#%% 3. Simulate stopwatch program

import os    
import time    
second = 0    
minute = 0    
hours = 0    
while(True):    
    print("Stopwatch")    
    print('\n\n\n\n\n\n\n')    
    print('\t\t\t\t-------------')    
    print('\t\t\t\t  %d : %d : %d '%(hours,minute,second))    
    print('\t\t\t\t-------------')    
    time.sleep(1)    
    second+=1    
    if(second == 60):    
        second = 0    
        minute+=1    
    if(minute == 60):    
        minute = 0    
        hour+=1;    
    os.system('cls')   

#%% 4. cross game or tic tac toe game

import numpy as np 
import random 
from time import sleep 

def create_board(): 
	return(np.array([[0, 0, 0], 
					[0, 0, 0], 
					[0, 0, 0]])) 

def possibilities(board): 
	l = [] 
	
	for i in range(len(board)): 
		for j in range(len(board)): 
			
			if board[i][j] == 0: 
				l.append((i, j)) 
	return(l) 

def random_place(board, player): 
	selection = possibilities(board) 
	current_loc = random.choice(selection) 
	board[current_loc] = player 
	return(board) 

def row_win(board, player): 
	for x in range(len(board)): 
		win = True
		
		for y in range(len(board)): 
			if board[x, y] != player: 
				win = False
				continue
				
		if win == True: 
			return(win) 
	return(win) 

def col_win(board, player): 
	for x in range(len(board)): 
		win = True
		
		for y in range(len(board)): 
			if board[y][x] != player: 
				win = False
				continue
				
		if win == True: 
			return(win) 
	return(win) 

def diag_win(board, player): 
	win = True
	y = 0
	for x in range(len(board)): 
		if board[x, x] != player: 
			win = False
	if win: 
		return win 
	win = True
	if win: 
		for x in range(len(board)): 
			y = len(board) - 1 - x 
			if board[x, y] != player: 
				win = False
	return win 
 
def evaluate(board): 
	winner = 0
	
	for player in [1, 2]: 
		if (row_win(board, player) or
			col_win(board,player) or
			diag_win(board,player)): 
				
			winner = player 
			
	if np.all(board != 0) and winner == 0: 
		winner = -1
	return winner 
 
def play_game(): 
	board, winner, counter = create_board(), 0, 1
	print(board) 
	sleep(2) 
	
	while winner == 0: 
		for player in [1, 2]: 
			board = random_place(board, player) 
			print("Board after " + str(counter) + " move") 
			print(board) 
			sleep(2) 
			counter += 1
			winner = evaluate(board) 
			if winner != 0: 
				break
	return(winner) 

print("Winner is: " + str(play_game())) 

#%% Programs for Junit testing


#%% Algorithm Programs
 
# 1.Recursion method

def permutations(s):
 
    partial = []
 
    partial.append(s[0])
 
    for i in range(1, len(s)):
 
 
        
        for j in reversed(range(len(partial))):
 
            curr = partial.pop(j)
 
 
            for k in range(len(curr) + 1):
                partial.append(curr[:k] + s[i] + curr[k:])
 
    print(partial, end='')
 
 
if __name__ == '__main__':
 
    s = "aroh"
    permutations(s)

#%% 2.binary search

def binarySearch(arr, x): 
	l = 0
	r = len(arr) 
	while (l <= r): 
		m = l + ((r - l) // 2) 

		res = (x == arr[m]) 

		if (res == 0): 
			return m - 1

		if (res > 0): 
			l = m + 1

		else: 
			r = m - 1

	return -1


if __name__ == "__main__": 

	arr = ["score", "goals", 
			"ide", "practice"]; 
	x = "ide"
	result = binarySearch(arr, x) 

	if (result == -1): 
		print("Element not present") 
	else: 
		print("Element found at index" , 
								result) 


#%% 3. Insertion sort

def insertion_sort(arr):
 
    #loop over all the elements in the list 
    for i in range(1, len(arr)): 
   
        val = arr[i]
   
        # move elements of list [0..i-1], that are 
        # greater than val, to one position ahead 
        # of the current position 
        j = i-1
        while j >=0 and val < arr[j] : 
            arr[j+1] = arr[j] 
            j -= 1
        arr[j+1] = val
     
    return arr
 
#given string
arr= "havertz"
print("Original String: ",arr)
arr = [i for i in arr]
sorted_arr = insertion_sort(arr)
print("Sorted String: ",sorted_arr)
insertion_sort(arr)

#%% 4. Bubble sort

def bubbleSort(arr): 
	n = len(arr) 

	for i in range(n-1): 
 
		for j in range(0, n-i-1): 

			if arr[j] > arr[j+1] : 
				arr[j], arr[j+1] = arr[j+1], arr[j] 

arr = [55, 33, 22, 99, 88, 11, 90] 

bubbleSort(arr) 

print ("Sorted array is:") 
for i in range(len(arr)): 
	print ("%d" %arr[i]), 

#%% 5. Merge sort

def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)

#%% 6. Anagram Detection 


def check(s1, s2): 
	
	# the sorted strings are checked 
	if(sorted(s1)== sorted(s2)): 
		print("The strings are anagrams.") 
	else: 
		print("The strings aren't anagrams.")		 
		
# driver code 
s1 ="abcd"
s2 ="dcba"
check(s1, s2) 

#%% 7. prime numbers 

lower = 0
upper = 1000

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)

#%% 8.prime numbers anagram and palindrome
 
import math as mt 

def isPrime(num): 

	if (num < 2 or num % 2 == 0): 
		return num == 2
	for i in range(3, mt.ceil(mt.sqrt(num + 1))): 
		if (num % i == 0): 
			return False
	return True

def primePalindrome(N): 

	# if(8<=N<=11) return 11 
	if (8 <= N and N <= 11): 
		return 11

		for x in range(1, 100000): 
	
		s = str(x) 
		d = s[::-1] 
		y = int(s + d[1:]) 
	 
		if (y >= N and isPrime(y)): 
			return y 
	
print(primePalindrome(112)) 

#%% 9.Rewrite Use Generics for Search and Sort Algorithms

def selection_sort(items):
    """Sorts a list of items into ascending order using the
       selection sort algoright.
       """
    for step in range(len(items)):
        # Find the location of the smallest element in
        # items[step:].
        location_of_smallest = step
        for location in range(step, len(items)):
            # determine location of smallest
            if items[location] < items[location_of_smallest]:
                location_of_smallest = location
        # Exchange items[step] with items[location_of_smallest]
        temporary_item = items[step]
        items[step] = items[location_of_smallest]
        items[location_of_smallest] = temporary_item
        
#%%

def binary_search(items, desired_item, start=0, end=None):
    if end == None:
        end = len(items)

    if start == end:
        raise ValueError("%s was not found in the list." % desired_item)

    pos = (end - start) // 2 + start

    if desired_item == items[pos]:
        return pos
    elif desired_item > items[pos]:
        return binary_search(items, desired_item, start=(pos + 1), end=end)
    else: 
        return binary_search(items, desired_item, start=start, end=pos)        

#%% 10 find number

def binary_search(arr, low, high, x): 
	if high >= low: 

		mid = (high + low) // 2

		if arr[mid] == x: 
			return mid 

		
		elif arr[mid] > x: 
			return binary_search(arr, low, mid - 1, x) 

		else: 
			return binary_search(arr, mid + 1, high, x) 

	else: 
		return -1

arr = [ 2, 3,78,9,11,13,14,19,20, 4, 10, 40 ] 
x = 20

result = binary_search(arr, 0, len(arr)-1, x) 

if result != -1: 
	print("Element is present at index", str(result)) 
else: 
	print("Element is not present in array") 

#%% 11. input output format



#%%  12. message demonstration using string funvtion and RegEx

import tkinter as tk  
from tkinter import ttk  
from tkinter import Menu  
from tkinter import messagebox as mbox  
app = tk.Tk()  
 
app.title("Python GUI App")  

ttk.Label(app, text="this is the message box").grid(column=0,row=0,padx=20,pady=30)  

menuBar=Menu(app)  
app.config(menu=menuBar)  

def _msgBox():  
   mbox.showinfo('Python Message Box',' Using Message box.')  
    
   infoMenu=Menu(menuBar, tearoff=0)  
   infoMenu.add_command(label="Info", command=_msgBox)  
   menuBar.add_cascade(label="Message", menu=infoMenu)  
   app.mainloop() 

_msgBox()

#%% Data structure programs

# 1. Unordered list
            
#%% 2. ordered list


#%%  3. Simple Balanced Parentheses

PAIRINGS = {
    '(': ')',
    '{': '}',
    '[': ']'
}

def is_balanced(symbols):
    stack = []
    for s in symbols:
        if s in PAIRINGS:
            stack.append(s)
            continue
        try:
            expected_opening_symbol = stack.pop()
        except IndexError:  
            return False
        if s != PAIRINGS[expected_opening_symbol]:  
            return False
    return len(stack) == 0 

is_balanced('{{([][])}()}')  
is_balanced('{[])')  
is_balanced('((()))')  
is_balanced('(()')  
is_balanced('())')  
#%% 4.Simulate Banking Cash Counter

class Bank_Account: 
	def __init__(self): 
		self.balance=0
		print("Hello!!! Welcome to the Deposit & Withdrawal Machine") 

	def deposit(self): 
		amount=float(input("Enter amount to be Deposited: ")) 
		self.balance += amount 
		print("\n Amount Deposited:",amount) 

	def withdraw(self): 
		amount = float(input("Enter amount to be Withdrawn: ")) 
		if self.balance>=amount: 
			self.balance-=amount 
			print("\n You Withdrew:", amount) 
		else: 
			print("\n Insufficient balance ") 

	def display(self): 
		print("\n Net Available Balance=",self.balance) 

s = Bank_Account() 

s.deposit() 
s.withdraw() 
s.display() 


#%% 5.Palindrome-Checker

def isPalindrome(str):
 
	for i in range(0, int(len(str)/2)): 
		if str[i] != str[len(str)-i-1]:
			return False
	return True

s = "radar"
ans = isPalindrome(s)

if (ans):
	print("Yes")
else:
	print("No")

#%% 6.Hashing Function to search a Number in a slot

country_code = [('15', 'germany'), ('20', 'china'), ('10', 'england')]
 
def insert(item_list, key, value):
    item_list.append((key, value))
 
def search(item_list, key):
    for item in item_list:
        if item[0] == key:
            return item[1]
    
print (search(country_code, '15')) 

#%% 7. Number of Binary Search Tree in website https://www.hackerrank.com/challenges/number-of-binary-search-tree

#%% 8. 2d array prime numbers

def prime(n): 

	for i in range(2, n): 
		if i * i > n: 
			break
		if(n % i == 0): 
			return False; 

	return True
	
def prime_range(start, end, a): 
	
	for i in range(start, end): 

		if(prime(a[i])): 
			print(a[i], end = " ") 

def Print(arr, n): 

	print("Prime numbers in the", 
		"first half are ", end = "") 
	prime_range(0, n // 2, arr) 
	print() 

	print("Prime numbers in the", 
		"second half are ", end = "") 
	prime_range(n // 2, n, arr) 
	print() 

arr = [2, 5, 10, 15, 17, 21, 23] 
n = len(arr) 
Print(arr, n) 

#%% 9. add anagram to above program

#%% 10.

#%% 11. 

#%% 12.Calender 
import calendar

yy = 2020
mm = 12

# yy = int(input("Enter year: "))
# mm = int(input("Enter month: "))

# display the calendar
print(calendar.month(yy, mm))


#%% 13.
import calendar
print(calendar.weekday(2016, 5, 15))

#%% 14.

