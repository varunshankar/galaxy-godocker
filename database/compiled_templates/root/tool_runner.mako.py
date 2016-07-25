# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1469467661.441125
_enable_loop = True
_template_filename = 'templates/webapps/galaxy/root/tool_runner.mako'
_template_uri = 'root/tool_runner.mako'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        h = context.get('h', UNDEFINED)
        job_errors = context.get('job_errors', UNDEFINED)
        out_data = context.get('out_data', UNDEFINED)
        len = context.get('len', UNDEFINED)
        num_jobs = context.get('num_jobs', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">\n<html>\n    <head>\n        <title>Galaxy</title>\n        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />\n        <link href="')
        __M_writer(unicode(h.url_for('/static/style/base.css')))
        __M_writer(u'" rel="stylesheet" type="text/css" />\n        <script type="text/javascript">\n            setTimeout( function() { top.location.href = \'')
        __M_writer(unicode(h.url_for( "/" )))
        __M_writer(u'\'; }, 1000 );\n        </script>\n    </head>\n    <body>\n        <div class="donemessagelarge">\n')
        if num_jobs > 1:
            __M_writer(u'              ')
            jobs_str = "%d jobs have" % num_jobs 
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['jobs_str'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n')
        else:
            __M_writer(u'              ')
            jobs_str = "A job has" 
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['jobs_str'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n')
        if len(out_data) == 1:
            __M_writer(u'              ')
            datasets_str = "dataset" 
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['datasets_str'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n')
        else:
            __M_writer(u'              ')
            datasets_str = "datasets" 
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['datasets_str'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n')
        __M_writer(u'            <p>\n                ')
        __M_writer(unicode(jobs_str))
        __M_writer(u' been successfully added to the queue - resulting in the following ')
        __M_writer(unicode(datasets_str))
        __M_writer(u':\n            </p>\n')
        for _, data in out_data:
            __M_writer(u'                <div style="padding: 10px"><b> ')
            __M_writer(unicode(data.hid))
            __M_writer(u': ')
            __M_writer(filters.html_escape(unicode(data.name )))
            __M_writer(u'</b></div>\n')
        __M_writer(u'            <p> You can check the status of queued jobs and view the resulting data by refreshing the <b>History</b> pane. When the job has been run the status will change from \'running\' to \'finished\' if completed successfully or \'error\' if problems were encountered. You are now being redirected back to <a href="')
        __M_writer(unicode(h.url_for( '/' )))
        __M_writer(u'">Galaxy</a>.</p>\n        </div>\n')
        if job_errors:
            __M_writer(u'            <div class="errormessagelarge">\n                There were errors setting up ')
            __M_writer(unicode(len(job_errors)))
            __M_writer(u' submitted job(s):\n                <ul>\n')
            for job_error in job_errors:
                __M_writer(u'                        <li><b>')
                __M_writer(filters.html_escape(unicode(job_error )))
                __M_writer(u'</b></li>\n')
            __M_writer(u'                </ul>\n            </div>\n')
        __M_writer(u'    </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"16": 0, "26": 1, "27": 6, "28": 6, "29": 8, "30": 8, "31": 13, "32": 14, "33": 14, "37": 14, "38": 15, "39": 16, "40": 16, "44": 16, "45": 18, "46": 19, "47": 19, "51": 19, "52": 20, "53": 21, "54": 21, "58": 21, "59": 23, "60": 24, "61": 24, "62": 24, "63": 24, "64": 26, "65": 27, "66": 27, "67": 27, "68": 27, "69": 27, "70": 29, "71": 29, "72": 29, "73": 31, "74": 32, "75": 33, "76": 33, "77": 35, "78": 36, "79": 36, "80": 36, "81": 38, "82": 41, "88": 82}, "uri": "root/tool_runner.mako", "filename": "templates/webapps/galaxy/root/tool_runner.mako"}
__M_END_METADATA
"""
