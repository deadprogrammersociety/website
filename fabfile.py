#!/usr/bin/env python

from fabric.api import env, sudo, local
from fabric.operations import put, run
from fabric.context_managers import cd

def nikola_build():
    local('nikola build')

def server():
    env.hosts = ['razz.hotnudiegirls.com']

def deploy():
    nikola_build()
    put('output/*', '/var/www/', use_sudo=True)

def clean():
    # This is probably a terrible idea...
    local('rm -rf cache output')
