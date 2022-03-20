#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 13:53:39 2022

@author: Linda
"""

def strip_punctuation(s):
    punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
    for char in s:
        #print("1st for loop:", char)
        for char in punctuation_chars:
            #print("2nd for loop:", char)
            s = s.replace(char, "")
            #print("after replce:", s)
        #print("back to 2nd for loop:", s)
        return s
    return s

positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
            
def get_pos(string):
    pos = 0
    string = string.lower()
    #print("Lower case:", string)
    string = strip_punctuation(string)
    #print("Stripped:", string)
    words = string.split()
    #print(words)
    for word in words:
        if word in positive_words:
            pos += 1
    return pos

def get_neg(string):
    neg = 0
    string = string.lower()
    #print("Lower case:", string)
    string = strip_punctuation(string)
    #print("Stripped:", string)
    words = string.split()
    #print(words)
    for word in words:
        if word in negative_words:
            neg += 1
    return neg


# read the csv file as text
twit_text = open("project_twitter_data.csv")
lines = twit_text.readlines()

# header is the first line
header = lines[0]
#print("colunmn names:", header)
twit_content = lines[1:]

# start an empty list of twit data
twit_data = []
for twit_lines in twit_content:
    twit_lines = twit_lines.rstrip()
    #print(twit_lines)
    twit_info = twit_lines.split(',')
    #print(twit_info)
    retweet_count = twit_info[1]
    reply_count = twit_info[2]
    n_pos = get_pos(twit_info[0])
    n_neg = get_neg(twit_info[0])
    net = n_pos - n_neg
    # twit_sum is a set of tuples
    twit_sum = (retweet_count, reply_count, n_pos, n_neg, net)
    #print(twit_sum)
    #twit_data is a list of tuples
    twit_data.append(twit_sum)

print(twit_data)

# write the data into a csv file

outfile = open("resulting_data.csv", "w")
# output the header row
outfile.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')
outfile.write('\n')

for item in twit_data:
    #print(item)
    for info in item:
        info = '{},{},{},{},{}'.format(item[0], item[1], item[2], item[3], item[4])
    print(info)
    outfile.write(info)
    outfile.write('\n')
