# Source - https://stackoverflow.com/a/46562895
# Posted by Daksh M., modified by community. See post 'Timeline' for change history
# Retrieved 2025-12-26, License - CC BY-SA 4.0

from __future__ import unicode_literals
import youtube_dl

ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://youtu.be/YVC4-Oahl60?si=mUSQAMn9y4dldTiE'])
