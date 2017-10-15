"""
This script will downgrade the database one revision.
You can run it multiple times to downgrade several revisions.
"""
from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO

# Get current version
version = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)

# Modify current version to previous state, currently last commit
api.downgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, (version - 1))

# Alter version to reflect changes
version = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)

print('\nCurrent database version: ' + str(version))
