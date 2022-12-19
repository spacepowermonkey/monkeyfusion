import docker
import io
import tarfile



def exec(pkg_path, pkg_name):
    client = docker.from_env()

    container = client.containers.get(f"mfpkg-{pkg_name}")
    report_stream, _ = container.get_archive('/docs')
    report_tar = bytearray()
    for chunk in report_stream:
        report_tar += chunk
    
    with tarfile.open(fileobj=io.BytesIO(report_tar), mode='r') as tar:
        tar.extractall(f"{pkg_path}")
    
    return


def cli(pkg_path, pkg_name, params):
    # Any further params parsing for this command.
    print(f"  publish: {pkg_name} results to {pkg_path}/docs")
    exec(pkg_path, pkg_name)
    print("    ...success!")
    return
