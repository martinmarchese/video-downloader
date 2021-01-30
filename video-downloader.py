# Uses https://github.com/ytdl-org/youtube-dl to download videos from a list of URLs in file.txt
# In case video is dowloaded but not playing Install ffmpeg or avconv and download again
# To change name_template refer to youtube-dl documentation

import subprocess
import shlex

filepath = ''
cookie_file = ''
output_dir = ''
name_template = '\%\(title\)s-\%\(id\)s.\%\(ext\)s'
with open(filepath) as fp:
   line = fp.readline()
   while line:
       if cookie_file == '':
          cmd = "youtube-dl -o {}{} {}".format(output_dir,name_template,line.strip(),cookie_file)
       else:
          cmd = "youtube-dl -o {}{} {} --cookies {}".format(output_dir,name_template,line.strip(),cookie_file)
       print("[VIDEO DOWNLOADER] Downloading: {}".format(line.strip()))
       process = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE)
       while True:
          output = process.stdout.readline()
          if output.decode('ascii') == '' and process.poll() is not None:
             break
          if output:
             print("[YOUTUBE-DL] {}".format(output.strip().decode('ascii').format))
       process.wait()
       print("[VIDEO DOWNLOADER] Download Finished")
       line = fp.readline()
   print("-----------------------------------")
process.poll()
print("[VIDEO DOWNLOADER] All videos have been downloaded.")