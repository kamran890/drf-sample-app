Django Application REST API (using django-rest-framework)

* User Signup
* API to list/retrieve/create/update a Post having fields id, title, body, status, author and created_on (and any other field you deem fit), where status can be draft, unpublished or published.
** Create is only allowed for logged in users, Update is only allowed by the author of the post.
** List API should only return id, title, status and created_on sorted by created_on. It should support filter to return post authored by authenticated API user only.
** List API should return draft and unpublished post ONLY to the author of the respective posts.
** If a Post is published, it can be retrieved by any user. It should log the count of retrieves against each published post by non-authors to keep a track of post views.

# Instructions for Ubuntu

* Update Software Repositories

`sudo apt-get update`

* Uninstall Old Versions of Docker

`sudo apt-get remove docker docker-engine docker.io`

* Install Docker

`sudo apt install docker.io`

* Start and Automate Docker

`sudo systemctl start docker`

`sudo systemctl enable docker`

* Install Docker Compose

`sudo apt install docker-compose`

* Start and Automate Docker Compose

`sudo systemctl start docker`

`sudo systemctl enable docker`

* Clone drf-sample-app

`git clone https://github.com/kamran890/drf-sample-app.git`

* Go to drf-sample-app directory

`cd drf-sample-app`

* Run the command to build and run image

`docker-compose up`

* Run the command to build and run image in detached mode

`docker-compose up -d`

* Database migration

`docker-compose exec app python3 /code/manage.py makemigrations`

`docker-compose exec app python3 /code/manage.py migrate`

* Create Super User

`docker-compose exec app python3 /code/manage.py createsuperuser`

Provide username and password for superuser as per instructions. 

Application will be available on http://localhost

# URL's

* Django REST Framework API's

`http://localhost/api`

* Swagger API's

`http://localhost/swagger`


* API Documenation

`http://localhost/redoc`

* Admin Panel

`http://localhost/admin`

* Registration of front-end application for accessing API's

`http://localhost/o/applications`

Click on the link to create a new application and fill the form with the following data:

    Name: just a name of your choice
    Client Type: confidential
    Authorization Grant Type: Resource owner password-based

Save your app! 

* Get Access Token

`curl -X POST -d "grant_type=password&username=<user_name>&password=<password>" -u"<client_id>:<client_secret>" http://localhost/o/token/`

The user_name and password are the credential of the users registered in your Authorization Server, like any user created in Step 2. Response should be something like:

`{
    "access_token": "<your_access_token>",
    "token_type": "Bearer",
    "expires_in": 36000,
    "refresh_token": "<your_refresh_token>",
    "scope": "read write groups"
}`


* Grab your access_token and start using OAuth2 API:

`curl -H "Authorization: Bearer <your_access_token>" http://localhost/api/post/`


