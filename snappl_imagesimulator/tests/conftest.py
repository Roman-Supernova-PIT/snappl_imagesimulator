# this is a module level file
import pytest # noqa: F401

import tox # noqa: F401
from tox.pytest import init_fixture # noqa: F401

from snappl.config import Config


@pytest.fixture( scope='session', autouse=True )
def init_config():
    Config.init( '/packages/snappl/snappl/tests/snappl_test_config.yaml', setdefault=True )
