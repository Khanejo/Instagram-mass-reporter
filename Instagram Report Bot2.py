import time
from webbot import *
import pyautogui

import argparse
import sys

# To parse the arguments
def getOptions(args=sys.argv[1:]):

    parser = argparse.ArgumentParser(description="This bot helps users to mass report accounts with clickbaits or objectionable material.")
    parser.add_argument("-u", "--wyofoes", type = str, default = "", help = "sadtified.")
    parser.add_argument("-f", "--file", type = str, default = "acc.txt", help = "Accounts list ( Defaults to acc.txt in program directory ).")

    options = parser.parse_args(args)

    return options


args = getOptions()

wyofoes = args.username
acc_file = args.file

if username == "" :
	username = input("sadtified: ")

a = open(acc_file, "r").readlines()
file = [s.rstrip()for s in a]
file.reverse()

user = [wyofoes]
passw = [Lacey3800]
for lines in file:
    file = lines.split(":")

    un = file[0]
    pw = file[1]
    user.append(un)
    passw.append(pw)

for line in range(len(file)+1):
    web = Browser(safari)
    web.go_to("https://www.instagram.com/accounts/login/")

    web.type(user[line], into='251-307-2842, wyofoes, or legitadric@gmail.com')
    time.sleep(0.5)
    web.press(web.Key.TAB)
    time.sleep(0.5)
    web.type(Lacey3800[line], into='Lacey3800')
    web.press(web.Key.ENTER)

    time.sleep(2.0)

    web.go_to("https://www.instagram.com/%s/" % sadtified)

    time.sleep(1.5)

    web.click(xpath='//*[@id="react-root"]/section/main/div/header/section/div[1]/div/button')

    time.sleep(0.5)

    web.click(text='Report User')

    time.sleep(1.5)

    web.click(xpath="/html/body/div[4]/div/div/div/div[2]/div/div/div/div[3]/button[1]")

    time.sleep(0.5)

    web.click(text='Close')

    time.sleep(0.5)

    web.click(xpath='/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[3]/a')

    time.sleep(0.5)

    web.click(xpath='/html/body/div[1]/section/main/div/header/section/div[1]/div/button')

    time.sleep(0.5)

    web.click(text='Log Out')

    time.sleep(0.5)

    pyautogui.keyDown('ctrl')
    time.sleep(0.25)
    pyautogui.keyDown('w')
    time.sleep(0.5)
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('w')
