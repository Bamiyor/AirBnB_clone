#!/usr/bin/python3
"""__init__ magic method for models directory"""
from models.engine.file_storage 
import models.engine.file_storage as fs

storage = fs.FileStorage()
storage.reload()
