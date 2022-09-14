#calculate "a" letter in the text 
text = input("Enter the message: ") 
count = 0
for i in text:
    if i == 'a': 
        count = count + 1
print("Count of a in text: " + str(count))
