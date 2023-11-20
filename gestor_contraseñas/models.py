from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

# Utilizando SQLAlchemy conectamos SGBD.
db = SQLAlchemy()


# Creamos tabla usuario.
class User(db.Model, UserMixin):
    __tablename__ = "User"
    Id_user = db.Column(db.Integer, primary_key=True)
    Usuario = db.Column(db.String(45), nullable=False)
    Email = db.Column(db.String(45), nullable=False)
    Password = db.Column(db.String(30), nullable=False)

    services = db.relationship("Service", backref="user", lazy=True)

    def __repr__(self):
        return f"<Usuario {self.Email}>"

    def set_Password(self, Password):
        self.Password = generate_password_hash(Password)

    def check_password(self, password):
        return check_password_hash(self.Password, password)

    def save(self):
        if not self.Id_user:
            db.session.add(self)
        db.session.commit()


# Creamos tabla Servicios
class Service(db.Model, UserMixin):
    __tablename__ = "Service"
    Id_service = db.Column(db.Integer, primary_key=True)
    Description = db.Column(db.String(120), nullable=True)
    User = db.Column(db.String(45), nullable=False)
    Password = db.Column(db.String(30), nullable=False)
    Id_user = db.Column(db.Integer, db.ForeignKey("User.Id_user"), nullable=False)

    def set_Password(self, Password):
        self.Password = generate_password_hash(Password)

    def check_password(self, password):
        return check_password_hash(self.Password, password)

    def save(self):
        if not self.Id_service:
            db.session.add(self)
        db.session.commit()
