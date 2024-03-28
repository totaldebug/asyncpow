from __future__ import annotations

import nox
from nox.sessions import Session


@nox.session(reuse_venv=True)
def format(session: Session) -> None:
    """Run automatic code formatters"""
    session.run("poetry", "install", external=True)
    session.run("black", ".")
    session.run("isort", ".")
    session.run("autoflake", "--in-place", ".")


@nox.session(reuse_venv=True)
def test_types(session: Session) -> None:
    """Check that typing is working as expected"""
    session.run("poetry", "install", external=True)
    session.run("mypy", "--show-error-codes", ".")


@nox.session(reuse_venv=True)
def test_style(session: Session) -> None:
    """Check that style guidelines are being followed"""
    session.run("poetry", "install", external=True)
    session.run("flake8", ".")
    session.run(
        "black",
        ".",
        "--check",
    )
    session.run("isort", ".", "--check-only")
    session.run("autoflake", "-r", ".")
    session.run("interrogate", ".")
    session.run("bandit", ".")


@nox.session(reuse_venv=True)
def docs(session: Session) -> None:
    """Create local copy of docs for testing"""
    session.run("poetry", "install", external=True)
    session.run("sphinx-autobuild", "docs", "build")


@nox.session(reuse_venv=True)
def release(session: Session) -> None:
    """Release a new version of the package"""
    pypi_password = session.posargs[0]
    session.run("poetry", "install", external=True)
    session.run("npx", "semantic-release", "--debug")
    session.run("poetry", "build", external=True)
    session.run("poetry", "publish", "-u", "__token__", "-p", pypi_password, external=True)
