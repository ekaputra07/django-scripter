from django.conf import settings

# Javascript library that available by default
# Format: ('libname', [('lib. url', 'ver')])
SCRIPTER_JS = (
    ('jquery', [
                ('scripter/js/jquery/jquery-1.7.2.min.js', '1.7.2')
               ]),
)

# Css framework that available by default
# Format: ('css name', [('url', 'ver')])
SCRIPTER_CSS = (
    ('reset', [
               ('scripter/css/960gs/reset.css', 'reset'),
               ('scripter/css/960gs/text.css', 'text')
              ]),

    ('960gs', [
               ('scripter/css/960gs/960_12_col.css', '12cols'),
               ('scripter/css/960gs/960_16_col.css', '16cols'),
               ('scripter/css/960gs/960_24_col.css', '24cols')
              ]),
)

