# Import dependencies
from flask import Flask, render_template, jsonify, request, redirect
import requests
import sqlite3 as sql
import model
import os
import data

#Flask Setup
app = Flask(__name__)


#Main Route
@app.route('/')
def home():
    return render_template('index.html')

#Route to return sample names
@app.route('/names')
def names():
    results = (session
               .query(meta.SAMPLEID)
               .all())
    names = []
    for row in results:
        names.append("BB_" + str(row[0]))

    return jsonify(names)


#Route to return list of OTU descriptions
@app.route('/otu')
def otu():
    results = (session
               .query(otu.lowest_taxonomic_unit_found)
               .all())
    descriptions = []
    for row in results:
        descriptions.append(row[])
    return descriptions


#metadata for a given sample
@app.route('/metadata/<sample>')
def metadata(sample):
    results = session.query(meta).all()
    
    metasample = []

    for result in results:
        row = {}
        row["SAMPLEID"] = results[1]
        row["ETHNICITY"] = results[3]
        row["GENDER"] = results[4]
        row["AGE"] = results[5]
        row["BBTYPE"] = results[7]
        row["LOCATION"] = results[8]
        metasample.append(row)

    return jsonify(metasample)


#Weekly washing frequency as a number
@app.route('/wfreq/<sample>')
def wwf(sample):

    freq = session.query(meta.WFREQ, meta.SAMPLEID).filter(SAMPLEID ==  sample).all()

    return freq



#OTU IDs and Sample Values for a given sample.
@app.route('/samples/<sample>')
def samples(sample):

    current = samples[sample].tolist()
    results = session.query(otu.otu_id).all()
    i = 0
    otu_ids = []
    sample_values = []

    for i in range(len(current)):
        if current[i] /= 0:
            otu_ids.append(results[i])
            sample_values.append(current[i])

    data = {
    'values': sample_values,
    'labels': otu_ids,
    'type': 'pie'
    }

    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)