#Here input.txt already has some text and a new string is appended in this program
f = open('input.txt','a+')
v = f.read()
vr = ' good morning!'
o = open('input.txt','a+')
o.write(vr)
