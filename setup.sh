#!/bin/bash

# Clear pip cache
pip cache purge

# install dependancies
pip install setuptools

pip install -r requirements.txt

#seed resume data into the db 
python manage.py seed_real_resume_data

# run the django commands

python manage.py makemigrations

python manage.py migrate 

python manage.py collectstatic

# python manage.py 