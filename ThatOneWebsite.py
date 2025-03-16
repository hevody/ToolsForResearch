with open('history.csv', 'rb') as f:
    histories = f.readlines()


blockedPrefixes = ('https://www.google.com',
                   'https://ngl.link',
                   'https://play.google.com',
                   'https://github.com/',
                   'http://cornhub.com/',
                   'https://www.reddit.com',
                   'https://m.facebook.com/',
                   'https://www.trustpilot.com',
                   'https://discord.com/',
                   'https://accountscenter.facebook.com',
                   'https://www.tiktok.com/',
                   'https://prnt.sc',
                   'https://m.youtube.com/',
                   'https://pastebin.com',
                   'https://stackoverflow.com',
                   'https://en.m.wikipedia.org',
                   'https://www.slideshare.net',
                   'https://www.scribd.com',
                   'https://l.facebook.com',
                   'chrome-extension://',
                   'https://www.youtube.com/',
                   'https://www.linkedin.com',
                   'https://excalidraw.com/',
                   'https://workspaceupdates.googleblog.com',
                   'https://www.chess.com/',
                   'https://www.facebook.com/',
                   'https://commons.libretexts.org/',
                   'https://lumenlearning.com/',
                   'https://drive.google.com',
                   'https://www.studocu.com',
                   'https://lichess.org',
                   'https://search.google.com/'
                   )


for history in histories:
    #print(history)
    element = history.split(b',')
    #print(element[5])
    urls = element[5].decode()
    if urls.startswith(blockedPrefixes):
        continue
    else:
        print(urls)
