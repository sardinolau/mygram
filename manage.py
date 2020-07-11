# -*-encoding=UTF-8  -*-

from mygram import app,db
from flask_script import Manager
from mygram.models import User,Image,Comment
import random
manager = Manager(app)

def get_image_url():
    return 'http://images.nowcoder.com/head/'+str(random.randint(0,1000))+'m.png'

@manager.command
def init_dababase():
    db.drop_all()
    db.create_all()
    for i in range(1,100):
        db.session.add(User('User'+str(i),'a'+str(i)))
        for j in range(0,6):
            db.session.add(Image(get_image_url(),i+1))
            for k in range(0,3):
                db.session.add(Comment('this is a comment'+str(k),1+3*i+j,i+1))
    db.session.commit()
    # print(User.query.filter_by(id=5).first())
if __name__ == '__main__':
    manager.run()