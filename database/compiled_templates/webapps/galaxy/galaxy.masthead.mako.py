# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1469467675.49043
_enable_loop = True
_template_filename = u'templates/webapps/galaxy/galaxy.masthead.mako'
_template_uri = u'/webapps/galaxy/galaxy.masthead.mako'
_source_encoding = 'ascii'
_exports = ['load']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('__anon_0x7f04acc409d0', context._clean_inheritance_tokens(), templateuri=u'/galaxy_client_app.mako', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f04acc409d0')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f04acc409d0')._populate(_import_ns, [u'get_user_dict'])
        __M_writer = context.writer()
        __M_writer(u'\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_load(context,active_view=None):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f04acc409d0')._populate(_import_ns, [u'get_user_dict'])
        get_user_dict = _import_ns.get('get_user_dict', context.get('get_user_dict', UNDEFINED))
        app = _import_ns.get('app', context.get('app', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        bool = _import_ns.get('bool', context.get('bool', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n    ')

        from markupsafe import escape
        ## get configuration
        masthead_config = {
            ## inject configuration
            'brand'                     : app.config.get("brand", ""),
            'nginx_upload_path'         : app.config.get("nginx_upload_path", h.url_for(controller='api', action='tools')),
            'use_remote_user'           : app.config.use_remote_user,
            'remote_user_logout_href'   : app.config.remote_user_logout_href,
            'enable_cloud_launch'       : app.config.get_bool('enable_cloud_launch', False),
            'lims_doc_url'              : app.config.get("lims_doc_url", "https://usegalaxy.org/u/rkchak/p/sts"),
            'biostar_url'               : app.config.biostar_url,
            'biostar_url_redirect'      : h.url_for( controller='biostar', action='biostar_redirect', qualified=True ),
            'support_url'               : app.config.get("support_url", "https://wiki.galaxyproject.org/Support"),
            'search_url'                : app.config.get("search_url", "http://galaxyproject.org/search/usegalaxy/"),
            'mailing_lists'             : app.config.get("mailing_lists", "https://wiki.galaxyproject.org/MailingLists"),
            'screencasts_url'           : app.config.get("screencasts_url", "https://vimeo.com/galaxyproject"),
            'wiki_url'                  : app.config.get("wiki_url", "https://wiki.galaxyproject.org/"),
            'citation_url'              : app.config.get("citation_url", "https://wiki.galaxyproject.org/CitingGalaxy"),
            'terms_url'                 : app.config.get("terms_url", ""),
            'allow_user_creation'       : app.config.allow_user_creation,
            'logo_url'                  : h.url_for(app.config.get( 'logo_url', '/')),
            'logo_src'                  : h.url_for( app.config.get( 'logo_src', '../../../static/images/galaxyIcon_noText.png' ) ),
            'is_admin_user'             : trans.user_is_admin(),
            'active_view'               : active_view,
            'ftp_upload_dir'            : app.config.get("ftp_upload_dir",  None),
            'ftp_upload_site'           : app.config.get("ftp_upload_site",  None),
            'datatypes_disable_auto'    : app.config.get_bool("datatypes_disable_auto",  False),
            'user_requests'             : bool( trans.user and ( trans.user.requests or app.security_agent.get_accessible_request_types( trans, trans.user ) ) ),
            'user_json'                 : get_user_dict()
        }
            
        
        __M_writer(u'\n\n')
        __M_writer(u'    <script type="text/javascript">\n        if( !window.Galaxy ){\n            Galaxy = {};\n        }\n\n        // if we\'re in an iframe, create styles that hide masthead/messagebox, and reset top for panels\n        // note: don\'t use a link to avoid roundtrip request\n        // note: we can\'t select here because the page (incl. messgaebox, center, etc.) isn\'t fully rendered\n        // TODO: remove these when we no longer navigate with iframes\n        var in_iframe = window !== window.top;\n        if( in_iframe ){\n            var styleElement = document.createElement( \'style\' );\n            document.head.appendChild( styleElement );\n            [\n                \'#masthead, #messagebox { display: none; }\',\n                \'#center, #right, #left { top: 0 !important; }\',\n             ].forEach( function( rule ){\n                styleElement.sheet.insertRule( rule, 0 );\n            });\n        }\n        // TODO: ?? move above to base_panels.mako?\n\n')
        __M_writer(u"        require([\n            'layout/masthead',\n            'mvc/ui/ui-modal',\n            'mvc/user/user-model'\n        ], function( Masthead, Modal, user ){\n            if( !Galaxy.user ) {\n                // this doesn't need to wait for the page being readied\n                Galaxy.user = new user.User(")
        __M_writer(unicode( h.dumps( masthead_config[ 'user_json' ], indent=2 ) ))
        __M_writer(u');\n            }\n\n            $(function() {\n                if (!Galaxy.masthead) {\n                    Galaxy.masthead = new Masthead.View(')
        __M_writer(unicode( h.dumps( masthead_config ) ))
        __M_writer(u");\n                    Galaxy.modal = new Modal.View();\n                    $('#masthead').replaceWith( Galaxy.masthead.render().$el );\n                }\n            });\n        });\n    </script>\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"96": 90, "33": 1, "39": 4, "87": 69, "50": 4, "51": 5, "84": 36, "85": 39, "86": 62, "23": 1, "88": 69, "89": 74, "26": 0, "90": 74}, "uri": "/webapps/galaxy/galaxy.masthead.mako", "filename": "templates/webapps/galaxy/galaxy.masthead.mako"}
__M_END_METADATA
"""
