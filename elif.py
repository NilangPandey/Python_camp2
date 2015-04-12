#The text is written in txt file here with the help if-else control statement
x = int(raw_input("Enter an integer value"))
if x > 300:
 y = 'Greater than 300'
elif x < 300:
 y = 'Less than 300'
else:
 y = 'Equal to 300'
print y
print 'Your answer has been stored to a text file'
o = open('output.txt','w')
o.write(y)
