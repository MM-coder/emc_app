import calculations # Import our custom coded cacluations module (calculations.py)
import homework # Import our custom coded homework module (homework.py)
import classes # Import our custom coded classes module (classes.py)
from flask import Flask, redirect, url_for, render_template, request # Import Flask
import sys
import datetime

version = "1.0A"


app = Flask(__name__)
app.secret_key = b"74 a7 62 83 f4 82 ca b1 78 34"

@app.route("/")
def index():
    next_class_obj = calculations.get_closest_class(calculations.get_day_timetable(calculations.get_weekday_int(datetime.datetime.now().weekday())))
    next_homework_obj = homework.get_next_task_due()
    return render_template('index.html', next_class = classes.create_readable_class(next_class_obj), readable_time = calculations.return_readable_time(next_class_obj['start']), next_homework = next_homework_obj, homework_time = calculations.return_readable_time(next_homework_obj['deliver_time']), version=version)

@app.route("/aulas")
def aulas():
    return render_template('classes.html', segunda = classes.create_readable_class_list(calculations.get_day_timetable('monday')), terca = classes.create_readable_class_list(calculations.get_day_timetable('tuesday')), quarta = classes.create_readable_class_list(calculations.get_day_timetable('wedensday')), quinta = classes.create_readable_class_list(calculations.get_day_timetable('thursday')), sexta = classes.create_readable_class_list(calculations.get_day_timetable('friday')))


@app.errorhandler(404)
def handle_404_error(e):
    return render_template('404.html', path = str(request.path))

if __name__ == "__main__":
    app.run()