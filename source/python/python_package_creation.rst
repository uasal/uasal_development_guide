Python Package Creation Guide
=============================

Written by Sanchit Sabhlok, Adam Schilperoort, Stephanie Rinaldi and
Patrick Ingraham on 03/02/2025

Making your Python package installable using pip
------------------------------------------------

This guide helps convert a python directory structure into an
installable package algorithmically. This is for people who have never
turned a python package into a pip installation and as such does not go
into the various details and advanced settings/configurations one can
get into. This is a very basic overview of the process. For a slightly
deeper dive, a bit more automation see
`LINCC <https://lincc-ppt.readthedocs.io/en/stable/source/new_project.html>`__
(Caution: May be for intermediate - advanced users).

1. Create your
directory structure. I’ve created one that looks like this -

::

   ├── docs
   ├── notebooks
   │   ├── sample_notebook.ipynb
   ├── pyproject.toml
   ├── README.md 
   ├── src
   │   ├── package_name
   │   │   ├── source_code.py
   │   │   ├── __init__.py
   │   │   ├── packaged_directory
   │   │   │   └── data.csv
   │   │   └── _version.py
   └── tests
       └── test.py

Here, the ``notebooks`` contains jupyter notebooks. The ``src``
directory is important to keep the name of as it makes sure that tests
are run against the installed version of your package rather than the
files in your package working directory, (For more details, `check
here <https://www.pyopensci.org/python-package-guide/package-structure-code/python-package-structure.html#the-src-layout-and-testing>`__).
Lastly, the ``packaged_directory`` directory can be used to contain any
data files required for the package. To ensure the data inside can be
found by python scripts when importing the package, check the
``pyproject.toml`` file setup.

2. Create ``pyproject.toml``. This file contains the metadata that will
   be used to convert the package into an installation and is the only
   file needed to be written in detail. However, a user doesn’t have to
   start from scratch, there are plenty of template files on the
   internet to choose from. One such template is provided here -

::

   [build-system]
   requires = ["setuptools", "setuptools-scm", "wheel"]
   build-backend = "setuptools.build_meta" 

   [project]
   name = "package_name"
   authors = [
   {name = "Aa****", email = "go*****@*****.edu"},
   {name = "Ju****", email = "ja*****@*****.edu"},
   {name = "Je****", email = "ja*****@*****.edu"}
   ]
   maintainers = [
   {name = "Sa****", email = "ss******@arizona.edu"}
   ]
   description = "Sample project description."
   readme = "README.md"
   license = { text = "GNU GENERAL PUBLIC LICENSE - Version 3" }
   requires-python = ">=3.8"
   dependencies = ["astropy"]

   dynamic = ["version"]

   [project.urls]
   Homepage = "https://github.com/uasal/package_name/blob/<branch_name>/README.md"
   Changelog = "https://github.com/uasal/package_name/blob/<branch_name>/CHANGELOG.md"
   Repository = "https://github.com/uasal/package_name"

   [tool.setuptools]
   packages = ["package_name"]
   package-dir = { "" = "src" }
   include-package-data = true

   [tool.setuptools_scm]
   write_to = "src/package_name/_version.py"
   version_scheme = "post-release"
   local_scheme = "node-and-date"

   [tool.pytest.ini_options]
   testpaths = [
   "tests",
   ]

   [tool.coverage.run]
   omit=["src/package_name/_version.py"]

   [tool.setuptools.package-data]
   "package_name" = ["packaged_directory/**/*"]    

Make note of which directories are preceded by ``src``, and which are
NOT. Where they aren’t, the root path is assumed to be the src
directory, automatically handled by the backend build tools.

Project URLs: The Project URLs contain metadata that is `described
here <https://docs.pypi.org/project_metadata/>`__. The links here are
for this specific project, modify them suitably for your project.

Changelog: CHANGELOG.md is autogenerated from GitHub after making a new
release, but perhaps won’t exist if the project doesn’t have any
releases yet Licenses: You can include either text OR a license file if
you’re including a ``LICENSE.md`` in the project’s root directory
Versions: There are strategies to implement a “Git tag” on version
control, effectively stamping each commit as a new “version” which is
something git/pip can automatically handle/update. This is called
“dynamic” version control and that is what is specified by the
``dynamic = ["version"]`` in the ``pyproject.toml`` file. For more
details, you can read a `primer article
here <https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#static-vs-dynamic-metadata>`__.
You can also read about `Semantic Versioning
here <https://semver.org/>`__ (Very short summary - Release versions
should be named MAJOR.MINOR.PATCH).

If excluding this section -

::

   Repository = "https://github.com/uasal/package_name"

   [tool.setuptools]
   packages = ["package_name"]
   package-dir = { "" = "src" }
   include-package-data = true

Setup tools will treat the package structure as ‘flat’ which has some
undesirable behaviour. Check this webpage for a `slightly deeper dive
into the
topic <https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/>`__.
The last line is only needed if including a ``packaged_directory`` kind
of directory which includes package data. This must then be specified
under the ``[tool.setuptools.package-data]`` heading.

3. Add a couple of files to the ``src/package_name/`` directories,
   namely ``__init__.py`` and ``_version.py``. The code inside
   ``__init__.py`` is -

::

   import importlib.metadata
   from pathlib import Path
   __version__ = importlib.metadata.version(__package__)

   def get_data_path():
       package_root = Path(__file__).parent.resolve()
       data_path = package_root / "packaged_directory"
       if not data_path.exists():
           raise FileNotFoundError(f"Support data directory not found: {data_path}")
       return str(data_path) + "/"

   __all__ = ["get_data_path", "__version__"]

The key thing here is the ``__all__`` parameter at the bottom is going
to make any functions inside that dictionary available throughout the
package no matter where you import from.

4. On the machine you want to install the package, first clone the repo
   -

::

   git clone <your_github_repo_link>/<git_repo_name>.git

The usual caveats on how to clone a repo apply. More importantly, the
``branch`` of the repo you clone and are actively working in at the time
of installation will be installed as the package if multiple branches
can be installed. So, for instance to install the package from the
``develop`` branch, after cloning, run -

::

   git checkout develop

And then build -

::

   pip install .

If you are on a different machine and would like to install the package
using pip, but do not wish to keep a permanent clone in your file
system, you can install via, for example

::

   pip install "git+https://github.com/<git_repo_name>.git@<branch_name>"

This automatically specifies the branch to be installed from.

Lastly, while developing the package, you may want to do an “Editable”
installation, which will prevent you from reinstalling the package over
and over while you develop it. To do this, you can instead install using
-

::

   pip install --editable .

or

::

   pip install -e .

You can check here for more details on `the advantages and drawbacks of
an Editable
installation <https://setuptools.pypa.io/en/latest/userguide/development_mode.html>`__
when the package is in active development.

That is about it! You can check your installed package by running

::

   pip list

And this should now show your package in the list of packages installed!

Reinstalling a broken package
-----------------------------

WARNING: The following commands need to be used with caution! It is not
recommended to use ``rm -rf`` regularly and should only be done when the
user understands exactly what the command is going to remove.

If a package is updated and needs to be reinstalled, the following
commands can be run inside the package directory to do a clean reinstall
-

::

   rm -rf build dist *.egg-info
   pip uninstall <config_stp_X>
   pip install --no-cache-dir --force-reinstall .

If you are doing this frequently, you can add the following function to
your ``~/.bashrc`` (or the MacOS equivalent) -

::

   clean_and_reinstall {
   rm -rf build dist *.egg-info;
   pip uninstall $1;
   pip install --no-cache-dir --force-reinstall .
   }

Once you save and source the ``~/.bashrc`` file, you can call this
function from inside the package directory -

::

   clean_and_reinstall <name_of_your_package>

Important note: Make sure to check the ``branch`` you are working on,
since that is the branch that will be installed. You can also add a
print statement to your quick command to check which branch has been
installed.
