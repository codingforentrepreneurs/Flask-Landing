import datetime
from landing import db

from sqlalchemy import event

class EmailSignup(db.Model):
    id          = db.Column(db.Integer, primary_key=True) # primary_key
    full_name   = db.Column(db.String(120), nullable=True)
    email       = db.Column(db.String(120), unique=True, nullable=False)
    timestamp   = db.Column(db.DateTime, index=True, default=datetime.datetime.utcnow)
    updated     = db.Column(db.DateTime, index=True, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    

    def save(self, commit=True):
        # create and update
        if commit:
            instance = self
            if not instance.id:
                db.session.add(instance)
            try:
                db.session.commit()
            except Exception as e:
                print("Exception occured\n", e, '\n')
                db.session.rollback()
                return False
            return True
        return False

    def delete(self, commit=True):
        # delete
        if self.id:
            db.session.delete(self)
            try:
                db.session.commit()
            except Exception as e:
                print("Exception occured\n", e, '\n')
                db.session.rollback()
                return False
            return True
        return False





# https://docs.sqlalchemy.org/en/latest/orm/events.html


# before_insert 
# after_insert

# before_update
# after_update

# before_delete
# after_delete

@event.listens_for(EmailSignup, 'before_update')
def email_signup_pre_update_signal(mapper, connection, target):
    pass
    # target = instance
    # target.full_name = target.full_name + " working..."
    # if target.slug is None:
    #     target.slug = full_name.lower().replace(" ", "-")

@event.listens_for(EmailSignup, 'after_update')
def email_signup_post_update_signal(mapper, connection, target):
    # target = instance
    assert target.id is not None






