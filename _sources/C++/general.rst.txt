C++ Development
====================

This document provides an overview of the standards and practice for contributing C++ code to the MagAOX, MagAOX-scoob 
and the XWCTk codebases to ensure consistency, maintainability, and adherence to project standards, but 
is applicable to any C++ code development within UASAL more generally. Familiarity with C++ is assumed.


Introduction
--------------
`MagAOX <https://github.com/magao-x/MagAOX>`__ is a framework designed for adaptive optics control on the MagAO-X ExAO system.
`MagAOX-scoob <https://github.com/uasal/MagAOX-scoob>`__ is a fork of the MagAOX framework, tailored for the Scoob testbed.
`XWCTk <https://github.com/uasal/XWCToolkit>`__ is a stand-alone framework that encapsulates the core functionalities of MagAOX, 
designed for general-purpose adaptive optics control.

The MagAOX API documentation is available `here <https://magao-x.org/docs/api/index.html>`__.
Particularly relevant are the steps for adding `a new application <https://magao-x.org/docs/api/page_module_appadd.html>`__.

General Coding Standards
--------------------------
Language Version
~~~~~~~~~~~~~~~~~~~
- Use C++17 for all new code contributions.
- Avoid deprecated features and prefer modern C++ idioms (e.g., ``std::unique_ptr`` over raw pointers).

Formatting and Style
~~~~~~~~~~~~~~~~~~~~~
Follow `Google C++ Style Guide <https://google.github.io/styleguide/cppguide.html>`__ for general formatting rules, with the following project-specific adjustments:
- Indentation: Use 4 spaces for indentation. Do not use tabs.
- Line Length: Limit lines to 120 characters.
- Braces: Always use braces for control structures, even for single-line blocks.
- Naming Conventions:

    - Classes: ``camelCase`` (e.g., ``MagAOXApp``, ``dmCtrl``)
    - Constants: Uppercase ``snake_case`` (e.g., ``DM_MAX_ACTUATORS``)
    - Member variables: ``camelCase`` prefixed with ``m_`` (e.g., ``m_configName``)
    - Accessors: Avoid prefixes like ``get`` or ``is``; use the member variable name without the ``m_`` prefix (e.g., ``configName``)
    - Functions: ``camelCase`` (e.g., ``sendArray``, ``getArrayToActuatorMapping``)
    - Local variables: ``snake_case`` (e.g., ``loop_pause``, ``config_dir``)
    - Namespaces: ``camelCase``, apart from the top-level namespace which is capitalized as ``MagAOX`` (e.g., ``MagAOX::app``, ``MagAOX::logger``)

- Header Files:

    - Use include guards (``#ifndef`` / ``#define``) or ``#pragma`` once to prevent multiple inclusions.
    - Group includes logically:

        - System / standard library headers
        - Third-party library headers.
        - Project-specific headers.

- Namespaces:

    - Subdivide namespaces for specific larger modules (e.g., ``MagAOX::app``, ``MagAOX::logger``), but not for individual apps.

- Avoid manual memory management (``new`` / ``delete``) unless absolutely necessary.

Auto-formatting Tools
~~~~~~~~~~~~~~~~~~~~~~~~~~~

To ensure consistent formatting across the codebase, the use of auto-formatting tools is strongly encouraged.
Integrating these tools into your workflow, reduces manual formatting effort and ensures that the project's style guidelines
are consistently implemented. For C++ projects ``clang-format`` is recommended and for multiple-language projects, ``.editorconfig``.
- `clang-format <https://clang.llvm.org/docs/ClangFormat.html>`__: A ``.clang-format`` file defines the project's formatting rules for C++ files. 
``clang-format`` can be used either through your IDE of choice or the command line.
An example of a `.clang-format` file can be found `here <https://github.com/magao-x/MagAOX/blob/dev/.clang-format>`__
- `.editorconfig <https://editorconfig.org/>`__: An `.editorconfig` file provides additional rules for general text files, 
Python scripts, Markdown files, and Makefiles. Most modern IDEs and text editors support .editorconfig for enforcing these rules.
An example of a `.editorconfig` file can be found `here <https://github.com/magao-x/MagAOX/blob/dev/.editorconfig>`__

Including and Delivering New Libraries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Evaluate Necessity and Viability
Before deciding to include a new library, its reliability and long-term viability should first be evaluated.
A "serious" library should demonstrate stability and a clear maintenance track record.
This assessment helps ensure that the library can be trusted without introducing unnecessary risks to the project.
Items to consider are:
- Ensure the library addresses a specific problem that cannot be addressed with existing code or libraries.
- Ensure the library is compatible with the project's licensing.
- Assess how frequently the library is updated and maintained.
- Evaluate the library's documentation for clarity and completenss.
- Evaluate the library's performance and its impact on the project.
- Research alternative libraries to ensure the best option is chosen.

2. Choosing a Delivery Method
Next we need to decide whether to rely on the operating-system's package manager or to vendor/bundle it in our repository (including its source in our repository or maintaining our own fork/copy of it and building it as part of our build process):

In general:
- O/S libraries:

    - **Prefer O/S-managed packages** whenever the version and build options in our target distributions meet our needs. This approach simplifies our repository and build process. Ensure that the exact package name and minimum version required are captured in the version-specific "configure_ubuntu" bash file or architecture-specific "conda_env_pinned" yaml file.
    - Vendor or bundle an O/S library when the O/S packages are missing, out of date, or built without the flags and optimizations we require (for example, OpenBLAS). In these cases, include a bash script with the specific build steps that use an exact source and version for the package. Include this in the project's build process so the library compiles automatically with the rest of the project.

- non-O/S libraries:

    -  **Always** bundle a local copy rather than invoking `git clone` at build time. This guarantees reproducibility even if the upstream repo changes or disappears.

When introducing a new library, make sure to update the dependency list in the project's documentation and README installation instructions.

Comments and Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~

For more details refer to the :doc:`Documentation <documentation>` page, but in general:
- Use Markdown files (``*.md``) for high-level documentation, such as README files.
- Use Doxygen-style comments for all files, classes and methods.
- Use inline comments to outline logic, paying particular attention to complex logic.
- Avoid redundant comments that merely restate the code.

Error Handling
~~~~~~~~~~~~~~~
- Use exceptions for critical errors that cannot be recovered.
- For recoverable errors, use logging mechanisms (``log<software_error>``, ``log<text_log>`` etc.).
- Avoid using ``assert`` in production code.

Testing
~~~~~~~~~
For more details refer to the :doc:`Testing <testing>` page, but in general:
- Write tests for new functionality using the Catch2 framework.
- Place test files in the app's corresponding tests directory (see the adding (a new application)[https://magao-x.org/docs/api/page_module_appadd.html] section in the API documentation).
- Use the ``SCENARIO`` structure for Behavior-Driven Development (BDD) style tests; e.g.

.. code-block:: c++

    SCENARIO("Testing sendArray with valid inputs", "[dmCtrl]") {
        GIVEN("A valid input vector and mode") {
            WHEN("sendArray is called") {
                THEN("It should return 0 and send the correct payload") {
                    REQUIRE(result == 0);
                }
            }
        }
    }