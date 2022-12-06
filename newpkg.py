import argparse
import json
import os
import shutil
import subprocess



TEMPLATE_ROOT = f"{os.path.dirname(os.path.realpath(__file__))}/templates"



def exec(pkg_path, pkg_name, config):
    os.makedirs(name=pkg_path, exist_ok=True)
    subprocess.call([
        "git", "init", pkg_path
    ])
    
    shutil.copytree(f"{TEMPLATE_ROOT}/package", pkg_path, dirs_exist_ok=True)
    
    _prev_cwd = os.getcwd()
    os.chdir(pkg_path)
    subprocess.call([
        "git", "add", "--all",
    ])
    subprocess.call([
        "git", "commit", "-m", f"New package [{pkg_name}] created via Monkey Fusion CLI."
    ])
    os.chdir(_prev_cwd)

    with open(f"{pkg_path}/conf.json", 'w') as outfile:
        json.dump(config, outfile)

    return


def cli(pkg_path, pkg_name, params):
    # Any further params parsing for this command.  
    print(f"  create: {pkg_name} at {pkg_path}")
    exec(pkg_path, pkg_name, {})
    print("    ...success!")
    return
