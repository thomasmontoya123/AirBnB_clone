#!/usr/bin/env python3
"""init wrapper"""
from .engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
