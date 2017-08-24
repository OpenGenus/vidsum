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

if __name__ == '__main__':
    parser = argparse.ArgumentParser("Watch videos quickly")
    parser.add_argument('-i', '--video-file', help="Input video file", required=True)
    parser.add_argument('-s', '--subtitles-file', help="Input subtitle file (srt)", required=True)

    args = parser.parse_args()

    

