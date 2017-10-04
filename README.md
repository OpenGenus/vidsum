## Generate summary of any video

Generate a summary of any video through its subtitles.

This is the community driven approach towards the summarization by the **[OpenGenus](https://github.com/opengenus)** community.

# Installing vidsum

In order to install vidsum, simply clone the repository to a local directory. You can do this by running the following commands:
```sh
$ git clone https://github.com/OpenGenus/vidsum.git

$ cd vidsum/code

```
Please note that vidsum requires the following packages to be installed:
- [pysrt](https://github.com/byroot/pysrt)
- [imageio](https://imageio.github.io/)
- [moviepy](https://zulko.github.io/moviepy/)
- [pytube](https://github.com/nficano/pytube)
- [sumy](https://github.com/miso-belica/sumy)

If you do not have these packages installed, then you can do so by running this command:
```sh
$ pip install -r requirements.txt

```

# Usage

To generate summary of a video file `sample.mp4` with subtitle file `subtitle.srt` :
```python
python sum.py -i sample.mp4 -s subtitle.srt
```
To download a YouTube video along with its subtitles from url:
```python
python sum.py -u "url"
```

# Future developments

For future development to this approach, see [Wiki](https://github.com/AdiChat/vidsum/wiki/Future_developments) and check out other [approaches](https://github.com/AdiChat/vidsum/wiki/Other-approaches).

# Contributions

All contributions are welcomed. Please see [COMMIT_TEMPLATE.md](https://github.com/OpenGenus/vidsum/blob/master/COMMIT_TEMPLATE.md) before making pull requests to this repository. See all contributors [here](https://github.com/AdiChat/vidsum/graphs/contributors).
