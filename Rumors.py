# Rumors.py

# This program  simulates the spreading of a rumor among a group of people.
# The user is prompted to enter a population size and the number of trials
# to run. The program detemines the number of meetings that occured and how
# many people did not hear the rumor and places the results for each trial
# in a CSV file for analysis.

import random

# returns file object in write mode named randomWalk.csv
# csv = comma separated values text file
dataFile = open("rumor.csv", "w")

# Function to simulate a rumor spreading among a populatin argument
def rumorSim(popSize):
    # List to represent the Population
    population = []
    
    # Variables to represent IGNORANTS, SPREADERS, STIFLERS
    IGNORANT = 1
    SPREADER = 2
    STIFLER = 3

    # Variables to hold the number of SPREADERS and IGNORANTS and meetings
    numSpreaders = 1
    numIgnorants = popSize - 1
    numMeetings = 0
    
    # Populates the list with all IGNORANT people
    for i in range(popSize):
        population.append(IGNORANT)
        
    # Places one SPREADER in the population at a random location
    firstSpreader = random.randint(0, popSize - 1)
    population[firstSpreader] = SPREADER

    # Has people meet until there are no more SPREADERS or no more IGNORANTS
    while numSpreaders != 0 and numIgnorants != 0:

        # Variables to pick 2 random people
        person1 = random.randint(0, popSize - 1)
        person2 = random.randint(0, popSize - 1)

        # Uncomment to troubleshoot
        # print(person1, population[person1])
        # print(person2, population[person2])

        # Handles the 2 people meeting
        if person1 != person2:
            # Increment Meetings
            numMeetings += 1
            
            if population[person1] == IGNORANT and population[person2] == SPREADER:
                population[person1] = SPREADER
                numSpreaders += 1
                numIgnorants -= 1
            elif population[person1] == SPREADER and population[person2] == IGNORANT:
                population[person2] = SPREADER
                numSpreaders += 1
                numIgnorants -= 1
            elif population[person1] == SPREADER and population[person2] == STIFLER:
                population[person1] = STIFLER
                numSpreaders -= 1
            elif population[person1] == STIFLER and population[person2] == SPREADER:
                population[person2] = STIFLER
                numSpreaders -= 1
            elif population[person1] == SPREADER and population[person2] == SPREADER:
                population[person1] = STIFLER
                population[person2] = STIFLER
                numSpreaders -= 2

        # Uncomment to troubleshoot
        # print(population[person1])
        # print(population[person2])
        # print(population)

    return numMeetings, numIgnorants

# Prompts the user to enter a population size
popInput = input("Enter a population size: ")

# Handles incorrectly entered population sizes
while True:
    try:
        popSize = int(popInput)
    except:
        print("That was not a whole number.")
        popInput = input("Try again: ")
        continue
    break

# Ensures a positive population size
popSize = abs(int(popSize))


# Prompts the user to enter the number of simulations to run
trialsInput = input("Enter the number of trials: ")

# Handles incorrectly entered number of trials
while True:
    try:
        numTrials = int(trialsInput)
    except:
        print("That was not a whole number.")
        trialsInput = input("Try again: ")
        continue
    break

# Ensures a positive number of trials
numTrials = abs(int(numTrials))

# Variables for number of meetings and ignorants left
meetings = 0
ignorants = 0

# Runs the trials
for i in range(numTrials):
    trial = rumorSim(popSize)
    meetings = trial[0]
    ignorants = trial[1]
    # uncomment to troubleshoot
    # print(meetings, ignorants)
    
    # writes the averages to randomWalk.csv
    dataFile.write(str(meetings) + "," + str(ignorants) + "\n")

# closes file object
dataFile.close()

# prints confirmation that the program has completed
print("Open rumor.csv in Microsoft Excel.")


    
