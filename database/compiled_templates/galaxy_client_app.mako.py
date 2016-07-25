# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1469467675.523263
_enable_loop = True
_template_filename = u'templates/galaxy_client_app.mako'
_template_uri = u'/galaxy_client_app.mako'
_source_encoding = 'ascii'
_exports = ['load', 'render_json', 'get_user_dict', 'bootstrap', 'get_user_json', 'get_config_json', 'get_config_dict']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_load(context,app=None,**kwargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        def render_json(dictionary):
            return render_render_json(context,dictionary)
        def get_config_dict():
            return render_get_config_dict(context)
        def get_user_dict():
            return render_get_user_dict(context)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'    ')
        __M_writer(unicode( self.bootstrap( **kwargs ) ))
        __M_writer(u'\n    <script type="text/javascript">\n        require([ \'require\', \'galaxy\' ], function( require, galaxy ){\n            //TODO: global...\n            window.Galaxy = new galaxy.GalaxyApp({\n                root    : \'')
        __M_writer(unicode(h.url_for( "/" )))
        __M_writer(u"',\n                config  : ")
        __M_writer(unicode( render_json( get_config_dict() )))
        __M_writer(u',\n                user    : ')
        __M_writer(unicode( render_json( get_user_dict() )))
        __M_writer(u',\n            }, window.bootstrapped );\n\n')
        if app:
            __M_writer(u"                require([ '")
            __M_writer(unicode(app))
            __M_writer(u"' ]);\n")
        __M_writer(u'        });\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_json(context,dictionary):
    __M_caller = context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(unicode( h.dumps( dictionary, indent=( 2 if trans.debug else 0 ) ) ))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_get_user_dict(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        AssertionError = context.get('AssertionError', UNDEFINED)
        Exception = context.get('Exception', UNDEFINED)
        int = context.get('int', UNDEFINED)
        float = context.get('float', UNDEFINED)
        util = context.get('util', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'    ')

        from markupsafe import escape
        user_dict = {}
        try:
            if trans.user:
                user_dict = trans.user.to_dict( view='element',
                    value_mapper={ 'id': trans.security.encode_id, 'total_disk_usage': float, 'email': escape, 'username': escape } )
                user_dict[ 'quota_percent' ] = trans.app.quota_agent.get_percent( trans=trans )
                user_dict[ 'is_admin' ] = trans.user_is_admin()
        
                # tags used
                users_api_controller = trans.webapp.api_controllers[ 'users' ]
                tags_used = []
                for tag in users_api_controller.get_user_tags_used( trans, user=trans.user ):
                    tag = escape( tag )
                    if tag:
                        tags_used.append( tag )
                user_dict[ 'tags_used' ] = tags_used
        
                return user_dict
        
            usage = 0
            percent = None
            try:
                usage = trans.app.quota_agent.get_usage( trans, history=trans.history )
                percent = trans.app.quota_agent.get_percent( trans=trans, usage=usage )
            except AssertionError, assertion:
                # no history for quota_agent.get_usage assertion
                pass
            return {
                'total_disk_usage'      : int( usage ),
                'nice_total_disk_usage' : util.nice_size( usage ),
                'quota_percent'         : percent
            }
        
        except Exception, exc:
            pass
            #TODO: no logging available?
            #log.exception( exc )
        
        return user_dict
            
        
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_bootstrap(context,**kwargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def render_json(dictionary):
            return render_render_json(context,dictionary)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'    <script type="text/javascript">\n        //TODO: global...\n')
        for key in kwargs:
            __M_writer(u"            ( window.bootstrapped = window.bootstrapped || {} )[ '")
            __M_writer(unicode(key))
            __M_writer(u"' ] = (\n                ")
            __M_writer(unicode( render_json( kwargs[ key ] ) ))
            __M_writer(u'\n            );\n')
        __M_writer(u"        define( 'bootstrapped-data', function(){\n            return window.bootstrapped;\n        });\n    </script>\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_get_user_json(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        def get_user_dict():
            return render_get_user_dict(context)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(unicode( h.dumps( get_user_dict() )))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_get_config_json(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        def get_config_dict():
            return render_get_config_dict(context)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(unicode( h.dumps( get_config_dict() )))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_get_config_dict(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        Exception = context.get('Exception', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'    ')

        config_dict = {}
        try:
            controller = trans.webapp.api_controllers.get( 'configuration', None )
            if controller:
                config_dict = controller.get_config_dict( trans, trans.user_is_admin() )
        except Exception, exc:
            pass
        return config_dict
            
        
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"150": 13, "134": 109, "151": 13, "140": 6, "175": 58, "16": 0, "152": 14, "146": 6, "147": 10, "148": 12, "21": 3, "22": 21, "23": 40, "24": 56, "25": 61, "26": 110, "27": 115, "154": 17, "197": 46, "160": 112, "33": 23, "167": 112, "168": 114, "169": 114, "45": 23, "46": 25, "47": 25, "48": 25, "49": 30, "50": 30, "51": 31, "52": 31, "53": 32, "54": 32, "55": 35, "56": 36, "57": 36, "58": 36, "59": 38, "190": 44, "65": 1, "196": 44, "182": 58, "198": 46, "71": 1, "72": 2, "73": 2, "183": 60, "79": 65, "184": 60, "215": 209, "89": 65, "90": 68, "91": 68, "209": 55, "153": 14, "149": 13}, "uri": "/galaxy_client_app.mako", "filename": "templates/galaxy_client_app.mako"}
__M_END_METADATA
"""
