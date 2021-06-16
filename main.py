from tkinter import *
import random

global question_answer
names_list = []
asked = []
score = 0 

question_answer = {
    1: [
        "What is Mental Health",
        'Mental Health is about my physical health',
        'Some game', 'Something to do with food',
        'A important issue in todays world', 'A fruit',
        'A Sport', 1
    ],
    2: [
        "How does Mental Health affect you?",
        'How you handle stress',
        'How you act',
        'How you feel',
        'Relating to others', 'all of them',
        'all of them', 5
    ],
    3: [
        "Which country has the most Mental Health problems?", 'Brazil', 'China',
        'United States of America', 'Germany', 'Russia', 'China', 2
    ],
    4: [
        "Which country creates the least pollution?", 'New Zealand', 'Finland',
        'France', 'Sweden', 'Australia', 'Sweden', 4
    ],
    5: [
        "How do you look after your Mental Health?", 'Staying Active',
        'Keep in touch',
        'Ask for help',
        'Doing things that make you happy', 'Stay in contact with friends and socialise with them',
        'Sit alone and do not tell anyone',
        3
    ],
    6: [
        "Which one of these causes the most Mental health problems in todays society?",
        'Being Bullied online', 
        'Being bullied at work or school', 
        'Dealing with health problems alone',
        'Family Arguments', 'Stressful life situations', 'Financial Problems', 4
    ],
    7: [
        "How many people seek public help everyday due to bullying caused by Cyber bullying",
        '5,000 people', 
        '20,000 people', 
        '100,000 people', 
        '1,000,000 people',
        '2,500 people', 
        '5,000 people', 
        1],
    8:[
        "unknown", 'hello1', 'hello2', 'hello3', 'hello4', 'hello5', 'hello1', 1],
    9:[
        "unknown", 'hello1', 'hello2', 'hello3', 'hello4', 'hello5', 'hello1', 1],
    10:[
        "unknown", 
     'hello1', 'hello2', 'hello3', 'hello4', 'hello5', 'hello1', 1]
}