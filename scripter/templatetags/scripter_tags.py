from django import template
from django.conf import settings
from scripter.utils import get_required_scripts
from scripter import scripts as scripts_reg

register = template.Library()


# Usage: {% scripter_css "reset;960gs==12cols" %}
@register.inclusion_tag('scripter/styles.html')
def scripter_css(default_css=None):
    css_list = []
    css_inline_list = []

    if default_css:
        required_css = default_css.split(',')
        for css in required_css:
            csses = get_required_scripts('css', css)
            if csses: css_list.extend(csses)            
            

    extern_css = scripts_reg.css_registry
    for css in extern_css:

        if css.get('require', None):
            for req_css in css['require']:
                csses = get_required_scripts('css', req_css)
                for c in csses:
                    if c not in css_list:
                        css_list.append(c)

        if css['type'] == 'inline':
            css_inline_list.append(css['css'])

        else:
            for c in css['css']:
                if c not in css_list:
                    css_list.append(c)
            
    
    return {
        'STATIC_URL': settings.STATIC_URL,
        'styles': css_list,
        'inline_styles': css_inline_list,
    }


# Usage: {% scripter_js "jquery==1.7.2" %}
@register.inclusion_tag('scripter/scripts.html')
def scripter_js(default_js=None):
    js_list = []
    js_inline_list = []

    if default_js:
        required_scripts = default_js.split(',')
        for script in required_scripts:
            scripts = get_required_scripts('js', script)
            if scripts: js_list.extend(scripts)            
            

    extern_js = scripts_reg.js_registry
    for js in extern_js:

        if js.get('require', None):
            for req_script in js['require']:
                scripts = get_required_scripts('js', req_script)
                for script in scripts:
                    if script not in js_list:
                        js_list.append(script)

        if js['type'] == 'inline':
            js_inline_list.append(js['scripts'])

        else:
            for script in js['scripts']:
                if script not in js_list:
                    js_list.append(script)
            
    
    return {
        'STATIC_URL': settings.STATIC_URL,
        'javascripts': js_list,
        'inline_javascripts': js_inline_list,
    }
