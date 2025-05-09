Setting up environment variables
================================

Several UASAL repositories and/or python packages require environment variables to be configured
in order to read in a configuration correctly. In context of configuration repos such as
config_stp or config_um, the environment variable is set to a remote file server so that
on package usage, the path to the file server is automatically expanded.

Environment Variable Setup
--------------------------

Linux / macOS
-------------

1. **Check which environment variable your configuration repository is using**

   Reference the README or inspect the config files for paths prepended by ``$``, e.g. ``$SERVER``.

2. **Temporarily add the environment variable to your session**

   In a terminal, type the following and press Enter:

   .. code-block:: bash

      export ENV_VARIABLE=/path/to/server

3. **Permanently add the environment variable**

   Add the `export` command above to one of your shell config files:

   - ``~/.bashrc``
   - ``~/.bash_profile``
   - ``~/.zshrc``
   - ``~/.profile``

   Then apply the changes with:

   .. code-block:: bash

      source ~/.bashrc

4. **Verify the environment variable**

   Open a new terminal and run:

   .. code-block:: bash

      echo $ENV_VARIABLE


Windows
-------

1. **Check which environment variable the configuration repository is using**

   Reference the README or inspect the config files for paths prepended by ``$``.

2. **Temporarily add the variable for the current Command Prompt session**

   .. code-block:: cmd

      set ENV_VARIABLE=\\path\to\server

   Replace with the actual UNC path to your network location.

3. **Permanently add the environment variable**

   - Search **"Environment Variables"** in the Start Menu |image1|
   - Open **"Edit the system environment variables"** and click **"Environment Variables..."** |image2|
   - Under **User variables** or **System variables**, click **New**:
     - **Name**: ``ENV_VARIABLE``
     - **Value**: ``\\path\to\server`` |image3|
   - Click OK to save.


4. **Verify the environment variable**

   Open a new Command Prompt or PowerShell window and run:

   .. code-block:: cmd

      echo %ENV_VARIABLE%


.. |image1| image:: /_static/windows_env_1.png
.. |image2| image:: /_static/windows_env_2.png
.. |image3| image:: /_static/windows_env_3.png
.. |br| raw:: html

  <br>


