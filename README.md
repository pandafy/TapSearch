# TapSearch

TapSearch is a minimalist search engine which indexes words from a document(paragraph). 
TapSearch is currently hosted on Heroku - [TapSearch](https://secret-sea-43815.herokuapp.com/)

### Technology Stack for Production
 - Python3
 - Django Rest Framework
 - NLTK
 - PostgreSQL

### Setting up development environment
Clone project repository

    $ git clone https://github.com/TheOneAboveAllTitan/TapSearch.git

Change working directory to project folder

    $ cd TapSearch

Create a python virtual environment

    $ python3 -m venv ./venv

Activate virtual environment 
On Linux 

    $ source venv/bin/activate 
On Windows

    $ venv\Scripts\activate.bat 

Heroku deployment uses PostgreSQL database. You can setup us PostgreSQL on your local machine or use SQLite as a database.

If you choose to use PostgreSQL as your database, uncomment following code change Databases prameters in `tapsearch/settings.py` accordingly.

    if DEBUG:
		DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.postgresql',
			'NAME': 'tapsearch', #Create a database named tapsearch
			'USER': 'demo',	#PostgreSQL username
			'PASSWORD': 'demo', #PostgreSQL password
			'HOST': 'localhost'
			}
		}	
For accessibility, SQLite has been setup as default database engine to quicking spinup the project in development. But it is highly recommended to use PostgreSQL for better performance.

Create database tables through migration

    $ python manage.py migrate

Run the application server

    $ python manage.py runserver

Visit [127.0.0.1:8000](127.0.0.1:8000) on your browser to view TapSearch.

## API Documentation

- Add 
	- Endpoint : [https://secret-sea-43815.herokuapp.com/api/](https://secret-sea-43815.herokuapp.com/api/)
	- GET : Returns all indexed documents
	- POST : Add new text for indexing
		- Request Format: `{"text": "Text to be indexed"}`
- Search
	- Endpoint : [https://secret-sea-43815.herokuapp.com/api/search](https://secret-sea-43815.herokuapp.com/api/search)
	- GET : Returns distinct indexed words
	- POST : Returns top 10 documents containing that word
		- Request Format : `{ "word" :  "seachedWord" }`
- Clear
	- Endpoint : [https://secret-sea-43815.herokuapp.com/api/clear](https://secret-sea-43815.herokuapp.com/api/clear)
	- GET : Clears all indexing and returns a confirmation message for clearing.


