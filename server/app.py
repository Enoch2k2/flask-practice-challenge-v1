from config import app, api
from models import Post, Comment
from flask_restful import Resource

# create routes here:


if __name__ == "__main__":
  app.run(port=5555, debug=True)