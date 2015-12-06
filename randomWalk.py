# Basic Structure for a Random Walk simulation
# Dan Neumann
'''

You flip a coin.
If it comes up heads, you take a step forward;
tails means to take a step backward.
Repeat this n times.
Calculate distance from start

Repeat this process a large number of times.
Calculate and print the average for a given value of n
Start with 100 to 1000, step 10
'''

import random

# Define ranges here

startRange = 100
endRange = 1000
stepRange = 10

def main():
    total = 0 
    for n in range(startRange,endRange,stepRange):
        total += getRandomWalk(n)
    n = endRange + stepRange / startRange
    print("The average postion: {}".format(total))


def getRandomWalk(steps):
    # Calculate a random walk of given steps
    position = 0
    for walk in range(steps):
        position = random.choice([position-1,position+1])
    return position
if __name__ == "__main__":
    main()