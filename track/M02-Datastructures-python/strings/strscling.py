# ============================================================

# STRING SLICING - POSITIVE SLICING PRACTICE

# ============================================================

#

# Syntax:

# string[start:stop:step]

#

# Rules:

# 1. start is included

# 2. stop is excluded

# 3. positive step moves from left to right

# 4. If step is not given, default step is 1

#

# Try to predict the output before running each question.

# ============================================================





# ------------------------------------------------------------

# LEVEL 1 - BASIC start:stop

# ------------------------------------------------------------



# 1. Extract the first 3 characters

text = "Python"

print(text[0:3])#p,y,t


# 2. Extract characters from index 1 to 4

text = "Programming"

print(text[1:5])#r,o,g,r


# 3. Extract characters from index 2 to 5

text = "Developer"

print(text[2:6]) #v,e,l,o

# 4. Extract characters from index 3 to 6

text = "Computer"

print(text[3:7]) #p,u,t,e





# 5. Extract the first 4 characters

text = "Artificial"

print(text[0:4])#A,r,t,i



# 6. Extract characters from index 2 to 6

text = "Education"

print(text[2:7])#u,c,a,t,i


# 7. Extract characters from index 4 to 9

text = "JavaScript"

print(text[4:10])#s,c,r,i,p,t


# 8. Extract characters from index 4 to 9

text = "DataScience"

print(text[4:10])#i,e,n,c,e


# ------------------------------------------------------------

# LEVEL 2 - MISSING START OR STOP

# ------------------------------------------------------------



# 9. Extract from beginning to index 5

text = "PythonProgramming"

print(text[:6])#P,y,t,h,o,n


# 10. Extract from index 6 to the end

text = "PythonProgramming"

print(text[6:])#p,r,o,g,a,m,m,i,n,g


# 11. Extract from beginning to index 8

text = "FullStackDeveloper"

print(text[:9])#F,u,l,l,S,t,a,c,k



# 12. Extract from index 9 to the end

text = "FullStackDeveloper"

print(text[9:])#D,e,v,e,l,o,p,e,r




# 13. Extract from beginning to index 6

text = "MachineLearning"

print(text[:7])#M,a,c,h,i,n,e





# 14. Extract from index 7 to the end

text = "MachineLearning"

print(text[7:])#L,e,a,r,n,i,n,g





# ------------------------------------------------------------

# LEVEL 3 - POSITIVE STEP

# ------------------------------------------------------------



# 15. Take every second character

text = "ABCDEFGHIJ"

print(text[0:8:2])#A,C,E,G





# 6. Take every second character

text = "ABCDEFGHIJ"

print(text[1:9:2])#B,D,F,H


# 17. Take every third character

text = "ABCDEFGHIJKL"

print(text[0:12:3])#A,D,G,J






# 18. Take every second character

text = "ABCDEFGHIJKL"

print(text[2:10:2])#C,E,G,I




# 19. Take every second number

text = "1234567890"

print(text[0:10:2])#1,3,5,7,9





# 20. Take every second number starting from index 1

text = "1234567890"

print(text[1:9:2])#2,4,6,8






# ------------------------------------------------------------

# LEVEL 4 - TRICKY POSITIVE SLICING

# ------------------------------------------------------------



# 21. Take every third character

text = "Programming"

print(text[0:11:3])#P,o,a,m,i





# 22. Take every third character starting from index 1

text = "Programming"

print(text[1:10:3])#r,g,m,i





# 23. Take every second character

text = "PythonProgramming"

print(text[2:14:2])#t,h,P,o,a,m,n





# 24. Take every third character

text = "PythonProgramming"

print(text[1:15:3])#y,o,P,o,a,m,i





# 25. Take every second character

text = "ABCDEFGHIJKLMNO"

print(text[3:13:2])#D,F,H,J,L





# 26. Take every third character

text = "ABCDEFGHIJKLMNO"

print(text[2:14:3])#C,F,I,L



# ------------------------------------------------------------

# LEVEL 5 - INTERVIEW STYLE

# ------------------------------------------------------------



# 27. Predict the output

text = "PythonProgramming"

print(text[0:16:4])#p,h,o,





# 28. Predict the output

text = "ABCDEFGHIJKLM"

print(text[1:12:3])#B,E,H,K





# 29. Predict the output

text = "DataScienceWithPython"

print(text[4:18:2])#S,e,W,p,h,n





# 30. Predict the output

text = "FullStackDevelopment"

print(text[2:19:3])#L,S,o,e,l,e,m





# ------------------------------------------------------------

# CONCEPT QUESTIONS

# ------------------------------------------------------------



# 31. Compare the following

text = "Python"



print(text[1:5])#y,t,h,o

print(text[1:5:1])#y,t,h,o

print(text[1:5:2])#y,h


# 32. What happens when start > stop?

text = "Python"

print(text[4:2])#p,y,t,h,n


# 33. What happens when start == stop?

text = "Python"

print(text[2:2])#





# 34. What happens when indexes are outside the string?

text = "Python"

print(text[10:20])#





# 35. What happens when stop is larger than the string length?

text = "Python"

print(text[0:100])#





# ------------------------------------------------------------

# BONUS CHALLENGES

# ------------------------------------------------------------



# 36. Predict the output

text = "ABCDEFGHIJKLM"

print(text[2:11:3])#

# 37. Predict the output

text = "ProgrammingLanguage"

print(text[3:15:2])#g,a,m,n,L,n

# 38. Predict the output

text = "PythonDeveloper"

print(text[1:12:3])#y,o,e,l

# 39. Predict the output

text = "DataScience"#

print(text[0:10:2])#D,t,S,i,c

# 40. Predict the output

text = "FullStackDeveloper"

print(text[4:16:2])# S,a,k,e,e,o