# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1469467675.42137
_enable_loop = True
_template_filename = u'templates/tagging_common.mako'
_template_uri = u'/tagging_common.mako'
_source_encoding = 'ascii'
_exports = ['render_tagging_element_html', 'community_tag_js', 'render_tool_tagging_elements', 'render_individual_tagging_element', 'render_community_tagging_element']



from cgi import escape
from galaxy.web.framework.helpers import iff
from random import random
from sys import maxint
from math import floor
from galaxy.model import Tag, ItemTagAssociation


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        in_form = context.get('in_form', UNDEFINED)
        def render_community_tagging_element(tagged_item=None,elt_context=None,use_toggle_link=False,tag_click_fn='default_tag_click_fn'):
            return render_render_community_tagging_element(context._locals(__M_locals),tagged_item,elt_context,use_toggle_link,tag_click_fn)
        elt_context = context.get('elt_context', UNDEFINED)
        use_toggle_link = context.get('use_toggle_link', UNDEFINED)
        user = context.get('user', UNDEFINED)
        def render_individual_tagging_element(user=None,tagged_item=None,elt_context=None,use_toggle_link=True,in_form=False,input_size='15',tag_click_fn='default_tag_click_fn',get_toggle_link_text_fn='default_get_toggle_link_text_fn',editable=True,render_add_tag_button=True):
            return render_render_individual_tagging_element(context._locals(__M_locals),user,tagged_item,elt_context,use_toggle_link,in_form,input_size,tag_click_fn,get_toggle_link_text_fn,editable,render_add_tag_button)
        tag_click_fn = context.get('tag_click_fn', UNDEFINED)
        input_size = context.get('input_size', UNDEFINED)
        tagged_item = context.get('tagged_item', UNDEFINED)
        tag_type = context.get('tag_type', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n\n')
        if tagged_item is not None:
            if tag_type == "individual":
                __M_writer(u'        ')
                __M_writer(unicode(render_individual_tagging_element( user=user, tagged_item=tagged_item, elt_context=elt_context, in_form=in_form, input_size=input_size, tag_click_fn=tag_click_fn, use_toggle_link=use_toggle_link )))
                __M_writer(u'\n')
            elif tag_type == "community":
                __M_writer(u'        ')
                __M_writer(unicode(render_community_tagging_element(tagged_item=tagged_item, elt_context=elt_context, tag_click_fn=tag_click_fn)))
                __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n\n')
        __M_writer(u'\n\n\n')
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_tagging_element_html(context,elt_id=None,tags=None,editable=True,use_toggle_link=True,input_size='15',in_form=False,tag_type='individual',render_add_tag_button=True):
    __M_caller = context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        unicode = context.get('unicode', UNDEFINED)
        isinstance = context.get('isinstance', UNDEFINED)
        len = context.get('len', UNDEFINED)
        str = context.get('str', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'    ')

        num_tags = len( tags )
            
        
        __M_writer(u'\n    <div class="tag-element"\n')
        if elt_id:
            __M_writer(u'            id="')
            __M_writer(unicode(elt_id))
            __M_writer(u'"\n')
        if num_tags == 0 and not editable:
            __M_writer(u'            style="display: none"\n')
        __M_writer(u'    >\n')
        if use_toggle_link:
            __M_writer(u'            <a class="toggle-link" href="#">')
            __M_writer(unicode(num_tags))
            __M_writer(u' Tag')
            __M_writer(unicode(iff( num_tags == 1, "", "s")))
            __M_writer(u'</a>\n')
        __M_writer(u'        <div class="tag-area\n')
        if tag_type == 'individual':
            __M_writer(u'                individual-tag-area\n')
        __M_writer(u'        ">\n\n')
        for tag in tags:
            __M_writer(u'                ')

                    ## Handle both Tag and ItemTagAssociation objects.
            if isinstance( tag, Tag ):
                tag_name = tag.name
                tag_value = None
            elif isinstance( tag, ItemTagAssociation ):
                tag_name = tag.user_tname
                tag_value = tag.user_value
            
            ## Convert tag name, value to unicode.
            if isinstance( tag_name, str ):
                tag_name = unicode( escape( tag_name ), 'utf-8' )
                if tag_value:
                    tag_value = unicode( escape( tag_value ), 'utf-8' )
            if tag_value:
                tag_str = tag_name + ":" + tag_value
            else:
                tag_str = tag_name
                            
            
            __M_writer(u'\n                <span class="tag-button">\n                    <span class="tag-name">')
            __M_writer(filters.html_escape(unicode(tag_str )))
            __M_writer(u'</span>\n')
            if editable:
                __M_writer(u'                        <img class="delete-tag-img" src="')
                __M_writer(unicode(h.url_for('/static/images/delete_tag_icon_gray.png')))
                __M_writer(u'"/>\n')
            __M_writer(u'                </span>\n')
        __M_writer(u'\n')
        if editable:
            if in_form:
                __M_writer(u'                    <textarea class="tag-input" rows=\'1\' cols=\'')
                __M_writer(unicode(input_size))
                __M_writer(u"'></textarea>\n")
            else:
                __M_writer(u'                    <input class="tag-input" type=\'text\' size=\'')
                __M_writer(unicode(input_size))
                __M_writer(u"'/>\n")
            if render_add_tag_button:
                __M_writer(u"                    <img src='")
                __M_writer(unicode(h.url_for('/static/images/fugue/tag--plus.png')))
                __M_writer(u'\' class="add-tag-button" title="Add tags"/>\n')
        __M_writer(u'        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_community_tag_js(context,controller_name):
    __M_caller = context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        item = context.get('item', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'<script type="text/javascript">\n    // Handle click on community tag.\n    function community_tag_click(tag_name, tag_value) {\n        var href = \'')
        __M_writer(unicode(h.url_for ( controller='/' + controller_name , action='list_published')))
        __M_writer(u'\';\n        href = href + "?f-tags=" + tag_name;\n        if (tag_value != undefined && tag_value != "") {\n            href = href + ":" + tag_value;\n        }\n        self.location = href;\n    }\n\n    // Map item rating to number of stars to show.\n    function map_rating_to_num_stars(rating) {\n        if (rating <= 0)\n            return 0;\n        else if (rating > 0 && rating <= 1.5)\n            return 1;\n        else if (rating > 1.5 && rating <= 2.5)\n            return 2;\n        else if (rating > 2.5 && rating <= 3.5)\n            return 3;\n        else if (rating > 3.5 && rating <= 4.5)\n            return 4;\n        else if (rating > 4.5)\n            return 5;\n    }\n\n    // Init. on document load.\n    $(function() {\n        // Set links to Galaxy screencasts to open in overlay.\n        $(this).find("a[href^=\'http://screencast.g2.bx.psu.edu/\']").each( function() {\n            $(this).click( function() {\n                var href = $(this).attr(\'href\');\n                show_in_overlay(\n                    {\n                        url: href,\n                        width: 640,\n                        height: 480,\n                        scroll: \'no\'\n                    }\n                );\n                return false;\n            });\n        });\n\n        // Init user item rating.\n        $(\'.user_rating_star\').rating({\n            callback: function(rating, link) {\n                $.ajax({\n                    type: "GET",\n                    url: "')
        __M_writer(unicode(h.url_for ( controller='/' + controller_name , action='rate_async' )))
        __M_writer(u'",\n                    data: { id : "')
        __M_writer(unicode(trans.security.encode_id( item.id )))
        __M_writer(u'", rating : rating },\n                    dataType: \'json\',\n                    error: function() { alert( "Rating submission failed" ); },\n                    success: function( community_data ) {\n                        $(\'#rating_feedback\').show();\n                        $(\'#num_ratings\').text(Math.round(community_data[1]*10)/10);\n                        $(\'#ave_rating\').text(community_data[0]);\n                        $(\'.community_rating_star\').rating(\'readOnly\', false);\n                        $(\'.community_rating_star\').rating(\'select\', map_rating_to_num_stars(community_data[0])-1);\n                        $(\'.community_rating_star\').rating(\'readOnly\', true);\n                    }\n                });\n            },\n            required: true // Hide cancel button.\n        });\n    });\n</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_tool_tagging_elements(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        int = context.get('int', UNDEFINED)
        self = context.get('self', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')

        elt_id = int ( floor ( random()*maxint ) )
        tags = trans.app.tag_handler.get_tool_tags()
            
        
        __M_writer(u'\n    ')
        __M_writer(unicode(self.render_tagging_element_html(elt_id=elt_id, \
                                        tags=tags, \
                                        editable=False, \
                                        use_toggle_link=False )))
        __M_writer(u'\n    <script type="text/javascript">\n        init_tag_click_function($(\'#')
        __M_writer(unicode(elt_id))
        __M_writer(u"'), tool_tag_click);\n    </script>\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_individual_tagging_element(context,user=None,tagged_item=None,elt_context=None,use_toggle_link=True,in_form=False,input_size='15',tag_click_fn='default_tag_click_fn',get_toggle_link_text_fn='default_get_toggle_link_text_fn',editable=True,render_add_tag_button=True):
    __M_caller = context.caller_stack._push_frame()
    try:
        isinstance = context.get('isinstance', UNDEFINED)
        unicode = context.get('unicode', UNDEFINED)
        int = context.get('int', UNDEFINED)
        h = context.get('h', UNDEFINED)
        self = context.get('self', UNDEFINED)
        dict = context.get('dict', UNDEFINED)
        str = context.get('str', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'    ')

        # Useful ids.
        tagged_item_id = str( trans.security.encode_id ( tagged_item.id ) )
        elt_id = int ( floor ( random()*maxint ) )
        
        # Get list of user's item tags. TODO: implement owner_tags for all taggable objects and use here.
        item_tags = [ tag for tag in tagged_item.tags if ( tag.user == user ) ]
            
        
        __M_writer(u'\n\n')
        __M_writer(u'    ')
        __M_writer(unicode(self.render_tagging_element_html(elt_id=elt_id, tags=item_tags, editable=editable, use_toggle_link=use_toggle_link, input_size=input_size, in_form=in_form, render_add_tag_button=render_add_tag_button)))
        __M_writer(u'\n\n')
        __M_writer(u'    <script type="text/javascript">\n        //\n        // Set up autocomplete tagger.\n        //\n\n        //\n        // Default function get text to display on the toggle link.\n        //\n        var default_get_toggle_link_text_fn = function(tags)\n        {\n            var text = "";\n            var num_tags = _.size(tags);\n            if (num_tags != 0)\n              {\n                text = num_tags + (num_tags != 1 ? " Tags" : " Tag");\n                /*\n                // Show first N tags; hide the rest.\n                var max_to_show = 1;\n\n                // Build tag string.\n                var tag_strs = new Array();\n                var count = 0;\n                for (tag_name in tags)\n                  {\n                    tag_value = tags[tag_name];\n                    tag_strs[tag_strs.length] = build_tag_str(tag_name, tag_value);\n                    if (++count == max_to_show)\n                      break;\n                  }\n                tag_str = tag_strs.join(", ");\n\n                // Finalize text.\n                var num_tags_hiding = num_tags - max_to_show;\n                text = "Tags: " + tag_str +\n                  (num_tags_hiding != 0 ? " and " + num_tags_hiding + " more" : "");\n                */\n              }\n            else\n              {\n                // No tags.\n                text = "Add tags";\n              }\n            return text;\n        };\n\n        // Default function to handle a tag click.\n        var default_tag_click_fn = function(tag_name, tag_value) { };\n\n        ')

            ## Build dict of tag name, values.
        tag_names_and_values = dict()
        for tag in item_tags:
            tag_name = escape( tag.user_tname )
            tag_value = ""
            if tag.value is not None:
                tag_value = escape( tag.user_value )
        
            ## Tag names and values may be string or unicode object.
            if isinstance( tag_name, str ):
                tag_names_and_values[unicode(tag_name, 'utf-8')] = unicode(tag_value, 'utf-8')
            else: ## isInstance( tag_name, unicode ):
                tag_names_and_values[tag_name] = tag_value
                
        
        __M_writer(u'\n        var options =\n        {\n            tags : ')
        __M_writer(unicode(h.dumps(tag_names_and_values)))
        __M_writer(u',\n            editable : ')
        __M_writer(unicode(iff( editable, 'true', 'false' )))
        __M_writer(u',\n            get_toggle_link_text_fn: ')
        __M_writer(unicode(get_toggle_link_text_fn))
        __M_writer(u',\n            tag_click_fn: ')
        __M_writer(unicode(tag_click_fn))
        __M_writer(u',\n')
        __M_writer(u'            ajax_autocomplete_tag_url: "')
        __M_writer(unicode(h.url_for( controller='/tag', action='tag_autocomplete_data', item_id=tagged_item_id, item_class=tagged_item.__class__.__name__ )))
        __M_writer(u'",\n            ajax_add_tag_url: "')
        __M_writer(unicode(h.url_for( controller='/tag', action='add_tag_async', item_id=tagged_item_id, item_class=tagged_item.__class__.__name__, context=elt_context )))
        __M_writer(u'",\n            ajax_delete_tag_url: "')
        __M_writer(unicode(h.url_for( controller='/tag', action='remove_tag_async', item_id=tagged_item_id, item_class=tagged_item.__class__.__name__, context=elt_context )))
        __M_writer(u'",\n            delete_tag_img: "')
        __M_writer(unicode(h.url_for('/static/images/delete_tag_icon_gray.png')))
        __M_writer(u'",\n            delete_tag_img_rollover: "')
        __M_writer(unicode(h.url_for('/static/images/delete_tag_icon_white.png')))
        __M_writer(u'",\n            use_toggle_link: ')
        __M_writer(unicode(iff( use_toggle_link, 'true', 'false' )))
        __M_writer(u"\n         };\n\n        $('#")
        __M_writer(unicode(elt_id))
        __M_writer(u"').autocomplete_tagging(options);\n    </script>\n\n")
        __M_writer(u'    <style>\n    .tag-area {\n        display: ')
        __M_writer(unicode(iff( use_toggle_link, "none", "block" )))
        __M_writer(u';\n    }\n    </style>\n\n    <noscript>\n    <style>\n    .tag-area {\n        display: block;\n    }\n    </style>\n    </noscript>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_community_tagging_element(context,tagged_item=None,elt_context=None,use_toggle_link=False,tag_click_fn='default_tag_click_fn'):
    __M_caller = context.caller_stack._push_frame()
    try:
        int = context.get('int', UNDEFINED)
        self = context.get('self', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'    ')

        elt_id = int ( floor ( random()*maxint ) )
        community_tags = trans.app.tag_handler.get_community_tags( item=tagged_item, limit=5 )
            
        
        __M_writer(u'\n    ')
        __M_writer(unicode(self.render_tagging_element_html(elt_id=elt_id, \
                                        tags=community_tags, \
                                        use_toggle_link=use_toggle_link, \
                                        editable=False, tag_type="community")))
        __M_writer(u'\n\n')
        __M_writer(u'    <script type="text/javascript">\n        init_tag_click_function($(\'#')
        __M_writer(unicode(elt_id))
        __M_writer(u"'), ")
        __M_writer(unicode(tag_click_fn))
        __M_writer(u');\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"16": 1, "25": 0, "42": 8, "43": 11, "44": 12, "45": 13, "46": 13, "47": 13, "48": 14, "49": 15, "50": 15, "51": 15, "52": 18, "53": 86, "54": 101, "55": 119, "56": 233, "57": 307, "63": 20, "72": 20, "73": 22, "74": 22, "78": 24, "79": 26, "80": 27, "81": 27, "82": 27, "83": 30, "84": 31, "85": 33, "86": 34, "87": 35, "88": 35, "89": 35, "90": 35, "91": 35, "92": 37, "93": 38, "94": 39, "95": 41, "96": 44, "97": 45, "98": 45, "118": 63, "119": 65, "120": 65, "121": 66, "122": 67, "123": 67, "124": 67, "125": 69, "126": 71, "127": 73, "128": 74, "129": 75, "130": 75, "131": 75, "132": 76, "133": 77, "134": 77, "135": 77, "136": 80, "137": 81, "138": 81, "139": 81, "140": 84, "146": 236, "153": 236, "154": 239, "155": 242, "156": 242, "157": 289, "158": 289, "159": 290, "160": 290, "166": 89, "173": 89, "174": 90, "179": 93, "180": 94, "184": 97, "185": 99, "186": 99, "192": 123, "204": 123, "205": 125, "206": 125, "215": 132, "216": 135, "217": 135, "218": 135, "219": 138, "220": 186, "236": 200, "237": 203, "238": 203, "239": 204, "240": 204, "241": 205, "242": 205, "243": 206, "244": 206, "245": 208, "246": 208, "247": 208, "248": 209, "249": 209, "250": 210, "251": 210, "252": 211, "253": 211, "254": 212, "255": 212, "256": 213, "257": 213, "258": 216, "259": 216, "260": 220, "261": 222, "262": 222, "268": 104, "275": 104, "276": 106, "277": 106, "282": 109, "283": 110, "287": 113, "288": 116, "289": 117, "290": 117, "291": 117, "292": 117, "298": 292}, "uri": "/tagging_common.mako", "filename": "templates/tagging_common.mako"}
__M_END_METADATA
"""
