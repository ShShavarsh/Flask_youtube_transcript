from youtube_transcript_api import TranslationLanguageNotAvailable
from youtube_transcript_api.formatters import JSONFormatter
from youtube_transcript_api.formatters import TextFormatter


from utils.transcripts import get_transcript_list, DEFAULT_LANGS
from flask import jsonify, request

from flask import Flask
application = Flask(__name__)


@application.route('/', methods=['GET'])
def hello():
    return "init-youtube-transcript-api"
    
@application.route('/multilingual-transcripts/<string:video_id>', methods=['GET'])
def multilingualTranscriptApi(video_id):
    transcript_list = get_transcript_list(video_id)
    transcript  = transcript_list.find_transcript(DEFAULT_LANGS) 
    return  JSONFormatter().format_transcript(transcript.fetch())


@application.route('/translation', methods=['GET'])
def translationApi():
    vid = request.args.get('vid')
    tl = request.args.get('tl')
    transcript_list = get_transcript_list(vid)
    transcript  = transcript_list.find_transcript(['en'])

    try:
        translated_transcript = transcript.translate(tl)
        json_formatted = JSONFormatter().format_transcript(translated_transcript.fetch())
        return json_formatted
    except TranslationLanguageNotAvailable:
        return jsonify({"error": "translation language not available", "language": tl}), 404


@application.route('/youtube-video-text/<string:video_id>', methods=['GET'])
def welcome(video_id):
    transcript_list = get_transcript_list(video_id)
    found_transcript = transcript_list.find_transcript(DEFAULT_LANGS)
    json_formatted = TextFormatter().format_transcript(found_transcript.fetch())
    return json_formatted

if __name__ == '__main__':
    application.config.from_pyfile('settings.py')
    application.run(host='0.0.0.0', port=5050)