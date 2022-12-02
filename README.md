## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [How it works](#how-it-works)

## General info
This project is a web app that helps restaurant workers to handle orders.

## Technologies
* Python
* Djnago
* HTML
* Bootstrap
* CSS
* Jquery
	
## Setup
To run this project, first install requirements, next set up Database and then run django server:

```
$ pip install -r requirements.txt
$ python manage.py makemigrations posts
$ python manage.py makemigrations users
$ python manage.py migrate
$ python manage.py runserver
```

## How it works?
Firstly u need to register as admin and add your restaurant

* In your terminal paste this line and follow the instructions
```
python manage.py createsuperuser
```

* Go to admin site by clicking `Admin Panel` on main page and log in
* Add Restaurant in 'Restauracjas' tab
* You can also add workers in `Custom Users` tab

Then workers can register and choose their worplace and restaurant or log in if you added them in admin panel
