Marks = int(input("Enter marks"))
Attendance = int(input("Enter Attendance"))
Project_Status = input("Enter Project Status")
if Marks >= 60 and Attendance >= 75:
    if Project_Status == "Yes":
        print ("Eligible")
    else:
        print ("Not Eligible")
else:
    print ( "Not Eligible")        