from gpm.cli import CLI
from gpm.utils.package import PackageOpration
from gpm.utils.console import puts


class CLIRemove(CLI):
    _OPTS    = {"shortcut": "hy", "name": ["help", "confirm"], "action": ["_help", None], "default": "_remove"}
    __doc__ = """

    """

    def _remove(self, *args, **kwargs):
        po = PackageOpration()
        target = args[0]        #TODO Upadte
        conf = po.find(target)
        po.remove(conf)

    def _help(self, *args, **kwargs):
        puts(self.__doc__)


_MOD = CLIRemove