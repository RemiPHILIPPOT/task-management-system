from flask import render_template, url_for, flash, redirect
from app import app, db
from .forms import TaskForm
from app.models import Task

@app.route("/", methods=['GET', 'POST'])
def index():
    form = TaskForm()
    if form.validate_on_submit():
        task = Task(title=form.title.data, description=form.description.data, priority=form.priority.data)
        db.session.add(task)
        db.session.commit()
        flash('Task created successfully!', 'success')
        return redirect(url_for('index'))
    tasks = Task.query.all()
    return render_template('index.html', form=form, tasks=tasks)

@app.route("/delete/<int:task_id>", methods=['POST'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    flash('Task deleted successfully!', 'success')
    return redirect(url_for('index'))
