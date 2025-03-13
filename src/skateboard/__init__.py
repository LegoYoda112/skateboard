from os.path import dirname, join as joinpath
WEB_DIR = joinpath(dirname(__file__), 'web')

from .skateboard import Skateboard
import skateboard.objects as objects
__all__ = ["Skateboard"]
objects = objects # TODO: Is this bad?