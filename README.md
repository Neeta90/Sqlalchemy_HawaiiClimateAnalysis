# Hawaii climate analysis
In this assignment, I did climate analysis on Honolulu, Hawaii!. I used Python and SQLAlchemy to do basic climate analysis and data exploration.

**Precipitation Analysis :** : By using a query to retrieve the last 12 months of precipitation data.and plot the result with 'date' and                                    'prcp'.

![Precipitation Analysis](https://user-images.githubusercontent.com/50187921/69100592-18893600-0a23-11ea-9dcd-03e424470bf0.png)

**Station Analysis :**     calculated number of stations and find out most active station and Plotted the histogram for last 12 months of                              temperature observation data (tobs).

![tob](https://user-images.githubusercontent.com/50187921/69100845-b7159700-0a23-11ea-869e-12c88bcf670f.png)

**Climate App :**          Designed a Flask API and created all routes that are available based on the developed queries.


 `/api/v1.0/precipitation`
 
Query for the dates and temperature observations from the last year.

`/api/v1.0/stations`

Return a json list of stations from the dataset.

`/api/v1.0/tobs`

Return a json list of Temperature Observations (tobs) for the previous year

`/api/v1.0/<start> and /api/v1.0/<start>/<end>`

Return a json list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

**Temperature Analysis :**  Plotted Bar chart for the min, avg, and max temperature by using  the calc_temps function to calculate the min,                             avg,and max temperatures for  trip using the matching dates from the previous year.


![tripavg](https://user-images.githubusercontent.com/50187921/69101002-0f4c9900-0a24-11ea-854a-3c6f2b2896b4.png)


**Daily Rainfall Average :** Plotted an area plot  for the daily normals by using 'daily_normals' function which calculate the daily normals                             for a specific date

![temppreyear](https://user-images.githubusercontent.com/50187921/69101454-466f7a00-0a25-11ea-88bb-f03ffe3b53a0.png)

