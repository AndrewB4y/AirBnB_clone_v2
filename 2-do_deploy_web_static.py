#!/usr/bin/python3

""" pack_web_static module """

from fabric.api import run, put, env
from datetime import datetime
import os

env.hosts = ['34.75.228.249', '35.231.205.149']


def do_deploy(archive_path):
    """ do_deploy function
    Distributes an archive to your web servers
    """
    if archive_path is None or os.path.isfile(archive_path) is False:
        return False

    try:
        a_name = archive_path.split('/')[-1]
        put('{}'.format(archive_path, '/tmp/{}'.format(a_name)))
        name_target =  a_name.split('.')[0]
        full_target = "/data/web_static/releases/{}".format(name_target)
        run('mkdir -p {}'.format(full_target))
        run("tar -xzf /tmp/{} -C {}".format(a_name, full_target))
        run('rm /tmp/{}')
        run('mv {}/web_static/* {}/'.format(full_target,full_target))
        run('rm -Rf {}/web_static'.format(full_target))
        run('rm -Rf /data/web_static/current')
        run('ln -s {} /data/web_static/current')
        return True
    except:
        return False
