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

from requests import session
import nox

from metarep import METAREP_DOCS


@nox.session(venv_backend='none')
def docs(session: nox.Session) -> None:
    """Build the HTML docs.

    Note this is a nox session with no virtual environment, based on the assumption
    that it is not very interesting to build the documentation with different
    versions of Python or the associated environment, since the final thing will
    be created remotely anyway. (This also illustrates the use of the nox.session
    decorator called with arguments.)
    """
    source_dir = METAREP_DOCS
    output_dir = METAREP_DOCS / '_build' / 'html'
    session.run('sphinx-build', '-b', 'html', source_dir, output_dir, *session.posargs)


@nox.session
def ruff(session: nox.Session) -> None:
    """Run ruff.
    """
    session.install('ruff')
    session.run('ruff', 'check', 'src', 'tests', *session.posargs)


# @nox.session
# def ruff(session: nox.Session) -> None:
#     """Run pylint.
#     """
#     session.install('pylint')
#     session.run('ruff', 'check', 'src', 'tests', *session.posargs)