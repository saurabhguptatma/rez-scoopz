name = "scoopz"
version = "2020.11.26.0"
requires = ["python-2.7+,<4"]

# Each version of Scoop of heavily coupled with whatever its
# repository of available packages look like at the time. It
# is an informal relationship, enforced by Scoop's automatic
# update mechanism.
_buckets = {
    "main": (
        "https://github.com/ScoopInstaller/Main/archive/b8d2cd70ee83897fb1091212f2e32cc3f12823c7.zip"
    ),
    "versions": (
        "https://github.com/ScoopInstaller/Versions/archive/329b4687451fd252b1030a8233a84844fc728397.zip"
    )
}

build_command = "python {root}/install.py %s" % version
build_command += " --overwrite"
build_command += " --bucket %s" % _buckets["main"]
build_command += " --bucket %s" % _buckets["versions"]

variants = [
    ["platform-windows", "arch-AMD64"]
]


def commands():
    global env
    global alias

    env.PATH.prepend("{root}/home/apps/scoop/current/bin")  # Expose scoop.ps1
    env.PYTHONPATH.prepend("{root}/python")

    alias("install", "python -u -m scoopz")

    env.SCOOP = "{root}/home"
    env.SCOOP_HOME = "{root}/home"
