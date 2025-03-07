Setting Up SSH for GitHub
=========================

Several UASAL repositories require ssh keys to be configured in order to
clone a repository or install a package. Follow this tutorial to set up
an ssh key for GitHub.

1. Generate an SSH Key
----------------------

1. Open a terminal.

2. Run the following command, replacing ``your_email@example.com`` with
   the email associated with your GitHub account:

   .. code:: sh

      ssh-keygen -t ed25519 -C "your_email@example.com"

3. When prompted, type the path and name of the key, hitting **Enter**
   to save it:

   ::

      $ Generating public/private ed25519 key pair.
      $ Enter file in which to save the key (/home/username/.ssh/id_ed25519): /home/username/.ssh/key_name

4. Enter a secure passphrase (optional, but recommended).

2. Add the SSH Key to the SSH Agent
-----------------------------------

1. Start the SSH agent in the background:

   .. code:: sh

      eval "$(ssh-agent -s)"

2. Add your private key to the SSH agent:

   .. code:: sh

      ssh-add ~/.ssh/key_name

2. (Alternate) Add target to SSH Config
---------------------------------------

1. Modify ~/.ssh/config and add the following:

   .. code:: sh

      Host github.com
       HostName ssh.github.com
       Port 443
       IdentityFile ~/.ssh/key_name

3. Add the SSH Key to GitHub
----------------------------

1. Copy your public key to the clipboard:

   .. code:: sh

      cat ~/.ssh/key_name.pub

2. Go to `GitHub SSH Key Settings <https://github.com/settings/keys>`__.

3. Click **New SSH key**.

4. Paste your public key into the “Key” field.

5. Give it a descriptive title.

6. Click **Add SSH key**.

4. Test the SSH Connection
--------------------------

Run the following command to verify the connection:

.. code:: sh

   ssh -T git@github.com

If successful, you should see a message like:

::

   Hi <your-username>! You've successfully authenticated, but GitHub does not provide shell access.

Troubleshooting
---------------

- If you encounter ``Permission denied (publickey)``, ensure that:

  - Your SSH key is added to GitHub and has not expired.
  - The SSH agent is running and the key is added (``ssh-add -l`` should
    list your key).
  - You are using the correct SSH URL.

--------------

Now you are ready to securely interact with GitHub using SSH!
