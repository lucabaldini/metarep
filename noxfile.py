# Copyright (C) 2025 Luca Baldini (luca.baldini@pi.infn.it)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import pathlib
import shutil

import nox

from metarep import __name__ as __package_name__

# Basic environment.
_ROOT_DIR = pathlib.Path(__file__).parent
_SRC_DIR = _ROOT_DIR / "src" / __package_name__
_TESTS_DIR = _ROOT_DIR / "tests"
_DOCS_DIR = _ROOT_DIR / "docs"

# Folders containing source code that potentially needs linting.
_LINT_DIRS = ("src", "tests", "tools")

# Reuse existing virtualenvs by default.
nox.options.reuse_existing_virtualenvs = True


@nox.session(venv_backend="none")
def cleanup(session: nox.Session) -> None:
    """Cleanup temporary files.
    """
    # Remove all the __pycache__ folders.
    for folder_path in (_ROOT_DIR, _SRC_DIR, _TESTS_DIR):
        _path = folder_path / "__pycache__"
        if _path.exists():
            shutil.rmtree(_path)
    # Cleanup the docs.
    _path = _DOCS_DIR / "_build"
    if _path.exists():
            shutil.rmtree(_path)


@nox.session(venv_backend="none")
def docs(session: nox.Session) -> None:
    """Build the HTML docs.

    Note this is a nox session with no virtual environment, based on the assumption
    that it is not very interesting to build the documentation with different
    versions of Python or the associated environment, since the final thing will
    be created remotely anyway. (This also illustrates the use of the nox.session
    decorator called with arguments.)
    """
    source_dir = _DOCS_DIR
    output_dir = _DOCS_DIR / "_build" / "html"
    session.run("sphinx-build", "-b", "html", source_dir, output_dir, *session.posargs)


@nox.session
def ruff(session: nox.Session) -> None:
    """Run ruff.
    """
    session.install("ruff")
    #session.install(".[dev]")
    session.run("ruff", "check", *session.posargs)


@nox.session
def pylint(session: nox.Session) -> None:
    """Run pylint.
    """
    session.install("pylint")
    #session.install(".[dev]")
    session.run("pylint", *_LINT_DIRS, *session.posargs)


@nox.session
def test(session: nox.Session) -> None:
    """Run the unit tests.
    """
    session.install("pytest")
    #session.install(".[dev]")
    session.run("pytest", *session.posargs)