import argparse
import os

from . import clean
from . import install
from . import newpkg
from . import publish
from . import run



CMD_MAP = {
    "clean": clean,
    "install": install,
    "new": newpkg,
    "publish": publish,
    "run": run,
}


def main():
    parser = argparse.ArgumentParser(
        prog="MonkeyFusion",
        description="Create and manage report packages.",
        epilog="For more - https://www.github.com/spacepowermonkey/monkeyfusion/"
    )

    parser.add_argument("command")
    parser.add_argument("pkg_name")
    parser.add_argument("--path",
        required=False, default=os.getcwd()
    )
    parser.add_argument("cmd_params", nargs=argparse.REMAINDER)

    args = parser.parse_args()

    print("MONKEY FUSION:")
    CMD_MAP[args.command].cli(f"{args.path}/mfpkg-{args.pkg_name}", args.pkg_name, args.cmd_params)
    return
