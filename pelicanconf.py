AUTHOR = 'Jake Stevens-Haas'
SITENAME = 'Jake Stevens-Haas'
SITEURL = ""
SITESUBTITLE = "Mathematics, Python, and Research engineering"
SITEDESCRIPTION = "Mathematics, Python, and Research engineering blog"
SITELOGO = "/images/me.jpg"

PATH = "content"

MAIN_MENU = True
MENUITEMS = (('Archives', './archives.html'),
             ('Categories', './categories.html'),
             ('Tags', './tags.html'),)

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
    ("mitosis", "https://pypi.org/project/mitosis/"),
    ("pysindy", "https://pysindy.readthedocs.io/en/latest/"),
)

THEME = 'Flex'

# Social widget
SOCIAL = (
    ("github", "https://github.com/Jacob-Stevens-Haas"),
    ("linkedin", "https://www.linkedin.com/in/jacob-stevens-haas/"),
    ("mastodon", "https://mastodon.social/@jake_stevens_haas")
)

DEFAULT_PAGINATION = 10

STATIC_PATHS = ['images', 'extra']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/CNAME': {'path': 'CNAME'},
}

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
