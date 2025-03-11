Using Git Large File Storage (LFS)
==================================

Git LFS is an additional git system which can help you manage
particularly large files. The true advantage of Git LFS comes from the
fact that when you clone a repo, you clone the history, so if a 50 MB
file has been modified 100 times, now you’re looking at a ~ 50 GB
download. Git LFS allows you to store the iterations on the server,
without overloading your machine disk space by only downloading the
checked out version of the file, and pointers to the history. Now, you
can absolutely just go ahead and follow instructions on the `git lfs
website <https://git-lfs.com/>`__. These will work, however the notes
down here also emphasize some additional points/pitfalls so read on if
you are installing for the first time and want to be extra cautious.

Installation
~~~~~~~~~~~~

Installation instructions `can be found
here <https://github.com/git-lfs/git-lfs?utm_source=gitlfs_site&utm_medium=installation_link&utm_campaign=gitlfs#installing>`__.
You can also install via Conda (not explicitly mentioned anywhere) using

::

   conda install git lfs

Note: At least on linux, ‘git lfs’ and ‘git-lfs’ result in the same
functionality.

After installation, you need to initialize LFS for your git account by
running -

::

   git lfs install

You only need to do this ONCE per git account on your machine. At this
point, LFS should be installed and initialized on your machine. You can
double check this by running ``git lfs --version``

Usage
~~~~~

The way LFS works is by tracking the file(s) you tell it to track,
typically using a wildcard expression (as used in shell script) or by
specifying individual files. These commands are tracked in the
``.gitattributes`` file. Usually, large file tracking means you pick a
type of file (``.fits``, ``.csv``, etc…) and just track all such files
at once. The important thing is the order you add files in and the order
in which you enable LFS.

Adding files to Git LFS for the first time
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is a tested algorithm to initialize using Git LFS to track ALL
files of a specific type (``*.fits`` in this example) in your entire
repo, which has previously not been initialized with LFS. For this,
first remove all files of the type you wish to track from the repo, so
in this case, remove all fits files from the repo.

1.  Navigate to the git repo you would like to add LFS files to.

2.  **Initialize all submodules** (Recursively by digging into every
    directory). This is to make sure none of these activate/create a
    .gitattributes file.

3.  Once everything is initialized, make sure there isn’t a pre-existing
    ``.gitattributes`` file in the repo.

4.  Double check you aren’t tracking any files by running
    ``git lfs ls-files``. This should return empty.

5.  Run ``git lfs track "*.fits"`` to start tracking fits files. Then
    check that your tracking command has created a new
    ``.gitattributes`` file, but with nothing written in it. Or, if you
    already had one, make sure no new line has been added.

6.  Add and commit the changes to your ``.gitattributes`` file

    ::

       git add .gitattributes; git commit -m "Some message here"; git push origin <branch name>

7.  Now copy the fits files you want to upload to git lfs to the
    directory.

8.  If you check ``git lfs ls-files`` this should still show up empty
    since you haven’t added any files yet to your git, just the rule and
    copied untracked files. Your ``.gitattributes`` file should also
    still be empty.

9.  Add your fits file to your git using

    ::

       git add <fits_file_name>

    Now your ``git lfs ls-files`` and ``.gitattributes`` should both
    finally be tracking this file.

10. Commit and push. The top of your push block should include an LFS
    statement and look something like this -

::

   Uploading LFS objects: 100% (1/1), 230 MB | 21 MB/s, done.
   Enumerating objects: 4, done.
   Counting objects: 100% (4/4), done.
   Delta compression using up to 22 threads
   Compressing objects: 100% (3/3), done.
   Writing objects: 100% (3/3), 398 bytes | 398.00 KiB/s, done.
   Total 3 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
   remote: Resolving deltas: 100% (1/1), completed with 1 local object.
   To github.com:sanchitsabhlok/wcc_designdocs.git
   305b05e..cee5dfb  develop -> develop

And that’s it! Any future ``*.fits`` files that are added to git should
be automatically tracked and handled by git lfs. If you ``git clone`` a
directory, you should only get a pointer to the file, not the file
itself. To download the large file you need to run -

::

   git lfs pull

You’ll know this worked because it will trigger a long download. Your
file structures will look identical, but with real data there. A final
note, while this workflow is to add a particular type of file, it is
applicable to individual files as well, i.e. ``*.fits`` can be replaced
by something like ``zodiacal.fits`` to track an individual file.

Working with a repo with LFS support
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you are cloning a git repo that uses LFS from a machine, then after
cloning the directory, you can initialize git lfs for this new repo with
``git lfs install`` and enable the lfs features for the new repo. Your
``pull`` and ``commit`` commands should work normally with git. If for
whatever reason there are issues pulling LFS files, you can explicitly
run ``git lfs pull``. For further description, check the `Atlassian
tutorial on Git
LFS <https://www.atlassian.com/git/tutorials/git-lfs#pulling-and-checking-out>`__.

Usage Limitations and recommendations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

LFS is great but there are limits. You cannot use arbitrary large files.
There is a **total** 1 GB limit to the total memory AND bandwidth usage.
The limits depend on your github plan and `can be found
here <https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-git-large-file-storage>`__.
There are also further important clarifications regarding the usage, how
different file versions are handled and the total bandwidth usage.
`These can be found
here <https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-storage-and-bandwidth-usage>`__.

Essentially, LFS should not be used for very large files unless you have
a billing plan. Even if you do, its worth exploring alternate options.

LFS is encouraged to store files that may be required for unit tests,
especially when you might have a large number of small files. These file
sizes should still be minimized for faster performance. The reason here
is due to the large number of individual processes opened for different
versions of files when files are pulled/cloned. By using LFS, only the
most recent files are checked out. You can also consider using LFS for
auto generated artifact files, especially if they are regenerated often.
This is because these files are usually not tracked and reviewed by
humans and their size and volume can grow in the background and slow
performance without any warnings.

Git LFS can also be `sped up with explicit
calls <https://www.atlassian.com/git/tutorials/git-lfs#speeding-up-pulls>`__.
Git can create a batch for large numbers of files and greatly reduce
speed issues due to process spawning. This does require some config
rejig -

::

   git -c filter.lfs.smudge= -c filter.lfs.required=false pull && git lfs pull

You can create an alias for yourself for a speedy pull

::

   $ git config --global alias.plfs "\!git -c filter.lfs.smudge= -c filter.lfs.required=false pull && git lfs pull"
   $ git plfs
