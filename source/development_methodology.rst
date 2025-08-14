Software Development Methodology
=================================

Our team employs an adaptive Agile approach tailored to the demands of a space mission, ensuring quality, traceability, and efficient collaboration.

Team Structure and Roles
--------------------------

The instruments software team comprises seven core members: one software manager, three software developers, two software scientists, and one systems engineer.

We maintain a flexible task-allocation model: individuals take on activities based on their expertise and current availability rather than rigidly defined roles. Every team member is responsible for feature design and implementation, testing, documentation, system integration, and troubleshooting support during lab operations.

Meetings and Ceremonies
-------------------------

Instruments each hold a weekly scrum meeting, led by their project manager and instrument lead. These scrums include representatives from all functional teams and cover overall project status, progress reviews, and prioritization of deliverables. Separately, our software team convenes weekly to examine backlog progress, resolve blockers, and discuss upcoming items. Ad hoc deep-dive sessions are scheduled as needed for architecture reviews or complex debugging efforts, as well as hackathons for team focus on one or a small number of issues.

Development Lifecycle and Workflow
-----------------------------------

Rather than strict sprint boundaries, we adopt a continuous planning approach driven by our issue backlog in GitHub and GitLab. Requirements, new feature requests, and bug reports are captured as issues.

Each week, during our dedicated software meeting, we triage new issues: we assign priority levels and allocate tasks to team members. High-priority instrument-specific items are also reviewed in the corresponding weekly instrument scrums, ensuring alignment across software and other functional teams. This model allows us to remain responsive to urgent needs while preserving overall project momentum.

Tools and Infrastructure
-------------------------

We rely on GitHub and GitLab for issue tracking and version control. We aim for all instrument-relevant repositories to implemented CI/CD pipelines, via GitHub Actions and GitLab CI, to automate the following processes:

- building and publishing of documentation
- executing unit and integration test suites
- performing static code analysis, and 
- generating coverage reports.

This infrastructure ensures rapid feedback on code quality and enforces consistency across development environments.

Quality Assurance and Testing
------------------------------

We aim to enforce rigorous quality goals across multiple testing layers:

Testing Layers
~~~~~~~~~~~~~~~~

- **Unit tests** accompany all new code contributions, ensuring each function and class behaves as expected. Existing code is backfilled with unit test, according to the coverage targets.
- **Modular integration tests** verify interactions within defined subsystems (e.g. data-saving workflows, power-management workflows etc.). A list of subsystems to cover will be compiled.
- **Regression tests** are performed end-to-end against an abstract-hardware simulation; these include the injection of fault conditions to validate error handling.
- **Wavefront-propagation tests** combine wavefront control algorithms with abstract-hardware models, also supporting fault injection to assess robustness.
- **Performance & benchmarking tests** allow measurement and tracking of latency, throughput and resource usage across updates and usage scenarios.
- **A dedicated ground-copy system**, mirroring flight software and hardware interfaces, supports on-sky troubleshooting.

Unit Test Coverage Targets
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- XWCTk: maintain 100 % function coverage and 90 % line coverage, with a monthly objective of increasing line coverage by 10 % until we reach the target.
- XWC Applications and libraries developed in-house or by connected groups:

    - Critical applications must achieve 100 % function and 90 % line coverage.
    - Important applications require 100 % function and 80 % line coverage.

For comprehensive details, see the :doc:`Testing Strategy document <testing_strategy>`.

Documentation
---------------

Our documentation hierarchy includes:

- Auto-generated API references and user guides derived from code comments and docstrings (for comprehensive details, see the :doc:`C++ Documentation Strategy document <C++/documentation>`).
- Architecture and interface diagrams stored in issues and design repositories.

Release
------------

Development occurs on feature branches, following the branching strategy documented in the :doc:`Git-Flow Guide <git/git-flow-guide>`.

All code merges into main / develop branches undergo peer review with at least one reviewer required. It is not required to include reviewers for merges to other branches, but it is recommended for complex features or branches used on testbeds.

Risk Management 
-----------------

Risks are documented as issues with severity ratings and mitigation plans. We review and update the risk register regularly, escalating high-impact items as needed.