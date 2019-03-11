from landing import db


class EmailSignup(db.Model):
    id          = db.Column(db.Integer, primary_key=True) # primary_key
    full_name   = db.Column(db.String(120), nullable=True)
    email       = db.Column(db.String(120), unique=True, nullable=False)

    def save(self, commit=True):
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


# id, full_name, email
# 1, <>, <email>
# 2, justin, hello@teamcfe.com