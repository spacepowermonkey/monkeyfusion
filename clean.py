import docker
import os
import shutil



def exec(pkg_path, pkg_name):
    # Remove volume; remove container.
    client = docker.from_env()

    try:
        container = client.containers.get(f"mfpkg-{pkg_name}")
        container.remove()
    except docker.errors.NotFound:
        pass

    try:
        volume = client.volumes.get(f"mfpkg-{pkg_name}-report")
        volume.remove()
    except docker.errors.NotFound:
        pass
    
    # Remove old report.
    report_path = f"{pkg_path}/report"
    
    shutil.rmtree(report_path)
    os.makedirs(report_path, exist_ok=True)
    return


def cli(pkg_path, pkg_name, params):
    # Any further params parsing for this command.
    print(f"  remove: {pkg_name} artifacts")
    exec(pkg_path, pkg_name)
    print("    ...success!")
    return
