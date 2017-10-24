from fabric.api import *

@task
def deploy():
    run("echo 'deployed!'")
