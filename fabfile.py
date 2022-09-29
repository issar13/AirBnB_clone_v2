from fabric.api import *
env.user = 'ubuntu'
env.hosts = ['44.210.103.220' ,'35.168.59.18']


def hello():
    target = run('ls -t ./AirBnB_Clone_V2/versions/')
    print(target.split())
