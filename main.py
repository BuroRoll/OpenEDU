from par import *
import re

with open("skills.txt", encoding="utf-8") as file:
    skills = [row.strip() for row in file]

parser = Parser()


def openEdu_analysis():
    print('OpenEDU')
    res = {}
    c = open('openEDU.txt', 'r')
    for l in c.readlines():
        par = Parser().get_Openedu_program(l).split(' ')
        for line in par:
            for s in skills:
                if s.lower() in line:
                    if l in res:
                        if s not in res.get(l):
                            res.get(l).append(s)
                    else:
                        res[l] = [s]
    print(res)


def skillBox_analysis():
    print('SkillBox')
    res = {}
    c = open('Skillbox.txt')
    for l in c.readlines():
        par = Parser().get_Skillbox_program(l)
        for line in par:
            for s in skills:
                if re.findall(s.lower(), line):
                    if l in res:
                        if s not in res.get(l):
                            res.get(l).append(s)
                    else:
                        res[l] = [s]
    print(res)


def stepik_analysis():
    print('Stepik')
    c = open('stepik.txt')
    for l in c.readlines():
        par = parser.get_Stepik_program(l)
        for line in par:
            for s in skills:
                if s.lower() in line:
                    print(l, s)

def coursera_analysis():
    print('Coursera')
    res = {}
    c = open('coursera.txt')
    for l in c.readlines():
        par = parser.get_coursera_program(l)
        for line in par:
            for s in skills:
                if re.findall(s.lower(), line):
                    if l in res:
                        if s not in res.get(l):
                            res.get(l).append(s)
                    else:
                        res[l] = [s]
    print(res)

def beonmax_analysis():
    print("BeonMax")
    res = {}
    res2 = []
    c = open('beonmax.txt')
    for l in c.readlines():
        par = parser.get_beonmax_program(l)
        for line in par:
            for s in skills:
                if re.findall(s.lower(), line):
                    if l in res:
                        if s not in res.get(l):
                            res.get(l).append(s)
                    else:
                        res[l] = [s]
    print(res)

def main():
    openEdu_analysis()
    skillBox_analysis()
    # stepik_analysis() ????
    coursera_analysis()
    beonmax_analysis()


if __name__ == '__main__':
    main()
