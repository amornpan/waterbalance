from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import plotly.express as px
import geopandas as gpd

app = Flask(__name__)
# Load configuration 
app.config.from_pyfile('system_configuration.py')
Bootstrap(app)

# Access configuration values
secret_key = app.config['SECRET_KEY']
database_uri = app.config['DATABASE_URI']
db_username = app.config['DB_USERNAME']
db_password = app.config['DB_PASSWORD']


@app.route('/')
def index():
    return "Water Balance"

@app.route('/mooban_map')
def mooban_map():
    # Read the shapefile
    gdf_mooban = gpd.read_file(
        'static/boundary_mooban_ll/boundary_mooban_ll.shp', encoding='cp874')

    # Create a map with Plotly Express and Mapbox for gdf_tambon
    fig = px.choropleth_mapbox(
        gdf_mooban,
        geojson=gdf_mooban.geometry,
        locations=gdf_mooban.index,
        color=gdf_mooban['MOO_NAME'],
        title="Interactive Map for gdf_mooban",
        center={"lat": gdf_mooban.geometry.centroid.y.mean(
        ), "lon": gdf_mooban.geometry.centroid.x.mean()},
        mapbox_style="carto-positron",
        zoom=10
    )

    # Calculate the figure size
    figure_width = 1090
    figure_height = 820

    # Set the figure size to fit the map content
    fig.update_layout(
        autosize=True,
        # width=figure_width,
        # height=figure_height,
        # Add margin to accommodate title and other elements
        margin={"r": 0, "t": 30, "l": 0, "b": 0}
    )

    # Render the map on the HTML template
    return render_template('mooban_map.html', plot=fig.to_html(full_html=False))


# if __name__ == '__main__':
#     host = '113.53.253.56'
#     port = 5000
#     app.run(host=host, port=port, debug=True)

if __name__ == '__main__':
    port = 5000
    app.run(host='0.0.0.0', port=port, debug=True)
