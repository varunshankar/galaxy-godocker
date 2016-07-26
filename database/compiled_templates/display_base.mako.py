# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1469467675.466874
_enable_loop = True
_template_filename = u'templates/display_base.mako'
_template_uri = u'/display_base.mako'
_source_encoding = 'ascii'
_exports = ['body', 'render_content', 'title', 'center_panel', 'right_panel', 'stylesheets', 'render_item', 'init', 'render_item_header', 'render_item_links', 'javascripts']



def inherit( context ):
    if context.get('no_panels'):
        return '/base.mako'
    else:
        return '/webapps/galaxy/base_panels.mako'

from galaxy.model import History, StoredWorkflow, Page
from galaxy.web.framework.helpers import iff


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('__anon_0x7f04acd8c210', context._clean_inheritance_tokens(), templateuri=u'/display_common.mako', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f04acd8c210')] = ns

    ns = runtime.TemplateNamespace('__anon_0x7f04acd8ce90', context._clean_inheritance_tokens(), templateuri=u'/tagging_common.mako', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f04acd8ce90')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, (inherit( context )), _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f04acd8c210')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x7f04acd8ce90')._populate(_import_ns, [u'render_individual_tagging_element', u'render_community_tagging_element', u'community_tag_js'])
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f04acd8c210')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x7f04acd8ce90')._populate(_import_ns, [u'render_individual_tagging_element', u'render_community_tagging_element', u'community_tag_js'])
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        __M_writer(unicode(self.render_content()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_content(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f04acd8c210')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x7f04acd8ce90')._populate(_import_ns, [u'render_individual_tagging_element', u'render_community_tagging_element', u'community_tag_js'])
        get_item_name = _import_ns.get('get_item_name', context.get('get_item_name', UNDEFINED))
        get_item_plural = _import_ns.get('get_item_plural', context.get('get_item_plural', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        item = _import_ns.get('item', context.get('item', UNDEFINED))
        get_class_display_name = _import_ns.get('get_class_display_name', context.get('get_class_display_name', UNDEFINED))
        get_controller_name = _import_ns.get('get_controller_name', context.get('get_controller_name', UNDEFINED))
        item_data = _import_ns.get('item_data', context.get('item_data', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n\n')
        __M_writer(u'    ')

        ##TODO: is there a better way to create this URL? Can't use 'f-username' as a key b/c it's not a valid identifier.
        controller_name = get_controller_name( item )
        item_plural = get_item_plural( item )
        href_to_all_items = h.url_for( controller='/' + controller_name, action='list_published')
        href_to_user_items = h.url_for( controller='/' + controller_name, action='list_published', xxx=item.user.username)
        href_to_user_items = href_to_user_items.replace( 'xxx', 'f-username')
            
        
        __M_writer(u'\n\n    <div class="unified-panel-header" unselectable="on" style="overflow: hidden">\n        <div class="unified-panel-header-inner">\n            <div style="float: right">\n                ')
        __M_writer(unicode(self.render_item_links( item )))
        __M_writer(u'\n            </div>\n')
        if item.published:
            __M_writer(u'                    <a href="')
            __M_writer(unicode(href_to_all_items))
            __M_writer(u'">Published ')
            __M_writer(unicode(item_plural))
            __M_writer(u'</a> |\n                    <a href="')
            __M_writer(unicode(href_to_user_items))
            __M_writer(u'">')
            __M_writer(unicode(item.user.username))
            __M_writer(u'</a>\n')
        elif item.importable:
            __M_writer(u'                Accessible ')
            __M_writer(unicode(get_class_display_name( item.__class__ )))
            __M_writer(u'\n')
        elif item.users_shared_with:
            __M_writer(u'                Shared ')
            __M_writer(unicode(get_class_display_name( item.__class__ )))
            __M_writer(u'\n')
        else:
            __M_writer(u'                Private ')
            __M_writer(unicode(get_class_display_name( item.__class__ )))
            __M_writer(u'\n')
        __M_writer(u'            | ')
        __M_writer(filters.html_escape(unicode(get_item_name( item ) )))
        __M_writer(u'\n        </div>\n    </div>\n\n    <div class="unified-panel-body">\n        <div style="overflow: auto; height: 100%;">\n            <div class="page-body">\n                <div>\n                    ')
        __M_writer(unicode(self.render_item_header( item )))
        __M_writer(u'\n                </div>\n\n                ')
        __M_writer(unicode(self.render_item( item, item_data )))
        __M_writer(u'\n            </div>\n\n\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f04acd8c210')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x7f04acd8ce90')._populate(_import_ns, [u'render_individual_tagging_element', u'render_community_tagging_element', u'community_tag_js'])
        item = _import_ns.get('item', context.get('item', UNDEFINED))
        get_class_display_name = _import_ns.get('get_class_display_name', context.get('get_class_display_name', UNDEFINED))
        get_item_name = _import_ns.get('get_item_name', context.get('get_item_name', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n    Galaxy | ')
        __M_writer(unicode(iff( item.published, "Published ", iff( item.importable , "Accessible ", iff( item.users_shared_with, "Shared ", "Private " ) ) ) + get_class_display_name( item.__class__ )))
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
        _mako_get_namespace(context, '__anon_0x7f04acd8c210')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x7f04acd8ce90')._populate(_import_ns, [u'render_individual_tagging_element', u'render_community_tagging_element', u'community_tag_js'])
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        __M_writer(unicode(self.render_content()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_right_panel(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f04acd8c210')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x7f04acd8ce90')._populate(_import_ns, [u'render_individual_tagging_element', u'render_community_tagging_element', u'community_tag_js'])
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        get_item_plural = _import_ns.get('get_item_plural', context.get('get_item_plural', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        render_community_tagging_element = _import_ns.get('render_community_tagging_element', context.get('render_community_tagging_element', UNDEFINED))
        num_ratings = _import_ns.get('num_ratings', context.get('num_ratings', UNDEFINED))
        item = _import_ns.get('item', context.get('item', UNDEFINED))
        get_class_display_name = _import_ns.get('get_class_display_name', context.get('get_class_display_name', UNDEFINED))
        user_item_rating = _import_ns.get('user_item_rating', context.get('user_item_rating', UNDEFINED))
        get_controller_name = _import_ns.get('get_controller_name', context.get('get_controller_name', UNDEFINED))
        render_individual_tagging_element = _import_ns.get('render_individual_tagging_element', context.get('render_individual_tagging_element', UNDEFINED))
        ave_item_rating = _import_ns.get('ave_item_rating', context.get('ave_item_rating', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n\n    ')

        ## FIXME: duplicated from above for now
        controller_name = get_controller_name( item )
        item_plural = get_item_plural( item )
        href_to_all_items = h.url_for( controller='/' + controller_name, action='list_published')
        href_to_user_items = h.url_for( controller='/' + controller_name, action='list_published', xxx=item.user.username)
        href_to_user_items = href_to_user_items.replace( 'xxx', 'f-username')
            
        
        __M_writer(u'\n\n    <div class="unified-panel-header" unselectable="on">\n        <div class="unified-panel-header-inner">\n            About this ')
        __M_writer(unicode(get_class_display_name( item.__class__ )))
        __M_writer(u'\n        </div>\n    </div>\n\n    <div class="unified-panel-body">\n        <div style="overflow: auto; height: 100%;">\n            <div style="padding: 10px;">\n\n                <div style="float: right;"><img src="https://secure.gravatar.com/avatar/')
        __M_writer(unicode(h.md5(item.user.email)))
        __M_writer(u'?d=identicon"></div>\n\n                <h4>Author</h4>\n\n                <p>')
        __M_writer(filters.html_escape(unicode(item.user.username )))
        __M_writer(u'</p>\n\n')
        __M_writer(u'                <h4>Related ')
        __M_writer(unicode(item_plural))
        __M_writer(u'</h4>\n                <p>\n                    <a href="')
        __M_writer(unicode(href_to_all_items))
        __M_writer(u'">All published ')
        __M_writer(unicode(item_plural.lower()))
        __M_writer(u'</a><br>\n                    <a href="')
        __M_writer(unicode(href_to_user_items))
        __M_writer(u'">Published ')
        __M_writer(unicode(item_plural.lower()))
        __M_writer(u' by ')
        __M_writer(filters.html_escape(unicode(item.user.username )))
        __M_writer(u'</a>\n\n')
        __M_writer(u'                <h4>Rating</h4>\n\n                ')

        label = "ratings"
        if num_ratings == 1:
            label = "rating"
                        
        
        __M_writer(u'\n                <div style="padding-bottom: 0.75em; float: left">\n                    Community<br>\n                    <span style="font-size:80%">\n                        (<span id="num_ratings">')
        __M_writer(unicode(num_ratings))
        __M_writer(u'</span> ')
        __M_writer(unicode(label))
        __M_writer(u',\n                         <span id="ave_rating">')
        __M_writer(unicode("%.1f" % ave_item_rating))
        __M_writer(u'</span> average)\n                    <span>\n                </div>\n                <div style="float: right">\n                    <input name="star1" type="radio" class="community_rating_star star" disabled="disabled" value="1"\n')
        if ave_item_rating > 0 and ave_item_rating <= 1.5:
            __M_writer(u'                        checked="checked"\n')
        __M_writer(u'\n                    />\n                    <input name="star1" type="radio" class="community_rating_star star" disabled="disabled" value="2"\n')
        if ave_item_rating > 1.5 and ave_item_rating <= 2.5:
            __M_writer(u'                        checked="checked"\n')
        __M_writer(u'                    />\n                    <input name="star1" type="radio" class="community_rating_star star" disabled="disabled" value="3"\n')
        if ave_item_rating > 2.5 and ave_item_rating <= 3.5:
            __M_writer(u'                        checked="checked"\n')
        __M_writer(u'                    />\n                    <input name="star1" type="radio" class="community_rating_star star" disabled="disabled" value="4"\n')
        if ave_item_rating > 3.5 and ave_item_rating <= 4.5:
            __M_writer(u'                        checked="checked"\n')
        __M_writer(u'                    />\n                    <input name="star1" type="radio" class="community_rating_star star" disabled="disabled" value="5"\n')
        if ave_item_rating > 4.5:
            __M_writer(u'                        checked="checked"\n')
        __M_writer(u'                    />\n                </div>\n                <div style="clear: both;"></div>\n')
        if trans.get_user():
            __M_writer(u'                    <div style="float: left">\n                        Yours<br><span id="rating_feedback" style="font-size:80%; display: none">(thanks!)</span>\n                    </div>\n                    <div style="float: right">\n                        <input name="star2" type="radio" class="user_rating_star" value="1"\n')
            if user_item_rating == 1:
                __M_writer(u'                            checked="checked"\n')
            __M_writer(u'                        />\n                        <input name="star2" type="radio" class="user_rating_star" value="2"\n')
            if user_item_rating == 2:
                __M_writer(u'                            checked="checked"\n')
            __M_writer(u'                        />\n                        <input name="star2" type="radio" class="user_rating_star" value="3"\n')
            if user_item_rating == 3:
                __M_writer(u'                            checked="checked"\n')
            __M_writer(u'                        />\n                        <input name="star2" type="radio" class="user_rating_star" value="4"\n')
            if user_item_rating == 4:
                __M_writer(u'                            checked="checked"\n')
            __M_writer(u'                        />\n                        <input name="star2" type="radio" class="user_rating_star" value="5"\n')
            if user_item_rating == 5:
                __M_writer(u'                            checked="checked"\n')
            __M_writer(u'                        />\n                    </div>\n')
        __M_writer(u'                <div style="clear: both;"></div>\n\n')
        __M_writer(u'                <h4>Tags</h4>\n                <p>\n')
        __M_writer(u'                <div>\n                    Community:\n                    ')
        __M_writer(unicode(render_community_tagging_element( tagged_item=item, tag_click_fn='community_tag_click', use_toggle_link=False )))
        __M_writer(u'\n')
        if len ( item.tags ) == 0:
            __M_writer(u'                        none\n')
        __M_writer(u'                </div>\n')
        if trans.get_user():
            __M_writer(u'                    <p>\n                    <div>\n                        Yours:\n                        ')
            __M_writer(unicode(render_individual_tagging_element( user=trans.get_user(), tagged_item=item, elt_context='view.mako', use_toggle_link=False, tag_click_fn='community_tag_click' )))
            __M_writer(u'\n                    </div>\n')
        __M_writer(u'            </div>\n        </div>\n    </div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stylesheets(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f04acd8c210')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x7f04acd8ce90')._populate(_import_ns, [u'render_individual_tagging_element', u'render_community_tagging_element', u'community_tag_js'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        __M_writer(unicode(parent.stylesheets()))
        __M_writer(u'\n    ')
        __M_writer(unicode(h.css(
        "autocomplete_tagging",
        "embed_item",
        "jquery.rating",
        "library",
        "jquery-ui/smoothness/jquery-ui"
    )))
        __M_writer(u'\n\n    <style type="text/css">\n        .page-body {\n            padding: 10px;\n')
        __M_writer(u'        }\n        .page-meta {\n            float: right;\n            width: 27%;\n            padding: 0.5em;\n            margin: 0.25em;\n            vertical-align: text-top;\n            border: 2px solid #DDDDDD;\n            border-top: 4px solid #DDDDDD;\n        }\n\n')
        __M_writer(u'        .toolForm {\n            max-width: 500px;\n        }\n\n')
        __M_writer(u'        div.toolForm{\n            margin-top: 10px;\n            margin-bottom: 10px;\n        }\n\n    </style>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_item(context,item,item_data=None):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f04acd8c210')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x7f04acd8ce90')._populate(_import_ns, [u'render_individual_tagging_element', u'render_community_tagging_element', u'community_tag_js'])
        __M_writer = context.writer()
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_init(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f04acd8c210')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x7f04acd8ce90')._populate(_import_ns, [u'render_individual_tagging_element', u'render_community_tagging_element', u'community_tag_js'])
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')

        self.has_left_panel=False
        self.has_right_panel=True
        self.message_box_visible=False
        self.active_view="shared"
        self.overlay_visible=False
        
        
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_item_header(context,item):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f04acd8c210')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x7f04acd8ce90')._populate(_import_ns, [u'render_individual_tagging_element', u'render_community_tagging_element', u'community_tag_js'])
        get_item_name = _import_ns.get('get_item_name', context.get('get_item_name', UNDEFINED))
        get_class_display_name = _import_ns.get('get_class_display_name', context.get('get_class_display_name', UNDEFINED))
        hasattr = _import_ns.get('hasattr', context.get('hasattr', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n    <h3>Galaxy ')
        __M_writer(unicode(get_class_display_name( item.__class__ )))
        __M_writer(u" '")
        __M_writer(filters.html_escape(unicode(get_item_name( item ))))
        __M_writer(u"'</h3>\n")
        if hasattr( item, "annotation") and item.annotation is not None:
            __M_writer(u'        <div class="annotation">Annotation: ')
            __M_writer(unicode(item.annotation))
            __M_writer(u'</div>\n')
        __M_writer(u'    <hr/>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_item_links(context,item):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f04acd8c210')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x7f04acd8ce90')._populate(_import_ns, [u'render_individual_tagging_element', u'render_community_tagging_element', u'community_tag_js'])
        __M_writer = context.writer()
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f04acd8c210')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, '__anon_0x7f04acd8ce90')._populate(_import_ns, [u'render_individual_tagging_element', u'render_community_tagging_element', u'community_tag_js'])
        community_tag_js = _import_ns.get('community_tag_js', context.get('community_tag_js', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        get_controller_name = _import_ns.get('get_controller_name', context.get('get_controller_name', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        item = _import_ns.get('item', context.get('item', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        __M_writer(unicode(parent.javascripts()))
        __M_writer(u'\n    ')
        __M_writer(unicode(h.js(
        "libs/jquery/jstorage",
        "libs/jquery/jquery.event.drag",
        "libs/jquery/jquery.mousewheel",
        "libs/farbtastic",
        "libs/jquery/jquery.autocomplete",
    )))
        __M_writer(u'\n    ')
        __M_writer(unicode(community_tag_js( get_controller_name( item ) )))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"16": 1, "34": 13, "37": 12, "43": 0, "51": 10, "52": 11, "53": 12, "54": 13, "55": 18, "56": 21, "57": 31, "58": 43, "59": 83, "60": 87, "61": 95, "62": 99, "63": 104, "64": 109, "65": 159, "66": 295, "72": 102, "80": 102, "81": 103, "82": 103, "88": 115, "103": 115, "104": 118, "105": 118, "114": 125, "115": 130, "116": 130, "117": 132, "118": 133, "119": 133, "120": 133, "121": 133, "122": 133, "123": 134, "124": 134, "125": 134, "126": 134, "127": 135, "128": 136, "129": 136, "130": 136, "131": 137, "132": 138, "133": 138, "134": 138, "135": 139, "136": 140, "137": 140, "138": 140, "139": 142, "140": 142, "141": 142, "142": 150, "143": 150, "144": 153, "145": 153, "151": 19, "161": 19, "162": 20, "163": 20, "164": 20, "165": 20, "171": 107, "179": 107, "180": 108, "181": 108, "187": 161, "206": 161, "207": 163, "216": 170, "217": 174, "218": 174, "219": 182, "220": 182, "221": 186, "222": 186, "223": 189, "224": 189, "225": 189, "226": 191, "227": 191, "228": 191, "229": 191, "230": 192, "231": 192, "232": 192, "233": 192, "234": 192, "235": 192, "236": 195, "237": 197, "243": 201, "244": 205, "245": 205, "246": 205, "247": 205, "248": 206, "249": 206, "250": 211, "251": 212, "252": 214, "253": 217, "254": 218, "255": 220, "256": 222, "257": 223, "258": 225, "259": 227, "260": 228, "261": 230, "262": 232, "263": 233, "264": 235, "265": 238, "266": 239, "267": 244, "268": 245, "269": 247, "270": 249, "271": 250, "272": 252, "273": 254, "274": 255, "275": 257, "276": 259, "277": 260, "278": 262, "279": 264, "280": 265, "281": 267, "282": 270, "283": 273, "284": 276, "285": 278, "286": 278, "287": 279, "288": 280, "289": 282, "290": 284, "291": 285, "292": 288, "293": 288, "294": 291, "300": 45, "309": 45, "310": 46, "311": 46, "312": 47, "319": 53, "320": 60, "321": 72, "322": 77, "328": 97, "335": 97, "341": 23, "349": 23, "350": 24, "358": 30, "364": 89, "374": 89, "375": 90, "376": 90, "377": 90, "378": 90, "379": 91, "380": 92, "381": 92, "382": 92, "383": 94, "389": 85, "396": 85, "402": 33, "414": 33, "415": 34, "416": 34, "417": 35, "424": 41, "425": 42, "426": 42, "432": 426}, "uri": "/display_base.mako", "filename": "templates/display_base.mako"}
__M_END_METADATA
"""
