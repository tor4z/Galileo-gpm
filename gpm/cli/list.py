from gpm.cli import CLI
from gpm.utils.package import PackageOpration
from gpm.utils.console import puts


class CLIList(CLI):
    _OPTS    = {"shortcut": "h", "name": ["help"], "action": ["_help"], "default": "_list"}
    __doc__ = """

    """

    def _list(self, *args, **kwargs):
        po = PackageOpration()
        po.list()

    def _help(self, *args, **kwargs):
        puts(self.__doc__)


_MOD = CLIList