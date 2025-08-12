C++ Documentation Guidelines
==============================

This document provides an overview of the standards for documenting C++ code in the MagAOX, MagAOX-scoob 
and the XWCTk codebases to ensure consistency, maintainability, and adherence to project standards, but 
is applicable to any C++ code development within UASAL more generally.

`Doxygen <https://www.doxygen.nl/>`__ is adopted as the primary tool for generating documentation from source code comments. 

Doxygen Overview
-----------------

What is Doxygen?
~~~~~~~~~~~~~~~~~

Doxygen is a documentation generator for C++, C, and other programming languages.

Doxygen allows developers to write structured comments directly in the code, which can then be processed to produce hosted HTML API documentation.

It extracts specially formatted comments from the source code and generates documentation in various formats.

Why Use Doxygen?
~~~~~~~~~~~~~~~~~

**Consistency**: Ensures all code is documented in a uniform manner.
**Ease of Use**: Allows developers to write documentation alongside the code.
**Automation**: Automatically generates documentation from comments, reducing manual effort.

Documentation and Comment Style
--------------------------------

General Guidelines
~~~~~~~~~~~~~~~~~~~~

- Use Doxygen-style comments for all files, classes and methods.
- Write comments intended to be included in the documentation and capture the code API in the Javadoc style:

.. code-block:: c++

   /**
    * This is a Doxygen Javadoc-style comment.
    * It describes the purpose of the code that follows.
    */

- Write comments intended to clarify logic and architectural decisions in the C++ single-line style:

.. code-block:: c++

   // This is a C++ comment explaining the following lines of code.

- Ensure comments are concise, descriptive, and relevant to the code they accompany.
- Avoid redundant comments that merely restate the code.
- Use Markdown files (``*.md``) for high-level documentation, such as README files.

File-Level Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~

Every file must include the project-specific abridged license statement at the top of the file, 
followed by a header comment at the top with the following information:

- **File Name**: Use ``\file`` to specify the file name.
- **Brief Description**: Use ``\brief`` to describe the purpose of the file.
- **Author**: Use ``\author``  to include the name and email of the authors.
- **Group**: Use ``\ingroup`` to specify the group this file belongs to.

Example:

.. code-block:: c++

    //***********************************************************************//
    // Copyright 2025 <author_name> (<author_email>)
    //
    // This file is part of <project_name>.
    //
    // <project_name> is free software: you can redistribute it and/or modify
    // it under the terms of the GNU General Public License as published by
    // the Free Software Foundation, either version 3 of the License, or
    // (at your option) any later version.
    //
    // <project_name> is distributed in the hope that it will be useful,
    // but WITHOUT ANY WARRANTY; without even the implied warranty of
    // MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    // GNU General Public License for more details.
    //
    // You should have received a copy of the GNU General Public License
    // along with <project_name>.  If not, see <http://www.gnu.org/licenses/>.
    //***********************************************************************//

    /** \file MagAOXApp.hpp
    * \brief The basic MagAO-X Application
    * \author Jared R. Males (jaredmales@gmail.com)
    *
    * \ingroup app_files
    */


Class Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Each class should be preceded by a comment block consisting of:

1. a concise (ideally single-line) description formatted in a ``\\\`` comment style 
2. a Javadoc-style comment block that provides further details on the class's functionality, usage, and any special considerations.

Example:

.. code-block:: c++

    /// The base-class for MagAO-X applications.
    /**
    * You can define a base configuration file for this class by defining
    * \code
    *  m_configBase = "base_name";
    *  \endcode
    * in the derived class constructor. This would be used, for instance, to have a config common to
    * all filter wheels.
    *
    * \todo Make m_powerMgtEnabled a template parameter, and static_assert check if _useINDI == false and power management
    * is true.
    *
    * \ingroup magaoxapp
    */
    template <bool _useINDI = true>
    class MagAOXApp : public application


Member Variables Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Document all member variables with inline comments marked with ``///<`` to describe the variable's purpose.

Example:

.. code-block:: c++

   std::string m_devicePort; ///< The device port
   double m_bootDelay {10}; ///< Time in seconds it takes the device to boot.


Function Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Each function should be preceded by a comment block consisting of:

1. a concise (ideally single-line) description formatted in a ``\\\`` comment style 
2. a Javadoc-style comment block that includes:

    - **Description**: a more detailed description of the function's functionality, usage, and any special considerations.
    - **Parameters**: an inline description of each parameter, starting with ``///<``. This comment string should start with
        ``[in]`` or ``[out]``, if the parameter is an input or output parameter, respectively. If the parameter
        is optional, also add ``[optional]``. 
    - **Template Parameters**: for function templates, a description of their parameters using ``\tparam``.
    - **Return Value**: a description of the return value using ``\returns``.

Example:

.. code-block:: c++

    /// Make a log entry
    /** Wrapper for logManager::log
     *
     * \tparam logT the log entry type
     * \tparam retval the value returned by this method.
     *
     */
    template <typename logT, int retval = 0>
    static int log( const typename logT::messageT &msg,   ///< [in] the message to log
                    logPrioT level = logPrio::LOG_DEFAULT /**< [in] [optional] the log level.  The default
                                                                               is used if not specified.*/
    );


Grouping and Organization
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Topics
^^^^^^^^

Files, classes, structures etc. can be organized into logical groups, called **topics**, 
making the documentation easier to navigate.

For example, all application-related files are grouped under the ``apps`` topic and each application 
defines its own topic and subtopics (e.g. ``streamWriter`` and ``streamWriter_files``).

Groups are defined using the ``\defgroup`` command, typically as the first thing after opening the namespace.
Each group is given a unique name and a brief description.
Groups can be nested to create subcategories within a larger topic.

Items (files, classes, structures, functions etc.) are added to groups using the ``\ingroup`` command.

The ``\ingroup`` command is placed in the Doxygen comment block of the item being added.

.. code-block:: c++

    /** \defgroup streamWriter ImageStreamIO Stream Writing
    *  \brief Writes the contents of an ImageStreamIO image stream to disk.
    *
    *  <a href="../handbook/operating/software/apps/streamWriter.html">Application Documentation</a>
    *
    *  \ingroup apps
    *
    */


Member Groups
^^^^^^^^^^^^^^^

Group related functions and variables within a member list using the ``\name`` and ``|@{/@}`` tags.
Also include a brief description of the member group.

Example:

.. code-block:: c++

    /** \name Pure Virtual Functions
     * Derived applications must implement these.
     * @{
     */

    /// ...
    /** ... */ 
    virtual int appStartup() = 0;

    /// ...
    /** ... */ 
    virtual int appLogic() = 0;

    /// ...
    /** ... */ 
    virtual int appShutdown() = 0;

    ///@} -- Pure Virtual Functions


Special Tags
~~~~~~~~~~~~~

Todo Items
^^^^^^^^^^^

Highlight areas for improvement or future work using the ``\todo`` command in comment blocks or inline comments.

Code Examples
^^^^^^^^^^^^^^

In the entity's coment block, include code examples using ``\code`` and ``\endcode``.

Example
^^^^^^^^^

.. code-block:: c++

    /// The base-class for MagAO-X applications.
    /**
    * You can define a base configuration file for this class by defining
    * \code
    *  m_configBase = "base_name";
    *  \endcode
    * in the derived class constructor. This would be used, for instance to have a config common to
    * all filter wheels.
    *
    *
    * \todo make m_powerMgtEnabled a template parameter, and static_assert check if _useINDI== false and power management
    * is true
    *
    * \ingroup magaoxapp
    */

