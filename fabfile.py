# encoding: utf-8

# fabfile format v3.0
from generix.deployment.base_fabfile import *
from generix.deployment.utils import extend_module_with_instance_methods

from fabconfig import CONFIG_MAP

# Example usages:
#
# First time run:
# fab <<env>> install
#
# To update:
# fab <<env>> deploy


def _update_config(project_name, instance_name, server):
    """
    Update server settings
    :param project_name: Project instance name. One of defined key from config_map.
    :param instance_name: server instance name e.g. stage, stage2, stage3, prod, local
    :param server: which server or group of servers to use e.g. `fab prod:santa_unchained,extra install`
    """
    config = CONFIG_MAP[project_name][instance_name]()
    env.update(config.env)
    if server:
        try:
            env.hosts = getattr(env, "hosts", [])[int(server) - 1]
        except (ValueError, IndexError):
            env.hosts = env.roledefs[server]


def stage(project_name="santa_unchained", server=None):
    """
    Use stage1 server settings
    :param project_name: Project instance name. One of defined key from CONFIG_MAP.
    :param server: which server or group of servers to use e.g. `fab prod:santa_unchained,extra install`
    """
    _update_config(project_name=project_name, server=server, instance_name="stage")


def prod(project_name="santa_unchained", server=None):
    """
    Use production server settings
    :param project_name: Project instance name. One of defined key from CONFIG_MAP.
    :param server: which server or group of servers to use e.g. `fab prod:santa_unchained,extra install`
    """
    _update_config(project_name=project_name, server=server, instance_name="prod")


def localhost(project_name="santa_unchained", server=None):
    print((yellow("Localhost")))

    _update_config(project_name=project_name, server=server, instance_name="local")
    virtualenv_activate()


instance = WithExtraDeployment(localhost=localhost)

# trick that allows using class-based fabric scripts
# note possible ways to reuse fabric methods:
#
# 1) inherit from base class, override
# 2) write a wrapper
# 3) after extend_module_with_instance_methods call re-implement fabric task as a function

extend_module_with_instance_methods(__name__, instance)

# override by re-implementing a task
# def base_task1():
#     fab.run("echo 'directly from module'")
