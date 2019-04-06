# Program Assignment:  Team           
# Name: A01378565
# ID: A01378565
# Date: April 6, 2019.
# Description: One day three best friends Petya, Vasya and Tonya decided to form a team and take part in programming contests. 
# Participants are usually offered several problems during programming contests. 
# Long before the start the friends decided that they will implement a problem if at least two of them are sure about the solution. 
# Otherwise, the friends won't write the problem's solution.

def computeProblem(numberOfProblems):
    a = []
    b = []
    counter = 0
    counterProblem = 0
    for i in range(numberOfProblems):
        number = input("").split(" ")
        for j in range(len(number)):
            b.append(int(number[j]))        
        a.append(b)
        b = []

    for k in range(numberOfProblems):
        for l in range(3):            
            if(a[k][l] == 1):
                counter += 1
                
        if(counter >= 2):
            counter = 0
            counterProblem += 1
        else:
            counter = 0
    print(counterProblem)



def main():
    n = int(input())
    computeProblem(n)
main()