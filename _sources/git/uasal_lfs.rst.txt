.. _uasal_archive:

Using the UASAL_Archive 
========================

We have setup an large-file service (LFS) that is independent of GitHub LFS primarily due to storage and bandwidth costs which balloon over time.

The `uasal_archive <https://github.com/uasal/uasal_archive>`__ is an area where the team can place files that are required for simulations but do not belong inside a specific repository.
This sometimes includes references to files that are too large to host in a configuration repo, or change frequently. 
It is also the place to store files that are used by multiple parties and/or analyses.
If unclear on when to use the archive or not, please ask in the #computing Slack channel or reach out to Patrick Ingraham.

.. note::
  There are times where these files are referenced from inside a configuration file via an environment variable that must be setup locally. An example of this can be found in the `config_project_template example notebook <https://github.com/uasal/config_project_template/blob/main/notebooks/example.ipynb>`_. See also details on :ref:`env_variables`.


**Disclaimer:** The UASAL Git LFS is managed via a GitLab instance. This
is **NOT** the same GitLab instance as the ITAR-compliant ANT GitLab and 
shall **NOT** be used for ITAR material, only for non-ITAR large file
storage.

Adding a new user to UASAL Git LFS with GitHub login
-----------------------------------------------------

As user
~~~~~~~

- New user workflow:

  - With the VPN active, go to “http://10.130.30.9/users/sign_in” and
    click on “GitHub”
  - This will redirect to a github page asking whther you want to
    “Authorize Stp-lfs GitLab” (and informing what personal user data it
    will use: Email addresses (read-only))
  - Click “Authorize uasal”
  - This will redirect back to GitLab
  - You might get a notification saying that your account needs to be
    validated by and admin
  - In the meantime, go to
    http://10.130.30.9/-/user_settings/personal_access_tokens and click
    ‘Add New Token’:

    - Give the token a descriptive name (e.g. git-lfs token)
    - Set the latest expiration date you can (a year from today)
    - Scopes: select the ‘read_repository’ and ‘write_repository’ scopes
    - Click ‘Create personal access token’
    - **Save the token!** You can’t access it again afterwards

  - As an aside, you can see what apps you have authorized to your
    github account under https://github.com/settings/applications and
    revoke access to any as required.

As admin
~~~~~~~~

- An admin needs to go to 10.130.30.9/admin/users/ and check whether any
  users are waiting validation. If so, validate them.
- An admin also needs to add new users to the lfs/stp_lfs project:

  - Go to http://10.130.30.9/lfs/stp_lfs/-/project_members, click on
    ‘Invite members’ and type in the (GitHub) usernames of new users
  - For each new user, select the role (e.g. Maintainer) and an optional
    expiration date for the access
  - Click Invite

Linking UASAL LFS to GitHub repo
---------------------------------

Assuming the git lfs is installed and initialized for you account
(e.g. ``conda install git lfs`` and ``git lfs install``)

Once you have linked your account to the UASAL LFS, an admin needs to add
you to the relevant repositories.

Using .fits files as an example.

Assuming github repository with no existing associated large files. In
this repository:

- Add a new .lsfconfig file containing:

::

   [lfs]
       url = "http://10.130.30.9/lfs/stp_lfs.git/info/lfs"

- On the command line in the repository, run:

::

   git lfs track "*.fits"

This will create a .gitattributes file with an entry:

::

   *.fits filter=lfs diff=lfs merge=lfs -text

- Add the changes to staging and commit, then push e.g.:

::

   git add .lsfconfig .gitattributes
   git commit -m "Adding git lfs tracking"
   git push

- Then add a .fits file, add it to staging and commit, then push. On
  push you will be prompted for username and password:

  - Username: your github username
  - Password: the personal access token you created earlier

- The list of files tracked by Git LFS can be checked with `git lfs ls-files`

Notes
~~~~~

- You need to be connected to the vpn / on the UofA network to push /
  pull tracked files, but not otherwise (for regular commits)
- If you try to push / pull tracked files and are not connected to the
  vpn / on the UofA network the command will hang and you’ll need to
  Ctrl+c it
- The credentials will not be saved by default, so you will be prompted
  for them every time you push a new lfs file. It is possible to
  configure git to used stored credentials:

  - Install git-credential-manager

  ::

     brew install git-credential-manager  # macOS
     sudo apt install -y git-credential-manager  # Ubuntu/Debian

  - Enable it in git

  ::

     git config --global credential.helper manager

  - In ``~/.git-credentials`` add this line, replacing ``USERNAME`` and
    ``PERSONAL_ACCESS_TOKEN``

  ::

     https://USERNAME:PERSONAL_ACCESS_TOKEN@github.com

Cloning a repo with Git LFS
---------------------------

**You need to be connected to the vpn / on the UofA network**

::

   git clone git@github.com:uasal/<REPOSITORY_NAME>.git

If you try to clone and are not connected to the vpn / on the UofA
network, the non lfs file structure will get cloned but the command will
hang and you’ll need to Ctrl+C it leaving the repository in an odd git
state.
