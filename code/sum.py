#!/usr/bin/env python

import argparse
import os
import re
import subprocess
import sys
import math
import pysrt
import imageio
imageio.plugins.ffmpeg.download()
from moviepy.editor import *
from itertools import starmap

from pytube import YouTube

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
from sumy.summarizers.lsa import LsaSummarizer

# generate segmented summary
def summarize(srt_file, n_sentences, language="english"):
    parser = PlaintextParser.from_string(srt_to_txt(srt_file), Tokenizer(language))
    stemmer = Stemmer(language)
    summarizer = LsaSummarizer(stemmer)
    summarizer.stop_words = get_stop_words(language)
    segment = []
    for sentence in summarizer(parser.document, n_sentences):
        index = int(re.findall("\(([0-9]+)\)", str(sentence))[0])
        item = srt_file[index]
        segment.append(srt_segment_to_range(item))
    return segment

# Extract text from subtitles file
def srt_to_txt(srt_file):
    text = ''
    for index, item in enumerate(srt_file):
        if item.text.startswith("["): continue
        text += "(%d) " % index
        text += item.text.replace("\n", "").strip("...").replace(".", "").replace("?", "").replace("!", "")
        text += ". "
    return text

# Handling of srt segments to time range
def srt_segment_to_range(item):
    start_segment = item.start.hours*60*60 + item.start.minutes*60 + item.start.seconds + item.start.milliseconds/1000.0
    end_segment = item.end.hours*60*60 + item.end.minutes*60 + item.end.seconds + item.end.milliseconds/1000.0
    return start_segment, end_segment

# duration of segments
def time_regions(regions):
    return sum(starmap(lambda start, end: end - start, regions))

# find important sections
def find_summary_regions(srt_filename, duration=30, language="english"):
    srt_file = pysrt.open(srt_filename)
    # generate average subtitle duration
    subtitle_duration = time_regions(map(srt_segment_to_range, srt_file))/len(srt_file)
    # compute number of sentences in the summary file
    n_sentences = duration / subtitle_duration
    summary = summarize(srt_file, n_sentences, language)
    total_time = time_regions(summary)
    too_short = total_time < duration
    if too_short:
        while total_time < duration:
            n_sentences += 1
            summary = summarize(srt_file, n_sentences, language)
            total_time = time_regions(summary)
    else:
        while total_time > duration:
            n_sentences -= 1
            summary = summarize(srt_file, n_sentences, language)
            total_time = time_regions(summary)
    return summary

# join segments
def create_summary(filename, regions):
    subclips = []
    input_video = VideoFileClip(filename)
    last_end = 0
    for (start, end) in regions:
        subclip = input_video.subclip(start, end)
        subclips.append(subclip)
        last_end = end
    return concatenate_videoclips(subclips)

# abstract function
def get_summary(filename="1.mp4", subtitles="1.srt"):
    regions = find_summary_regions(subtitles,60,"english")
    summary = create_summary(filename, regions)
    base, ext = os.path.splitext(filename)
    output = "{0}_1.mp4".format(base)
    summary.to_videofile( output, codec="libx264", temp_audiofile="temp.m4a", remove_temp=True, audio_codec="aac")
    return True

def download_video(url):
    print(url)
    yt = YouTube(url)
    yt.set_filename('1')
    video = yt.filter('mp4')[-1]
    print(video)
    video.download(os.getcwd())
    return True

if __name__ == '__main__':
    parser = argparse.ArgumentParser("Watch videos quickly")
    parser.add_argument('-i', '--video-file', help="Input video file")
    parser.add_argument('-s', '--subtitles-file', help="Input subtitle file (srt)")
    parser.add_argument('-u', '--url', help="Video url")

    args = parser.parse_args()

    url = args.url
    if not url:
        get_summary(args.video_file, args.subtitles_file)
    else:
        download_video(url)
        # download subtitles
        # proceed with general summarization


