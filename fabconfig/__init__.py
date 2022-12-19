from fabconfig import santa_unchained
from fabconfig.base import LocalhostConfig

CONFIG_MAP = {
    "santa_unchained": {
        "local": LocalhostConfig,
        "stage": santa_unchained.StageConfig,
    },
}
