.. _actions:

GitHub actions
==============

In the same way that nox allows to automate local tasks, GitHub actions can be
used to automate repetitive tasks in the cloud. This means you can set up workflows
that run on specific events (e.g., push, pull request) and perform actions such as
running tests, building packages, or deploying code without manual intervention.

The basic concept of GitHub actions is that of a `workflow`, which is implemented
in the form of a YAML file under ``.github/workflows/``. We have already seen
examples of workflows for continuous integration and deployment, and you find
all the documentation `here <https://docs.github.com/en/actions/how-tos/write-workflows>`__.