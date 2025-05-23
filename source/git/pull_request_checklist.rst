.. |uncheck| raw:: html 
  
  <input type="checkbox">

.. |br| raw:: html

  <br>

Pull Request Checklist
======================

*When performing a pull or merge request (PR or MR), ensuring the
following are completed helps minimize unnecessary notifications to
reviewers and helps ensure your PR is reviewed promptly and traceable.*

Creating PR
-----------

*List of items to check / general guidelines for when creating a new
Pull Request under a repository.*

|uncheck| Select a PR template *if applicable* |br|
|uncheck| Edit Pull Request Name

  -  Pull Request **should** have the branch title in the description that is to be merged in.
  -  Ex: ``Merge pingraham/initial-dev-guide into develop``

|uncheck| Open Pull Request as *draft* |br|
|uncheck| Add assignees |br|
|uncheck| Add relevant tags and projects

  -  This includes setting a status for the PR if you add a project association to the PR

|uncheck| Add links to related issues |br|
  -  Refer to the `GitHub Docs <https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue>`__ if you want to use closing syntax (auto-close issues after a PR is merged) |br|

Marking for Review
------------------

*List of steps for when PR is ready for reviewing and what to check
after approval has been received.*

|uncheck| Add reviewers |br|
|uncheck| Select ‘ready for review’ to change Pull Request out of draft state |br|
|uncheck| Notify reviewers PR is ready

  -  If you think the reviewer may not already be aware, it is sometimes helpful to notify them the PR is ready by `@`-ing them within the PR to inform them.

After Review
-------------

|uncheck| Verify all open / unresolved conversations are closed out (if applicable). |br|
  -  Conversations *should* be resolved by the reviewer that made the comment **not** the assignee.
  -  If a suggestion is applied within a PR, GitHub will auto-resolves the conversation (this is acceptable).

|uncheck| Squash excess commits together *if applicable* |br|
  -  Select the ``Squash and Merge`` *or equivalent* option on GitHub **after** PR is approved if you want to squash all commits together

|uncheck| Update Issue Statuses *if applicable* |br|
|uncheck| Update Source/Feature branch *if applicable* for linear history |br|
|uncheck| Remove feature / ‘working’ branch after PR is complete *if* no longer being used |br|


**Note:** Refer to the :doc:`Git-Flow-Guide <git-flow-guide>` for additional assistance as needed.

