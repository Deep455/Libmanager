# PROJECT NAME : Lib Manager





#### NOTE : THE PROJECT WAS BUILT ENTIRELY ON LINUX , SO RUNNING IN LINUX IS ESSENTIAL


#### ADMIN USER PASSWORD
you may be prompted to set the user id and password , still following are userID and Password used by us,
``UserID : admin``
``Password : 1234``

## CONTENTS
Our project requires Django to run.
The preferred OS is Linux , where frontend was developed .
Some parts of the pages are coded with respect to resolution of Chrome in linux , and may cause some distortion in Windows.
THe project consists of following:
Library_project folder : its the main folder and contains main files required as listed below:
 settings.py
urls.py
wsgi.py
asgi.py

##### Libmanager : Its the folder for our main application.Due to simplicity of our project we have only one application , it contains following files/folders:
Static: it contains all the images and stylesheets required for the project.
Migrations folder : contains the migrations applied to the database design.
Templates: contains all the HTML pages of the project.
Pyhton files: the usual required files for running this application.


## STARTING THE PROJECT:

Database name : mylibdatabase
configure the following code according to your settings, its in settings.py.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mylibdatabase',
        'USER' : 'root',
        'PASSWORD' : '12345678',
        'PORT' : '3306',
        'HOST' : '127.0.0.1',
    }
}




.
Start the project with ``python manage.py runserver``.








