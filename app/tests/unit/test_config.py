from config import ConfigApp


def test_config_setups():
    # Test that the class if has an attribute(setup)
    assert hasattr(ConfigApp, "GITHUB_USER_NAME")
