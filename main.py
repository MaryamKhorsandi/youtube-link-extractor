
# https://github.com/MaryamKhorsandi/youtube-link-extractor.git

import re

html = input()

pattern = r'''src\s*=\s*["']https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)'''

match = re.search(pattern, html)

if match:
    video_id = match.group(1)
    print("https://youtu.be/" + video_id)
else:
    print("None")
