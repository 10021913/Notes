"""
=====================================================================
=========================== PYTHON BASICS ===========================
=====================================================================
"""

# choose Numonic variables that you can
# additiion
a = a +1

#multiplication
a = a * 2

#subraction
a = a-1

# exponest
a = a ** 2

#less than and greater than
a = #assigning a value to the variable
a > 10 # a is greater than 10
a < 10 # a is less than 10
a <= 10 # a less than or equal to 10
a >= 10 # a greater than ot equal to 10
a != 10 # a is not equla to 10
a == ("10") # this is seeing if x is 10. it is a question mark more tha assigning a value



"""Adding and subracting strings and lists"""
#Strings can be added making one string the litterly combines the two
#Strings can be spliced
# List can be added making one list that litterlay combines the two
#list  can be spliced

#this is the print function
print ("Message you are printining")

#this is how you define a variable
    variable = 100

#This is the input function
    var = input ("This is the message the person gets EX: Password")

#Converting the input fraom a string to a float in an equation , this is differnet from the next one becasue it works with decimals
    y = float(String value) * 10

#converting the input from a string to an integer
    InterValue = int(StringValue)

#This is how you add time
    import time #At the begining of your code
    time.sleep(5)# You would put this in your code, 5 is in seconds

#conditinal statements
    if B = 30
        print ("B is greater than 30")#must have an indent, if statements is fale the the code is skipped
    else
        print ("b is equal to or less than 30")# this many or many not happen, This will happen if the if statement is false
# indents can be longer than 1 line

#elif statements
    if c > 10:# only one of the 3 will run
        print("10")
    elif c > 30:# if any of the first 2 run then the code ends
        print ("30")
    else:
        print ("else")#if both the first 2 statemnets are not true then the else runs
    print("done")# if there is no else none will execute

# try exept statement
    variable = ("Vignesh")
    try:
        stringvariable = int(variable)#this will fail as the input is not a integer
    except: #this will run if there is a break ini the code and will nto display an error Message
        stringvariable = 100 # this is the code tha runs if there is a break
        print("Error you have typed in an input that is not a number")
# this will not run if there is not break

# defining your own function
    def NameOfFunction():#you can use this function any where in the code
        print ("Hellow")# this will ony work in this program
        #this will not execute it will only store in the memory
    NameOfFunction()#this is where the function will execute
    print ("Hellow")
    NameOfFunction()# this can be used mutilpe times

#the maxiumum command
    Variable  = max(123456789)#this picks the largest number in the sequence
    print(Variable) #if you use this with letter then the last letter of the alphabets is picked

#the smallest coommand
    Variable = min(123456789)#this picks the smallest number in the sequence

#the type coommand
    type(30)#this will automatically print the type. for example this is an integer

#return coommand
    return "hello" #can be used in stead of the print statement
    # rteurn immediately ends the command and return out of the indent and directly to the next piece of code
    #this command returns the result to  us  not the User
    #example
    big = max("hellow world")
    # this statemnets returns the value of max("hellow worl") and puts it in big instead of printing it

#Looping a code
    n = 10
    while n > 0:# this code  will run till n > 0
        print("n") #this causes the code to repeat 10 times
        n = n - 1 # not changing the variable will cause an infinite loop

#How to force exit a Loop
    while x = 45:
        y = input("Write done to exit:")
        if y ==  ("Done"):
            break# this will automatically exit the whole loop. Will not skip to a specific part of the loop code
        print("Repeating the code")#The will run infinately if you do not input don
    print("Done")

#How to force exit prt of a Loop
    while x = 45:
        y = input("Write done to restart the loop:")#this will make in sot that the code restarts from the while
        if y == ("Done"):
            continue
        print("hi")

# simple Loop
    for i in [5, 4 , 3, 2, 1]:# the code will run i 5 times in the order you typed the number
        print(i)# this will run once for string that you have
    print("Blast off")# it will only exit the loop when all of the number have been executed

# How to find the largest and smallest number
    y = None #
    for i in [1, 2, 3, 4, 4 ,5, 6, 7, 8, 1231313]:
        if i > y:# if this is less than you can find the smallest vaule
            i = y
            print("Greates number so far is",i )
        else:
            print("Greatest number so far is",i)
    print("Greatest number is"i)
    #The Not Functions
        x = True
        if not x: # This flips the bolean value of the variablew
            print("False")
        else:
            print("True")

# Looksing inside strings
    fruit = ("BOB")
    letter = fruit[1] # You can find the specific letter of a strings
    # this will point out the second letter in BOB This is beacuse the charecters go fomr 0 ,1 2,
    # This is know as a chrecter function

=====================================================================
==========================| ACCESING FILES |=========================
=====================================================================

# Turning  string into all lower or upper cause
    greeting = ("Hellow Bob")
    LowerCaseGreeting = greet.lower() # This function makes a lower case version of all the variables
    print(LowerCaseGreeting)
#Output: hellow bob
    greeting = ("Hellow Bob")
    UpperCaseGreeting
# Output: HELLOW BOB

# Finding a charecter in astring
    greeting = ("Hellow Bob")
    x = greeting.find("He")# this fill find and return the position of the Finding

#output: 0
    greeting = ("Hellow Bob")
    x = greeting.find("qwerty")
#output: -1 # This signifies that the thing you were looking for was not found

# Replacing a charecter whithin a variables
    greet = ("Hello Bob")# Replaces all the Bob in the prgram
    newgreet = greet.replace("Bob","Jeff")
    print(newgreet)
#Output: Hello Jeff

# Removing Whitespace in a string
    greet = ("     Hello Bob     ")
    greet = greet.lstrip()
    print(greet) # Output: "Hello Bob     "
    greet = greet.rstrip()# Output: "Hello Bob"
# Note Quotes are used to show the Whitespace

#Finding the prefixes of a string
    line = ("Please Subscibe")
    line.startswith("Please")#Output: true
    line.startswith("Bob")# Output: False

#printing a range of the string from the position
    line = ("Hello")
    y = line.find("e")# finds the lower range
    z = line.find("o")# Finds the higher range
    x = line[y:z] # stores it in a variable
    print(x)

# Calling files
    File = open('python.py','r')# The r is wether you wnat to red it or write it
# if a file does not exsit then you get a trace back

# How to make  an enter in the middle of a strings
    print('Hellow\nWorld')
# Output Hellow
#        World

# Finding the lenth of a strings
    File = 012345678
    len(file)
# Output: 8

# How to open and print every line in a files
# Use words.txt as the file name
    fname = input("Enter file name: ")
    fh = open(fname)
    for lx in fh:
        print(lx)

#Making a list of strings in a variable
    list = ['eggs', 'potato', 'rice', 'bannana'] #the varible be converted from a string to a list

#Building a list
    list = list()
    list = append('Eggs')
    list = append('Banana')
    print(list)
#Output :['book', 99]

#checking what is in a list
    list = [A,B,C,D,E,F,G,H]
    9 in list
#Output: True

#Alphabetically sort Names
    letters = [Z,E,F,G,H,T,W,S,W,D]
    letters.sort()
    print(letters)
#Output: A,B,C,D,E,F

# Organizing Numbers in a lists
    print(len(list))#Number of charecters
    print(max(list))#maxiumum
    print(min(list))#Miniumum
    print(sum(list))#Sum
    print(sum(list)/len(list))# Avarage

# Defining a variable as a lists
    x = list()

# Spliting a string into a list
    Words = Hello World
    listwords = Words.split()# split on defualt by wite space Treates more than one space as the same
    print(listowrds)
#Output = HELLOW

# Changing what siplts split based on
    listwords = words.split(';')

#Constructing a dictinary
    dictinary = dict()
    dictinary['Greeting'] = 'Hello'
    dictinary['Name'] = 'Vignesh'
    dictinary['Last Name'] = 'Saravanakumar'
    print(dictinary)
#Output: 'Greeting: Hello', 'Name: Vignesh', 'Last Name: Saravanakumar'
# The first one inside the brackest is the key, The other one is the value
# You can get a value by inputing  the key
    print(dictinary['Greeting'])
#Output : 'Hello'

#Another way to make an empty dictianry
    dcitinary = {}
#Filled in by
    dictinary = {'Greeting': 1,'Name':'Vignesh','Last Name':'Saravanakumar'}
    print(dictinary)

# searching for a value in a dictinary
    counts = dict()

# Getting the keys of a dictinary
    var.keys()

# Getting the values of a dictinary
    var.values()

#Get function in python
    car = dict()
    car = {
    'Brand':'Ford'
    'Model':'Mustang'
    'Year': 1964
    }
    x = car.get('Model')

#Setting up a fail safe for gets
    x = car.get('Mole',-30)
#the code will print out -30 if there are no is nothing assiciaoted with Mole in the dictinary

#Finding how many times a word repeats in a dictinary
    counts[key] = counts.get(key,0) + 1
    #or
    if key in counts:
        counts[key] = counts[key] + 1
    else:
        counts[key] = 1

# Tuples
# Can be used with both string, integers and none types
# assigned similarly to lists
# Assignmng Tuples
    x = ('Glenn','Sally','Josh')
    print(x[2])
# Output: Josh
# uses prethesis instead of brackets
# Tuples are the same as lists except they are not modifiable
# Tuple does not support item assignmnet
# You can only count and index a Tuple ( Use the dir command on a tuple)

#finding the max of a tuple
    y = (1,2,3,4,5)
    print(max(y))
#Output: 5

# putting a tuple on the right right side
    (x,y) = (4,'Fred')
# x and y will take on the correct values in the Tuple
# This can not be Done

# Comparing Tuples
    (0,1,2) < (5,2,1)
#Output : True
# checks the first number if the first numbers arent the saame then it gives you an answer right there. Becasue the first digit has the gretest value like number.

# Tuples can be sorter by thier first
    d = {'a':10,'b',1:'c', 100}
    sorted(dictinary.items())
    [('a',10),('b',1)()'c',100]

# Looping throught a dictinry in key order
    for k,v in  sorted(d.itmes()):
    print(k,v)

# Looping throught a dictinary in value order
    tmp = list()
    for k,v in dictinary.items():
    tmp.append((v,k))
    tmp = sorted(tmp)
    print(tmp)
    tmp - list()

#to sort backwards
    tmp = sorted(tmp, reverse = True)


# Finding the top
    fhand = open ('mbox-short.txt')
    counts = dict()
    for line  in fhand:
        words = line.split()
        for word  in words:
            counts[word] = counts.get(word,0) + 1
    {
    lst = list()
    for k,v in counts.items():
        newtup = (v,k)
        lst.append(newtup)
    lst = sorted(lst, reverse = True)
    for v,k in lst[:10]:
    print(k,v)}
# Making the lines above in the braces into one line
    print(sorted([(v,k) for k,v in c.items()]))

"""
=====================================================================
========================= ACCESING THE WEB ==========================
=====================================================================
"""

# making the connection to the internet
    import socket # importing sockets
    var = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# A bunch of unexplained giberish
    mysock.connect(('data.pr4e.org',80))# 80 is the port, # The url is the actual host

# Establishing a connection to a website
    import socket
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# A bunch of unexplained giberish
    mysock.connect(('data.pr4e.org',80))# 80 is the port, # The url is the actual host
    cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
    mysock.send(cmd)

    while True:
        data = mysock.recv(512)
        if (len(data) < 1):
            break
        print(data.decode())
    mysock.close()
# Encode converts the datat to a readable foramt for the server
# 80 is the port
    # a port os a connection to a website especially https://www.webstite.com
#decode is the conoversion to the language that [ython understands
# The len is to stop the print from printing infinite blank lines after the data
# you m ust close the connection


# find the value of the number: AScii
print(ord('H'))

# making the import procces simpler
import urllib.request, urllib.parse, urllib.error
var = urllib.request.urlopen('https://data.pr4e.org/romeo.txt')
for line in  var:
    print(line.deode().strip())

# bypassing certifcate erros
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# importing BeautifulSoup
from urllib.request import urlopen
from bs4 import BeautifulSoup

# useing beutiful soup to ingnore erros in forgien code
url = input('Enter - ') # url input
html = urlopen(url, context=ctx).read() # reading the info that comes from the website
soup = BeautifulSoup(html, "html.parser") # beutiful soup parsing the data to ingonre all the unwanted errors

# tags are the <a> part of a html code
tags = soup('a')

# href is the <href> in html code it represents a link the the code
URL = tags[link_line].get("href", None)

 #When talking to another webiste across the internet. you might encounter many
 #differnet launguages, coding launguages and formats of data. to make all of this
 #work ther is a standard way of communicating to other comouters across the internet
 #This is called the wire format or xml.

 #java is organized something like this
 <people>
    <person>
        <name>chuck<name>
        <phone>303 4456</phone>
    <person>
    <person>
        <name>chuck<name>
        <phone>303 4456</phone>
    <person>
<people>
# multiple differnet sub folders insude the folder. These are xml. White spcace does nto matter


# XML Shema. A way to see wich side of the internet blew up. menaing messed up. XML basically takes a document checks it with a moderator

# Interaninal Internet date format
YEAR : MO : DA ,
2020 : 03 : 17

HO : MI : SE
05 : 59 : 59


# Having a multi line string
print(''' Hello \n hello \n Hello''')# The muplti line string prints over 3 lines
# Output: HELLO
#         hello
#         HELLO


# import  Xml tree
import xml.etree.ElementTree as ET

input = '''
<stuff>
  <users>
    <user x="2">
      <id>001</id>
      <name>Chuck</name>
    </user>
    <user x="7">
      <id>009</id>
      <name>Brent</name>
    </user>
  </users>
</stuff>'''
# input usually from the website
stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User count:', len(lst))
# takes the string and makes it into a usable form
for item in lst:
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute', item.get('x'))
# for each of the tags tge ocmputer loops and prints the neatly parsed data


# another example of parsing
import xml.etree.ElementTree as ET

data = '''
<person>
  <name>Chuck</name>
  <phone type="intl">
    +1 734 303 4456
  </phone>
  <email hide="yes" />
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))
# same format of the parser


# Json is basically XML execpt works more with launguages
import json

data = '''
{
  "name" : "Chuck",
  "phone" : {
    "type" : "intl",
    "number" : "+1 734 303 4456"
   },
   "email" : {
     "hide" : "yes"
   }
}'''

info = json.loads(data)
print('Name:', info["name"])
print('Hide:', info["email"]["hide"])
# using json more often that xml is better

# another examplem to iterate throught each once
import json

data = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Brent"
  }
]'''

info = json.loads(data)
print('User count:', len(info))

for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])


# exmple with json

# imports
import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# main loop
while True:
    # entering adress and if ther eis no input then the code breaks
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address # dictinary with one tre,
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)# concatanating the url adding your search key to the urllib this is the reason for a API perameter

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)# opening the url
    data = uh.read().decode() # reading and decoding the data
    print('Retrieved', len(data), 'characters') # showing the number of charcters you reterieved

    try:
        js = json.loads(data) # if there is a sytax error then you get non as js
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    # final data
    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)# coordinates in longitude and lattitude
"""
======================================================================================================
========================================= Using Data Bases============================================
======================================================================================================
"""
class  partyAnimal: # like defining a function
    x = 0
    def party(self): # defining a fucntion
        self.x = self.x + 1 # what the ficntion does
        print('so far' ,self.x)
an = partyAnimal() # define the class partyAnimal as an
an.party() # from the an class the party function is exectued
an.party() # again
an.party() # and again

# another example of class
import time
time.sleep(10) # time is the module , sleep is the fucntion in t he module , the 10 is the parameter

# more exmaple of classes
class PartyAnimal:
   x = 0

   def party(self) :
     self.x = self.x + 1
     print("So far",self.x)

an = PartyAnimal()
print ("Type", type(an))# the type of an
print ("Dir ", dir(an)) # print alll stuff you can do with this  vaiable or instance this will list def party slef
print ("Type", type(an.x))# shows the type
print ("Type", type(an.party))# type of the party insatce bieng applied to an

# more examles
class PartyAnimal:
   x = 0
   name = '' # name is the parameter
   def __init__(self, name): # instance # only defines doesnt run
     self.name = name`
     print(self.name,'constructed')

   def party(self) : # instance # only defines doesnt run
     self.x = self.x + 1 # this runs each timie the party function is called
     print(self.name,'party count',self.x)

s = PartyAnimal('Sally')  # sally is constructed
j = PartyAnimal('Jim') # jim is contructed

s.party() # party function is applied to s
j.party() # party function is appled to j
s.party() # party function is applied to s


# the last exmple of classes
from party  import PartyAnimal
# party is the name of the file
# party animals is the class you are importinig from party


class CricketFan(PartyAnimal): # this means the cricket fan includes alll the functions of party animal plus the functions fo Cricketfam
   points = 0
   def six(self):
      self.points = self.points + 6
      self.party()
      print(self.name,"points",self.points)

s = PartyAnimal("Sally")
s.party()
j = CricketFan("Jim")
j.party()
j.six()
print(dir(j))


# more examples of
class Rectangle:
   def __init__(self, length, breadth, unit_cost=0): # iinstance set up
       self.length = length # defining lenght
       self.breadth = breadth # defining breath
       self.unit_cost = unit_cost # defining unit_cost

   def get_perimeter(self):
       return 2 * (self.length + self.breadth) # a procces that can be executed with x.get_perimeter returns the value

   def get_area(self):
       return self.length * self.breadth # a procces that can be executed with x.get_area returns the value


   def calculate_cost(self): # a procces that can be executed with x.get_calculate_cost returns the value
       area = self.get_area()
       return area * self.unit_cost
# breadth = 120 cm, length = 160 cm, 1 cm^2 = Rs 2000
r = Rectangle(160, 120, 2000) # contructing r with the following pareaeter in __init__
print("Area of Rectangle: %s cm^2" % (r.get_area())) # passing get_area into r
print("Cost of rectangular field: Rs. %s " %(r.calculate_cost())) # passing calculate cost into r
print(r.get_area())






"""
Things to add: 
 - Inheritance
 - 
"""