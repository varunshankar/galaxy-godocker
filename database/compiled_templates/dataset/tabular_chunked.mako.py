# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1469467675.379816
_enable_loop = True
_template_filename = 'templates/webapps/galaxy/dataset/tabular_chunked.mako'
_template_uri = '/dataset/tabular_chunked.mako'
_source_encoding = 'ascii'
_exports = ['stylesheets', 'javascripts', 'title']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('__anon_0x7f04acf62f50', context._clean_inheritance_tokens(), templateuri=u'/dataset/display.mako', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f04acf62f50')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.mako', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f04acf62f50')._populate(_import_ns, [u'render_deleted_data_message'])
        render_deleted_data_message = _import_ns.get('render_deleted_data_message', context.get('render_deleted_data_message', UNDEFINED))
        dataset = _import_ns.get('dataset', context.get('dataset', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(unicode( render_deleted_data_message( dataset ) ))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stylesheets(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f04acf62f50')._populate(_import_ns, [u'render_deleted_data_message'])
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        __M_writer(unicode(parent.stylesheets()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f04acf62f50')._populate(_import_ns, [u'render_deleted_data_message'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        chunk = _import_ns.get('chunk', context.get('chunk', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        dataset = _import_ns.get('dataset', context.get('dataset', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        __M_writer(unicode(parent.javascripts()))
        __M_writer(u'\n\n    <script type="text/javascript">\n        require([ \'mvc/dataset/data\' ], function( data ) {\n            data.createTabularDatasetChunkedView({\n                dataset_config : _.extend( ')
        __M_writer(unicode( h.dumps( trans.security.encode_dict_ids( dataset.to_dict() ) )))
        __M_writer(u', {\n                        first_data_chunk: ')
        __M_writer(unicode( chunk ))
        __M_writer(u"\n                    }),\n                parent_elt : $( 'body' )\n            });\n        });\n    </script>\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f04acf62f50')._populate(_import_ns, [u'render_deleted_data_message'])
        __M_writer = context.writer()
        __M_writer(u'Dataset Display')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"23": 2, "29": 0, "38": 1, "39": 2, "40": 4, "41": 19, "42": 23, "43": 25, "44": 25, "50": 21, "57": 21, "58": 22, "59": 22, "65": 6, "76": 6, "77": 7, "78": 7, "79": 12, "80": 12, "81": 13, "82": 13, "88": 4, "94": 4, "100": 94}, "uri": "/dataset/tabular_chunked.mako", "filename": "templates/webapps/galaxy/dataset/tabular_chunked.mako"}
__M_END_METADATA
"""
