# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1469467675.506997
_enable_loop = True
_template_filename = u'templates/base/base_panels.mako'
_template_uri = u'/base/base_panels.mako'
_source_encoding = 'ascii'
_exports = ['overlay', 'late_javascripts', 'stylesheets', 'init', 'javascript_app', 'masthead', 'javascripts']


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
        trans = context.get('trans', UNDEFINED)
        app = context.get('app', UNDEFINED)
        hasattr = context.get('hasattr', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'<!DOCTYPE HTML>\n')
        __M_writer(u'\n\n')

        self.has_left_panel = hasattr( self, 'left_panel' )
        self.has_right_panel = hasattr( self, 'right_panel' )
        self.message_box_visible = app.config.message_box_visible
        self.show_inactivity_warning = False
        if trans.webapp.name == 'galaxy' and trans.user:
            self.show_inactivity_warning = ( ( trans.user.active is False ) and ( app.config.user_activation_on ) and ( app.config.inactivity_box_content is not None ) )
        self.overlay_visible=False
        self.active_view=None
        self.body_class=""
        self.require_javascript=False
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in [] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'<html>\n    <!--base_panels.mako-->\n    ')
        __M_writer(unicode(self.init()))
        __M_writer(u'\n    <head>\n')
        if app.config.brand:
            __M_writer(u'            <title>')
            __M_writer(unicode(self.title()))
            __M_writer(u' / ')
            __M_writer(unicode(app.config.brand))
            __M_writer(u'</title>\n')
        else:
            __M_writer(u'            <title>')
            __M_writer(unicode(self.title()))
            __M_writer(u'</title>\n')
        __M_writer(u'        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />\n')
        __M_writer(u'        <meta name = "viewport" content = "maximum-scale=1.0">\n')
        __M_writer(u'        <meta http-equiv="X-UA-Compatible" content="IE=Edge,chrome=1">\n')
        __M_writer(u'        <link rel="index" href="')
        __M_writer(unicode( h.url_for( '/' ) ))
        __M_writer(u'"/>\n        ')
        __M_writer(unicode(self.stylesheets()))
        __M_writer(u'\n        ')
        __M_writer(unicode(self.javascripts()))
        __M_writer(u'\n        ')
        __M_writer(unicode(self.javascript_app()))
        __M_writer(u'\n    </head>\n\n    ')

        body_class = self.body_class
        if self.message_box_visible:
            body_class += " has-message-box"
        if self.show_inactivity_warning:
            body_class += " has-inactivity-box"
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['body_class'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n\n    <body scroll="no" class="full-content ')
        __M_writer(unicode(body_class))
        __M_writer(u'">\n')
        if self.require_javascript:
            __M_writer(u'            <noscript>\n                <div class="overlay overlay-background">\n                    <div class="modal dialog-box" border="0">\n                        <div class="modal-header"><h3 class="title">Javascript Required</h3></div>\n                        <div class="modal-body">The Galaxy analysis interface requires a browser with Javascript enabled. <br> Please enable Javascript and refresh this page</div>\n                    </div>\n                </div>\n            </noscript>\n')
        __M_writer(u'        <div id="everything" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;">\n')
        __M_writer(u'            <div id="background"></div>\n')
        __M_writer(u'            <div id="masthead" class="navbar navbar-fixed-top navbar-inverse">\n                ')
        __M_writer(unicode(self.masthead()))
        __M_writer(u'\n            </div>\n')
        if self.message_box_visible:
            __M_writer(u'                <div id="messagebox" class="panel-')
            __M_writer(unicode(app.config.message_box_class))
            __M_writer(u'-message" style="display:block">\n                    ')
            __M_writer(unicode(app.config.message_box_content))
            __M_writer(u'\n                </div>\n')
        if self.show_inactivity_warning:
            __M_writer(u'                <div id="inactivebox" class="panel-warning-message">\n                    ')
            __M_writer(unicode(app.config.inactivity_box_content))
            __M_writer(u' <a href="')
            __M_writer(unicode(h.url_for( controller='user', action='resend_verification' )))
            __M_writer(u'">Resend verification.</a>\n                </div>\n')
        __M_writer(u'            ')
        __M_writer(unicode(self.overlay(visible=self.overlay_visible)))
        __M_writer(u'\n')
        if self.has_left_panel:
            __M_writer(u'                <div id="left">\n                    ')
            __M_writer(unicode(self.left_panel()))
            __M_writer(u'\n                    <div class="unified-panel-footer">\n                        <div class="panel-collapse"></div>\n                        <div class="drag"></div>\n                    </div>\n                </div><!--end left-->\n')
        __M_writer(u'            <div id="center" class="inbound">\n                ')
        __M_writer(unicode(self.center_panel()))
        __M_writer(u'\n            </div><!--end center-->\n')
        if self.has_right_panel:
            __M_writer(u'                <div id="right">\n                    ')
            __M_writer(unicode(self.right_panel()))
            __M_writer(u'\n                    <div class="unified-panel-footer">\n                        <div class="panel-collapse right"></div>\n                        <div class="drag"></div>\n                    </div>\n                </div><!--end right-->\n')
        __M_writer(u'        </div><!--end everything-->\n        <div id=\'dd-helper\' style="display: none;"></div>\n')
        __M_writer(u'        ')
        __M_writer(unicode(self.late_javascripts()))
        __M_writer(u'\n    </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_overlay(context,title='',content='',visible=False):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        __M_writer(u'\n    ')
        __M_writer(u'\n\n    ')

        if visible:
            display = "style='display: block;'"
            overlay_class = "in"
        else:
            display = "style='display: none;'"
            overlay_class = ""
        
        
        __M_writer(u'\n\n    <div id="top-modal" class="modal fade ')
        __M_writer(unicode(overlay_class))
        __M_writer(u'" ')
        __M_writer(unicode(display))
        __M_writer(u'>\n        <div id="top-modal-backdrop" class="modal-backdrop fade ')
        __M_writer(unicode(overlay_class))
        __M_writer(u'" style="z-index: -1"></div>\n        <div id="top-modal-dialog" class="modal-dialog">\n            <div class="modal-content">\n                <div class="modal-header">\n                    <button type=\'button\' class=\'close\' style="display: none;">&times;</button>\n                    <h4 class=\'title\'>')
        __M_writer(unicode(title))
        __M_writer(u'</h4>\n                </div>\n                <div class="modal-body">')
        __M_writer(unicode(content))
        __M_writer(u'</div>\n                <div class="modal-footer">\n                    <div class="buttons" style="float: right;"></div>\n                    <div class="extra_buttons" style=""></div>\n                    <div style="clear: both;"></div>\n                </div>\n            </div>\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_late_javascripts(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        app = context.get('app', UNDEFINED)
        t = context.get('t', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'    <script type="text/javascript">\n\n')
        if self.has_left_panel:
            __M_writer(u"        var lp = new panels.LeftPanel({ el: '#left' });\n        force_left_panel = function( x ) { lp.force_panel( x ) };\n")
        __M_writer(u'\n')
        if self.has_right_panel:
            __M_writer(u"        var rp = new panels.RightPanel({ el: '#right' });\n        window.handle_minwidth_hint = function( x ) { rp.handle_minwidth_hint( x ) };\n        force_right_panel = function( x ) { rp.force_panel( x ) };\n")
        __M_writer(u'\n')
        if t.webapp.name == 'galaxy' and app.config.ga_code:
            __M_writer(u"          (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){\n          (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),\n          m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)\n          })(window,document,'script','//www.google-analytics.com/analytics.js','ga');\n          ga('create', '")
            __M_writer(unicode(app.config.ga_code))
            __M_writer(u"', 'auto');\n          ga('send', 'pageview');\n")
        __M_writer(u'\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stylesheets(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        __M_writer(unicode(h.css(
        'base',
        'jquery.rating',
        'bootstrap-tour'
    )))
        __M_writer(u'\n    <style type="text/css">\n    #center {\n')
        if not self.has_left_panel:
            __M_writer(u'            left: 0 !important;\n')
        if not self.has_right_panel:
            __M_writer(u'            right: 0 !important;\n')
        __M_writer(u'    }\n    </style>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_init(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascript_app(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        galaxy_client = _mako_get_namespace(context, 'galaxy_client')
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'    ')
        __M_writer(unicode( galaxy_client.load() ))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_masthead(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
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
                __M_writer(filters.html_escape(unicode(trans.user.email )))
                __M_writer(u'" } );\n')
            __M_writer(u'        </script>\n')
        __M_writer(u'\n    ')
        __M_writer(unicode(h.js(
        ## TODO: remove when all libs are required directly in modules
        'bundled/libs.bundled',
        'libs/require',
    )))
        __M_writer(u'\n\n    <script type="text/javascript">\n        // configure require\n        // due to our using both script tags and require, we need to access the same jq in both for plugin retention\n        // source http://www.manuel-strehl.de/dev/load_jquery_before_requirejs.en.html\n        window.Galaxy = window.Galaxy || {};\n        window.Galaxy.root = \'')
        __M_writer(unicode(h.url_for( "/" )))
        __M_writer(u'\';\n        define( \'jquery\', [], function(){ return jQuery; })\n        // TODO: use one system\n\n        // shims and paths\n        require.config({\n            baseUrl: "')
        __M_writer(unicode(h.url_for('/static/scripts') ))
        __M_writer(u'",\n            shim: {\n                "libs/underscore": {\n                    exports: "_"\n                },\n                "libs/backbone": {\n                    deps: [ \'jquery\', \'libs/underscore\' ],\n                    exports: "Backbone"\n                }\n            },\n            // cache busting using time server was restarted\n            urlArgs: \'v=')
        __M_writer(unicode(app.server_starttime))
        __M_writer(u"',\n        });\n    </script>\n\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"23": 2, "26": 0, "36": 1, "37": 2, "38": 4, "53": 15, "54": 19, "55": 38, "56": 85, "57": 90, "58": 119, "59": 124, "60": 156, "61": 159, "62": 161, "63": 161, "64": 163, "65": 164, "66": 164, "67": 164, "68": 164, "69": 164, "70": 165, "71": 166, "72": 166, "73": 166, "74": 168, "75": 170, "76": 172, "77": 174, "78": 174, "79": 174, "80": 175, "81": 175, "82": 176, "83": 176, "84": 177, "85": 177, "86": 180, "96": 186, "97": 188, "98": 188, "99": 189, "100": 190, "101": 199, "102": 201, "103": 203, "104": 204, "105": 204, "106": 206, "107": 207, "108": 207, "109": 207, "110": 208, "111": 208, "112": 211, "113": 212, "114": 213, "115": 213, "116": 213, "117": 213, "118": 216, "119": 216, "120": 216, "121": 217, "122": 218, "123": 219, "124": 219, "125": 226, "126": 227, "127": 227, "128": 229, "129": 230, "130": 231, "131": 231, "132": 238, "133": 243, "134": 243, "135": 243, "141": 126, "145": 126, "146": 127, "147": 128, "148": 130, "157": 137, "158": 139, "159": 139, "160": 139, "161": 139, "162": 140, "163": 140, "164": 145, "165": 145, "166": 147, "167": 147, "173": 93, "180": 93, "181": 96, "182": 98, "183": 99, "184": 102, "185": 103, "186": 104, "187": 108, "188": 109, "189": 110, "190": 114, "191": 114, "192": 117, "198": 22, "204": 22, "205": 23, "210": 27, "211": 30, "212": 31, "213": 33, "214": 34, "215": 36, "221": 17, "225": 17, "231": 87, "236": 87, "237": 89, "238": 89, "239": 89, "245": 122, "249": 122, "255": 41, "262": 41, "263": 43, "264": 44, "265": 44, "266": 44, "267": 46, "268": 46, "269": 47, "270": 48, "271": 48, "272": 48, "273": 50, "274": 52, "275": 53, "280": 57, "281": 64, "282": 64, "283": 70, "284": 70, "285": 81, "286": 81, "292": 286}, "uri": "/base/base_panels.mako", "filename": "templates/base/base_panels.mako"}
__M_END_METADATA
"""
