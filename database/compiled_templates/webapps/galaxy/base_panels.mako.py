# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1469467675.482162
_enable_loop = True
_template_filename = 'templates/webapps/galaxy/base_panels.mako'
_template_uri = '/webapps/galaxy/base_panels.mako'
_source_encoding = 'ascii'
_exports = ['masthead', 'javascripts', 'late_javascripts', 'title']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'mod_masthead', context._clean_inheritance_tokens(), templateuri=u'/webapps/galaxy/galaxy.masthead.mako', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'mod_masthead')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base/base_panels.mako', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'\n<!-- webapps/galaxy/base_panels.mako -->\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_masthead(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        mod_masthead = _mako_get_namespace(context, 'mod_masthead')
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')

        mod_masthead.load(self.active_view);
            
        
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(unicode(parent.javascripts()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_late_javascripts(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(unicode(parent.late_javascripts()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u'Galaxy')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"23": 3, "29": 0, "34": 1, "35": 3, "36": 6, "37": 10, "38": 14, "39": 21, "45": 17, "51": 17, "52": 18, "56": 20, "62": 8, "67": 8, "68": 9, "69": 9, "75": 12, "80": 12, "81": 13, "82": 13, "88": 6, "92": 6, "98": 92}, "uri": "/webapps/galaxy/base_panels.mako", "filename": "templates/webapps/galaxy/base_panels.mako"}
__M_END_METADATA
"""
