num=int(input("Enter number of students: "))
increment=1
students_marks=[]
while increment<= num:
    print(f"........Students: {increment}...........")
    for mark in range(1):
        nep=int(input("Enter nep mark: "))
        eng=int(input("Enter eng mark: "))
        sci=int(input("Enter sci mark: "))
        pop=int(input("Enter pop mark: "))
        math=int(input("Enter math mark: "))
        marks=[nep,eng,math,sci,pop]
        students_marks.appen(marks)
    increment+=1
print(students_marks)

for students in students_marks:
    total=0
    for get_mark in students:
        total+=get_mark

    percentage=total/5
    div=''
    if percentage>=75 and percentage<=100:
        div+="Distinction"
    elif percentage>=60 and percentage<75:
        div+="First division"
    elif percentage>=45 and percentage<60:
        div+="Second division"
    elif percentage>=35 and percentage<45:
        div+="Third division"
    else:
        div+="fail"

    print(f"Total marks:{total} and percentage:{percentage} and division: {div}")