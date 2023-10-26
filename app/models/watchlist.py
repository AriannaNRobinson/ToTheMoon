from sqlalchemy import Column, ForeignKey
# from .db import db
# add environment and add_prefix-for_prod to existing import statement
from .db import db, environment, SCHEMA, add_prefix_for_prod
import datetime


class Watchlist(db.Model):
    __tablename__ = 'watchlist'
    # add to every model file under __table_name__
    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = Column(ForeignKey(add_prefix_for_prod('users.id')))
    stock_id = Column(ForeignKey(add_prefix_for_prod('stocks.id')))
    created_at = db.Column('created_at', db.DateTime, default=datetime.datetime.now, nullable=False)

    user = db.relationship("User", back_populates="stocks")
    stock = db.relationship("Stock", back_populates="users")


    def watchlist_to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'stock_id': self.stock_id,
            'created_at': self.created_at,
        }
