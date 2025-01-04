### SETUP ###

##Create ENV 
 py -m venv pyenv  (pyenv env name)

## Activate ENV
 pyenv\Scripts\activate.bat 

## Intall django
pip install django

## Create Project
 django-admin startproject mydjango

## Create APP
 CD mydjango
 django-admin startproject service_um

### create requirement
 py freeze > requirements.txt

## Run Project
 CD mydjango
 python manage.py runserver

## front End setup
CREATE Dir on root for Front End 
mkdir react-frontend

Init npm
cd react-frontend
npm init -y  
 



### DOCKER ###
docker-compose up --build  (Rebuild and start the services)

docker-compose down  (Stop any running containers:)


