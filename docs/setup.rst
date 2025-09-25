.. _setup:

Repository setup
================

Setting up a respository on |GitHub| is easied done than said: assuming that you
have an account that you are logged in into, you should see a nice, shining, green
"New" button somewhere that will bring you to a new page guiding you through the
creation of a brand new repository.

You will have to pick out a name---choose a nice, short and expressive one, if you
want your next software creation to go viral---and go through a few configuration
steps. If you are unsure about any of them and want to follow the least action
principle, here is a few suggestions:

* make it public (unless you foresee the possibility of holding sensitive data);
* add ``README``? Yes: this will be the first thing that people will see on
  the landing page for your repo;
* add ``.gitignore``? Yes, in the Python flavor. If you take anything on this
  repo serisouly, the file will be useful to you;
* add ``license``? Yes, GPL 3, please.


Interacting with the repository
-------------------------------

Did you just create the first repository on |GitHub|? Congratulations! You are
not quite there, yet, but halfway through.

For one thing, you will have to install `git <https://git-scm.com/>`_ on your machine and
make sure it is available in your working environment. At this point, ideally, you
would be able to do

.. code-block::

  cd some/where
  git clone git@github.com:lucabaldini/metarep.git

and that's it! You have a brand new clone of your repo, you can checkout your
favorite revision and start coding!


.. note::

  Where do I find the actual link to clone a git repo? Well, it shouldn't be `too`
  hard to construct it from username and project name, but just in case you should
  see a big, green "Code" button at the top of the page, and if you click on that
  you should get a drop-down menu with a few tabs. Pick ``SSH`` and go to the next
  section.


SSH and all that
----------------

This is one of the instances where we are not going to read the fine prints and
go straight to the solution: `use SSH for day-to-day cloning/pushing from your machines`.
In order to do that you will have to `exchange a ssh key` with |GitHub|.

.. note::

  SSH, or `Secure Shell`, is a network protocol and a set of tools for securely
  accessing and controlling a remote computer over a network.

  Creating an SSH key pair means generating two mathematically linked keys:

  * a private key (keep secret): stays on your machine, optionally protected by a
    passphrase.
  * a public key (share freely): you upload it to the server or service (e.g., GitHub).

  The two work together via public-key (asymmetric) crypto. During login, the server
  sends a challenge; your SSH client proves it has the private key by signing that
  challenge. The server verifies the signature using the public key it has on file---no
  password travels over the network.

In reality, you don't have to be crypto-ninja to use |GitHub|. All you need to understand
that:

* you need a private ssh key (which you can create) `and` ssh agent
  (which you usually have) on your working computer;
* GitHub needs to know the corresponding public ssh key.

Roughly speaking, from a practical standpoint this entails to creating a pair
of ssh keys

.. code-block::

  ssh-keygen

and copy the `public` key to |GitHub|---go to the global "Settings" -> "SSH and GPG keys"
and push the "New SSH" green button.

Windows
-------

1. Open Windows Powershell.
2. Generate a new SSH key pair (use your own email!):

.. code-block:: shell

 ssh-keygen -t ed25519 -C "example@email.com"

3. Copy the public SSH key to your clipboard:

.. code-block:: shell

 cat ~/.ssh/id_ed25519.pub | clip

4. Copy the `public` key to |GitHub|---go to the global "Settings" -> "SSH and GPG keys" -> push the "New SSH" green button
5. Paste your public key into the "Key" field and give it a title.
6. Test your SSH connection:

.. code-block:: shell

 ssh -T git@github.com

If this message appears: ``Are you sure you want to continue connecting (yes/no/[fingerprint])?`` type ``yes`` and press Enter.
If successful, you should see a message like:
  Hi username! You've successfully authenticated, but GitHub does not provide shell access.

You should now (hopefully) be able to clone your repo using the ssh link.


.. todo::

  We should add specific instructions for Mac OS.

Just for fun, the public ssh key on my personal laptop is

.. code-block:: shell

  less ~/.ssh/id_ed25519.pub
  ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIHX+HHa/GY+YFzuYE/11xDWpNSmc18UQl0P9RxCM7zbh lbaldini@wlguest23.pi.infn.it

There is no harm in publicly showing your public ssh key. You should never, ever tell
annybody what the corresponding private key is---not even under torture.

.. warning::

  When you create a pair of ssh keys, you have the option of setting a password for
  the private key. Shall you?

  Well, it depends. Having a password adds extra security and is always a good practice.
  On the other hand, if you set a password, you will have to type it every time
  you push a change to the remote repo. If you are the only one using the
  computer and you are not using the pair of ssh keys for something particularly
  sensitive, go ahead and press enter for an empty password (i.e., no password)---you
  will thank yourself you did when you start coding.



