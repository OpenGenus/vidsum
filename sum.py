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

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
from sumy.summarizers.lsa import LsaSummarizer

def summarize(srt_file, n_sentences, language="english"):
    parser = PlaintextParser.from_string(srt_to_doc(srt_file), Tokenizer(language))
    stemmer = Stemmer(language)
    summarizer = LsaSummarizer(stemmer)
    summarizer.stop_words = get_stop_words(language)
    segment = []
    for sentence in summarizer(parser.document, n_sentences):
        index = int(re.findall("\(([0-9]+)\)", str(sentence))[0])
        item = srt_file[index]
        segment.append(srt_item_to_range(item))
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

if __name__ == '__main__':
    parser = argparse.ArgumentParser("Watch videos quickly")
    parser.add_argument('-i', '--video-file', help="Input video file", required=True)
    parser.add_argument('-s', '--subtitles-file', help="Input subtitle file (srt)", required=True)

    args = parser.parse_args()

    

