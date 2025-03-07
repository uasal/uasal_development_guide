Using UASAL Git LFS (hosted on stp-lfs)
=======================================

Adding new user to gitlab with github login
-------------------------------------------

As user
~~~~~~~

- New user workflow:

  - With the VPN active, go to “http://10.130.30.9/users/sign_in” and
    click on “GitHub”
  - This will redirect to a github page asking whther you want to
    “Authorize Stp-lfs Gitlab” (and informing what personal user data it
    will use: Email addresses (read-only))
  - Click “Authorize uasal”
  - This will redirect back to gitlab
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

Linking gitlab lfs to github repo
---------------------------------

Assuming the git lfs is installed and initialized for you account
(e.g. ``conda install git lfs`` and ``conda install git lfs``)

Using .fits files as an example.

Assuming github repository with no existing associated large files. In
this repository: - Add a new .lsfconfig file containing:

::

   [lfs]
       url = "http://10.130.30.9/lfs/test_stp_lfs.git/info/lfs"

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

Cloning a repo with git-lfs
---------------------------

**You need to be connected to the vpn / on the UofA network**

::

   git clone git@github.com:uasal/<REPOSITORY_NAME>.git

If you try to clone and are not connected to the vpn / on the UofA
network, the non lfs file structure will get cloned but the command will
hang and you’ll need to Ctrl+c it leaving the repository in an odd git
state.
