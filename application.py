from youtube_transcript_api import YouTubeTranscriptApi

from flask import Flask
application = Flask(__name__)

@application.route('/', methods=['GET'])
def hello():
    return "hello"

@application.route('/getYoutubeVideoTextByID/<string:ID>', methods=['GET'])
def welcome(ID):
    listOfTexts= YouTubeTranscriptApi.get_transcript(ID)
    return ''.join(str(e) for e in listOfTexts)
if __name__ == '__main__':
    application.run(host='0.0.0.0', port=5050)