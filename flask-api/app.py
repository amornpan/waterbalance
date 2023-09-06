from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import plotly.express as px
import geopandas as gpd
import plotly.graph_objects as go

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

    # Calculate the center of the GeoDataFrame
    center_lat = gdf_mooban.geometry.centroid.y.mean()
    center_lon = gdf_mooban.geometry.centroid.x.mean()

    # Calculate the bounds of the GeoDataFrame
    min_lat, max_lat = gdf_mooban.geometry.bounds['miny'].min(
    ), gdf_mooban.geometry.bounds['maxy'].max()
    min_lon, max_lon = gdf_mooban.geometry.bounds['minx'].min(
    ), gdf_mooban.geometry.bounds['maxx'].max()

    # Set the zoom level based on the bounds
    zoom = 10.00  # You can adjust this value to your preference

    # Create a map with Plotly Express and Mapbox for gdf_mooban
    fig = px.choropleth_mapbox(
        gdf_mooban,
        geojson=gdf_mooban.geometry,
        locations=gdf_mooban.index,
        color=gdf_mooban['MOO_NAME'],
        title="Interactive Map for gdf_mooban",
        center={"lat": gdf_mooban.geometry.centroid.y.mean(
        ), "lon": gdf_mooban.geometry.centroid.x.mean()},
        mapbox_style="carto-positron",
        zoom=zoom
    )

    # Set the figure size to fit the map content
    fig.update_layout(
        mapbox=dict(
            center=dict(lat=center_lat, lon=center_lon),
            style="carto-positron",
            zoom=zoom,
        ),
        autosize=True,
        # Add margin to accommodate title and other elements
        margin={"r": 0, "t": 30, "l": 0, "b": 0}
    )

    # Render the map on the HTML template
    return render_template('mooban_map.html', plot=fig.to_html(full_html=False))


@app.route('/tambon_map')
def tambon_map():
    # Read the shapefile
    gdf_tambon = gpd.read_file(
        'static/boundary_tb_hks0_adjusted/boundary_tb_hks0_adjusted.shp', encoding='cp874')

    # Calculate the center of the GeoDataFrame
    center_lat = gdf_tambon.geometry.centroid.y.mean()
    center_lon = gdf_tambon.geometry.centroid.x.mean()

    # Calculate the bounds of the GeoDataFrame
    min_lat, max_lat = gdf_tambon.geometry.bounds['miny'].min(
    ), gdf_tambon.geometry.bounds['maxy'].max()
    min_lon, max_lon = gdf_tambon.geometry.bounds['minx'].min(
    ), gdf_tambon.geometry.bounds['maxx'].max()

    # Set the zoom level based on the bounds
    zoom = 8.45  # You can adjust this value to your preference

    # Create a map with Plotly Express and Mapbox for gdf_tambon
    fig = px.choropleth_mapbox(
        gdf_tambon,
        geojson=gdf_tambon.geometry,
        locations=gdf_tambon.index,  # Use the index as locations
        # Replace 'Your_Column' with the column you want to color by
        color=gdf_tambon['TB_NAME'],
        # hover_name='TB_NAME',  # Replace 'Your_Other_Column' with the column for hover text
        title="Interactive Map for gdf_tambon",
        center={"lat": gdf_tambon.geometry.centroid.y.mean(
        ), "lon": gdf_tambon.geometry.centroid.x.mean()},  # Center the map
        mapbox_style="carto-positron",  # Choose a Mapbox style
        # fitbounds="locations",  # Auto-adjust zoom to fit all locations
        # zoom=8.45  # Adjust the initial zoom level
        zoom=zoom
    )

    # Set the figure size to fit the map content
    fig.update_layout(
        # Use layout.mapbox.fitbounds to automatically set the zoom level
        mapbox=dict(
            center=dict(lat=center_lat, lon=center_lon),
            style="carto-positron",
            zoom=zoom,
        ),
        autosize=True,
        margin={"r": 0, "t": 0, "l": 0, "b": 0}
    )

    # Render the map on the HTML template
    return render_template('tambon_map.html', plot=fig.to_html(full_html=False))


if __name__ == '__main__':
    port = 5000
    app.run(host='0.0.0.0', port=port, debug=True)
