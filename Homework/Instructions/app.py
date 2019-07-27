import numpy as np
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def Home():
    """ Welcome"""
    return (
        f"Welcome<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
         f"/api/v1.0/stations<br/>"
          f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start</br/>"
        f"/api/v1.0/start/end"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return a list of precipitation data including the date, prcp"""
     #  Calculate the date 1 year ago from the last data point in the database
    latest_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    #print(latest_date)
    one_year_ago=dt.date(2017,8,23) -dt.timedelta(days=365)
    #print(one_year_ago)
    # Perform a query to retrieve the data and precipitation scores
    prec_date =session.query(Measurement.date,Measurement.prcp).\
    filter(Measurement.date <= '2017-08-23').filter(Measurement.date>'2016-08-23').order_by(Measurement.date).all() 
    #Convert the query results to a Dictionary using date as the key and prcp as the value.
    prec_data = []
    for date,prcp in prec_date:
      prec_dict = {}
      prec_dict["date"] = date
      prec_dict["prcp"] = prcp
      prec_data.append(prec_dict)
    return jsonify(prec_data)   

    
@app.route("/api/v1.0/stations")
def stations():
    """Return a JSON list of stations from the dataset."""
    session = Session(engine)
    # Query to list station name with ID
    stations = session.query(Station.name, Station.station).order_by(Station.name).all()
    # Convert list of tuples into normal list
    all_stations = list(np.ravel(stations))
    return jsonify(all_stations)


@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    """Return a JSON list of Temperature Observations (tobs) for the previous year."""
    # query for the dates and temperature observations from a year from the last data point.
    latest_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    #print(latest_date)
    one_year_ago=dt.date(2017,8,23) -dt.timedelta(days=365)
    tob = session.query(Measurement.date, Measurement.tobs).\
              filter(Measurement.date > one_year_ago).\
                order_by(Measurement.date).all()
    #print(tob)
    # Convert list of tuples into normal list
    all_tobs = list(np.ravel(tob))
    return jsonify(all_tobs)    

# find the min,max,avarage temperature
@app.route('/api/v1.0/<start>')
@app.route('/api/v1.0/<start>/<end>')
def temperature(start=None,end=None):
  session = Session(engine)
#when given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive'''
  if end != None:
       temp_start_end = session.query(func.min(Measurement.tobs),func.avg(Measurement.tobs),func.max(Measurement.tobs)).\
                        filter(Measurement.date >= start).filter(Measurement.date <= end).all()
#When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
  else:
       temp_start_end = session.query(func.min(Measurement.tobs),func.avg(Measurement.tobs),func.max(Measurement.tobs)).\
                         filter (Measurement.date >= start).all()
   #convert list of tuple into normal list
  temp_start_end_rav = list(np.ravel(temp_start_end))
  return jsonify(temp_start_end_rav)

if __name__ == '__main__':
    app.run(debug=True, port = 9999)
