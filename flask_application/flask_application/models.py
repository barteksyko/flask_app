from flask_application import db


class Checker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    check = db.Column(db.String(10), unique=True, nullable=False)
    check2 = db.Column(db.String(10), unique=True, nullable=False)
    check3 = db.Column(db.String(10), unique=True, nullable=False)
    check4 = db.Column(db.String(10), unique=True, nullable=False)

    def __repr__(self):
        return f"TO1:{self.check}, TO2:{self.check2}, ODZ:{self.check3}, Remote:{self.check4}"


class Slider(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    slider = db.Column(db.String(100), unique=True, nullable=False)
    slider2 = db.Column(db.String(100), unique=True, nullable=False)
    slider3 = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return f"slider:{self.slider}, slider2:{self.slider2}, slider3:{self.slider3}"
