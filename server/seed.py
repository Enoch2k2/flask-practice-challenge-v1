from config import app
from models import *

with app.app_context():
  # delete all first
  Comment.query.delete()
  Post.query.delete()

  post_1 = Post(title="The frog ended up not being a prince", author="Princess Joanna", content="It took weeks to recover")
  post_2 = Post(title="I once stepped on a lego", author="Randy", content="It hurt really bad")
  post_3 = Post(title="I have a puppy named Toby", author="Carla", content="After 2 years he still thinks he's a puppy!")

  db.session.add_all([post_1, post_2, post_3])
  db.session.commit()

  post_1_comment_1 = Comment(commenter="Sam", post_id=post_1.id, content="Gross!")
  post_1_comment_2 = Comment(commenter="Sara", post_id=post_1.id, content="So sorry to hear! That happened to me too!")
  post_1_comment_3 = Comment(commenter="Frank", post_id=post_1.id, content="Maybe it was the frog next to that frog??? Try again??")

  db.session.add_all([post_1_comment_1, post_1_comment_2, post_1_comment_3])
  db.session.commit()

  post_2_comment_1 = Comment(commenter="Sam", post_id=post_2.id, content="I step on legos all the time!")
  post_2_comment_2 = Comment(commenter="Frank", post_id=post_2.id, content="My son leaves legos all over the floor. I step on them on purpose because if I'm going down, it's going to be on my terms!")

  db.session.add_all([post_2_comment_1, post_2_comment_2])
  db.session.commit()

  post_3_comment_1 = Comment(commenter="Sara", post_id=post_3.id, content="Cute Dog!")
  post_3_comment_2 = Comment(commenter="Sara", post_id=post_3.id, content="Reminds me of Yodi")

  db.session.add_all([post_3_comment_1, post_3_comment_2])
  db.session.commit()