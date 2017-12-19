from flask_script import Manager, Shell
# from flask_migrate import MigrateCommand
from application import create_app, db
from application.models.models import User, Role


app = create_app('default')


def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)


manager = Manager(app)
manager.add_command("shell", Shell(make_context=make_shell_context))


@manager.command
def createdatas():
    Role.initrole()
    User.inituser()


@manager.command
def init_db():
    db.drop_all()
    db.create_all()


if __name__ == "__main__":
    manager.run()
