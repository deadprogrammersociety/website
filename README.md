# Dead Programmers Society Website

## Setting up your system

On Ubuntu, install some packages:

    sudo aptitude install fabric python-virtualenv python-pip libxslt1-dev libxml2-dev git

If anything is missing from the above, please add it!

Check out the code from Github:

    git clone git@github.com:deadprogrammersociety/website.git

(This assumes you've SSH keys, etc setup w/ GitHub already). Next, enter the directory and setup a virtualenv:

    cd website
    virtualenv venv

Activate the virtualenv, and install dependencies:

    source venv/bin/activate
    pip install -r requirements.txt

It will take a few minutes for the dependencies to download and install.

## Adding posts, etc

Activate the virtualenv:

    source venv/bin/activate

and run:

    nikola new_post

and follow the on-screen instructions. You can also edit the theme, add photos to the gallery, etc. You can rebuild the Website and check out how it looks on your local computer with:

    nikola build
    nikola serve

After the server starts, navigate to http://localhost:8000/

## Deploy

To build & deploy the Website to the Raspberry Pi, run:

    fab razz deploy

To build & deploy the Website to the CS domain, run:

    fab cs deploy
