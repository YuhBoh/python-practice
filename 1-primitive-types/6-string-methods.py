course = "Python Programming"
print(course.upper())
print(course.lower())
print(course.title())

# Gets rid of space from beginning and end
print(course.strip())

# find the index of pro
print(course.find("Pro")) 

print(course.find("pro" in course)) 
# Output: true

print(course.find("Pro" not in course)) 
# Output: false
