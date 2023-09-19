from app.database import db
from backend.app.models.user import User
from sqlalchemy.orm import relationship

class Message(db.Model):

    __tablename__ = "message"

    id =  db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    created = db.Column(db.DateTime(timezone=True), default=db.func.now())
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)

    user = relationship(User.__name__, backref="messages", cascade="all")