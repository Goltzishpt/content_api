# API

This project is a simple social media platform where users can create, read, update, and delete posts. Users can also register, log in, and log out.

## Getting Started
To run this project, you need to have Python 3.x and pip installed on your machine.

- Clone the repository: git clone https://github.com/Goltzishpt/content_api
Navigate to the project directory:
``` bash Copy code
cd content_api
```

- Install the required dependencies:
``` Copy code
pip install -r requirements.txt
```
- Set the environment variables by creating a .env file in the project's root directory:
makefile
```Copy code
SECRET_KEY=<your-secret-key>
REDIS_HOST=<redis-host>
REDIS_PORT=<redis-port>
REDIS_DB=<redis-db>
```
## Running the Application
To run the application, execute the following command in the project's root directory:

``` arduino Copy code
python main.py
```
This will start the Flask development server. You can access the application at http://localhost:5000/.

### Files
``` app/init.py
This file initializes the Flask application.
```

app/config.py
This file contains the configuration variables for the Flask application.

app/handlers/auth.py
This file contains the functions for user authentication.

app/handlers/post.py
This file contains the functions for post creation, retrieval, update, and deletion.

app/loader.py
This file creates and returns the Flask application instance.

app/sessions.py
This file contains the functions for managing user sessions using Redis and JSON Web Tokens (JWT).

app/routes.py
This file maps the URLs to the corresponding views (functions) for handling requests.

Usage
Registration
To register a new user, send a POST request to /registration with the following JSON data:

json
Copy code
{
    "username": "your-username",
    "password": "your-password"
}
Login
To log in, send a POST request to /login with the following JSON data:

json
Copy code
{
    "username": "your-username",
    "password": "your-password"
}
If the credentials are valid, the response will contain a JSON Web Token (JWT) that should be used to authenticate the user in subsequent requests.

Logout
To log out, send a POST request to /logout with the JWT in the Authorization header:

makefile
Copy code
Authorization: Bearer <jwt>
Create a Post
To create a new post, send a POST request to /post with the following JSON data:

json
Copy code
{
    "title": "post-title",
    "body": "post-body"
}
Include the JWT in the Authorization header to authenticate the user.

Show All Posts
To retrieve all posts, send a GET request to /post.

Show a Post
To retrieve a specific post, send a GET request to /post/<post-id> where <post-id> is the ID of the post.

Update a Post
To update a post, send a PUT request to /post/<post-id> with the following JSON data:

json
Copy code
{
    "title": "updated-post-title",
    "body": "updated-post-body"
}
Include the JWT in the Authorization header to authenticate the user.

Delete a Post
To delete a post, send a DELETE request to /post/<post-id> where <post-id> is the ID of the post.

Include the JWT in the Authorization header to authenticate the user.

Credits
This project was created by your-name.