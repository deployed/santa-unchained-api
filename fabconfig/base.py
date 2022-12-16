import os

from fabric.utils import _AttributeDict


class BaseConfig:
    def __init__(self) -> None:
        self.env = _AttributeDict()

        self.env.git_server = "git@gitlab.deployed.pl"
        self.env.git_repo = "spooler/spooler-service.git"
        self.env.git_branch = "master"

        self.env.project_dir = "santa-unchained-api"
        self.env.project_name = "santa_unchained"

        self.env.path = f"{self.env.project_dir}"
        self.env.use_ssh_config = True
        self.env.forward_agent = True
        self.env.envname = "example"
        self.env.pip_version = "22.2.2"
        self.env.virtualenv_path = "~/venv"
        self.env.virtualenv_args = "--python=python3.10"
        self.env.pip_args = ""
        self.env.project_path = self.env.project_name
        self.env.requirements_file = "requirements/base.txt"
        self.env.skip_rebuild_index_on_deploy = True
        self.env.asyncworker = "celery"
        self.env.warn_when_fixtures_fail = True
        self.env.fixtures_format = "yaml"

        self.collectstatic_excluded = ["*.scss", "*.md", "*.less", "demo", "src"]

        self.env.excluded_files = self.get_excluded_files()

    def init_roles(self) -> None:
        """by default all hosts have all roles"""
        self.env.roledefs = {
            "webserver": self.env.hosts,
            "worker": self.env.hosts,
            "extra": self.env.hosts,
        }

    def get_excluded_files(self) -> str:
        return " ".join("--ignore=%s" % rule for rule in self.collectstatic_excluded)


class LocalhostConfig(BaseConfig):
    def __init__(self) -> None:
        super(LocalhostConfig, self).__init__()
        self.env.hosts = ["localhost"]
        self.env.envname = "local"
        self.env["virtualenv_path"] = os.environ.get("VIRTUAL_ENV")
        self.init_roles()
        if not self.env["virtualenv_path"]:
            print("Make sure your virtualenv is activated (with VIRTUAL_ENV set)")
