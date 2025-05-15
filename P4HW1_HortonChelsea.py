# Chelsea Horton
# 4/30/25
# P4HW1
# Enhance a exisiting program by incorporating loops 

# Start the program and ask how many scores the user wants to enter
num_scores = int(input("How many scores do you want to enter? "))

# Create an empty list to hold the scores
scores = []

# Create a loop to collect each score
i = 1
while i <= num_scores:
    score = float(input("Enter score #" + str(i) + ": "))

 # Check if the score is valid (between 0 and 100)
    if score < 0 or score > 100:
        print("INVALID Score entered!!!!")
        print("Score should be between 0 and 100")
    else:
# If valid, add score to list
        scores += [score]
        i += 1

# Next find the lowest score
lowest = scores[0]
for score in scores:
    if score < lowest:
        lowest = score

# Create a new list without the lowest score
sum_scores = 0
count = 0
for score in scores:
    if score != lowest or count == 1: 
        sum_scores += score
    else:
        count += 1

# Calculate the average after removing the lowest score
average = sum_scores / (num_scores - 1)

# Determine the letter grade based on average
if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

# Display the results
print("\n----------Results----------")
print("Lowest Score  :", lowest)
print("Modified List :", [score for score in scores if score != lowest] + ([lowest] if scores.count(lowest) > 1 else []))
print("Scores Average:", round(average, 2))
print("Grade         :", grade)
print("----------------------------")

