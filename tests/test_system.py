import sys
import pytest


pytestmark = pytest.mark.skipif(
    sys.platform == 'win32',
    reason='unix system helpers are not available on Windows')


def test_open_command_uses_xdg_open(monkeypatch):
    from thefuck.system import unix

    monkeypatch.setattr('thefuck.system.unix.which',
                        lambda executable: '/usr/bin/' + executable)

    assert unix.open_command('https://example.com') \
        == 'xdg-open https://example.com'


def test_open_command_falls_back_to_open(monkeypatch):
    from thefuck.system import unix

    monkeypatch.setattr('thefuck.system.unix.which',
                        lambda executable: None)

    assert unix.open_command('https://example.com') \
        == 'open https://example.com'
