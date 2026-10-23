from importlib.metadata import version, PackageNotFoundError
__all__ = []



try:
    __version__ = version("snappl_imagesimulator")
except PackageNotFoundError:
    # package is not installed
    pass
