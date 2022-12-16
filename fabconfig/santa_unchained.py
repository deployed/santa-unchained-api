from fabconfig.base import BaseConfig as DefaultConfig


class BaseConfig(DefaultConfig):
    def __init__(self):
        super(BaseConfig, self).__init__()
        self.env.project_name = "santa_unchained"


class StageConfig(BaseConfig):
    def __init__(self):
        super().__init__()
        self.env.envname = "stage"
        self.env.settings = "santa_unchained.settings.production"
        self.env.hosts = ["santa_unchained_stage@stage9.deployed.space:2222"]
        self.env.vhost = "santa_unchained.deployed.space"
        self.env.requirements_file = "requirements/prod.txt"
        self.env.skip_dbbackup = True
        self.init_roles()
        self.env.roledefs["worker"] = []
        self.env.roledefs["extra"] = []
