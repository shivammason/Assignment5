#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Card
#referred from Ramyas program

import random

class card:

def __init__(self, suit, value):

self.suit = suit

self.value = value

class deckOfCards:

deck = []

def __init__(self):

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

for s in suits:

for v in values:

self.deck.append(card(s, v))

def shuffle(self):

self.deck = random.sample(self.deck, len(self.deck))

def deal(self):

p1 = self.deck.pop(0)

p2 = self.deck.pop(0)

return p1, p2

def print_deck(doc):

for card in doc.deck: print(f'{card.value} {card.suit}')

num_values = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
'8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13}

while(True):

input('Press any key to start...')

doc = deckOfCards()

doc.shuffle()

count_player = 0

count_opp = 0

while(len(doc.deck) > 0):

p1, p2 = doc.deal()

print(f'Your card: {p1.value} {p1.suit} \tOpponent\'s card: {p2.value} {p2.suit}')

if num_values[p1.value] == num_values[p2.value]:

print('WAR')

elif num_values[p1.value] > num_values[p2.value]:

print('You win the hand!')

count_player += 1

else:

print('You lose the hand')

count_opp += 1

if(count_player > count_opp):

print(f'\nYOU WIN: {count_player} x {count_opp}')

elif(count_player < count_opp):

print(f'\nYOU LOSE: {count_player} x {count_opp}')

else:

print(f'\nWAR: {count_player}')

inValue = input('\nPress any key to continue or \'q\' to quit')

if inValue == 'q': break


# In[ ]:


#XML

import xml.etree.ElementTree as ET

fname = input("Enter file name: ")
try:
    tree = ET.parse(fname)
except:
    print(f'File cannot be opened: {fname}')
    exit()

root = tree.getroot()
print(f'Total Events: {len(root)}\n')

count = 0

#Count wil be used to print the first 61 lines returned from 'findall', which corresponds to all different
# columns defined for each event
print('Entry data Attributes:')
for event in root.findall("./viewentry/entrydata"): #/*[@name='EventName']/text"):
    if count == 61: break
    print(event.attrib)
    count += 1

print('\n\n')
count = 0

#Code to print first 5 objects.
#We choose to print columns: Name, Area, Categories, Date Begin Show and Admission
for event in root.findall(".viewentry"):
    if count == 5: break
    print(f'Event {count + 1}')
    print('Name: '+ event.find(".//*[@name='EventName']/text").text)
    print('Area: ' + event.find(".//*[@name='Area']/text").text)
    print('Categories: ' + ', '.join(cat.text for cat in event.findall(".//*[@name='CategoryList']//textlist//text")))
    print('Date Begin Show: ' + event.find(".//*[@name='DateBeginShow']/text").text)
    print('Admission: ' + event.find(".//*[@name='Admission']/text").text  + '\n')
    count += 1


#JSON
# referred from Nuthan's program

import json

import re

def dict_keys(data,father, level):

result = []

for key in data.keys():

if type(data[key]) != dict and type(data[key]) != list:

result.append('\t'*level + key + '\n')

else:

if type(data[key]) == dict:

result.append('\t'*level + key + ':\n' + '\t'*(level) + '{\n')

level += 1

result += dict_keys(data[key], key, level)

level -= 1

else: #keys with list

if len(data[key]) == 0:

result.append('\t'*level + key + '\n')

else:

result.append('\t'*level + key + ':\n' + '\t'*(level) + '{\n')

level += 1

for i in range(len(data[key])):

result += dict_keys(data[key][i], key, level)

level -= 1

if level != 0:

result.append('\t'*(level-1) + '}\n')

return result

fname = input('Enter file name: ')

try:

file_data = open(fname, encoding='utf8')

except:

print(f'File cannot be opened: {fname}')

exit()

events = json.load(file_data)

print(f'Total Events: {len(events)}\n')

print('Data structure:')

print (''.join(key for key in dict_keys(events[0],'', 0)))

print('\n')

print('Last 5 events:')

for event in events[:len(events)-6:-1]:

print(f"Name: {event['calEvent']['eventName']}")

print(f"Location: {event['calEvent']['locations'][0]['locationName']}")

print(f"Categories: {event['calEvent']['categoryString']}")

print("Start date: ", re.findall('\d\d\d\d-\d\d-\d\d', event['calEvent']['startDate'])[0])

print(f"Free: {event['calEvent']['freeEvent']}\n")


# In[ ]:


#group Database

import sqlite3

try:

conn = sqlite3.connect('testdata.db')

conn.execute("PRAGMA foreign_keys = ON")

except Error as e:

print(e)

exit()

cur = conn.cursor()

cur.execute('DROP TABLE IF COURSE EXISTS)

cur.execute('CREATE TABLE COURSE(
course_id integer PRIMARY KEY,
course_name text NOT NULL)')

cur.execute('DROP TABLE IF STUDENT EXISTS)

cur.execute('CREATE TABLE STUDENT(
student_id integer PRIMARY KEY,
Student_name text NOT NULL,
course1 integer,
course2 integer,
course3 integer,
course4 integer,
course5 integer,
course6 integer,
FOREIGN KEY (course1)
REFERENCES course(course_id) ON DELETE SET NULL ON UPDATE CASCADE
FOREIGN KEY (course2)
REFERENCES course(course_id) ON DELETE SET NULL ON UPDATE CASCADE
FOREIGN KEY (course3)
REFERENCES course(course_id) ON DELETE SET NULL ON UPDATE CASCADE
FOREIGN KEY (course4)
REFERENCES course(course_id) ON DELETE SET NULL ON UPDATE CASCADE
FOREIGN KEY (course5)
REFERENCES courses(course_id) ON DELETE SET NULL ON UPDATE CASCADE
FOREIGN KEY (course6)
REFERENCES course(course_id) ON DELETE SET NULL ON UPDATE CASCADE)')

cur.execute('INSERT INTO courses (course_id, course_name) VALUES(?, ?)', (1, 'Data Programming'))

cur.execute('INSERT INTO courses (course_id, course_name) VALUES(?, ?)', (2, 'Data Manipulation Techniques'))

cur.execute('INSERT INTO courses (course_id, course_name) VALUES(?, ?)', (3, 'Data Systems Architecture'))

cur.execute('INSERT INTO courses (course_id, course_name) VALUES(?, ?)', (4, 'Business Process'))

cur.execute('INSERT INTO courses (course_id, course_nam) VALUES(?, ?)', (5, 'Math for Data Analytics'))

cur.execute('INSERT INTO courses (course_id, course_name) VALUES(?, ?)', (6, 'Information Encoding Standards'))

cur.execute('INSERT INTO student (student_id, student_name, course1, course2)
VALUES (?, ?, ?, ?)', (1, 'Shivam', 1, 2))

cur.execute('INSERT INTO student (student_id, student_name, course_id, course2)
VALUES (?, ?, ?, ?)', (2, 'Yogesh', 3, 4))

cur.execute('INSERT INTO student (student_id, student_name, course_id)
VALUES (?, ?, ?)', (3, 'Chitresh', 5))

conn.commit()

cur.execute('SELECT course.name, student.student_id, student.student_name
FROM student
INNER JOIN course on course.course_id = student.course1 OR
course.course_id = student.course2 OR
course.course_id = student.course3 OR
course.course_id = student.course4 OR
course.course_id = student.course5 OR
course.course_id = student.course6
ORDER BY course.course_name')

rows = cur.fetchall()

cur.close()

for row in rows:

print(row)

