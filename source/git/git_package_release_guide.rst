Releasing a Package on Github
=============================

This guide details the checks to undertake before releasing a package on github, the UASAL guidelines on releasing the package, and the actual release process on github. The guide requires no prior knowledge of creating software releases on Github. While this guide is developed for Github, the ideas themselves can be applied to releases on other git management systems (such as Gitlab).

Preliminaries
~~~~~~~~~~~~~

The release version of the package is created by creating a stable self-contained version of the package (called a *Release*), tagging it with a version and creating accompanying metadata such as Release Notes and Changelogs. Depending on the development environment, Changelogs and version tags can be automated. Release notes are targeted at the end user, highlighting the features of the new release, whereas a Changelog is usually a detailed description of all changes since the last release version.

The standard convention for naming versions (also known as `Semantic Versioning <https://semver.org/>`__) is to tag a release as MAJOR.MINOR.PATCH where
1. MAJOR refers to an update to the whole package that is backwards incompatible with the previous versions.
2. MINOR refers to either new features, functional updates, or a large number of bundled bug fixes.
3. PATCH refers to small bug fixes, hotfixes, or minor changes in the code. 

On github, creating a release usually entails creating a stable version of the package on a branch, then creating a release tag for the specific stable commit. These branches can be standard main/develop or a dedicated release branch, which is usually dependent on the conventions of the organization creating the package. 

Pre-Release Checks
~~~~~~~~~~~~~~~~~~

Prior to release, consider the following checks on your github repo:

1. Is the package on a stable release branch? Or will the package release be on the main/develop branch of the repo?
2. Does the release branch have any conflicts with the main/develop branches?
3. Do all the tests pass?
4. Does the release version have any dependencies/links to local files that are not in the repo?
5. Does the code have any TODO or FIXME tags that need to be addressed before the release?
6. If using docstrings to create documentation, have all the docstrings been created/updated?
7. Does the README need to be updated?
8. Do the installation instructions need to be updated?
9. If the code comes with examples/notebooks, are these updated to work with the latest version of the code?
10. Is the release public? If so, are other users allowed to fork the repo?
11. Does the release require a discussion section? This may not be necessary with minor releases, but is encouraged for major releases.
12. Is the released version in alpha/beta testing?

Release Procedure
~~~~~~~~~~~~~~~~~

Once all checks have been completed and any issues have been resolved, users can draft a new release `On Github <https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository>`__

The remainder of this guide is an abbreviated reproduction of the release guide from Github, with additional comments where deemed necessary:

1. Create a new release from the sidebar on the github repo.
2. Write down the release tag, or pick one. This should be dictated by semantic versioning.
3. Select the branch to be used as the target for the release from the *Target* dropdown menu.
4. If this is an update, the *Previous Tag* option will display previous release tags. This release tag is useful for autogenerating release notes and Changelogs, if the user chooses to do so. At the very least, it will be useful in creating an initial draft that can be suitably modified. If this is a brand new release version, no previous version will be available for selection in the *Previous tag* dropdown. 
5. Proof read the release notes for clarity, consistency and to ensure sharing of necessary and important information.
6. Add any binaries to be released alongside the code. 
7. If this is a *Pre-release*, check the *Set as a pre-release* checkbox.
8. If this is set to be the latest release, check the *Set as the latest release* checkbox. This will not be visible for a first release.
9. Before finalizing, make sure that if there are any Git LFS objects in the repo, they are `managed appropriately in the release <https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/managing-git-lfs-objects-in-archives-of-your-repository>`__.
10. Publish the release!

After the Release
~~~~~~~~~~~~~~~~~

Releases can be edited and deleted, including updating the commit for a specific release tag, if assigned incorrectly, or if hotfixes were implemented after a release was published. While this should be done sparingly, it is a good option to fix any errors/problems with the release. 
