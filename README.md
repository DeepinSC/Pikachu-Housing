# Pikachu-Housing
CS411 Project Pikachu-housing Development Guide

## Project introduction


Pikachu Housing is a single page website for house/apartment rentals in Champaign-Urbana, Illinois.The goal of this website is to provide renters better overviews on house rental prices in Champaign-Urbana area, especially for new students.


Our project is a complete LAMP (Linux+Apache+MySQL+PHP) web application. Basic functions contain CRUD, multiple-param query search and python data crawler. Advanced functions are house suggestion and roommate suggestion. (detail in our wiki: https://wiki.illinois.edu/wiki/display/cs411sfa18/Pikachu) 


Tech stack for LAMP: 
- System: AWS EC2
- Server: Nginx
- Database: PostgreSQL
- Backend: Django (python)


## Prepare for development
* Install prerequisite packages: python(2.7), pip, virtualenv, git, postgreSQL, Nodejs(frontend)；
* Download private key - pikachu.pem (provided by the team leader, important：use this key to login AWS)；
* Set private key permission
`chmod 0400 pikachu.pem`
* Open terminal, go to the folder of pikachu.pem，connect the server via ssh: 
` ssh -i "pikachu.pem" ec2-user@ec2-52-14-154-253.us-east-2.compute.amazonaws.com` 

### Start backend on server
* Check if gunicron (wgsi between Django and Nginx) is open: `lsof -i :8000`；
* If process exists，`sudo kill xxx(the pid of the process)`；
* cd /home/Pikachu-Housing，start gunicorn service of wsgi: `gunicorn settings.wsgi:application --bind 0.0.0.0:8000` 
* Open http://www.pikachu-housing.art/ , the project is working if success. If Nginx error appears, it means gunicorn fails to start. 

## Delevopment - Backend
* Finish "Prepare for development" and read the tutorial of Django https://www.djangoproject.com/;
git fork and clone!
`git clone https://github.com/DeepinSC/Pikachu-Housing.git` 
* Activate virtual environment:
`virtualenv venv, source venv/bin/activate`
* Install requirements, execute `pip install -r requirements.txt`;
* Execute `python manage.py migrate`, then `python manage.py runserver 8000`，the Django server starts and connect to the local database；
* Before progamming, `git pull`;
* Do something exciting；
* Pull request if you want to make contribution;

## Delevopment - Frontend
* Finish "Prepare for development" and read the tutorial of Vue: https://vuejs.org/index.html ;
* Finish "Delevopment - Backend", `cd frontend`, execute `npm install`;
* Create some exciting buttons；
* Check layout by `npm run dev`, browsing 127.0.0.1:3000（Use chrome to debug）；
* Before submission，`cd frontend` , execute `npm run build` to pack your code；
* Pull request if you want to make contribution;

## Postgres setting
* /var/lib/pgsql/*/data/pg_hba.conf
* host    all    all    0.0.0.0/0    md5 

