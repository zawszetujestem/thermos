from thermos import app, db
from thermos.models import Bookmark
from flask_script import Manager, prompt_bool
from flask_migrate import Migrate, MigrateCommand


manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


@manager.command
def init_db():
    db.create_all()

    db.session.add(Bookmark(url="http://goole.com", description="dbuabda"))
    db.session.add(Bookmark(url="http://mama.com", description="dbudeddabda"))

    db.session.commit()
    print("Initialized the database")


@manager.command
def drop_db():
    if prompt_bool("Are you sure you want to lose all your data?"):
        db.drop_all()
        print("Dropped the db")


@manager.command
def insert_data():
    pass


if __name__ == '__main__':
    manager.run()
