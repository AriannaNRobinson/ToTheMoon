from flask_sqlalchemy import SQLAlchemy

# added for render
# add import and set variable to access flask environment
import os
environment = os.getenv("FLASK_ENV")
SCHEMA = os.environ.get('SCHEMA')
# end

db = SQLAlchemy()

# added for render
# add function to add a prefix to table names in production environment only
def add_prefix_for_prod(attr):
    if environment == "production":
        return f"{SCHEMA}.{attr}"
    else:
        return attr
# end