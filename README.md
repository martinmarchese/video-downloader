# Video Downloader
Simple Python Script to Download Multiple Videos Using youtube-dl

Uses https://github.com/ytdl-org/youtube-dl to download videos from URLs listed in a txt file.

## Requirements

Make sure you have both python3 and youtube-dl installed and in your PATH.

## Usage
Get the video URLs and add them to a txt file (one URL per line)
If the site hosting the video needs login, login using chrome and with the Get cookies.txt extension (https://chrome.google.com/webstore/detail/get-cookiestxt/bgaddhkoddajcdgocldbbfleckgcbcid) download the cookies.txt file.

### Complete the following lines

The complete path to the txt files with the videos URLs listed (one per line).

```
filepath = ''
```

The complete path to the cookie file (if needed).
```
cookie_file = ''
```

The output directory where the videos should be downloaded
```
output_dir = ''
```

For the name template leave the default values or change it based on https://github.com/ytdl-org/youtube-dl#output-template
```
name_template = '\%\(title\)s-\%\(id\)s.\%\(ext\)s'
```
### Run the Script

```
python3 video-downloader.py
```
