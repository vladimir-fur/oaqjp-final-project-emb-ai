﻿''' Running the module initiates the application of emotion detection 
    executed over the Flask channel and deployed on localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask ("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    ''' This code gets the text from the HTML interface and runs emotion detection using 
        emotion_detector() function. The output shows various emotion scores and a 
        dominant emotion for the provided text.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return '<b>Invalid text! Please try again!</b>'

    return f"""For the given statement, the system response is 'anger': {anger_score},
    'disgust': {disgust_score}, 'fear': {fear_score}, 'joy': {joy_score} and 'sadness': {sadness_score}. 
    The dominant emotion is <b>{dominant_emotion}</b>."""

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
