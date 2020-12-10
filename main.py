from par import *

skills = []
c = open('courses.txt', 'r')

with open("skills.txt", encoding="utf-8") as file:
    skills = [row.strip() for row in file]

for l in c.readlines():
    par = Parser.get_program(l)
    for s in skills:
        if par.find(s) != -1:
            print(l, s)
