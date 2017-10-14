mylist=[]
total=0

for i in range(4):
  total=0 
  expenses = raw_input("Bale ta probata pou epestrepsan th nuxta (xwrismena me koma):") 
  for expense in expenses.split(","):
   total += int(expense) 
   mylist.append(total)
  
  
  print( "Total: " + str(total) )

k=raw_input("dwse arxika probata")

if (mylist[i]<k):
     y=int(k)-total 
     print ("exases %d probata") %y