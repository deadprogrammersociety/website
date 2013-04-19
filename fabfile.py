#!/usr/bin/env python

from fabric.api import env, sudo, local
from fabric.operations import put, run
from fabric.context_managers import cd

from fabric.colors import *

def nikola_upgrade():
    print(red("You're running within a virtualenv, right? Please cancel this immediately if you're not!"))
    local('pip install --upgrade nikola')

def nikola_build():
    local('nikola build')

def cs():
    print(red('Not implemented yet'))

def serve():
    print(red('The "serve" target is deprecated; please use razz instead'))
    razz()

def razz():
    env.hosts = ['razz.hotnudiegirls.com']

def deploy():
    nikola_build()
    put('output/*', '/var/www/', use_sudo=True)

def clean():
    # This is probably a terrible idea...
    local('rm -rf cache output')
