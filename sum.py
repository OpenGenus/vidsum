#!/usr/bin/env python

import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser("Watch videos quickly")
    parser.add_argument('-i', '--video-file', help="Input video file", required=True)
    parser.add_argument('-s', '--subtitles-file', help="Input subtitle file (srt)", required=True)

    args = parser.parse_args()

    

