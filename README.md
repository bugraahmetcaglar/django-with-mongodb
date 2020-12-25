# Django-With-Mongodb
Django Rest Framework and Mongodb Integration
This project explains how to connect python django framework and mongodb. In the project, users log into the system through Json Web Token. First of all, you should create a virtual environment and you should install libraries via:
```
pip install -r requirements.txt
```
You can install the necessary libraries by doing.


If Debug = True in djangowithmongo / settings.py, the database in the dev environment is active, and if False, the database in the prod environment is active. You can update your own mongodb information from DATABASE in this file (settings.py). After updating 
you can create your database.
```
python manage.py makemigrations
```
```
python manage.py migrate
```
