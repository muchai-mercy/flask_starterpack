from thermos import app, db
from flask.ext.script import Manager, prompt_bool

manager=Manager(app)

@manager.command
def initdb():
  db.create_all()
  print ('Database initialised!')

@manager.command
def dropdb():
  if prompt_bool(
    'Are you sure you want lose all your data?'):
    db.drop_all()
    print ('Database has been dropped!')

if __name__ == '__main__':
  manager.run()


  