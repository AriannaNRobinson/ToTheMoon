from sqlalchemy import Table, Column, ForeignKey
# from .db import db
# add environment and add_prefix-for_prod to existing import statement
from .db import db, environment, SCHEMA, add_prefix_for_prod

association_table = Table('association', db.Model.metadata,
    Column('left_id', ForeignKey(add_prefix_for_prod('users.id')), primary_key=True),
    Column('right_id', ForeignKey(add_prefix_for_prod('assets.id')), primary_key=True)
)

