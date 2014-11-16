from flask import render_template

from app import app

@app.route("/")
def show_homepage():
	questions = ["How many bits are in a byte ?", "How do you represent an integer in C++ ?"]
	questions_info = [{"letter" : "A", "description": "8 bits"}, {"letter" : "B", "description": "2 bits"}]
	heading = "COP3014 Quiz 1"
	return render_template("index.html", quiz_heading=heading, question=questions[0], answers=questions_info);

@app.route("/quiz/<id>/")
def show_quiz(quiz_id):
	pass