define(["mvc/history/history-view","mvc/history/hda-li","mvc/history/hdca-li","mvc/base-mvc","utils/localization"],function(a,b,c,d,e){"use strict";var f=a.HistoryView,g=f.extend({className:f.prototype.className+" annotated-history-panel",_buildNewRender:function(){var a=f.prototype._buildNewRender.call(this);return this.renderHistoryAnnotation(a),a},renderHistoryAnnotation:function(a){var b=this.model.get("annotation");b&&a.find(".controls .annotation-display").text(b)},renderItems:function(a){a=a||this.$el,a.find(".list-items").replaceWith($("<table/>").addClass("list-items"));var b=f.prototype.renderItems.call(this,a);return this.$list(a).prepend($("<tr/>").addClass("headers").append([$("<th/>").text(e("Dataset")),$("<th/>").text(e("Annotation"))])),b},_attachItems:function(a){return this.$list(a).append(this.views.map(function(a){var b=_.find(a.el.classList,function(a){return/^state\-/.test(a)}),c=a.model.get("annotation")||"",d=$("<tr/>").append([$("<td/>").addClass("contents-container").append(a.$el).addClass(b?b.replace("-","-color-"):""),$("<td/>").addClass("additional-info").text(c)]);return d})),this},events:_.extend(_.clone(f.prototype.events),{"click tr":function(a){$(a.currentTarget).find(".title-bar").click()},"click .icon-btn":function(a){a.stopPropagation();var b=$(a.currentTarget);b.length&&"dropdown"===b.attr("data-toggle")&&b.dropdown("toggle")}}),toString:function(){return"AnnotatedHistoryView("+(this.model?this.model.get("name"):"")+")"}});return{AnnotatedHistoryView:g}});
//# sourceMappingURL=../../../maps/mvc/history/history-view-annotated.js.map