from flask import Flask, render_template,request, redirect
import json
import re



app = Flask(__name__)


students = [
    {"id": 1, "name": "Brendan", "age": 30},
    {"id": 2, "name": "Chris", "age": 28},
    {"id": 3, "name": "Kathrin", "age": 35},
    {"id": 4, "name": "Colleen", "age": 39},
    {"id": 5, "name": "Mark", "age": 40},
    {"id": 6, "name": "Daniel", "age": 45},
    {"id": 7, "name": "Tati", "age": 98},
]


#
#
# classes = [
#     {"name": "CS101", "hours": 30},
#     {"name": "History", "hours": 28},
#     {"name": "Art", "hours": 35},
#     {"name": "Design", "hours": 39},
#     {"name": "Geography", "hours": 40},
#     {"name": "Music", "hours": 45},
# ]


@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/students')
def show_students():
    return render_template("students.html",students=students)
@app.route('/students/<int:id>')
def student_details(id):
    for student  in students:
        if student['id']==id :
            return render_template('detail.html', student=student)

    return "Student Not Found"

@app.route('/students/add' , methods=['GET','POST'])
def add_student():
    if request.method=='POST':
        name = request.form['Name']
        age = request.form['Age']
        id = len(students) + 1
        students.append({'id': id, 'name': name, 'age': age})
        return redirect('/students')

    else:
        return render_template('addstudent.html')


# @app.route('/classes')
# def show_classes():
#     return render_template("show_classes.html", classes = classes)
#
# @app.route('/classes/<classname>')
# def show_class(classname):
#     return render_template("class.html", name = classname)


if __name__ == '__main__':
    app.run(debug=True)