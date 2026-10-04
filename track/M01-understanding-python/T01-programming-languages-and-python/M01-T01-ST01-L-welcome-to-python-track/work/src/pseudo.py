# ==========================================
# 1. To print Hello World
# ==========================================
# Pseudocode:
# START
# PRINT "Hello World"
# END

print("Hello World")


# ==========================================
# 2. To find whether number (n) is even or odd
# ==========================================
# Pseudocode:
# START
# PUT number INTO n
# IF n % 2 == 0
#     PRINT "even"
# OTHERWISE
#     PRINT "odd"
# END

n = 4
if n % 2 == 0:
    print("even")
else:
    print("odd")


# ==========================================
# 3. To find whether the number is positive, negative, or zero
# ==========================================
# Pseudocode:
# START
# PUT number INTO n
# IF n > 0
#     PRINT "positive"
# ELSE IF n < 0
#     PRINT "negative"
# ELSE
#     PRINT "zero"
# END

n = 0
if n > 0:
    print("positive")
elif n < 0:
    print("negative")
else:
    print("zero")


# ==========================================
# 4. To find the largest among 3 numbers a, b, c
# ==========================================
# Pseudocode:
# START 
# INPUT a
# INPUT b
# INPUT c
# IF a >= b and a >= c
#     PRINT "a is largest"
# ELSE IF b >= a and b >= c
#     PRINT "b is largest"
# ELSE
#     PRINT "c is largest"
# END IF
# END

a = 10
b = 2
c = 0

if a >= b and a >= c:
    print("a is largest")
elif b >= a and b >= c:
    print("b is largest")
else:
    print("c is largest")
