Testing Guidelines
===================

This document provides an overview of the standards for writing tests in the MagAOX, MagAOX-scoob 
and the XWCTk codebases to ensure code quality, reliability, and maintainability, but 
is applicable to any C++ code development within UASAL more generally.

There are many resources that cover testing in general and test writing in C++ in particular, so this
document is not intended as an introduction to testing, but it will highlight several basic concepts
in order to establish a common language and starting point. To skip this and refer only to the specific guidelines
for writing tests, refer to the Guidelines section below.


Testing primer
----------------

What is the point of testing?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Testing is one pillar of software validation, alongside formal verification and code review.
In C++, hidden issues such as undefined behavior, memory leaks, and pointer errors make systematic testing essential.
Software testing is hard because:

- The space of potential inputs and states grows combinatorially.
- Failures often occur at discrete boundaries (overflow, null pointers).
- Random or ad-hoc tests miss corner cases.

The goal of a tester is to find inputs and conditions that break the code, not merely to show it works.


Test first programming
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Aspirationally, one should aim to write tests before writing the code they are testing.
This is known as Test-Driven Development (TDD).
TDD encourages you to think about the requirements and expected behavior of your code before implementation,
leading to better-designed and more maintainable code.

However, in practice, this is often not feasible for all code. 
Instead, test early and often, aim to write tests as soon as possible after writing the code. 
It is far more pleasant to test your code as you develop it, than once you have a large untested codebase.


Coverage
~~~~~~~~~~~~~~~~~
Coverage aims to be an objective measures of how thoroughly a set of tests exercise the code.
Three common coverage metrics are:

- **Statement coverage**: Has every line of code been executed at least once?
- **Branch coverage**: For each conditional (``if``, ``switch``, ``ternary``), have all branches been taken?
- **Path coverage**: Have all possible sequences of branches been traversed?

Path coverage quickly becomes infeasible for all but tiny functions,
but aiming for at least 80 percent statement coverage on newly written code is a practical baseline.

The two most wide-spread coverage analysis tools for C++ are GNU gcov/lcov toolchain and LLVM's llvm-cov.
We adopt and support the GNU gcov/lcov toolchain for coverage analysis within UASAL.


Types of tests
~~~~~~~~~~~~~~~~~
Many different types of tests exist, a ballanced test suite includes at least:

- **Unit Tests**: verify single classes or functions in isolation.
- **Integration Tests**: exercise multiple modules together, catching interface mismatches or system-level failures.
- **Performance Tests**: benchmark critical code paths for throughput and latency (this can be done with, for example, Google Benchmark).


Stubs and mocks
~~~~~~~~~~~~~~~~~

For testing in general, but for unit tests, in particular, it is important to isolate the code under test from its dependencies.
To isolate units under test, replace real dependencies with test doubles:

- **Stubs**: simple implementations that return fixed data.
- **Mocks**: programmable objects that record calls, enforce interaction expectations, and simulate errors.

Using stubs and mocks ensures that failures point directly at the code under test, not at external dependencies.


Test automation and Continuous Integration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Manual testing is error-prone and slow.
A robust project automatically compiles and executes the entire test suite with a single command. 
This can be done locally or integrated into a Continuous Integration (CI) pipeline, such that every change to the codebase triggers a full test run.
CI systems such as GitHub Actions, or GitLab CI pick up every pushed change, 
run the full test suite, collect coverage reports, and enforce coverage thresholds before allowing new code to merge. 
Regression testing is baked into this pipeline: every time a previously passing test fails, 
the CI issues an alert, ensuring new changes do not allow old bugs from creeping back.



.. _guidelines:

Guidelines
-------------

- We adopt and support the Catch2 framework.
- Write tests for new functionality using the Catch2 framework.
- Place test files in the corresponding ``tests`` directory for the module or application being tested.
- Test files should follow the naming convention ``<module_name>_test.cpp`` (e.g fsmCtrl_test.cpp for the fsmCtrl module).
- Use the ``SCENARIO`` structure provided by Catch2 for Behavior-Driven Development (BDD) style tests:

    - ``GIVEN``: Sets up the initial conditions.
    - ``WHEN``: Describes the action being tested.
    - ``THEN``: Specifies the expected outcome.
    - Use ``REQUIRE`` for critical assertions that must pass.
    - Use ``CHECK`` for non-critical assertions that provide additional information.

Example:

.. code-block:: c++

    SCENARIO( "xxxx", "[template]" )
    {
        GIVEN("xxxxx")
        {
            int rv;
            WHEN("xxxx")
            {
                rv = [some test];
                REQUIRE(rv == 0);
            }
        }
    }

Generating coverage analysis reports
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Todo
