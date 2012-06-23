from django.conf import settings

from scripter.settings import *
try:
    SCRIPTER_CSS = settings.SCRIPTER_CSS
except AttributeError:
    pass

try:
    SCRIPTER_JS = settings.SCRIPTER_JS
except AttributeError:
    pass


class ScriptRegistry(object):
    """ Script registry, holds a record of registered scripts """

    def __init__(self):
        self.js_registry = []
        self.css_registry = []

    def include_js(self, script, require=None):         
        self.js_registry.append({'type': 'source', 'scripts': script, 'require': require})

    def print_js(self, script, require=None):         
        self.js_registry.append({'type': 'inline', 'scripts': script, 'require': require})


    def include_css(self, css, require=None):         
        self.css_registry.append({'type': 'source', 'css': css, 'require': require})

    def print_css(self, css, require=None):         
        self.css_registry.append({'type': 'inline', 'css': css, 'require': require})

scripts = ScriptRegistry()


def get_all_script(script_type, name):
    """ Return all version in scripts bundle (if available) """
    
    if script_type == 'css':
        source = SCRIPTER_CSS
    else:
        source = SCRIPTER_JS

    for i in source:
        if i[0] == name:
            return i[1]

    return False



def get_script(script_type, name, version):
    """ return specific script based on its name and version (if available) """

    if script_type == 'css':
        source = SCRIPTER_CSS
    else:
        source = SCRIPTER_JS

    for i in source:
        if i[0] == name:
            for script in i[1]:
                if script[1] == version:
                    return script

    return False


def get_required_scripts(types, script):
    """Return required scripts """
    
    # if version of js specified
    script = script.strip()
    if '==' in script:
        name_version = script.split('==')
        name = name_version[0].strip()
        version = name_version[1].strip()
        script = get_script(types, name, version)
        if script:
            return [script[0]]
    else:
        scripts = get_all_script(types, script)
        if scripts:
            return [script[0] for script in scripts]
    
    return False



