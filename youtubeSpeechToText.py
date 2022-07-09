from youtube_transcript_api import YouTubeTranscriptApi

from flask import Flask
app = Flask(__name__)

@app.route('/getYoutubeVideoTextByID/<string:ID>', methods=['GET'])
def welcome(ID):
    listOfTexts= YouTubeTranscriptApi.get_transcript(ID)
    return ''.join(str(e) for e in listOfTexts)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8088)