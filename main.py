from par import *

with open("skills.txt", encoding="utf-8") as file:
    skills = [row.strip() for row in file]

parser = Parser()

def openEdu_analysis():
    c = open('openEDU.txt', 'r')
    for l in c.readlines():
        par = Parser().get_Openedu_program(l)
        for line in par:
            for s in skills:
                if s.lower() in line.lower():
                    print(l, s)


def skillBox_analysis():
    c = open('Skillbox.txt')
    for l in c.readlines():
        par = Parser().get_Skillbox_program(l)
        for line in par:
            for s in skills:
                if s.lower() in line.lower():
                    print(l, s)


# openEdu_analysis()
# skillBox_analysis()

parser.get_Stepik_program('https://stepik.org/course/2223/promo')