from flask_script import Manager, Shell
from flask_migrate import MigrateCommand
from application import create_app, db
from application.models.models import User, Role


app = create_app('default')
manager = Manager(app)


def make_shell_context():
    return dict(app=app, db=db)


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


@manager.command
def createdatas():
    admin_role = Role(name='Admin')
    mod_role = Role(name='Moderator')
    user_role = Role(name='User')
    user_john = User(username='john', role=admin_role)
    user_susan = User(username='susan', role=user_role)
    user_david = User(username='david', role=user_role)
    db.session.add_all(
        [admin_role, mod_role, user_role, user_john, user_susan, user_david])
    db.session.commit()


@manager.command
def init_db():
    db.drop_all()
    db.create_all()


if __name__ == "__main__":
    manager.run()
