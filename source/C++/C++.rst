C/C++ Development
====================

This guide provides an overview of the standards and practice for contributing C++ code to the MagAOX, MagAOX-scoob 
and the XWCTk codebases to ensure consistency, maintainability, and adherence to project standards, but 
is applicable to any C++ code development within UASAL more generally. It assumes familiarity with C++.


Introduction
--------------
(MagAOX)[https://github.com/magao-x/MagAOX] is a framework designed for adaptive optics control on the MagAO-X ExAO system.
(MagAOX-scoob)[https://github.com/uasal/MagAOX-scoob] is a fork of the MagAOX framework, tailored for the Scoob testbed.
(XWCTk)[https://github.com/uasal/XWCToolkit] is a stand-alone framework that encapsulates the core functionalities of MagAOX, 
designed for general-purpose adaptive optics control.

The MagAOX API documentation is available (here)[https://magao-x.org/docs/api/index.html].
Particularly relevant are the steps for adding (a new application)[https://magao-x.org/docs/api/page_module_appadd.html].

General Coding Standards
--------------------------
Language Version
~~~~~~~~~~~~~~~~~~~
- Use C++17 for all new code contributions.
- Avoid deprecated features and prefer modern C++ idioms (e.g., ``std::unique_ptr`` over raw pointers).

Formatting and Style
~~~~~~~~~~~~~~~~~~~~~
Follow (Google C++ Style Guide)[https://google.github.io/styleguide/cppguide.html] for general formatting rules, with the following project-specific adjustments:
- Indentation: Use 4 spaces for indentation. Do not use tabs.
- Line Length: Limit lines to 120 characters.
- Braces: Always use braces for control structures, even for single-line blocks.
- Naming Conventions:
    - Classes: ``CamelCase`` (e.g., ``MagAOXApp``, ``dmCtrl``)
    - Member variables: ``snake_case`` prefixed with ``m_`` (e.g., ``m_mode``, ``m_nbAct``)
    - Constants: ``UPPER_CASE`` (e.g., ``DM_MAX_ACTUATORS``)
    - Functions: ``camelCase`` (e.g., ``sendArray``, ``getArrayToActuatorMapping``)
    - Local variables: ``snake_case`` (e.g., ``loop_pause``, ``config_dir``)
    - Namespaces: ``snake_case``, apart from the top-level namespace which is ``MagAOX`` (e.g., ``MagAOX::app``, ``MagAOX::logger``)
- Header Files:
    - Use include guards (``#ifndef`` / ``#define``) or ``#pragma`` once to prevent multiple inclusions.
    - Group includes logically:
        - System / standard library headers
        - Third-party library headers.
        - Project-specific headers.
- Namespaces
    - Subdivide namespaces for specific larger modules (e.g., ``MagAOX::app``, ``MagAOX::logger``), but not for individual apps.
- Avoid manual memory management (``new`` / ``delete``) unless absolutely necessary.
- Libraries: Minimize the use of third-pary libraries. If required:
    - Ensure the library is compatible with the project's licensing.
    - Update the dependency list in the project's documentation and README installation instructions.

Comments and Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~
For more details refer to the :doc:`Documentation <documentation>` page, but in general:
- Use Doxygen-style comments for all public classes, methods, and files.
- Use inline comments to outline logic, paying particular attention to complex logic.
- Self-describing code doesn't need a comment. 

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

.. code-block:: C++
    SCENARIO("Testing sendArray with valid inputs", "[dmCtrl]") {
        GIVEN("A valid input vector and mode") {
            WHEN("sendArray is called") {
                THEN("It should return 0 and send the correct payload") {
                    REQUIRE(result == 0);
                }
            }
        }
    }