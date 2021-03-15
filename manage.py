from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import app
from db import db
from models import *


try:
    db.create_all()
except Exception as error:
    app.logger.error(str(error))

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
