# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1469467675.534791
_enable_loop = True
_template_filename = u'templates/base.mako'
_template_uri = u'/base.mako'
_source_encoding = 'ascii'
_exports = ['title', 'stylesheets', 'init', 'javascript_app', 'javascripts', 'metas']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'galaxy_client', context._clean_inheritance_tokens(), templateuri=u'/galaxy_client_app.mako', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'galaxy_client')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        h = context.get('h', UNDEFINED)
        self = context.get('self', UNDEFINED)
        next = context.get('next', UNDEFINED)
        n_ = context.get('n_', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        self.js_app = None 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in [] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n\n')
        _=n_ 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['_'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n<!DOCTYPE HTML>\n<html>\n    <!--base.mako-->\n    ')
        __M_writer(unicode(self.init()))
        __M_writer(u'\n    <head>\n        <title>')
        __M_writer(unicode(self.title()))
        __M_writer(u'</title>\n        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />\n')
        __M_writer(u'        <link rel="index" href="')
        __M_writer(unicode( h.url_for( '/' ) ))
        __M_writer(u'"/>\n        ')
        __M_writer(unicode(self.metas()))
        __M_writer(u'\n        ')
        __M_writer(unicode(self.stylesheets()))
        __M_writer(u'\n        ')
        __M_writer(unicode(self.javascripts()))
        __M_writer(u'\n        ')
        __M_writer(unicode(self.javascript_app()))
        __M_writer(u'\n    </head>\n    <body class="inbound">\n        ')
        __M_writer(unicode(next.body()))
        __M_writer(u'\n    </body>\n</html>\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stylesheets(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        __M_writer(unicode(h.css('base')))
        __M_writer(u'\n    ')
        __M_writer(unicode(h.css('bootstrap-tour')))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_init(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascript_app(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        galaxy_client = _mako_get_namespace(context, 'galaxy_client')
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        __M_writer(unicode( galaxy_client.load( app=self.js_app ) ))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        app = context.get('app', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        form_input_auto_focus = context.get('form_input_auto_focus', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if app.config.sentry_dsn:
            __M_writer(u'        ')
            __M_writer(unicode(h.js( "libs/raven" )))
            __M_writer(u"\n        <script>\n            Raven.config('")
            __M_writer(unicode(app.config.sentry_dsn_public))
            __M_writer(u"').install();\n")
            if trans.user:
                __M_writer(u'                Raven.setUser( { email: "')
                __M_writer(filters.html_escape(unicode(trans.user.email)))
                __M_writer(u'" } );\n')
            __M_writer(u'        </script>\n')
        __M_writer(u'\n    ')
        __M_writer(unicode(h.js(
        ## TODO: remove when all libs are required directly in modules
        'bundled/libs.bundled',
        'libs/require',
        "libs/bootstrap-tour",
    )))
        __M_writer(u'\n\n    <script type="text/javascript">\n')
        __M_writer(u"        window.Galaxy = window.Galaxy || {};\n        window.Galaxy.root = '")
        __M_writer(unicode(h.url_for( "/" )))
        __M_writer(u'\';\n        window.Galaxy.config = {};\n\n        // configure require\n        // due to our using both script tags and require, we need to access the same jq in both for plugin retention\n        // source http://www.manuel-strehl.de/dev/load_jquery_before_requirejs.en.html\n        define( \'jquery\', [], function(){ return jQuery; })\n        // TODO: use one system\n\n        // shims and paths\n        require.config({\n            baseUrl: "')
        __M_writer(unicode(h.url_for('/static/scripts') ))
        __M_writer(u'",\n            shim: {\n                "libs/underscore": {\n                    exports: "_"\n                },\n                "libs/backbone": {\n                    deps: [ \'jquery\', \'libs/underscore\' ],\n                    exports: "Backbone"\n                }\n            },\n            // cache busting using time server was restarted\n            urlArgs: \'v=')
        __M_writer(unicode(app.server_starttime))
        __M_writer(u"'\n        });\n    </script>\n\n")
        if not form_input_auto_focus is UNDEFINED and form_input_auto_focus:
            __M_writer(u'        <script type="text/javascript">\n            $(document).ready( function() {\n                // Auto Focus on first item on form\n                if ( $("*:focus").html() == null ) {\n                    $(":input:not([type=hidden]):visible:enabled:first").focus();\n                }\n            });\n        </script>\n')
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_metas(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"129": 37, "130": 39, "131": 40, "132": 40, "133": 40, "134": 42, "135": 42, "136": 43, "137": 44, "138": 44, "139": 44, "140": 46, "141": 48, "142": 49, "173": 164, "152": 71, "148": 54, "149": 59, "150": 60, "23": 1, "151": 60, "153": 71, "26": 0, "155": 82, "156": 86, "154": 82, "158": 96, "35": 1, "36": 2, "40": 2, "41": 4, "45": 4, "46": 8, "47": 8, "48": 10, "49": 10, "50": 13, "51": 13, "52": 13, "53": 14, "54": 14, "55": 15, "56": 15, "57": 16, "58": 16, "59": 17, "60": 17, "61": 20, "62": 20, "63": 25, "64": 28, "65": 34, "66": 97, "67": 101, "68": 104, "74": 25, "164": 104, "83": 31, "88": 31, "89": 32, "90": 32, "91": 33, "92": 33, "98": 28, "107": 99, "157": 87, "113": 99, "114": 100, "115": 100, "121": 37}, "uri": "/base.mako", "filename": "templates/base.mako"}
__M_END_METADATA
"""
