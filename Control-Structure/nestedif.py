age=input("Enter Age")
nation=input("Enter Nation")
age=int(age)
if age>=18:
    if nation == 'Indian':
      print("Voting Allowed")
    else:
        print("Not a Indian")
else:
   print("Voting not Allowed")    