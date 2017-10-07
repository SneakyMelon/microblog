"""
Additions functions usable by the whole applications.
"""
def opt():
    """
    Some lorem ipsum data for filler data.
    """
    options = {
        'app': {
            'name': 'WDD_PY_2017',
            'author': 'Allan Davidson | http://github.com/SneakyMelon/',
            'description':
                'Building Python Web Applications using Flask as the operating engine.',
            'version': '127.0.0.1',
            'build_date': '2017'
        },
        'users': [
            {
                'name': 'World',
                'nick': 'Whole Wide World'
            },
            {
                'name': 'Allan',  # Data
                'nick': 'Melon'  # Data
            },
            {
                'name': 'Steve',  # Data
                'nick': 'Sloth'  # Data
            },
            {
                'name': 'Phil',  # Data
                'nick': 'Beavur'  # Data
            }
        ],
        'page': {
            'title': "Home Page",
            'resources': {
                'bootstrap': {
                    'js': [
                        'static/vendor/jquery/jquery.min.js',
                        'static/vendor/popper/popper.min.js',
                        'static/vendor/bootstrap/js/bootstrap.min.js',
                        'static/vendor/jquery-easing/jquery.easing.min.js',
                        'static/js/scrolling-nav.js'
                    ],
                    'css': [
                        'static/vendor/bootstrap/css/bootstrap.min.css',
                        'static/css/scrolling-nav.css'
                    ],
                },
                'stylesheets': {
                    'custom':	[
                        #'static/style.css',
                    ]
                },
            },
        },
        'content': {
            # world, name, nick
        }
    }

    return options


def env(string=''):
    """
    Get key-value paied values from the environment file.
    Pass the key using the dot-notion (key.subkey) methodology.

    Example: global.settings returns the settings value.
    """

    import os

    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

    key = string.upper().replace('.', '_')

    with open(os.path.join(__location__, 'env')) as textfile:
        for line in textfile:
            if line.startswith(key) is True:
                value = line.split('=', 1)[1].strip()
    return str(value)
