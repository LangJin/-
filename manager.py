from app import create_app, db
from app.models.model import User
from flask_script import Manager, Shell
app = create_app("development")
manager = Manager(app)


def make_shell_context():
    return dict(app=app, db=db, User=User)


manager.add_command("shell", Shell(make_context=make_shell_context))


if __name__ == '__main__':
    manager.run()
