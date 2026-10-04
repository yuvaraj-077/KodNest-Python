# inbilt string methods -Single Program
s = " KoNest Technologies 123  "

print("orginal String:", s) #kodNest Technologies 123

#case conversion methods
print("upper():", s.upper()) #KODNEST TECHNOLOGIES 123
print("lower():", s.lower()) #kodnest technologies 123
print("capitalize():", s.capitalize()) #kodnest technologies 123
print("title():",s.title()) # Kodnest Technologies 123
print("swapcase():", s.swapcase()) # koDNest Technologies 123

#Searching & counting
print("find('Tech'):", s.find("Tech")) #10
print("count('o'):", s.count("o")) #3

# Replace
print("replace('123', '2025'):", s.replace("kodNest", "2025")) #KodNest 2025

#start & End check
print("startswith('  kod'):", s.startswith("  kod")) # true
print("endswith('123  '):", s.endswith("123  ")) #ture

#Split & Join
words = s.split()
print("split():", words)
print("join():", "-".join(words))

#Strip space
print("strip():", s.strip())
print("lstrip():", s.lstrip())
print("rstrip():", s.rstrip())



