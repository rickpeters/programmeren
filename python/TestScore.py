#  LPT Scoring Calculator to Console version
# Create a routine to calculate Coursera percentage for Learn to Program course
# ngc - Sept 2013
# Final link (?) -- http://paste.debian.net/hidden/115c38ac
# 2nd last Debian Paste Link -- http://paste.debian.net/hidden/47a0e363
############### NOTES on user updating of Lists:
## scores_max = [33, 49, 63, 77]   33 is possible points for Ex 1 and 2;
## 49 is Ex 1 & 2 with ex 3 added, and so on. 77 is total possible through quiz 5;
## IF (for example) quiz ex 6 has 15 points and quiz ex 7 has 20 points
#  You can update program by changing to
## scores_max = [33, 49, 63, 77, 92, 112]
## Likewise, asst_scores_max = [41, 65] is total possible points for
## Assignments 1 and 2; if assignment 3 is worth 35 points, you can update to
## asst_scores_max = [41, 65, 100] and the program will be current.
##
## 90% or more of the routines here are things we learned in the
## first 4 weeks of the course, so if you like, see if you can
## improve it to better fit your own needs.

""" Inputs:

Work	      Weight	Total Points
Exercise 1	5%	15
Exercise 2	5%	18
Assignment 1	10%	41
Exercise 3	5%	16
Exercise 4	5%	14
Assignment 2	15%	24
Exercise 5	5%	14
Exercise 6	5%	13
Assignment 3	15%	37
Exercise 7	5%	12
Final Exam	25%	Monday 7 October 11:59 am (13 questions)

"""
### f1 = open('./testfile.txt', 'a')

# Start with Exercises (7 total for 35% of grade)
num_ex = input("How many Exercises to input? (2-7) --> ")
###convert to integer
num_ex = int(num_ex)
my_weeks = list(range(1, num_ex + 1))
my_scores = []

for n in my_weeks:
    blurb = "Score for Week " + str(n) + " --> "
    my_scores.append(input(blurb))

# now convert the list to floats
my_scores = [float(i) for i in my_scores]

# find average for Exercises & percentage so far
scores_max = [33, 49, 63, 77, 90, 102]  #running total starting at 2
ex_percent = (sum(my_scores)/scores_max[num_ex - 2]) * 100
poss_score = (num_ex * 0.05) * 100

print('')
print("Possible points for all 7 exercises = 102")
print("Total points for first", num_ex, "exercises = ",sum(my_scores))
print("Average points for first", num_ex, "exercises = ", round(sum(my_scores)/num_ex, 3))
print('')
print("Your percentage score for exercises reported = ", round(ex_percent, 3),"%")
print('')
print("Exercises (quizzes) are 35% of your total score.")
print("Your first", num_ex, "exercises account for", poss_score, "percent.")
print("\t\t==============================")
print('')
#===============================================
# Next do Assignments (3 total for 40% of grade)
num_asst = input("How many Assignments to input? (1 - 3) --> ")
num_asst = int(num_asst)

if num_asst == 1:
    asst_percent = 10
elif num_asst == 2:
    asst_percent = 25
elif num_asst == 3:       # all assignments done
    asst_percent = 40

my_assts = list(range(1, num_asst + 1))
your_scores = []

for n in my_assts:
    gabble = "Score for Assignment " + str(n) + " --> "
    your_scores.append(input(gabble))

# Fix extra point (42/41 score problem) & Conv to float
if int(your_scores[0]) > 41:
    your_scores[0] = 41

your_scores = [float(i) for i in your_scores]

asst_scores_max = [41, 65, 102]    # running total
your_percent = (sum(your_scores)/asst_scores_max[num_asst - 1]) * 100
print('')
print("Possible points for all 3 assignments = 102")
print("Total points for", num_asst, "assignments = ",sum(your_scores))
print("Average points for", num_asst, "assignments = ", round(sum(your_scores)/num_asst, 3))
print('')
print("Your percentage score for assignments reported = ", round(your_percent, 3), "%")
print('')
print("Assignments (projects) are 40% of your total score.")
print("Your first", num_asst, "assignments account for", asst_percent,"percent.")
print('')
print()
print()
# Give a wrap up of calculations
running_percent = poss_score + asst_percent
average_percent = (ex_percent + your_percent) / 2

# Add calculation for Final Exam
##print("Final Exam is worth 25% of grade. Calculate your percentage below:")
##num_qs = 13  # Instructors announced this number on Oct 1 or 2 2013
##num_correct = input("How many points did you receive of total? (max = 13) --> ")
##final_percent = float(num_correct)/num_qs
##percent_of_final_grade = 25 * final_percent

def where_am_i():
    before_final = running_percent * average_percent * .01

    for i in range(0, 14):
        my_total = before_final + ((i/13) * 25)
        print(i, "correct questions in Final make your total =", round(my_total, 3))



#f1 = open('./testfile.txt', 'a')
print("\t\t______________________________")
print("\t\tYour combined Percentage Score")
print('')
print("\tTo date you have done", num_ex, "exercises, and", num_asst, "assignments.")
print("\tThis accounts for", running_percent, "% of your final total grade,")
print("\tand your overall percentage so far is", round(running_percent * average_percent * .01, 3))
print('')
my_final = input('Do you want to see necessary Final results and related percentage scores? Y/N ')
if my_final.upper() == 'Y':
    where_am_i()

#print("Including the Final, your overall percentage is", (percent_of_final_grade + (running_percent * average_percent) * .01))

### f1.close()
print('')
print("Finished")