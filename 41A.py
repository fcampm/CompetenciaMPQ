# Program Assignment:  41A  
# Program Name: Translation            
# Name: Fabián Camp Mussa
# ID: A01378565.
# Date: April 6, 2019.
# Description: The translation from the Berland language into the Birland language is not an easy task. 
# Those languages are very similar: a berlandish word differs from a 
# birlandish word with the same meaning a little: it is spelled (and pronounced) reversely. 
# For example, a Berlandish word code corresponds to a Birlandish word edoc. 
# However, it's easy to make a mistake during 
# the «translation». Vasya translated word s from Berlandish into Birlandish as t. Help him: find out if he translated the word correctly.

def computeProblem(stringA, stringB):
    stringC = stringB[::-1]
    if(stringA == stringC):
        print("YES")
    else:
        print("NO")

def main():
    a = input("")
    b = input("")
    computeProblem(a, b)
main()