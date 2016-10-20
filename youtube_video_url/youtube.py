# coding: utf-8
from urlparse import parse_qs

import requests

from youtube_video_url.models import YouTubeURLs


def get_youtube_urls(youtube_id):
    url = 'http://youtube.com/get_video_info?video_id={}'.format(youtube_id)
    response = requests.get(url)

    answer = parse_qs(response.text, keep_blank_values=True)
    stream_map = answer['url_encoded_fmt_stream_map'][0]

    urls = []
    for stream_raw in stream_map.split(','):
        stream_qry = parse_qs(stream_raw, keep_blank_values=True)

        sig = stream_qry['sig'][0] if 'sig' in stream_qry else None

        urls.append(
            YouTubeURLs(stream_qry['url'][0], stream_qry['quality'][0], sig))

    return urls
