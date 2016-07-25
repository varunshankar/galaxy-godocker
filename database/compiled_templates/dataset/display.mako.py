# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1469467675.393198
_enable_loop = True
_template_filename = u'templates/webapps/galaxy/dataset/display.mako'
_template_uri = u'/dataset/display.mako'
_source_encoding = 'ascii'
_exports = ['title', 'center_panel', 'right_panel', 'render_item', 'init', 'render_item_links', 'render_deleted_data_message', 'javascripts']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('__anon_0x7f04acc95a50', context._clean_inheritance_tokens(), templateuri=u'/tagging_common.mako', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f04acc95a50')] = ns

    ns = runtime.TemplateNamespace('__anon_0x7f04acc95610', context._clean_inheritance_tokens(), templateuri=u'/display_common.mako', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f04acc95610')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/display_base.mako', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f04acc95a50')._populate(_import_ns, [u'render_individual_tagging_element', u'render_community_tagging_element'])
        _mako_get_namespace(context, '__anon_0x7f04acc95610')._populate(_import_ns, [u'*'])
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
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
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f04acc95a50')._populate(_import_ns, [u'render_individual_tagging_element', u'render_community_tagging_element'])
        _mako_get_namespace(context, '__anon_0x7f04acc95610')._populate(_import_ns, [u'*'])
        item = _import_ns.get('item', context.get('item', UNDEFINED))
        get_class_display_name = _import_ns.get('get_class_display_name', context.get('get_class_display_name', UNDEFINED))
        get_item_name = _import_ns.get('get_item_name', context.get('get_item_name', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n    Galaxy | ')
        __M_writer(unicode(get_class_display_name( item.__class__ )))
        __M_writer(u' | ')
        __M_writer(filters.html_escape(unicode(get_item_name( item ) )))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_panel(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f04acc95a50')._populate(_import_ns, [u'render_individual_tagging_element', u'render_community_tagging_element'])
        _mako_get_namespace(context, '__anon_0x7f04acc95610')._populate(_import_ns, [u'*'])
        item_data = _import_ns.get('item_data', context.get('item_data', UNDEFINED))
        get_class_display_name = _import_ns.get('get_class_display_name', context.get('get_class_display_name', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        item = _import_ns.get('item', context.get('item', UNDEFINED))
        get_item_name = _import_ns.get('get_item_name', context.get('get_item_name', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n    <div class="unified-panel-header" unselectable="on">\n        <div class="unified-panel-header-inner">\n                ')
        __M_writer(unicode(get_class_display_name( item.__class__ )))
        __M_writer(u'\n            | ')
        __M_writer(filters.html_escape(unicode(get_item_name( item ) )))
        __M_writer(u'\n        </div>\n    </div>\n\n    <div class="unified-panel-body">\n        <div style="overflow: auto; height: 100%;">\n            <div class="page-body">\n                <div style="float: right">\n                    ')
        __M_writer(unicode(self.render_item_links( item )))
        __M_writer(u'\n                </div>\n                <div>\n                    ')
        __M_writer(unicode(self.render_item_header( item )))
        __M_writer(u'\n                </div>\n\n                ')
        __M_writer(unicode(self.render_item( item, item_data )))
        __M_writer(u'\n            </div>\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_right_panel(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f04acc95a50')._populate(_import_ns, [u'render_individual_tagging_element', u'render_community_tagging_element'])
        _mako_get_namespace(context, '__anon_0x7f04acc95610')._populate(_import_ns, [u'*'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        render_community_tagging_element = _import_ns.get('render_community_tagging_element', context.get('render_community_tagging_element', UNDEFINED))
        item = _import_ns.get('item', context.get('item', UNDEFINED))
        get_class_display_name = _import_ns.get('get_class_display_name', context.get('get_class_display_name', UNDEFINED))
        render_individual_tagging_element = _import_ns.get('render_individual_tagging_element', context.get('render_individual_tagging_element', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n    <div class="unified-panel-header" unselectable="on">\n        <div class="unified-panel-header-inner">\n            About this ')
        __M_writer(unicode(get_class_display_name( item.__class__ )))
        __M_writer(u'\n        </div>\n    </div>\n\n    <div class="unified-panel-body">\n        <div style="overflow: auto; height: 100%;">\n            <div style="padding: 10px;">\n                <h4>Author</h4>\n\n                <p>')
        __M_writer(filters.html_escape(unicode(item.history.user.username )))
        __M_writer(u'</p>\n\n                <div><img src="https://secure.gravatar.com/avatar/')
        __M_writer(unicode(h.md5(item.history.user.email)))
        __M_writer(u'?d=identicon&s=150"></div>\n\n')
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'                <p>\n                <h4>Tags</h4>\n                <p>\n')
        __M_writer(u'                <div>\n                    Community:\n                    ')
        __M_writer(unicode(render_community_tagging_element( tagged_item=item, tag_click_fn='community_tag_click', use_toggle_link=False )))
        __M_writer(u'\n')
        if len ( item.tags ) == 0:
            __M_writer(u'                        none\n')
        __M_writer(u'                </div>\n')
        __M_writer(u'                <p>\n                <div>\n                    Yours:\n                    ')
        __M_writer(unicode(render_individual_tagging_element( user=trans.get_user(), tagged_item=item, elt_context='view.mako', use_toggle_link=False, tag_click_fn='community_tag_click' )))
        __M_writer(u'\n                </div>\n            </div>\n        </div>\n    </div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_item(context,data,data_to_render):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f04acc95a50')._populate(_import_ns, [u'render_individual_tagging_element', u'render_community_tagging_element'])
        _mako_get_namespace(context, '__anon_0x7f04acc95610')._populate(_import_ns, [u'*'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        def render_deleted_data_message(data):
            return render_render_deleted_data_message(context,data)
        truncated = _import_ns.get('truncated', context.get('truncated', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        __M_writer(unicode( render_deleted_data_message( data ) ))
        __M_writer(u'\n')
        if data_to_render:
            if truncated:
                __M_writer(u'            <div class="warningmessagelarge">\n                 This dataset is large and only the first megabyte is shown below. |\n                 <a href="')
                __M_writer(unicode(h.url_for( controller='dataset', action='display_by_username_and_slug', username=data.history.user.username, slug=trans.security.encode_id( data.id ), preview=False )))
                __M_writer(u'">Show all</a>\n            </div>\n')
            __M_writer(u'        <pre style="font-size: 135%">')
            __M_writer(filters.html_escape(unicode( data_to_render )))
            __M_writer(u'</pre>\n')
        else:
            __M_writer(u"        <p align='center'>Cannot show dataset content</p>\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_init(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f04acc95a50')._populate(_import_ns, [u'render_individual_tagging_element', u'render_community_tagging_element'])
        _mako_get_namespace(context, '__anon_0x7f04acc95610')._populate(_import_ns, [u'*'])
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')

        self.has_left_panel=False
        self.has_right_panel=True
        self.message_box_visible=False
        self.active_view="user"
        self.overlay_visible=False
        
        
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_item_links(context,data):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f04acc95a50')._populate(_import_ns, [u'render_individual_tagging_element', u'render_community_tagging_element'])
        _mako_get_namespace(context, '__anon_0x7f04acc95610')._populate(_import_ns, [u'*'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'    <a href="')
        __M_writer(unicode(h.url_for( controller='/dataset', action='display', dataset_id=trans.security.encode_id( data.id ), to_ext=data.ext )))
        __M_writer(u'" class="icon-button disk" title="Save dataset"></a>\n        <a\n            href="')
        __M_writer(unicode(h.url_for( controller='/dataset', action='imp', dataset_id=trans.security.encode_id( data.id ) )))
        __M_writer(u'"\n            class="icon-button import"\n            title="Import dataset"></a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_deleted_data_message(context,data):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f04acc95a50')._populate(_import_ns, [u'render_individual_tagging_element', u'render_community_tagging_element'])
        _mako_get_namespace(context, '__anon_0x7f04acc95610')._populate(_import_ns, [u'*'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')
        if data.deleted:
            __M_writer(u'        <div class="errormessagelarge" id="deleted-data-message">\n            You are viewing a deleted dataset.\n')
            if data.history and data.history.user == trans.get_user():
                __M_writer(u'                <br />\n                <a href="#" onclick="$.ajax( {type: \'GET\', cache: false, url: \'')
                __M_writer(unicode(h.url_for( controller='dataset', action='undelete_async', dataset_id=trans.security.encode_id( data.id ) )))
                __M_writer(u'\', dataType: \'text\', contentType: \'text/html\', success: function( data, textStatus, jqXHR ){ if (data == \'OK\' ){ $( \'#deleted-data-message\' ).slideUp( \'slow\' ) } else { alert( \'Undelete failed.\' ) } }, error: function( data, textStatus, jqXHR ){ alert( \'Undelete failed.\' ); } } );">Undelete</a>\n')
            __M_writer(u'        </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f04acc95a50')._populate(_import_ns, [u'render_individual_tagging_element', u'render_community_tagging_element'])
        _mako_get_namespace(context, '__anon_0x7f04acc95610')._populate(_import_ns, [u'*'])
        item = _import_ns.get('item', context.get('item', UNDEFINED))
        first_chunk = _import_ns.get('first_chunk', context.get('first_chunk', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        __M_writer(unicode(parent.javascripts()))
        __M_writer(u'\n\n')
        if item.datatype.CHUNKABLE:
            __M_writer(u'\n    <script type="text/javascript">\n        require([\'mvc/dataset/data\'], function(data) {\n            //\n            // Use tabular data display progressively by deleting data from page body\n            // and then showing dataset view.\n            //\n            $(\'.page-body\').children().remove();\n\n            data.createTabularDatasetChunkedView({\n                // TODO: encode id.\n                dataset_config:\n                    _.extend( ')
            __M_writer(unicode(h.dumps( item.to_dict() )))
            __M_writer(u', {\n                        chunk_url: "')
            __M_writer(unicode(h.url_for( controller='/dataset', action='display',
                                         dataset_id=trans.security.encode_id( item.id ))))
            __M_writer(u'",\n                        first_data_chunk: ')
            __M_writer(unicode(first_chunk))
            __M_writer(u"\n                    }),\n                parent_elt: $('.page-body')\n            });\n        });\n    </script>\n\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"23": 4, "26": 3, "32": 0, "40": 2, "41": 3, "42": 4, "43": 34, "44": 44, "45": 48, "46": 57, "47": 74, "48": 86, "49": 110, "50": 154, "56": 46, "66": 46, "67": 47, "68": 47, "69": 47, "70": 47, "76": 88, "88": 88, "89": 91, "90": 91, "91": 92, "92": 92, "93": 100, "94": 100, "95": 103, "96": 103, "97": 106, "98": 106, "104": 112, "118": 112, "119": 115, "120": 115, "121": 124, "122": 124, "123": 126, "124": 126, "125": 129, "126": 131, "127": 133, "128": 137, "129": 139, "130": 139, "131": 140, "132": 141, "133": 143, "134": 145, "135": 148, "136": 148, "142": 60, "154": 60, "155": 61, "156": 61, "157": 62, "158": 63, "159": 64, "160": 66, "161": 66, "162": 70, "163": 70, "164": 70, "165": 71, "166": 72, "172": 36, "180": 36, "181": 37, "189": 43, "195": 50, "204": 50, "205": 52, "206": 52, "207": 52, "208": 54, "209": 54, "215": 76, "224": 76, "225": 77, "226": 78, "227": 80, "228": 81, "229": 82, "230": 82, "231": 84, "237": 6, "249": 6, "250": 7, "251": 7, "252": 10, "253": 11, "254": 23, "255": 23, "256": 24, "258": 25, "259": 26, "260": 26, "266": 260}, "uri": "/dataset/display.mako", "filename": "templates/webapps/galaxy/dataset/display.mako"}
__M_END_METADATA
"""
