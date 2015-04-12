def hour():
 n_hr = int(raw_input("Enter number of hours: "))
 return n_hr

def day():
 d_hr = int(raw_input("Enter the number of days: "))
 return d_hr

def cost(h,d):
 c = h*d*8
 return c

h2 = hour()
d2 = day()

print 'Total cost is ', cost(h2,d2)
