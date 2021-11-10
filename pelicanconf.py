AUTHOR = 'Johnny Richard'
SITENAME = "Johnny Richard's blog"
SITEURL = 'https://johnnyrichard.com'

PATH = 'content'
THEME = 'themes/cristal'

DEFAULT_LANG = 'en'
TIMEZONE = 'Europe/Stockholm'
DEFAULT_DATE_FORMAT = ('%Y-%m-%d')

STATIC_PATHS = ['static/CNAME']
EXTRA_PATH_METADATA = {
    'static/CNAME': {'path': 'CNAME'},
}

DISPLAY_CATEGORIES_ON_MENU = False

ARTICLE_URL = '{lang}/posts/{date:%Y}/{date:%m}/{slug}'
ARTICLE_SAVE_AS = '{lang}/posts/{date:%Y}/{date:%m}/{slug}.html'

ARTICLE_LANG_URL = '{lang}/posts/{date:%Y}/{date:%m}/{slug}'
ARTICLE_LANG_SAVE_AS = '{lang}/posts/{date:%Y}/{date:%m}/{slug}.html'

TRANSLATION_FEED_ATOM = '{lang}/feeds/atom.xml'

AUTHOR_SAVE_AS = '' 
CATEGORY_SAVE_AS = ''

MENUITEMS = [('sourcehut', 'https://sr.ht/~johnnyrichard/'),
             ('github', 'https://github.com/johnnyrichard'),
             ('email', 'mailto:~johnnyrichard/public-inbox@lists.sr.ht'),
             ('rss', '/en/feeds/atom.xml'),]

FEED_MAX_ITEMS = 15
DEFAULT_PAGINATION = 10

