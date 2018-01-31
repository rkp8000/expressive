# Expressive
Browser-based app for increasing the precision of your thoughts.

# Installation

Download Expressive into the directory of your choice:

`$ git clone https://github.com/rkp8000/expressive`

Enter directory and install requirements:

`$ cd expressive`
`$ pip install -r requirements.txt`

Initialize Lexicon database:

`$ python manage.py makemigrations lexicon`
`$ python manage.py migrate`

Create superuser:

`$ python manage.py createsuperuser`

Start server:

`$ python manage.py runserver 8000`

(Change the last argument to specify a port besides 8000.)

In your browser, navigate to: 'localhost:8000'.
