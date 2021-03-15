from flask_sqlalchemy import SQLAlchemy

from app import app
import endpoints


app.config['SQLALCHEMY_DATABASE_URI'] = endpoints.POSTGRESQL_DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
