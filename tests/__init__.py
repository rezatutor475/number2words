# tests/__init__.py

"""
Test package initialization for the number-to-words conversion library.
Provides setup for shared fixtures, configuration, and custom test behavior.
"""

import sys
import os
import logging

# Configure logger for tests
logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] %(message)s')
logger = logging.getLogger("test_logger")
logger.debug("Initializing test environment...")

# Add parent directory to sys.path for direct imports from main package
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)
logger.debug(f"Added project root to sys.path: {project_root}")

# Shared constants or fixtures placeholder
DEFAULT_TEST_LANGUAGES = ['en', 'fa']

__all__ = ['logger', 'DEFAULT_TEST_LANGUAGES']
