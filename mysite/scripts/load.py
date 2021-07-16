from os import read
from unesco.models import Site, Category, Iso, Region, State
import csv


def load_data(name,description,justification,
                year,longitude,latitude,
                area_hectares,category,state,
                region,iso):
    
    try:
        year = int(year)
    except:
        year = None

    try:
        longitude = int(longitude)
    except:
        longitude = None

    try:
        latitude = int(latitude)
    except:
        latitude = None

    try:
        area_hectares = int(area_hectares)
    except:
        area_hectares = None

    region, created = Region.objects.get_or_create(name=region)
    state, created = State.objects.get_or_create(name=state)
    iso, created = Iso.objects.get_or_create(name=iso)
    category, created = Category.objects.get_or_create(name=category)
    site, created = Site.objects.get_or_create(name=name, description=description,
                                                justification=justification, year=year,
                                                longitude=longitude, latitude=latitude,
                                                area_hectares=area_hectares, category=category,
                                                state=state, region=region, iso=iso)

    site.save()


with open('scripts/data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader)

    Site.objects.all().delete()
    Category.objects.all().delete()
    Iso.objects.all().delete()
    Region.objects.all().delete()
    State.objects.all().delete()

    for row in reader:
        load_data(*row)
