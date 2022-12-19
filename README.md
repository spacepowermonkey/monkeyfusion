# MonkeyFusion

This is a CLI tool for working with packages that collect, analyze, and report data.



## Commands
These commands allow you to interact with packages.

### Clean
This command does three things:
1. remove old copies of the installed container
1. remove old copies of the storage volume
1. remove old the contents of `/docs` in a package

WARNING: This command is highly destructive!

Example:

```
python -m monkeyfusion clean <pkg name>
```

### Install
This command builds the docker image of the package locally.

Example:

```
python -m monkeyfusion install <pkg name>
```

### New Package

### Publish
This command extracts the most recent version of the package output to the `/docs` folder, for publishing.

Example:

```
python -m monkeyfusion publish <pkg name>
```

### Run
This command runs the most recent version of the docker container, built locally. Additionally, you can pass environment variables to your container.

Example:

```
python -m monkeyfusion run <pkg name>
```

Example:

```
python -m monkeyfusion run <pkg name> --env <KEY1>=<val1> --env <KEY2>=<val2> ...
```
