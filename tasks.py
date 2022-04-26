import platform
from invoke import task


def get_os_name():
    os_name = platform.system()
    return os_name


@task
def build(c, mode='dev'):

    if get_os_name() == 'Windows':
        if(mode == 'prod'):
            c.run('echo Docker to prod')
            c.run('docker-compose -f production.yml build')
        else:
            c.run('echo Docker to dev')
            c.run('docker-compose -f local.yml build')

    else:
        if(mode == 'prod'):
            c.run('echo Docker to prod')
            c.run('sudo docker-compose -f production.yml build')
        else:
            c.run('echo Docker to dev')
            c.run('sudo docker-compose -f local.yml build')


@task
def upApp(c, mode='dev'):
    if get_os_name() == 'Windows':
        if(mode == 'prod'):
            c.run('echo Up APP to prod')
            c.run('docker-compose -f production.yml up')
        else:
            c.run('echo Up APP to dev')
            c.run('docker-compose -f local.yml up')
    else:
        if(mode == 'prod'):
            c.run('echo Up APP to prod')
            c.run('sudo docker-compose -f production.yml up')
        else:
            c.run('echo Up APP to dev')
            c.run('sudo docker-compose -f local.yml up')
