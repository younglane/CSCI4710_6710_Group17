import sqlite3

from flask import Flask, render_template
from csv import reader

import util

app = Flask(__name__)

db = sqlite3.connect('hw5.db')

db.execute('''DROP TABLE MODEL''')


db.execute('''CREATE TABLE MODEL(
                              [index] Integer PRIMARY KEY,
                              [What country do you live in?] text,
                              [How old are you?] Integer,
                              [What is your gender?] text,
                              [To what extent do you feel FEAR due to the coronavirus?] text,
                              [To what extent do you feel ANXIOUS due to the coronavirus?] text,
                              [To what extent do you feel ANGRY due to the coronavirus?] text,
                              [To what extent do you feel HAPPY due to the coronavirus?] text,
                              [To what extent do you feel SAD due to the coronavirus?] text,
                              [Which emotion is having the biggest impact on you?] text, 
                              [What makes you feel that way?] text,
                              [What brings you the most meaning during the coronavirus outbreak?] text,
                              [What is your occupation?] text)''')

with open('t.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    next(csv_reader)
    for row in csv_reader:
        item = row[0]
        item2 = row[1]
        item3 = row[2]
        item4 = row[3]
        item5 = row[4]
        item6 = row[5]
        item7 = row[6]
        item8 = row[7]
        item9 = row[8].decode('utf-8')
        item10 = row[9].decode('utf-8')
        item11 = row[10].decode('utf-8')
        item12 = row[11].decode('utf-8')
        item13 = row[12].decode('utf-8')
        db.execute('''INSERT INTO MODEL('index', 'What country do you live in?', 'How old are you?', 'What is your gender?', 'To what extent do you feel FEAR due to the coronavirus?', 'To what extent do you feel ANXIOUS due to the coronavirus?', 'To what extent do you feel ANGRY due to the coronavirus?', 'To what extent do you feel HAPPY due to the coronavirus?', 'To what extent do you feel SAD due to the coronavirus?', 'Which emotion is having the biggest impact on you?', 'What makes you feel that way?', 'What brings you the most meaning during the coronavirus outbreak?', 'What is your occupation?')
                    VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                   (item, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13))
        db.commit()


databaseList = list()


def storedatabase(db):
    cursorDB = db.cursor()
    cursorDB.execute('''SELECT * FROM MODEL''')
    rows = cursorDB.fetchall()

    for row in rows:
        databaseList.append(row)


step1group1List = list()


def step1group1(db):
    cursor1 = db.cursor()
    cursor1.execute('''SELECT * FROM MODEL WHERE "What is your gender?" LIKE 'Male' AND "How old are you?" <= 35''')
    rows = cursor1.fetchall()

    for row in rows:
        step1group1List.append(row)


step1group2List = list()


def step1group2(db):
    cursor1 = db.cursor()
    cursor1.execute('''SELECT * FROM MODEL WHERE "What is your gender?" LIKE 'Male' AND "How old are you?" >= 36''')
    rows = cursor1.fetchall()

    for row in rows:
        step1group2List.append(row)


def step1group3(db):
    cursor1 = db.cursor()
    cursor1.execute('''SELECT * FROM MODEL WHERE "What is your gender?" LIKE 'Female' AND "How old are you?" <= 35''')
    rows = cursor1.fetchall()

    for row in rows:
        print(row)


def step1group4(db):
    cursor1 = db.cursor()
    cursor1.execute('''SELECT * FROM MODEL WHERE "What is your gender?" LIKE 'Female' AND "How old are you?" >= 36''')
    rows = cursor1.fetchall()

    for row in rows:
        print(row)


countryList = ["USA", "Switzerland", "Romania", "UK", "Hong Kong", "Columbia", "Canada", "Australia", "France",
               "Germany", "Cyprus", "Rwanda", "Israel", "Portugal", "Ireland", "New Zealand", "China", "Palestine",
               "Spain"]
listOfList = list()
listOfList2 = list()
listOfList3 = list()
listOfList4 = list()


def step2group1(db):
    cursor1 = db.cursor()
    cursor1.execute('''SELECT * FROM MODEL WHERE "What is your gender?" LIKE 'Male' AND "How old are you?" <= 35''')
    rows = cursor1.fetchall()

    for country in countryList:

        print(country + " Table")
        emptyList = list()
        for row in rows:
            if row[1] in country:
                emptyList.append(row)

        for x in emptyList:
            print(x)

        print()

        listOfList.append(emptyList)


def step2group2(db):
    cursor1 = db.cursor()
    cursor1.execute('''SELECT * FROM MODEL WHERE "What is your gender?" LIKE 'Male' AND "How old are you?" >= 36''')
    rows = cursor1.fetchall()

    for country in countryList:

        print(country + " Table")
        emptyList = list()
        for row in rows:
            if row[1] in country:
                emptyList.append(row)

        for x in emptyList:
            print(x)

        print()

        listOfList2.append(emptyList)


def step2group3(db):
    cursor1 = db.cursor()
    cursor1.execute('''SELECT * FROM MODEL WHERE "What is your gender?" LIKE 'Female' AND "How old are you?" <= 35''')
    rows = cursor1.fetchall()

    for country in countryList:

        print(country + " Table")
        emptyList = list()
        for row in rows:
            if row[1] in country:
                emptyList.append(row)

        for x in emptyList:
            print(x)

        print()

        listOfList3.append(emptyList)


def step2group4(db):
    cursor1 = db.cursor()
    cursor1.execute('''SELECT * FROM MODEL WHERE "What is your gender?" LIKE 'Female' AND "How old are you?" >= 36''')
    rows = cursor1.fetchall()

    for country in countryList:

        print(country + " Table")
        emptyList = list()
        for row in rows:
            if row[1] in country:
                emptyList.append(row)

        for x in emptyList:
            print(x)

        print()

        listOfList4.append(emptyList)


anotherList = list()


def step3group1():
    for list1 in listOfList:
        if len(list1) > 10:
            labels = util.cluster_user_data(list1)
            print("Predicted Labels Are: ", labels)

            split_result = util.split_user_data(list1, labels)
            print("Split original user data to: ")
            print(split_result)
            print("Split_result length is: ", len(split_result))


def step3group2():
    for list2 in listOfList2:
        if len(list2) > 10:
            labels = util.cluster_user_data(list2)
            print("Predicted Labels Are: ", labels)

            split_result = util.split_user_data(list2, labels)
            print("Split original user data to: ")
            print(split_result)
            print("Split_result length is: ", len(split_result))


def step3group3():
    for list3 in listOfList3:
        if len(list3) > 10:
            labels = util.cluster_user_data(list3)
            print("Predicted Labels Are: ", labels)

            split_result = util.split_user_data(list3, labels)
            print("Split original user data to: ")
            print(split_result)
            print("Split_result length is: ", len(split_result))


def step3group4():
    for list4 in listOfList4:
        if len(list4) > 10:
            labels = util.cluster_user_data(list4)
            print("Predicted Labels Are: ", labels)

            split_result = util.split_user_data(list4, labels)
            print("Split original user data to: ")
            print(split_result)
            print("Split_result length is: ", len(split_result))


# the data should be obtained from your db

storedatabase(db)
step1group1(db)
step1group2(db)
step3group4()
step3group3()
step3group2()
print(listOfList3)
