from flask import Flask, render_template
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'some_key'

@app.route('/')
def index():
    db_session.global_init(f'db/blogs.db')
    db_sess = db_session.create_session()
    colon = db_sess.query(User).all()
    return render_template('journal.html', title='Журнал работ', colonists=colon)


if __name__ == '__main__':
    app.run()

   # #
   #  user = User()
   #  user.name = "Ridley"
   #  user.surname = 'Scott'
   #  user.position = 'captain'
   #  user.age = 21
   #  user.email = "scott_chief@mars.org"
   #  user.address = 'module_1'
   #  user.hashed_password = '12324421'
   #  db_sess.add(user)
   #
   #  user2 = User()
   #  user2.name = "Ridley2"
   #  user2.surname = 'Scott2'
   #  user2.position = 'captain2'
   #  user2.age = 22
   #  user2.email = "scott_chief2@mars.org"
   #  user2.address = 'module_2'
   #  user2.hashed_password = '123244212'
   #  db_sess.add(user2)
   #
   #  user3 = User()
   #  user3.name = "fgf[gfgf"
   #  user3.surname = 'ахаХаха'
   #  user3.position = '123'
   #  user3.age = 70
   #  user3.email = "coolboy@mars.org"
   #  user3.address = 'module_3'
   #  user3.hashed_password = 'asdadadasda'
   #  db_sess.add(user3)
   #
   #  user4 = User()
   #  user4.name = "АХАХАХАХА"
   #  user4.surname = 'АхпапхАХ'
   #  user4.position = 'Диерктор'
   #  user4.age = 35
   #  user4.email = "idk@mars.org"
   #  user4.address = 'module_4'
   #  user4.hashed_password = 'asdfmovie'
   #  db_sess.add(user4)
   #  db_sess.commit()


