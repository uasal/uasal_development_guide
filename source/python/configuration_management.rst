UASAL Configuration Management Summary
======================================

UASAL software is being architected such that programs and/or methods
are provided a distinct set of parameters, known as a configuration, and
the program (e.g. a simulation tool) is to return an object (or objects)
with the data interest. The format of the object itself is up to the
user, but the intention is that the computations are done inside the
program, and the presentation (e.g. plots) are performed external to the
toolset as part of an analysis document (e.g. a script or notebook).

Much of the reasoning for employing configuration management and
developing tooling to support it is to enable rapid analyses and trade
studies that have repeatable results. As programs develop, there are two
separate use-cases that often encapsulate the majority of user needs:

1. An exploratory study where a small number of parameters are iterated
   over and the results are compared.

   - An example of this would be to look at the sensitivity of an
     instrument for different coating choices.

2. An analysis that is used to derive a key value that must be
   continually re-evaluated and shown to be in compliance.

   - An example of this would be expected performance (e.g. sensitivity)
     of the observatory main instrument.

In case 1, the analysis is performed at a fixed point in time relative
to a specific configuration. This often produces an artifact that is
then used to make a decision in one direction or another. The analysis
is recorded and can be redone at a future time if required, with the
same of different starting values, but is generally not revisited
regularly.

In case 2, the analysis needs to be re-done with every change to the
system that impacts it. The value and/or result is generally monitored
and evaluated over time. This could be a key performance metric (aka a
technical performance measure or TPM) or a requirement that is derived
and placed on another component. Evaluation of the expected wavefront
error of an observatory would be an example of this. Each time a change
to the observatory configuration occurs, the metric needs to be
re-evaluated to ensure performance will be met.

Maintaining a structure where the tools are built to accept
configurations, and analyses are written to call these tools allows both
of these use-cases to be accomplished.

The following figure demonstrates how UASAL organizes and structures a
subset of its tools and configuration repositories and how they are
called from within an analysis.

.. figure:: /_static/config-figure.png
   :alt: Configuration mapping

   Configuration mapping

*UASAL structure for analyses, simulation tooling, and configuration
repositories.*

It is important to note that each simulation tool gathers it’s
configuration from a multiple sources (and repositories). The parameters
needed by each tool differ, but the *SOURCES* of the parameters which
encompass the observatory and instrument are the same. This ensures that
there is no duplication of parameters which could lead to errors in the
analyses.

Each tool is provided, or automatically invokes a default configuration.
Users can then iterate over over a single parameter in a configuration,
or load an entirely different one. Utilizing this structure ensures
repeatability and traceability of results while simultaneously allowing
the exploration of configuration parameters and their effects on
performance.

It is important to note that configuration files in all the repositories
are machine-readable. This assists in managing the traceability of the
values from requirements, budgets or other point of origin and enables
the opportunity to make a specific set of analyses be able incorporated
into a continuous integration framework.

.. raw:: html

   <!-- A secondary set of tools is then developed that interacts with that data to provide plots, fit relationships, or derive key values.
   The configuration(s) for these tools are then stored in areas such that the analyses can be repeated at a later date and the results are repeatable (so long as the same versions of the tools are used.) -->

Configuration Repositories
--------------------------

The configurations managed by UASAL are organized into discrete
repositories that contain the configuration files, often written in
`TOML <https://toml.io/en/>`__, as well as associated documentation and
incorporated continuous integration tests. The TOML files support
AstroPY units, which is discussed further in the FAQ section below.

The configuration repositories written as Python packages with very
minimal dependencies to ensure they are easy to incorporate into your
code and environment. Utilizing the package structure also assists with
path management of supporting files. The one dependency is the
`config_utils <https://github.com/uasal/utils_config>`__ package, which
contains methods that help to ingest TOML files as well as containing
the integration tests that run on all repos. Of course, non-Python
software can still clone and/or download the repository and work
directly with the TOML files, bypassing all the Python helper functions
and implementation.

Repository Naming
~~~~~~~~~~~~~~~~~

Configuration repositories all follow the same naming convention,
notably ``config_project_element``. So a hypothetical example could be
``config_hubble_acs``. The ``config_`` prefix indicates it’s a
configuration, the ``project`` indicates which
observatory/telescope/project it is applied to (e.g. STP (Space Telescope Pathfinder) or UM
(Ultramarine)), and the ``element`` indicates the instrument
which it is applied to. It is not required that an instrument name be
used as the element, but to date it has been the only element to be
used.

Generally, there is a top level repository for the project
(e.g. ``config_stp``) which contains the items that are applicable to
all parties and controlled at the system level. FIXME: expand this and
make it clear what things are documented in the repo vs here.

Then there are configurations that are applied to each individual
instrument (e.g. config_stp_wcc and config_stp_esc).

Navigating and finding config repos can be done from from UASAL GitHub
page, and entering ``config_`` in the repository search towards the
bottom of the page as can be seen `at this
link <https://github.com/uasal/?q=config_&type=all&language=&sort=>`__.

Expanding configuration to other systems
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The current set of configuration repositories are focused on the Space
Telescope Pathfinder (STP) mission. It is anticipated that a
new set will be created for the Ultramarine mission that
will follow the same structure. However, it is important to note that
the infrastructure is easily expandable to other projects and also local
hardware setups. Examples include the phase retrieval testbench or
SCoOB.

It is also possible to have configurations be specific to a location
(e.g the ARB vs Steward), although this will require some additional
implementation of features in the
`config_utils <https://github.com/uasal/utils_config>`__ package.

Configuration Repository Structure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The directory structure is designed as follows:

- Configuration parameters that are common to all tools in the
  repository belong in the ``common_params.toml`` file.
- A separate directory (should be named the same as the repo) is needed
  for python packaging (``config_project_template``).
- Config files must contain both values and units.

  - Units shall utilize the astropy format.

- Values without a unit will be marked as *unitless* if being read via
  the config_loader in
  `config_utils <https://github.com/uasal/utils_config>`__. See the
  documentation in that package for behavior details.
- The origin of the values should be in a comment (for now).
- At this time, no other filenames should start with an ``_``. This
  functionality is reserved for future feature implementation(s).
- Any added configuration file must contain the *full set* of available
  parameters and not just overrides for the defaults.

Configuration files may contain key valued pairs, but also utilize
groupings and lists. Such as:

.. code:: toml

   OD_optic1 = '50e-3m'
   [sim_settings]  # settings for simulation tool
   npix = 4096 # number of pixels per frame
   beamrad = 0.4 # fractional beam radius
   wavelengths = [500,600,700]

An example repository, which also provides a template for future
configuration repos, is found at
`config_project_template <https://github.com/uasal/config_project_template>`__.

Performing an Analysis with Existing Tools
------------------------------------------

An `example
notebook <https://github.com/uasal/config_project_template/blob/main/docs/example.ipynb>`__
is provided in the
`config_project_template <https://github.com/uasal/config_project_template>`__
that (very roughly) demonstrates how an analysis can be written that
utilizes a tool that is provided a configuration.

A more representative example `is in
development <https://github.com/uasal/wcc_designdocs/issues/188>`__.

Configuration FAQ
-----------------

1. How do I find all the configuration repositories?

   - Search Github repos and GitLab repositories for anything named
     ``config_``, as is done
     `here <https://github.com/uasal/?q=config_&type=all&language=&sort=>`__.

2. Does my tool require a separate configuration repository?

   - In cases where your tool is being used to conduct analyses or is
     related to the determination of budgets or requirements then it is
     advised to utilize a separate configuration repository that
     contains the defaults which should be called

3. Why/When should config files be stored separately from the code?

   - Facilitates easy versioning (and impact assessment) between code
     changes and config changes
   - Single configs can/should be usable with different
     versions/branches/tags
   - Multiple people (or instances) can use them without permission from
     the code owners
   - Allows for rapid automated unit testing that verifies file is
     readable/parse-able so you don’t accidentally break your or someone
     else’s code
   - Allows for configurations that are specific to a site/machine/setup

4. Where should I put the configuration for my tool?

   - If your tool is often used in combination with another tool, then
     it may make sense to share a configuration directory, otherwise it
     should be separate.

5. Do ALL configuration repositories need to be packages?

   - No, but it may be useful.
   - We do require for traceability in reporting, which means we need to
     know which tags/versions you were running, and how your simulation
     was configured, so what is most important is that your config repo
     is maintained and versioned correctly.
   - Advantages to python packages: can rely on your environment to take
     care of directory management
   - Allows functionality to be built into package and shared between
     users.
   - Advantages to repos with just files:
   - Easier to maintain, must hard code a repo (bad), or set an
     environment variable (less bad), then execute system commands from
     within a python script/notebook. Currently doing this in psd_utils
     to detect if stp_reference data is dirty.

6. Config files mention filenames, where should those files be located?

   - They should reside in the ``support_data`` directory. Note that in
     many cases the support data will contain files managed by
     `gitlfs <https://git-lfs.com/>`__.

7. Do filenames or paths in config files require a unit?

   - UASAL configs utilize `Astropy
     units <https://docs.astropy.org/en/stable/units/index.html>`__.
     They should be formatted as strings as per `this
     example <https://docs.astropy.org/en/stable/units/format.html#converting-from-strings>`__.
     If no unit is provided, it is assumed to be unitless. Details
     regarding the automated testing for the units are currently being
     implemented in the
     `utils_config <https://github.com/uasal/utils_config/tree/develop>`__
     repository and then will be called from the CI tests in all
     ``config_*`` repos.

8. When should the configuration version be augmented?

   - configuration versions are not currently tracked.
   - Normally, when the code is no longer backwards compatible and the
     format for the file no longer applies. This occurs when either
     additional mandatory keywords are required or removed. This cannot
     be implemented because the tools are not utilizes schemas for
     configuration and therefore config files cannot be validated
     against versions of the schemas.

9. Should I use `semantic versioning <https://semver.org/>`__? Yes, but
   note that only major revisions require version bumps.
