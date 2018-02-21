from sqlalchemy.ext.automap import automap_base
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, Column, Integer, String, Float, Date, inspect
import os
import pandas as pd

dbpath = os.path.join('db', 'belly_button_biodiversity.sqlite')
engine = create_engine(f'sqlite:///{dbpath}', echo=False)

inspector = inspect(engine)

Base = automap_base()
Base.prepare(engine, reflect=True)

# meta = Base.classes.meta
# mc = Base.classes.metacolumn
# otu = Base.classes.otu_id

samples = pd.DataFrame(pd.read_csv("belly_button_biodiversity_samples.csv"))


