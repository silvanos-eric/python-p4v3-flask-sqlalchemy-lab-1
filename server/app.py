# server/app.py
#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Earthquake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)


@app.route('/')
def index():
    body = {'message': 'Flask SQLAlchemy Lab 1'}
    return make_response(body, 200)


# Add views here
@app.route("/earthquakes/<int:id>")
def earthquakes(id):
    earthquake = Earthquake.query.filter_by(id=id).first()
    if earthquake:
        return {
            "id": earthquake.id,
            "location": earthquake.location,
            "magnitude": earthquake.magnitude,
            "year": earthquake.year
        }
    return {"message": f"Earthquake {id} not found."}, 404


@app.route("/earthquakes/magnitude/<float:magnitude>")
def earthquake_magnitude(magnitude):
    quakes = Earthquake.query.filter(Earthquake.magnitude >= magnitude).all()
    count = len(quakes)
    if count > 0:
        return {
            "count":
            count,
            "quakes": [{
                "id": quake.id,
                "location": quake.location,
                "magnitude": quake.magnitude,
                "year": quake.year
            } for quake in quakes]
        }
    return {"count": count, "quakes": quakes}


if __name__ == '__main__':
    app.run(port=5555, debug=True)
