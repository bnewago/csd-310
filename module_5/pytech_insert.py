from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.ziqiy.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

Client = MongoClient(url)

db = Client.pytech

""" Student Documents"""


# Bruno Madrigal
bruno = {
    "student_id": "1007",
    "first_name": "Bruno",
    "last_name": "Madrigal",
    "enrollments": [
        {
            "term": "Spring 2065",
            "gpa": "4.0",
            "start_date": "March 1, 2065",
            "end_date": "May 1, 2065",
            "courses": [
        {
            "course_id": "Cybr410",
            "description": "Data/Database Security",
            "instructor": "Professor Lappe",
            "grade": "A"
        }

            ]
        }
    ]
}

# Craig List
craig = {
    "student_id": "1008",
    "first_name": "Craig",
    "last_name": "List",
    "enrollments": [
        {
            "term": "Summer",
            "gpa": "2.9",
            "start_date": "July 1, 2065",
            "end_date": "September 1, 2065",
            "courses": [
                {
                    "course_id": "CIS331",
                    "description": "Into to Code",
                    "instructor": "John Cena",
                    "grade": "C"
                },
                {
                    "course_id": "Cybr100",
                    "description": "Computers 100",
                    "instructor": "Joe Rogan",
                    "grade": "A"
                }
            ]
        }
    ]
}



            


students = db.students
# insert statements
print("\n --INSERT STATEMENTS --")
bruno_student_id = students.insert_one(bruno).inserted_id
print(" Inserted student record Bruno Madrigal into the students collection with student_id " + str(bruno_student_id))
print(" Inserted student record Bruno Madrigal into the students collection with document_id " + str(bruno_student_id))

craig_student_id = students.insert_one(craig).inserted_id
print(" Inserted student record Craig List into the students collection with student_id " +str(craig_student_id))
print(" Inserted student record Craig List into the students collection with document_id " + str(craig_student_id))


input("\n\n End of program, press any key to exit..")
