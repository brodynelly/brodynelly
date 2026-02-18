"""Smoke tests for the GitHub profile README."""
import pathlib

ROOT = pathlib.Path(__file__).parent.parent


def test_readme_exists():
    assert (ROOT / "README.md").exists(), "README.md not found"


def test_readme_not_empty():
    content = (ROOT / "README.md").read_text()
    assert len(content) > 100, "README is too short"


def test_readme_has_contact_info():
    content = (ROOT / "README.md").read_text()
    assert "linkedin" in content.lower() or "email" in content.lower(), \
        "README should have contact info"
