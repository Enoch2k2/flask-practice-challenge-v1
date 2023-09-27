# Flask Live Code Practice Challenge

Use this practice project to help sharpen your skills for the phase 4 live code!

### Instructions

* If you don't have `python version 3.9.2`, you may have to install with `pyenv install 3.9.2`.
* Install the dependencies with `pipenv install`. Then go into `pipenv shell`.
* cd into `server`. From there you can run the server with `python app.py`

### Project Structure

You will have two models:

Post:
* has a title
* has content
* has an author
* has many comments

Comment:
* has content
* has a commenter
* belongs to post

### Challenge 1

Create a `GET` route that goes to `/api/sorted_posts`. This route should return as json all the posts alphabetized by `title`.

### Challenge 2

Create a `GET` route that goes to `/api/posts_by_author/<author_name>`. This route should return as json the post by the author's name. For example: `/api/posts_by_author/sara` would return all post that belong to sara.

### Challenge 3

Create a `GET` route that goes to `/api/search_posts/<title>`. This route should return as json all the posts that include the title. Capitalization shouldn't matter. So if you were to use this route like `/api/search_posts/frog`. It would give back all post that include `frog` in the title.

### Challenge 4

Create a `GET` route that goes to `/api/posts_ordered_by_comments`. This route should return as json the posts ordered by how many comments the post contains in descendeding order. So the post with the most comments would show first all the way to the post with the least showing last.

### Challenge 5

Create a `GET` route that goes to `/api/most_popular_commenter`. This route should return as json a dictionary like `{ commenter: "Bob" }` of the commenter that's made the most comments. Since commenter isn't a model, think of how you can count the comments that has the same commenter name.

### Note
For these challenges, you will create all of the routes in the `app.py` file. Look for the comment `# create routes here:` to know where you will place your code.