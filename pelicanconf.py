AUTHOR = 'yrd241'
SITENAME = 'CrazyBanana'
SITEURL = ""

PATH = "content"

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'en'
THEME = 'themes/Peli-Kiera'
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['readtime', 'neighbors']
STATIC_PATHS = ['images']



# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

SOCIAL = (
     ('github', 'https://yrd241.github.com/'),
     ('twitter', 'https://x.com/yrd241'),
)


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
