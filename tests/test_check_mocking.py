import importlib

from pytest_mock import MockFixture

import check_mocking.mocking


def get_bar():
    importlib.reload(check_mocking.mocking)
    from check_mocking.mocking import Bar

    return Bar()


def test_check_mocking(mocker: MockFixture):
    mocker.patch("check_mocking.mocking.foo", mocker.Mock())
    get_bar().run()
