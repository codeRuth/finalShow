#!flask/bin/python
from flask import Flask
import dataAnalysis
import jsonify
import json

app = Flask(__name__)

@app.route('/getBranchSpeech/<int:branchName>', methods=['GET'])
def getBranchSpeech(branchName):
    return json.dumps(dataAnalysis.speechAnalysis('speechData/' + branchName))

@app.route('/getBranchText/<int:branchName>', methods=['GET'])
def getBranchText(branchName):
    return json.dumps(dataAnalysis.tweetAnalysis('tweetData/tweet'+branchName+'.csv'))

if __name__ == '__main__':
    app.run(debug=True)