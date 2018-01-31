# Expressive
A browser-based app for increasing the precision of your thoughts.

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

# Launching Expressive

Expressive runs as a webserver you access through your browser.

To start the server:

`$ python manage.py runserver 8000`

(Change the last argument to specify a port besides 8000.)

To begin using the app, navigate to: 'localhost:8000' in your browser.
