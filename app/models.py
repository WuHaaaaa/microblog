from datetime import datetime
from app import db


class User(db.Model):
    # User类继承自db.Model基类
    # db.Column()传入字段类型，字段可索引（对数据检索很重要），字段唯一
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    # 这不是实际的数据库字段，而是用户和其动态关系的高级师徒，因此它不在表中
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        """
        repr 用于调试的时候，打印用户实例，表示操作成功
        >>> from app.models import User
        >>> u = User(username='susan',email='susan@example.com')
        >>> u
        <User susan>
        """
        return "<User {}>".format(self.username)


class Post(db.Model):
    """
    用户发表状态
    """
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    # 默认一个用户发表状态的时间，utcnow表示函数本身，而不是其返回值
    # 在服务器中使用当前时间，可以根据用户所在位置获取当前时间
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    
    # 设置外键，引用user表的主键，
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return "<Post {}>".format(self.body)

        
