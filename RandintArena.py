"""
Randint Arena
Author: Kevin Friedrich
Last Edited: 10/25/19
"""

#imports
import random

#Stats
playerH=100
playerMHP=100
playerA=10
gold=10
goldGain=1.0
count=0
gameOver="n"
mHealth=0
mDamage=0
mGold=0

#Functions
#_________________________

#Monsters
def monFrog():
    global mName
    mName="Frog"
    global mHealth
    mHealth=20
    global mDamage
    mDamage=5
    global mGold
    mGold=10
    
def monChicken():
    global mName
    mName="Chicken"
    global mHealth
    mHealth=20
    global mDamage
    mDamage=7
    global mGold
    mGold=14
    
def monGoblin():
    global mName
    mName="Goblin"
    global mHealth
    mHealth=30
    global mDamage
    mDamage=10
    global mGold
    mGold=18
    
def monSkeleton():
    global mName
    mName="Skeleton"
    global mHealth
    mHealth=35
    global mDamage
    mDamage=12
    global mGold
    mGold=22
    
def monBarbarian():
    global mName
    mName="Barbarian"
    global mHealth
    mHealth=38
    global mDamage
    mDamage=14
    global mGold
    mGold=26
    
def monAlien():
    global mName
    mName="Alien"
    global mHealth
    mHealth=40
    global mDamage
    mDamage=16
    global mGold
    mGold=28

def monGrimReaper():
    global mName
    mName="Grim Reaper"
    global mHealth
    mHealth=50
    global mDamage
    mDamage=20
    global mGold
    mGold=40

#Weapons
def wepStick():
    global wepName
    wepName="Stick"
    global mDamage
    mDamage=mDamage*1.1

def wepSpork():
    global wepName
    wepName="Spork"
    global mDamage
    mDamage=mDamage*1.15

def wepBelt():
    global wepName
    wepName="Belt"
    global mDamage
    mDamage=mDamage*1.2

def wepFisti():
    global wepName
    wepName="Fisticuff"
    global mDamage
    mDamage=mDamage*1.25

def wepClippers():
    global wepName
    wepName="Hedge Clippers"
    global mDamage
    mDamage=mDamage*1.3

def wepSword():
    global wepName
    wepName="Sword"
    global mDamage
    mDamage=mDamage*1.35

def wepScythe():
    global wepName
    wepName="Scythe"
    global mDamage
    mDamage=mDamage*1.4

def wepGun():
    global wepName
    wepName="Gun"
    global mDamage
    mDamage=mDamage*1.45

def wepChancla():
    global wepName
    wepName="Chancla"
    global mDamage
    mDamage=mDamage*1.5



#Introduction
print("Welcome to the Randint Arena!")
name = input("Please enter your name: ")
print("Hi", name,"! You will be thrown into an arena to fight a variety of different, randomly generates monsters. Each monster has different stats and comes equiped with a randomly generated weapon.")
print("You have", playerH,"hp and start with", playerA, "attack. You also start with", gold,"gold.")
print("")
while True:
    answer=input("Hit enter if you are ready to fight!")
    if answer=="":
        break

#Main Loop   
while True:

#Random Monster
    ranMonster = random.randint(1,7)
    if ranMonster==1:
        monFrog()
        
    if ranMonster==2:
        monChicken()
        
    if ranMonster==3:
        monGoblin()
        
    if ranMonster==4:
        monSkeleton()
        
    if ranMonster==5:
        monBarbarian()
        
    if ranMonster==6:
        monAlien()
        
    if ranMonster==7:
        monGrimReaper()


#Random Weapon
    ranWeapon = random.randint(1,9)

    if ranWeapon==1:
        wepStick()
        
    if ranWeapon==2:
        wepSpork()
        
    if ranWeapon==3:
        wepBelt()
        
    if ranWeapon==4:
        wepFisti()
        
    if ranWeapon==5:
        wepClippers()
        
    if ranWeapon==6:
        wepSword()
        
    if ranWeapon==7:
        wepScythe()
        
    if ranWeapon==8:
        wepGun()
        
    if ranWeapon==9:
        wepChancla()

    #Player Choice
    print("")
    print("You encounter a", mName, "weilding a", wepName,"!")
    while True:
        while True:
            print("")
            print("You have",round(playerH,0),"Health.")
            print("The",mName,"has",round(mHealth,0),"Health.")
            pChoice = input("Type A to Attack or W to run: ")
            if pChoice=="A" or pChoice=="W":
                break

        
        #Chance to Flee
        if pChoice=="W":
            chToRun = random.randint(1,2)
            if chToRun==1:
                print("You got away!")
                break
            if chToRun==2:
                print("You failed to get away!")
                print("")
                print("The", mName,"attacks and does",round(mDamage,1),"!")
                playerH-=mDamage
                if playerH<=0:
                    break


        #Fight
        if pChoice=="A":
            print("")
            print("You attack the", mName,"and deal", playerA,"damage!")
            mHealth-=playerA
            if mHealth<=0:
                print("You have defeated the", mName,"!")
                print("You have recieved",round(mGold*goldGain,0),"gold!")
                gold= gold +(mGold*goldGain)
                while True:
                    enter = input("Hit enter to continue.")
                    if enter=="":
                        break
                break
            print("The", mName,"attacks and does",round(mDamage,1),"!")
            playerH-=mDamage
            if playerH<=0:
                break
    #Death
    if playerH<=0:
        print("You have perished. Restart to try again!")
        break
    
    #Shop
    print("")
    print("Welcome to the shop",name,".")
    print("")

    while True:
        print("")
        print("Gold Balance:",gold)
        print("")
        shopChoice= input("Type H for a Health pot(restores health), S for a sharpening stone(increases attack), HS for a health Scroll(increases Maximum Health), or C for a Clover(increased gold gain). Press Enter to exit the shop.")
        print("")

        if shopChoice=="H":
            if gold >=5:
                playerH+=20
                if playerH > playerMHP:
                    playerH=playerMHP
                    print("Your HP is now full.")
                gold-=5
                print("Your hp is now at", round(playerH,0),".")
            else:
                print("You do not have enough gold.")
        if shopChoice=="S":
            if gold >= 10:
                playerA+=1
                gold-=10
                print("Your attack is now at",playerA,".")
            else:
                print("You don't have enough gold.")
                
        if shopChoice=="HS":
            if gold>=15:
                playerMHP+=10
                gold-=15
                print("You now have a max HP of",playerMHP)
            else:
                print("You don't have enough gold.")

        if shopChoice=="C":
            if gold>=20:
                goldGain+=0.5
                gold-=20
                print("You have increased gold gain.")
            else:
                print("You don't have enough gold.")



        if shopChoice=="":
            break

    
    count+=1

    if count%5==0:
        gameOver= input("Would you like to exit the game? y/n: ")
    if gameOver=="y":
        print("Thank you for playing!")
        break
    
