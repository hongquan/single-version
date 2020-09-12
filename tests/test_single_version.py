from single_version import __version__
from single_version.ver import _REGEX_VERSION


def test_version():
    assert __version__ == '1.3.0'


def test_version_regex():
    assert _REGEX_VERSION.match('version="1.2"')


def test_version_regex_with_prefix():
    assert _REGEX_VERSION.match('version="v1.2"')


def test_version_regex_with_patch():
    assert _REGEX_VERSION.match('version="1.2.3"')


def test_version_regex_prerelease():
    assert _REGEX_VERSION.match('version="1.2.3-alpha"')


def test_version_regex_prerelease_revision():
    assert _REGEX_VERSION.match('version="1.2.3-alpha.4"')


def test_version_regex_metadata():
    assert _REGEX_VERSION.match('version="1.2.3+456789abc"')
