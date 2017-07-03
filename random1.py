import random
import time
print "hey! let's play rock paper scissors!"
options = ["rock", "paper", "scissors"]
i=0
while i<5:
    cominput = random.choice(options)
    myinput = raw_input("rock, paper, scissors,\n")
    if myinput=="scissors" and cominput=="rock":
        print "SHOOT! ...HA! I did rock! I win!!!"
        time.sleep(3)
        print "let's play again!"
        time.sleep(3)
    elif myinput=="rock" and cominput=="paper":
        print "SHOOT! ...HA! I did paper! I win!!!"
        time.sleep(3)
        print "let's play again!"
        time.sleep(3)
    elif myinput=="paper" and cominput=="scissors":
        print "SHOOT! ...HA! I did scissors! I win!!!"
        time.sleep(3)
        print "let's play again!"
        time.sleep(3)
    elif myinput=="paper" and cominput=="rock":
        print "SHOOT!...DANG! I did rock. You win."
        time.sleep(3)
        print "let's play again!"
        time.sleep(3)
    elif myinput=="scissors" and cominput=="paper":
        print "SHOOT!...DANG! I did paper. You win."
        time.sleep(3)
        print "let's play again!"
        time.sleep(3)
    elif myinput=="rock" and cominput=="scissors":
        print "SHOOT!...DANG! I did scissors. You win."
        time.sleep(3)
        print "let's play again!"
        time.sleep(3)
    elif myinput=="rock" and cominput=="rock":
        print "SHOOT!...Welp, we did the same thing."
        time.sleep(3)
        print "let's play again!"
        time.sleep(3)
    elif myinput=="scissors" and cominput=="scissors":
        print "SHOOT!...Welp, we did the same thing."
        time.sleep(3)
        print "let's play again!"
        time.sleep(3)
    elif myinput=="paper" and cominput=="paper":
        print "SHOOT!...Welp, we did the same thing."
        time.sleep(3)
        print "let's play again!"
        time.sleep(3)
    i = i + 1
print "Actually, you know what, that's it. i'm done."
