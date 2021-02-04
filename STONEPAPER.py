#importing the random module
import random
#X is a global list consisting real inputs game wants
x = ["Stone","Paper","Scissor"]
#Defining the class 
class game():
    #Some Instructions.........
    print("\t\t\t\tStone Paper Scissor")
    print("\t\t\t************************************")
    print("\nHey Gamer!WELCOME")
    print("")
    print("\nINSTRUCTIONS:You have to input Stone/Paper/Scissor\nYou have to use the first letter large case and following small cases for your choice.\neg:Stone")
    print("\nPRESS ENTER")
    input()
    #Defining init function
    def __init__(self):
         #Ask name of gamer
         name = input("Your name: ")
         #making it as classe's value
         self.name = name
         print("\n%s,Have fun with machine!!!!!!"%(name))
         print("PRESS ENTER")
         input()
         #Ask number of choice gamer wants to make
         n = input("Number of choices you want to make[5-10 for nice game]: ")
         #setting a flag
         z = 0
         #this loop for checking wether n is a number(int) or not
         while(z==0):
             try:
                 int(n)
                 z = 2
             except:
                 z = 1
         #if n is not a number,giving warning and ask again for n
         while(z==1):
             print("INVALID!ENTER A NUMBER")
             n = input("Number of choices you want to make[5-10 for nice game]: ")
             try:
                 int(n)
                 z = 0
             except:
                 z = 1
         #making n the  classe's value
         self.n = n
         #initiating score values
         self.comp= 0
         self.user = 0
         #calling  defined functions
         self.iterate()
         self.compare()
         #Display END at the last
         print("\n************************************GAME END************************************************")
    #defining iterate function
    def iterate(self):
        #setting the number of choices the gamer wants to do
        for i in range(int(self.n)):
            self.usr_input()
            self.com_reply()
    #defining usr_iput function
    def usr_input(self):
        #ask user for input[Stone/Paper/Scissor]
        user_input = input("\nYour choice: ")
        #checking user did give any other input
        while(user_input not in x):
            print("\nYou have to input Stone/Paper/Scissor")
            print("INSTRUCTIONS:You have to use the first letter large case and following small cases for your choice.\neg:Stone")
            user_input = input("\nYour choice: ")
        self.user_input = user_input
    #defining computer reply function
    def com_reply(self):
        #making random selection from the inputs
        a = random.choice(x)
        #making it classes's value
        self.a = a
        #display the random choice computer made
        print("Machine choice:",a)
        #Game conditions for assigning scores
        if self.a=="Stone" and self.user_input=="Paper":
            self.user+=1
        elif self.a=="Paper" and self.user_input=="Stone":
            self.comp+=1
        elif a=="Stone" and self.user_input=="Scissor":
            self.comp+=1
        elif self.a=="Scissor" and self.user_input=="Stone":
            self.user+=1
        elif self.a=="Scissor" and self.user_input=="Paper":
            self.comp+=1
        elif self.a=="Paper" and self.user_input=="Scissor":
            self.user+=1
        #Display gamer's and machine's score
        print("[+]%s's Score:%d"%(self.name,self.user))
        print("[+]Machine's Score:%d"%(self.comp))
    #defining compare function
    def compare(self):
        #Analyzing the scores and announcing the winner or tie.
        if self.user>self.comp:
            print("\nCongratulations %s,You are rocking!!!!!!!!!!!!!!!!!!!!!!!!!!!"%(self.name))
        elif self.user==self.comp:
            print("\nA TIE!!!!!!!!!!!!!!!!!")
        elif self.comp>self.user:
            print("\n%s,you are beaten by Machine,BETTER LUCK NEXT TIME"%(self.name))
#storing class game in a variable and execution
q = game()














#start
#score initialize
#user ipnut (stone,paper,csr)
#random from computer
#compare all cases and assign mark
#5 choices
#announce winner
#stop
#class
