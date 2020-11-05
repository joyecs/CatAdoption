from django.contrib.contenttypes.models import ContentType
# move all data into new database.
# 1 create new database as DB
# 2 add DB into settings
# 3 run python manage.py migrate --run-syncdb --database DB
# 4 call this function
def migrate_db(db_name):
    pass
