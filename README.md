## Table of contents
* [General info](#general-info)
* [Setup](#setup)
* [How it works](#how-it-works)

## General info
This project is a web app that helps restaurant workers to handle orders. 
	
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
Firstly u need to register as restaurator or driver
*restaurator can add order and track delivery status
*driver can take multiple orders and navigate to them 
