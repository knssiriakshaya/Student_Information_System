from flask import Flask, render_template, request, redirect, url_for, flash
from config import get_db_connection

app = Flask(__name__)
app.secret_key = 'your_secure_random_secret_key'  # Replace with a secure key


# **Home Route**
@app.route('/')
def index():
    return render_template('index.html')


# **Student Routes**
@app.route('/students')
def students():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Students')
        students = cursor.fetchall()
        conn.close()
        return render_template('students.html', students=students)
    except Exception as e:
        flash(f"Error fetching students: {e}", 'error')
        return redirect(url_for('index'))


@app.route('/add_student', methods=('GET', 'POST'))
def add_student():
    if request.method == 'POST':
        id = request.form['id']
        name = request.form['name']
        dob = request.form['dob']
        email = request.form['email']
        contact = request.form['contact']

        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                'INSERT INTO Students (id, name, dob, email, contact) VALUES (%s, %s, %s, %s, %s)',
                (id, name, dob, email, contact)
            )
            conn.commit()
            conn.close()
            flash('Student added successfully!', 'success')
            return redirect(url_for('students'))
        except Exception as e:
            flash(f"Error adding student: {e}", 'error')
            return render_template('add_student.html')  # Stay on the add_student page if error occurs

    return render_template('add_student.html')

@app.route('/add_course', methods=('GET', 'POST'))
def add_course():
    if request.method == 'POST':
        course_id = request.form['course_id']
        course_name = request.form['course_name']
        credits = request.form['credits']

        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('INSERT INTO Courses (id, name, credits) VALUES (%s, %s, %s)',
                           (course_id, course_name, credits))
            conn.commit()
            conn.close()
            flash('Course added successfully!', 'success')
            return redirect(url_for('courses'))
        except Exception as e:
            flash(f"Error adding course: {e}", 'error')
            return render_template('add_course.html')

    return render_template('add_course.html')


# **Course Routes**
@app.route('/courses')
def courses():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Courses')
        courses = cursor.fetchall()
        conn.close()
        return render_template('courses.html', courses=courses)
    except Exception as e:
        flash(f"Error fetching courses: {e}", 'error')
        return redirect(url_for('index'))


# **Enrollment Routes**
@app.route('/enrollments')
def enrollments():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Enrollments')
        enrollments = cursor.fetchall()
        conn.close()
        return render_template('enrollments.html', enrollments=enrollments)
    except Exception as e:
        flash(f"Error fetching enrollments: {e}", 'error')
        return redirect(url_for('index'))


# **Grade Routes**
@app.route('/grades')
def grades():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Grades')
        grades = cursor.fetchall()
        conn.close()
        return render_template('grades.html', grades=grades)
    except Exception as e:
        flash(f"Error fetching grades: {e}", 'error')
        return redirect(url_for('index'))



@app.route('/add_enrollment', methods=('GET', 'POST'))
def add_enrollment():
    if request.method == 'POST':
        id = request.form['id']
        student_id = request.form['student_id']
        course_id = request.form['course_id']
        date = request.form['date']

        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('INSERT INTO Enrollments (id,student_id, course_id,enrollment_date) VALUES (%s, %s, %s, %s)',
                           (id,student_id, course_id, date))
            conn.commit()
            conn.close()
            flash('Enrollment added successfully!', 'success')
            return redirect(url_for('enrollments'))
        except Exception as e:
            flash(f"Error adding enrollment: {e}", 'error')
            return render_template('add_enrollment.html')

    # Fetch data for the dropdowns
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT id, name FROM Students')
    students = cursor.fetchall()
    cursor.execute('SELECT id, name FROM Courses')
    courses = cursor.fetchall()
    conn.close()

    return render_template('add_enrollment.html', students=students, courses=courses)
@app.route('/add_grade', methods=('GET', 'POST'))
def add_grade():
    if request.method == 'POST':
        student_id = request.form['student_id']
        enrollment_id = request.form['enrollment_id']
        grade = request.form['grade']

        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('INSERT INTO Grades (student_id, enrollment_id, grade) VALUES (%s, %s, %s)',
                           (student_id, enrollment_id, grade))
            conn.commit()
            conn.close()
            flash('Grade assigned successfully!', 'success')
            return redirect(url_for('grades'))
        except Exception as e:
            flash(f"Error adding grade: {e}", 'error')
            return render_template('add_grade.html')

    # Fetch data for the dropdowns
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT id FROM Students')
    students = cursor.fetchall()
    cursor.execute('SELECT id FROM Enrollments')
    enrollments = cursor.fetchall()
    conn.close()

    return render_template('add_grade.html', students=students, enrollments=enrollments)


# **Run the Application**
if __name__ == '__main__':
    app.run(debug=True)
