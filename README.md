# Django For Everyone
A course on django by Dr. Chucks - [dj4e](https://dj4e.com)

* Understanding the various high level overview of the components of Django.
    * views
    * templates
    * URL configuration
    * Models
* Setting up a django project and creating an app in a project.
* Directing urls to views.
* Use of Django ORM to create models, perform CRUD actions, and perform Databse migrations.
* Use of Views and Templates.
* Understanding and use of Django Class-based views.
* Right techniques of dealing with forms and form data in Django.
* Handling of cookies and session data.
* Database design (one-to-many models, many-to-many models, database normalization - 3NF)
* Preloading of data into the database using the `django_extensions` library.



## Setting up environment

Clone project folder

`git clone https://github.com/EkpoEsua/Django-For-Everyone`

Change working directory to the folder

`cd Django-For-Everyone/`

Create python virtual environment

`python3 -m venv venv`

Activate virtual environment

`source venv/bin/activate`

Install project dependencies

`pip install -r requirements.txt`

Change working directory to project folder

`cd mysite/`

Perform database migrations

`python manage.py makemigrations`
`python manage.py migrate`

Run the server
`python manage.py runserver`

Open the project site on a broswer [http://127.0.0.1:8000](http://127.0.0.1:8000)