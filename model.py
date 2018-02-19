'''
Module containing the database set-up
'''

# Import dependencies
import os
from sqlalchemy import create_engine, Column, Integer, String, func, Float, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
import pandas as pd

# Base definition
Base = declarative_base()

# Create engine
dbpath = os.path.join('db', 'belly_button_biodiversity.sqlite')
engine = create_engine(f'sqlite:///{dbpath}')

#subject metadata class
class Metadata(Base):
    __tablename__ = 'meta'
    id = Column(Integer, primary_key=True)
    SAMPLEID = Column(Integer)
    EVENT = Column(String(64))
    ETHNICITY = Column(String(64))
    GENDER = Column(String(10))
    AGE = Column(Integer)
    WFREQ = Column(Integer)
    BBTYPE = Column(String(10))
    LOCATION = Column(String(64))
    COUNTRY012 = Column(String(64))
    ZIP012 = Column(String(64))
    COUNTRY1319 = Column(String(64))
    ZIP1319 = Column(String(64))
    DOG = Column(String(10))
    CAT = Column(String(10))
    IMPSURFACE013 = Column(Integer)
    NPP013 = Column(Float)
    MMAXTEMP013 = Column(Float)
    PFC013 = Column(Integer)
    IMPSURFACE1319 = Column(Integer)
    NPP1319 = Column(Integer)
    MMAXTEMP1319 = Column(Float)
    PFC1319 = Column(Float)


class MetaColumn(Base):
    __tablename__ = 'metacolumn'
    id = Column(Integer, primary_key=True)
    COLUMN = Column(String(64))
    TYPE = Column(String(64))
    DESCRIPTION = Column(String)

class OTU_ID(Base):
    __tablename__ = 'otu_id'
    otu_id = Column(Integer, primary_key=True)
    lowest_taxonomic_unit_found = Column(String)


Base.metadata.create_all(engine)

# Create session
session = Session(engine)

# Populate Database
metadf = pd.DataFrame(pd.read_csv("Belly_Button_Biodiversity_Metadata.csv"))
metadf = metadf.reset_index(drop=False)
metadf = metadf.rename(columns={'index': 'id'})
metadf.to_sql('meta', engine, if_exists="replace", index = False)

mcdf = pd.DataFrame(pd.read_csv("metadata_columns.csv"))
mcdf = mcdf.reset_index(drop=False)
mcdf = mcdf.rename(columns={'index': 'id'})
metadf.to_sql('metacolumn', engine, if_exists="replace", index = False)

otudf = pd.DataFrame(pd.read_csv("belly_button_biodiversity_otu_id.csv"))
otudf = otudf.set_index("otu_id")
otudf.to_sql('metacolumn', engine, if_exists="replace", index = False)