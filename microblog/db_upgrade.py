"""
This script upgrades the database to the latest revision, 
by applying the migration scripts stored in the database repository.
"""
from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO

# Migrate andn upgrade current database to new migration rule set
api.upgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)

# Update version to reflect changes.
version = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)

# Output to console
print('\nCurrent database version: ' + str(version))
