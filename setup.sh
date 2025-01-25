#!/bin/bash

# Clear pip cache
pip cache purge

# install dependancies
pip install setuptools

pip install -r requirements.txt

# run the django commands

python manage.py makemigrations

python manage.py migrate 

python manage.py collectstatic

# python manage.py 