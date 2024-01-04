from flask import Flask, render_template
from ctf import get_task_by_id

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/task/<int:task_id>')
def task(task_id):
    task = get_task_by_id(task_id)
    return render_template('task.html', task=task)

if __name__ == '__main__':
    app.run(debug=True)
