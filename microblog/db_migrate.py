"""
The way SQLAlchemy-migrate creates a migration is by comparing the
structure of the database (obtained in our case from file database.db)
against the structure of our models (obtained from file app/models.py).

The differences between the two are recorded as a migration script inside
the migration repository. The migration script knows how to apply a
migration or undo it, so it is always possible to upgrade or downgrade
a database format.

Limitations: Currently works with +/- one at a time.
"""
import imp
import os.path
from migrate.versioning import api

from app import db
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO

version = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
migration = os.path.join(SQLALCHEMY_MIGRATE_REPO,
                         'versions',
                         ('%03d_migration.py' % (version + 1)))

tmp_module = imp.new_module('old_module')
old_module = api.create_model(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)

exec(old_module, tmp_module.__dict__)

script = api.make_update_script_for_model(SQLALCHEMY_DATABASE_URI,
                                          SQLALCHEMY_MIGRATE_REPO,
                                          tmp_module.meta,
                                          db.metadata)

open(migration, "wt").write(script)

api.upgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
version = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)

print('New migration set to: ' + migration)
print('Current active version:' + str(version))
