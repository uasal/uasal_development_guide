General Development Practices
==============================

We encourage that all code follows some basic principals:
- Assume that one of your colleagues will be using your code in the near future
- Code should be written as stand-alone tools with minimal dependencies
- Tools should be handed a configuration to be used during execution
- Parameters should not be hard-coded
- Configurations, parameters and procedures required to reproduce results should be documented

Coding Standards
----------------

- Avoid hard coding numbers and/or paths wherever possible. If
  unavoidable, define them all as constants in one block at the top of
  the module (as per
  `PEP8 <https://peps.python.org/pep-0008/#constants>`__)
- Avoid re-using/clobbering the same variable names in scripts or
  example notebooks.
- Avoid copy-pasting code wherever possible. Write a function and call
  it again.

Formatting
~~~~~~~~~~

Follow `PEP8 <https://peps.python.org/pep-0008/>`__ whenever possible.
People have spent years developing (and arguing over) it.

Variables should be ``snake_case``. The naming of variables should be
sufficiently long to provide information into the content of the
variable, but not so long as to take a sizable fraction of the line
length. Arrange the variable name to aid in grouping and tab completion
(e.g. ``inst1_config`` and ``inst2_config`` should be ``config_inst1``
and ``config_inst2``)

Autoformatters are your friend: - black - flake8 - ruff

Setting up pre-commit hooks are useful for maintaining readable code and
assisting with evaluating changes in merge requests (called pull
requests in GitHub).

IDEs like VSCode also have plugins that can apply autoformatting on save
(e.g. `ruff plugin for
VSCode <https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff>`__).

Comments
~~~~~~~~

Comments are useful for your future self and also the next person to use
your code. `docstrings <https://peps.python.org/pep-0257/>`__ have been
developed to help with this and can also be automatically parsed to
generate documentation in html format.

Several styles of documenting code are common (e.g. some examples
`here <https://www.geeksforgeeks.org/python/python-docstrings/>`__). For
consistency across UASAL code, we encourage the use of `Numpy
style <https://numpydoc.readthedocs.io/en/latest/format.html>`__.

Tip: You can ask an online AI model to generate comments/docstrings for
your code and double check the results to save time/effort.

Using AI in Content Development.
--------------------------------

AI offers interesting applications to increase coding efficiency and
learn new techniques. It also presents significant security risks if
there is export controlled content on the device. For novice programmers
we recommend that AI is not used to generate code as it can develop poor
habits and/or slow down the learning process. However, AI may be useful
for developing initial docstrings or potential unit tests. In all cases,
the content must be thoroughly reviewed by the programmer. To avoid risk
of unintentional sharing data or copyright issues with responses we
recommend copy/pasting into `duck.ai <https://Duck.ai>`_ where the data is
anonymous and the prompt and output are owned by user.

Note that all AI generated content should be disclosed in the file
containing the content. This includes the AI system that was used. All
content is subject to the copyrights of the AI provider and must be
explicitly followed.

Python Packaging
----------------

Python packages should use a
`pyproject.toml <https://packaging.python.org/en/latest/guides/writing-pyproject-toml/>`__
structure. A template repository (or instructions on how to make one)
are currently being developed.

Configuration Practices
-----------------------

Configuration files should be written using one of the standard machine
readable table formats. This mostly includes: - TOML - YAML - CSV

Whether or not configuration files live with the code that uses them is
dependent upon the application. If multiple people are using the tool,
and configurations are being updated independent of the software that
uses them, then they should probably live in a separate repository. An
example configuration repository with details on its usage is available
`at this link <https://github.com/uasal/config_project_template>`__

Summary of Formats
~~~~~~~~~~~~~~~~~~

- TOML is the most-used format in UASAL and MagAOX for its ease of
  readability and use. The configuration files for most tools and
  calculators utilize TOML.
- YAML is a superset of both TOML and JSON and is best suited for more
  complicated and detailed tables. The budgets utilize YAML.
- CSV is what gets exported from Excel and other tools (e.g. Zemax)
  which is why it gets significant use. It is machine readable but
  requires increased parsing and massaging to be used in code.

Other Notes
-----------

Many of these items result from questions or common themes are observed

- Do not use `os <https://docs.python.org/3/library/os.html>`__ package
  for path management.
  `pathlib <https://docs.python.org/3/library/pathlib.html>`__ has
  superseded this and offers more functionality.

Useful tools
------------

Semantic line breaks are useful when writing most documentation
(e.g. Markdown, TeX, rST). Read about them `here <https://sembr.org/>`__

Unit Testing
------------

Unit testing and practicing `test-driven
development <https://en.wikipedia.org/wiki/Test-driven_development>`__
is encouraged for multiple reasons. People are encouraged to read up on
the advantages of both.

To date, unit tests have not been widely used but we’re shifting to
include them both as standalone checks and as part of continuous
integration (CI) frameworks.

The `unittest <https://docs.python.org/3/library/unittest.html>`__
standard package is generally used most frequently but others are
available.

Pytest
~~~~~~

The use of `pytest <https://docs.pytest.org/en/stable/>`__ offers some
nice conveniences.

Once installed, the following commands are useful:

- ``pytest -vsx`` - Runs in verbose (v), no-capture standard output (s),
  and fail-first (x) mode. This will scan for an run all tests,
  outputting print statements to the terminal and will exit as soon as a
  test is failed.

You can add a filename at the end to have only a subset of tests run
such as: -
``pytest -vsx tests/test_maintel_disable_m1m3_balance_system.py``

Or a specific test via supplying a filename and the regular expression -
``pytest -vsx tests/test_maintel_disable_m1m3_balance_system.py -k test_executable``

- ``pytest -vsx --log-cli-level DEBUG`` will show log messages in a
  pretty format if a logger is being used.

Loggers
-------

Logging is useful and is more powerful than peppering your code with
print statements. Examples on how to incorporating logging is at `this
link <https://docs.python.org/3/howto/logging.html>`__.

Debuggers
---------

Debuggers are a useful way of finding and fixing errors and bugs in your
code.

`Pdb <https://docs.python.org/3/library/pdb.html>`__ comes built-in to
the Python standard library and is a widely used command-line debugger.

An alternative with more GUI integration, is VSCode’s Python Debugger
extension. An example on how to set it up is provided
`here <https://code.visualstudio.com/docs/python/python-tutorial#_configure-and-run-the-debugger>`__.

Git LFS
-------

Git LFS should be used for Large File uploads to git. For further
information, refer to the 
:doc:`Git LFS Guide </git/Git_LFS_Guide>` and the :doc:`UASAL Git LFS Guide </git/uasal_lfs>`.

UASAL Configuration Management
------------------------------

Simulations and analysis tools should be structured to accept a
configuration. In cases where the analyses need to be archived and
repeatable (which should be the high majority of cases!) then the 
:doc:`UASAL configuration management approach </python/configuration_management>`
should be followed.

Git-Flow Overview
-----------------

General questions relating to git-flow and order of operations can be
founded in the :doc:`Git-Flow-Guide </git/git-flow-guide>`.

*Information detailed the* :doc:`Git-Flow-Guide </git/git-flow-guide>`
*include but are not limited to the following:*

- GitHub Overview

  - Pull Request Info, Usage, PR Template Example

- GitLab Overview

  - Merge Request Info, Usage

- Git-Flow Diagram

  - Branch Types Overview

- Git Tools / Resources

  - Applications, Training, GitDocs, Checklists

- Naming Standards

  - Repositories, Branches, Pull Requests, Merge Requests

- Repository Settings

  - Default Settings to Verify

- Fork Usage Information
