from sqlalchemy import ForeignKey
# from .db import db
# add environment and add_prefix-for_prod to existing import statement
from .db import db, environment, SCHEMA, add_prefix_for_prod

import simplejson as json
from decimal import Decimal
from .jtable import association_table

class Asset(db.Model):
    __tablename__= "assets"
    # add to every model file under __table_name__
    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey(add_prefix_for_prod('users.id')))
    stock_id = db.Column(db.Integer, ForeignKey(add_prefix_for_prod('stocks.id')))
    num_shares = db.Column(db.Numeric(precision=8, scale=2))

    user = db.relationship('User', secondary=association_table, back_populates='asset')
    stock = db.relationship('Stock', back_populates='asset2')
    transaction = db.relationship('Transaction', back_populates='asset')

    def asset_to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'stock_id': self.stock_id,
            'num_shares': json.dumps(Decimal(self.num_shares), use_decimal=True),
            'stock': self.stock.stock_to_dict()
        }

    def asset_to_dict_no_user(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'stock_id': self.stock_id,
            'num_shares': json.dumps(Decimal(self.num_shares), use_decimal=True)
        }

    def asset_to_dict_no_stock(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'stock_id': self.stock_id,
            'num_shares': json.dumps(Decimal(self.num_shares), use_decimal=True)
        }
