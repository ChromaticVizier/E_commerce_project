"""
The quality of mercy is not strained,
It drops as the gentle rain from heaven.
"""

from flask_api import create_app, db
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager


app = create_app('develop')
manager = Manager(app)
mig = Migrate(app, db)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    # app.run()
    manager.run()
