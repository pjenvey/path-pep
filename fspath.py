import abc
import typing as t


class PathLike(abc.ABC):

    """Abstract base class for implementing the file system path protocol."""

    @abc.abstractmethod
    def __fspath__(self) -> t.Union[str, bytes]:
        """Return the file system path representation of the object."""
        raise NotImplementedError


def fspath(path: t.Union[PathLike, str, bytes]) -> t.Union[str, bytes]:
    """Return the string representation of the path.

    If str or bytes is passed in, it is returned unchanged.
    """
    if isinstance(path, (str, bytes)):
        return path

    # Work from the object's type to match method resolution of other magic
    # methods.
    path_type = type(path)
    try:
        return path_type.__fspath__(path)
    except AttributeError:
        if hasattr(path_type, '__fspath__'):
            raise

        raise TypeError("expected str, bytes or os.PathLike object, not "
                        + path_type.__name__)
