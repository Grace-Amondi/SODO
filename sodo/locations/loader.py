from django.contrib.gis.utils import LayerMapping

from sodo.locations.models import *

mapping = {'name': 'COUNTY', 'poly': 'MULTIPOLYGON',}


shp = '/home/geogirl/counties/counties.geojson'

def run(verbose=True):
    lm = LayerMapping(
        Counties, shp, mapping,
        transform=False, encoding='iso-8859-1',
    )
    lm.save(strict=True, verbose=verbose)