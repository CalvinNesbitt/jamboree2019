import numpy as np
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap,shiftgrid


def plot_map(lons,lats):
    map = Basemap()
    # draw coastlines, country boundaries, fill continents.
    map.drawcoastlines(linewidth=0.25)
    map.drawcountries(linewidth=0.25)

    # draw the edge of the map projection region (the projection limb)
    map.drawmapboundary(fill_color='lightseagreen')
    # draw lat/lon grid lines every 30 degrees.
    map.drawmeridians(np.arange(0,360,30))
    map.drawparallels(np.arange(-90,90,30))

    # Create lon lat grid for plotting
    longrid,latgrid = np.meshgrid(lons,lats)

    plt.xlabel('Longitude')
    plt.xticks(np.arange(-180.,185.,90.))
    plt.yticks(np.arange(-90.,91.,30.))
    plt.ylabel('Latitude')
    plt.tight_layout()

    return map


# example code
lons = np.arange(-90.,90.,30)
lats = np.arange(-180.,180.,30)
plot_map(lons,lats)
plt.title('map')
plt.savefig('plots/test.png')
