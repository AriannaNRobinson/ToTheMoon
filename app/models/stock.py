# from .db import db
# add environment and add_prefix-for_prod to existing import statement
from .db import db, environment, SCHEMA, add_prefix_for_prod
import simplejson as json
from decimal import Decimal

class Stock(db.Model):
    __tablename__= "stocks"
    # add to every model file under __table_name__
    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    ticker = db.Column(db.String(6))
    long_name = db.Column(db.String(50))
    i_price = db.Column(db.Numeric(precision=8, scale=2))
    info1 = db.Column(db.String(255))
    info2 = db.Column(db.Text)
    info3 = db.Column(db.String(255))

    asset2 = db.relationship('Asset', back_populates='stock')
    users = db.relationship("Watchlist", back_populates="stock")


    def stock_to_dict(self):
        return {
            'id': self.id,
            'ticker': self.ticker,
            'long_name': self.long_name,
            'i_price' : json.dumps(Decimal(self.i_price), use_decimal=True),
            'info1' : self.info1,
            'info2' : self.info2,
            'info3' : self.info3
        }
