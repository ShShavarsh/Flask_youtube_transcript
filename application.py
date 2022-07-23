from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import JSONFormatter

from flask import Flask
application = Flask(__name__)

@application.route('/', methods=['GET'])
def hello():
    return "wordbook"

@application.route('/getYoutubeVideoTextByID/<string:ID>', methods=['GET'])
def welcome(ID):
    listOfTexts= YouTubeTranscriptApi.get_transcript(ID)
    formatter = JSONFormatter()
    json_formatted = formatter.format_transcript(listOfTexts)
    return json_formatted    
if __name__ == '__main__':
    application.run(host='0.0.0.0', port=5050)