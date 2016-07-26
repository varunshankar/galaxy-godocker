# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1469467675.442467
_enable_loop = True
_template_filename = u'templates/display_common.mako'
_template_uri = u'/display_common.mako'
_source_encoding = 'ascii'
_exports = ['get_class_plural_display_name', 'get_item_user', 'get_item_plural', 'render_message', 'get_class_plural', 'get_item_name', 'get_class_display_name', 'get_controller_name', 'get_item_slug', 'get_history_link']


from galaxy import model 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_get_class_plural_display_name(context,a_class):
    __M_caller = context.caller_stack._push_frame()
    try:
        def get_class_display_name(a_class):
            return render_get_class_display_name(context,a_class)
        __M_writer = context.writer()
        __M_writer(u'\n')

    # Start with exceptions, end with default.
        if a_class is model.History:
            return "Histories"
        elif a_class is model.FormDefinitionCurrent:
            return "Forms"
        else:
            return get_class_display_name( a_class ) + "s"
        
        
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_get_item_user(context,item):
    __M_caller = context.caller_stack._push_frame()
    try:
        isinstance = context.get('isinstance', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')

        # Exceptions first, default last.
        if isinstance( item, model.HistoryDatasetAssociation ):
            return item.history.user
        else:
            return item.user
            
        
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_get_item_plural(context,item):
    __M_caller = context.caller_stack._push_frame()
    try:
        def get_class_plural(a_class):
            return render_get_class_plural(context,a_class)
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        return get_class_plural( item.__class__ ) 
        
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_message(context,message,status):
    __M_caller = context.caller_stack._push_frame()
    try:
        util = context.get('util', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if message:
            __M_writer(u'        <p>\n            <div class="')
            __M_writer(unicode(status))
            __M_writer(u'message transient-message">')
            __M_writer(unicode(util.restore_text( message )))
            __M_writer(u'</div>\n            <div style="clear: both"></div>\n        </p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_get_class_plural(context,a_class):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u'\n')

        if a_class == model.History:
            class_plural = "Histories"
        elif a_class == model.StoredWorkflow:
            class_plural = "Workflows"
        elif a_class == model.Page:
            class_plural = "Pages"
        elif a_class == model.Library:
            class_plural = "Libraries"
        elif a_class == model.HistoryDatasetAssociation:
            class_plural = "Datasets"
        elif a_class == model.SampleDataset:
            class_plural = "Sample Datasets"
        elif a_class == model.FormDefinitionCurrent:
            class_plural = "Forms"
        elif a_class == model.RequestType:
            class_plural = "request types"
        elif a_class == model.UserOpenID:
            class_plural = "OpenIDs"
        else:
            class_plural = "items"
        return class_plural
        
        
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_get_item_name(context,item):
    __M_caller = context.caller_stack._push_frame()
    try:
        hasattr = context.get('hasattr', UNDEFINED)
        type = context.get('type', UNDEFINED)
        unicode = context.get('unicode', UNDEFINED)
        str = context.get('str', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')
 
        # Start with exceptions, end with default.
        if type( item ) is model.Page:
            item_name = item.title
        elif type( item ) is model.Visualization:
            item_name = item.title
        elif hasattr( item, 'get_display_name'):
            item_name = item.get_display_name()
        else:
            item_name = item.name
        
        # Encode in unicode.
        if type( item_name ) is str:
            item_name = unicode( item_name, 'utf-8' )
        return item_name    
            
        
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_get_class_display_name(context,a_class):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u'\n')

    ## Start with exceptions, end with default.
        if a_class is model.StoredWorkflow:
            return "Workflow"
        elif a_class is model.HistoryDatasetAssociation:
            return "Dataset"
        else:
            return a_class.__name__
        
        
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_get_controller_name(context,item):
    __M_caller = context.caller_stack._push_frame()
    try:
        isinstance = context.get('isinstance', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')

        if isinstance( item, model.History ):
            return "history"
        elif isinstance( item, model.StoredWorkflow ):
            return "workflow"
        elif isinstance( item, model.HistoryDatasetAssociation ):
            return "dataset"
        elif isinstance( item, model.Page ):
            return "page"
        elif isinstance( item, model.Visualization ):
            return "visualization"
            
        
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_get_item_slug(context,item):
    __M_caller = context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        isinstance = context.get('isinstance', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')

        # Exceptions first, default last.
        if isinstance( item, model.HistoryDatasetAssociation ):
            return trans.security.encode_id( item.id )
        else:
            return item.slug
            
        
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_get_history_link(context,history,qualify=False):
    __M_caller = context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if history.slug and history.user.username:
            __M_writer(u'        ')
            return h.url_for( controller='/history', action='display_by_username_and_slug', username=history.user.username, slug=history.slug, qualified=qualify ) 
            
            __M_writer(u'\n')
        else:
            __M_writer(u'        ')
            return h.url_for( controller='/history', action='view', id=trans.security.encode_id( history.id ), qualified=qualify, use_panels=context.get('use_panels', True) ) 
            
            __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"256": 137, "257": 138, "258": 139, "235": 126, "261": 139, "262": 140, "263": 141, "264": 141, "236": 127, "266": 141, "151": 21, "16": 8, "145": 95, "18": 0, "259": 139, "23": 7, "24": 8, "25": 19, "26": 38, "27": 51, "28": 64, "29": 69, "30": 96, "31": 112, "32": 123, "33": 134, "34": 143, "35": 153, "198": 63, "41": 41, "47": 41, "48": 42, "177": 37, "183": 54, "244": 133, "58": 50, "159": 21, "188": 55, "64": 115, "160": 22, "69": 115, "70": 116, "204": 99, "78": 122, "209": 99, "210": 100, "84": 67, "90": 67, "91": 68, "93": 68, "223": 111, "272": 266, "99": 146, "229": 126, "104": 146, "105": 147, "106": 148, "107": 149, "108": 149, "109": 149, "110": 149, "116": 72, "187": 54, "120": 72, "121": 73, "250": 137}, "uri": "/display_common.mako", "filename": "templates/display_common.mako"}
__M_END_METADATA
"""
