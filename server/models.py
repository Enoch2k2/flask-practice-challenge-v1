from config import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import ForeignKey

class Post(db.Model, SerializerMixin):
  __tablename__ = "posts"

  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String)
  content = db.Column(db.String)
  author = db.Column(db.String)

  comments = db.relationship("Comment", back_populates="post")

  serialize_rules=("-comments.post",)

  def __repr__(self):
    return f'<Post id={self.id} author={self.author} title={self.title}>'
  

class Comment(db.Model, SerializerMixin):
  __tablename__ = "comments"

  id = db.Column(db.Integer, primary_key=True)
  content = db.Column(db.String)
  commenter = db.Column(db.String)
  post_id = db.Column(db.Integer, ForeignKey("posts.id"))

  post = db.relationship("Post", back_populates="comments")

  serialize_rules=("-post.comments",)

  def __repr__(self):
    return f'<Comment id={self.id} commenter={self.commenter}  content={self.content}>'