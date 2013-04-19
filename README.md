# Dead Programmers Society Website

## Setting up your system

The below assumes you're using pip and virtualenv, for which [there is a good tutorial](http://dabapps.com/blog/introduction-to-pip-and-virtualenv-python/).

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

First, make sure you're running the latest version of Nikola. Run:

   fab nikola_upgrade

within your virtualenv to upgrade Nikola and any of its dependencies.

To create a new post:

    nikola new_post

and follow the on-screen instructions. The format for post is reStructuredText, for which you can find a [primer](http://sphinx-doc.org/rest.html) and [reference manual](http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html) on the Web.

You can also edit the theme, add photos to the gallery, etc. You can rebuild the Website and check out how it looks on your local computer with:

    nikola build
    nikola serve

After the server starts, navigate to [localhost:8000](http://localhost:8000/) to see what the website looks like.

To commit your changes, type:

    git status

To see what files have changed. Type:

    git add <filename>

to add whatever files were changed and you want committed to git's index. To commit, run:

    git commit

And add an appropriate commit message. Once you're sure all your changes are good, push back to GitHub (this assumes you've setup your machine for working with GitHub):

    git push origin master

More information in the [Nikola Handbook](http://nikola.ralsina.com.ar/handbook.html).

## Deploy

To build & deploy the Website to the Raspberry Pi, run:

    fab razz deploy

To build & deploy the Website to the CS domain, run:

    fab cs deploy

## Todo

 * [GitHub Timeline Widget](https://github.com/jmealo/github-timeline-widget) — JavaScript widget that displays latest GitHub activity
