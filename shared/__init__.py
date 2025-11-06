"""Shared modules for agent collaboration."""

from .state import SharedState
from .utils import save_to_file, load_from_file

__all__ = ['SharedState', 'save_to_file', 'load_from_file']
