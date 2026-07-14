from flask import Flask, render_template, request, send_file
import sqlite3
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

app = Flask(__name__)


# Database connection function
def get_db_connection():
    conn = sqlite3.connect("students.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/result", methods=["POST"])
def result():

    hall_ticket = request.form["hall_ticket"].strip()
    
    if hall_ticket == "":
        return render_template("not_found.html")

    conn = get_db_connection()

    student = conn.execute(
        "SELECT * FROM students WHERE hall_ticket = ?",
        (hall_ticket,)
    ).fetchone()

    conn.close()

    if student:
        return render_template(
            "result.html",
            student=student
        )

    else:
        return render_template(
            "not_found.html"
        )


@app.route("/download/<hall_ticket>")
def download(hall_ticket):

    conn = get_db_connection()

    student = conn.execute(
        "SELECT * FROM students WHERE hall_ticket = ?",
        (hall_ticket,)
    ).fetchone()

    conn.close()


    if student:

        file_name = "student_result.pdf"

        pdf = canvas.Canvas(file_name, pagesize=letter)


        pdf.setFont("Helvetica", 14)

        pdf.drawString(
            200,
            750,
            "Student Result"
        )


        pdf.setFont("Helvetica", 12)


        pdf.drawString(
            100,
            700,
            f"Name: {student['name']}"
        )


        pdf.drawString(
            100,
            670,
            f"Hall Ticket: {student['hall_ticket']}"
        )


        pdf.drawString(
            100,
            640,
            f"Branch: {student['branch']}"
        )


        pdf.drawString(
            100,
            610,
            f"Semester: {student['semester']}"
        )


        pdf.drawString(
            100,
            560,
            f"Python: {student['python']}"
        )


        pdf.drawString(
            100,
            530,
            f"Java: {student['java']}"
        )


        pdf.drawString(
            100,
            500,
            f"DBMS: {student['dbms']}"
        )


        pdf.drawString(
            100,
            470,
            f"Web Technology: {student['web']}"
        )


        pdf.drawString(
            100,
            420,
            f"CGPA: {student['cgpa']}"
        )


        pdf.save()


        return send_file(
            file_name,
            as_attachment=True
        )


    else:
        return "Student not found"



if __name__ == "__main__":
    app.run(debug=True)

