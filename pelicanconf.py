AUTHOR = 'Jake Stevens-Haas'
SITENAME = 'Jake Stevens-Haas'
SITEURL = ""

PATH = "content"

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("UW Amath", "https://amath.washington.edu/"),
    ("Kutz Lab", "https://faculty.washington.edu/kutz/"),
)

# Social widget
SOCIAL = (
    ("Github", "https://github.com/Jacob-Stevens-Haas"),
    ("LinkedIn", "https://www.linkedin.com/in/jacob-stevens-haas/"),
    ("Mastodon", "https://mastodon.social/@jake_stevens_haas")
)

DEFAULT_PAGINATION = False

STATIC_PATHS = ['images', 'extra']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'.': 'favicon.ico'},
    'extra/CNAME': {'.': 'CNAME'},
}

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
