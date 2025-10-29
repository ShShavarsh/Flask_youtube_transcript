from os import environ
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.proxies import WebshareProxyConfig

DEFAULT_LANGS = ['en', 'es', 'fr', 'de', 'pt', 'vi', 'hy', 'cs', 'th', 'sw', 'sv', 'fil', 'fi', 'fa', 'ru', 'ja']

def get_transcript_list(video_id):
    proxy_cfg = WebshareProxyConfig(
        proxy_username=environ.get("web_share_username"),
        proxy_password=environ.get("web_share_password"),
        filter_ip_locations=["de", "us"]
    )
    return YouTubeTranscriptApi(proxy_config=proxy_cfg).list(video_id)