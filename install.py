import docker



def exec(pkg_path, pkg_name):
    client = docker.from_env()
    client.images.build(
        path=pkg_path,
        tag=f"spacepowermonkey/mfpkg-{pkg_name}:latest"
    )

    return


def cli(pkg_path, pkg_name, params):
    # Any further params parsing for this command.
    print(f"  install: {pkg_name} from {pkg_path}")
    exec(pkg_path, pkg_name)
    print("    ...success!")
    return
