# Program Assignment:  ChatRoom           
# Name: Fabián Camp Mussa.
# ID: A01378565
# Date: April 6, 2019.
# Description: Vasya has recently learned to type and log on to the Internet. 
# He immediately entered a chat room and decided to say hello to everybody. 
# Vasya typed the word s. It is considered that Vasya managed to say hello 
# if several letters can be deleted from the typed word so that it resulted in the word "hello". 
# For example, if Vasya types the word "ahhellllloou", it will be considered that he said hello, and 
# if he types "hlelo", it will be considered that Vasya got misunderstood and he didn't manage to say hello. 
# Determine whether Vasya managed to say hello by the given word s.

def computeProblem(stringA):
    string = "hello"
    a = ""
    count = 0

    for i in range(len(string)):
        for j in range(len(stringA)):
            if(ord(stringA[j]) == ord(string[i])):
                

    
            
            
        

def main():
    a = input("")
    computeProblem(a)
main()