import argparse
import docker



def exec(pkg_path, pkg_name, env):
    client = docker.from_env()

    client.containers.run(f"spacepowermonkey/mfpkg-{pkg_name}",
        name=f"mfpkg-{pkg_name}",
        volumes=[f"mfpkg-{pkg_name}-report:/report"],
        environment=env
    )
    return


def cli(pkg_path, pkg_name, params):
    parser = argparse.ArgumentParser()
    parser.add_argument("--env", action="append", default=[])
    args = parser.parse_args(params)

    print(f"  run: {pkg_name} using spacepowermonkey/mfpkg-{pkg_name}:latest")
    if len(args.env) > 0:
        print("    ...detected ENV:")
        for entry in args.env:
            print(f"      {entry}")

    exec(pkg_path, pkg_name, args.env)
    print("    ...success!")
    return
