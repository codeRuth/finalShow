from flask import Flask
import dataAnalysis
import json

app = Flask(__name__)

@app.route('/getBranchSpeech/<int:branchName>', methods=['GET'])
def getBranchSpeech(branchName):
    return json.dumps(dataAnalysis.speechAnalysis('speechData/' + str(branchName)))

@app.route('/getBranchText/<int:branchName>', methods=['GET'])
def getBranchText(branchName):
    return json.dumps(dataAnalysis.tweetAnalysis('tweetData/tweet'+str(branchName)+'.csv'))

@app.route('/getBranchImage/<int:branchName>', methods=['GET'])
def getBranchImage(branchName):
    return json.dumps(dataAnalysis.tweetAnalysis('imageData/image' +branchName+ '.tiff'))

if __name__ == '__main__':
    app.run(debug=True)