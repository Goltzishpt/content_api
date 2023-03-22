import datetime
from app import Base, Session
from app.loader import app
from sqlalchemy import DateTime, Column, Integer, String, ForeignKey


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    phone = Column(String(30), unique=True, nullable=False)
    login = Column(String(30), unique=True, nullable=False)
    password = Column(String(64), nullable=False)

    def __repr__(self):
        return "<%s(name='%s', phone='%s', login='%s', password='%s')>" \
            % (self.__class__.__qualname__, self.name, self.phone, self.login, self.password)

    def save(self):
        with Session() as s:
            s.add(self)


class Post(Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True)
    title = Column(String(80), nullable=False)
    text = Column(String(512), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)

    def __repr__(self):
        return "<%s(title='%s', text='%s', user_id='%s', created_at='%s'" \
            % (self.__class__.__qualname__, self.title, self.text, self.user_id, self.created_at)

    def save(self):
        with Session.begin() as s:
            s.add(self)

    def update_post(self, title, text):
        with Session.begin() as s:
            post = s.query(Post).filter(Post.id == self.id).first()
            if title:
                post.title = title
            if text:
                post.text = text
            s.commit()

    def delete(self):
        with Session.begin() as s:
            post = s.query(Post).filter(Post.id == self.id).first()
            s.delete(post)
            s.commit()

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'text': self.text,
            'user_id': self.user_id,
            'created_at': self.created_at.timestamp()
        }


with Session() as s:
    User.objects = s.query(User)
    Post.objects = s.query(Post)
