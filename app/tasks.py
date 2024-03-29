from app import app, db
from app.models import Task
from datetime import datetime, timedelta
from flask_mail import Mail, Message

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your_email@gmail.com'
app.config['MAIL_PASSWORD'] = 'your_email_password'
mail = Mail(app)

def send_email_notifications():
    tasks_due_today = Task.query.filter(Task.due_date == datetime.today().date()).all()
    for task in tasks_due_today:
        msg = Message('Task Reminder: ' + task.title,
                      sender='your_email@gmail.com',
                      recipients=['recipient_email@gmail.com'])
        msg.body = f"Dear User,\n\nThis is a reminder that the following task is due today:\n\nTitle: {task.title}\nDescription: {task.description}\nPriority: {task.priority}\n\nPlease complete the task on time.\n\nRegards,\nTask Management System"
        mail.send(msg)

if __name__ == '__main__':
    with app.app_context():
        send_email_notifications()
