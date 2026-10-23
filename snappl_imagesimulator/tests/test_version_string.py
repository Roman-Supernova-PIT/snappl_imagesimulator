def test_version_is_string():
    from snappl_imagesimulator import __version__
    assert isinstance(__version__, str)
