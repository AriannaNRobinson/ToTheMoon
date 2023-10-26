from sqlalchemy import ForeignKey
# from .db import db
# add environment and add_prefix-for_prod to existing import statement
from .db import db, environment, SCHEMA, add_prefix_for_prod
import simplejson as json
from decimal import Decimal

class Wallet(db.Model):
    __tablename__= "wallets"
    # add to every model file under __table_name__
    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
    
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Numeric(precision=8, scale=2), nullable=False)
    user_id = db.Column(db.Integer, ForeignKey(add_prefix_for_prod('users.id')))
    
    user = db.relationship("User", back_populates="wallet")
    
    def wallet_to_dict(self):
        return {
            'id': self.id,
            'amount': json.dumps(Decimal(self.amount), use_decimal=True),
            'user_id': self.user_id,
            'user' : self.user.to_dict_no_wallet()         
        }
        
    def to_dict_no_user(self):
        return {
            'id': self.id,
            'amount': json.dumps(Decimal(self.amount), use_decimal=True),
            'user_id': self.user_id
        }