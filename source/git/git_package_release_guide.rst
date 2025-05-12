Releasing a Package on Github
=============================

This guide details the pre release checks to undertake before releasing a package on github, and the actual release process on github. The guide requires no prior knowledge of creating software releases on Github. While this guide is developed for Github, the ideas themselves can be applied to releases on other git management systems (such as Gitlab).

Preamble
~~~~~~~~

The release version of the package is created as a stable self-contained version of the package (called a *Release*), tagging it with a version and creating accompanying metadata such as Release Notes and Changelogs. Depending on the development environment, Changelogs and version tags can be automated. Release notes are targeted at the end user, highlighting the features of the new release, whereas a Changelog is usually a detailed description of all changes since the last release version.

The standard convention for naming versions (also known as `Semantic Versioning <https://semver.org/>`__) is to tag a release as `MAJOR.MINOR.PATCH<alpha/beta>` where:

1. `MAJOR` refers to an update to the whole package that is backwards incompatible with the previous versions.
2. `MINOR` refers to either new features, functional updates, or a large number of bundled bug fixes.
3. `PATCH` refers to small bug fixes, hotfixes, or minor changes in the code. 
4. Optional tag `<alpha/beta>` (angular braces `<>` indicate optional keywords) - This indicates the package has been released but is currently being tested and may not be stable. `alpha` testing usually implies testing within the broader community of the team that developed the package, whereas `beta` testing implies a wider release to the audience/end users, who can then report bugs which can be fixed. 

On github, creating a release usually entails creating a stable version of the package on a branch, then creating a release tag for the specific stable commit. These branches can be standard main/develop or a dedicated release branch, which is usually dependent on the conventions of the organization creating the package. 

When numbering versions, in rare cases, a package may need to be released before it is tested, or even when it is in active development. These should be tagged as a `v0.MINOR.PATCH<alpha>` release and it is good practice to highlight that the release is unstable or in active development. Once a package has a first stable release, the leading digit should roll over to `v1.MINOR.PATCH<alpha>`. For all subsequent releases, the first digit should only roll over once backward compatibility is broken, so subsequent tags should go as `v1.0.0`, `v1.1.0`, `v1.2.0`, etc... 

Pre-release, release branches and archiving releases
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Note that the tagging of `v0.MINOR.PATCH<alpha>` is not the same as creating a Pre-release on github, as tagging a commit is not the same as creating a release. UASAL organization preference is to *NOT create Pre-release versions* of packages.

UASAL organization preference is to tag a release on the main branch. Prior to release, all feature branches should be merged into a develop branch, and then these changes should be pushed to the main branch and then tagged as a release from there. 

When releasing code alongside a paper, a user can archive a copy of the github code on Zenodo. Zenodo usually generates two DOIs for each archived code, one for the code as a whole, and one for the specific release tag. So, creating a release tag will create a new snapshot of the archived code on Zenodo. Thus, in future papers, authors can choose to reference the package as a whole, or specific versions of code that were used for analysis, provided they were tagged as a github release to trigger the Zenodo archiving process.

Checks before releasing a package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Prior to release, consider the following checks on your github repo:

1. Is the package on a stable release branch? Or will the package release be on the main/develop branch of the repo?
2. Does the release branch have any conflicts with the main/develop branches?
3. Do all the tests pass?
4. Does the release version have any dependencies/links to local files that are not in the repo? 
5. Are the installation instructions detailed, with the pre-requisites specified in the pyproject.toml file?
6. Does the code have any TODO or FIXME tags that need to be addressed before the release?
7. If using docstrings to create documentation, have all the docstrings been created/updated?
8. Does the README need to be updated?
9. Do the installation instructions need to be updated?
10. If the code comes with examples/notebooks, are these updated to work with the latest version of the code?
11. Is the release public? If so, are other users allowed to fork the repo?
12. Does the release require a discussion section? This may not be necessary with minor releases, but is encouraged for major releases.
13. Is the released version in alpha/beta testing?

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

While releases can be edited and deleted, edits after a release should be exceedingly rare, as all problems should be caught during the release PR. If there are bugs that were not addressed or found after the release, users should instead prefer to release a new version. *As an organization preference, no UASAL releases should be deleted.*
