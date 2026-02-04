""" tip = input("How much did you tip")
if (tip) == 25:
    print ('great')
elif int(tip) == 20:
     print ('good')
elif int(tip) == 15:
     print ('okay')
elif int(tip) == 10:
     print ('bad')  """





""" def discount (age, isMember, isResident):
    if age < 12 or age >= 65 and (isResident or isMember):
        print ('qualifies') """

service = input("How was the service?").capitalize
if service == "Great":
    print("25%")
elif service == "Good":
    print("20%")
elif service == "Okay":
    print("15%")
elif service == "Bad":
    print("0%")