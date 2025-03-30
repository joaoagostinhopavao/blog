AUTHOR = 'João Pavão'
SITENAME = 'Navegar sem Medo'
SITEURL = ""

PATH = "content"

TIMEZONE = 'Europe/Lisbon'

DEFAULT_LANG = 'pt'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("linkedin", "https://www.linkedin.com/"),
)

# Social widget
SOCIAL = (
    ("mastodon", "https://mastodon.social"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = 'alchemy'
THEME_STATIC_DIR = 'theme'