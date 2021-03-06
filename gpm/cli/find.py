from gpm.cli import CLI
from gpm.utils.package import PackageOpration
from gpm.utils.console import puts


class CLIFind(CLI):
    _OPTS    = {"shortcut": "h", "name": ["help"], "action": ["_help"], "default": "_find"}
    __doc__ = """
        GPM find
Find installed gpm packages
Usage:
    gpm find [package-name]
Options:
    -h, --help  Show gpm find manual
    """

    def _find(self, *args, **kwargs):
        po = PackageOpration()
        if args:
            po.find(args[0], show=True)
        else:
            po.list()

    @classmethod
    def _help(cls, *args, **kwargs):
        puts(cls.__doc__)


_MOD = CLIFind