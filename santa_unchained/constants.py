from django.db import models
from django.utils.translation import gettext_lazy as _


class Role(models.TextChoices):
    SANTA = "Santa", _("Santa")
    ELF = "Elf", _("Elf")
