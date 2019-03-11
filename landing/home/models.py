from landing import db


class EmailSignup(db.Model):
    id          = db.Column(db.Integer) # primary_key
    full_name   = db.Column(db.String(120), nullable=True)
    email       = db.Column(db.String(120), unique=True, nullable=False)



# id, full_name, email
# 1, <>, <email>
# 2, justin, hello@teamcfe.com