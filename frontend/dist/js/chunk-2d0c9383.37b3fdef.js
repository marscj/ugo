(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-2d0c9383"],{"57e0":function(t,e,o){"use strict";o.r(e);var n=function(){var t=this,e=t.$createElement,o=t._self._c||e;return o("a-spin",{attrs:{spinning:t.loading}},[t.form?o("a-card",[o("template",{slot:"title"},[o("icon-font",{attrs:{type:t.Category[t.form.category].type}}),t._v("\n      "+t._s(t.Category[t.form.category].label)+"\n    ")],1),1==t.form.category?o("restaurant",{ref:"form",attrs:{isEdit:!0},on:{onTitle:t.onTitle,update:t.update}}):t._e(),2==t.form.category?o("tour",{ref:"form",attrs:{isEdit:!0},on:{onTitle:t.onTitle,update:t.update}}):t._e(),3==t.form.category?o("transport",{ref:"form",attrs:{isEdit:!0},on:{onTitle:t.onTitle,update:t.update}}):t._e(),4==t.form.category?o("hotel",{ref:"form",attrs:{isEdit:!0},on:{onTitle:t.onTitle,update:t.update}}):t._e()],2):t._e()],1)},a=[],r=o("2b1b"),i=o("b02a"),l=o("4d3c"),c=o("af3a"),f=o("518f"),u=o("0c63"),s=u["a"].createFromIconfontCN({scriptUrl:"//at.alicdn.com/t/font_1402881_gsh78a0lnya.js"}),d=[{value:0,label:"All",type:"iconf-30"},{value:1,label:"Restaurant",type:"iconf-30"},{value:2,label:"Tour",type:"iconticket"},{value:3,label:"Transport",type:"iconche"},{value:4,label:"Hotel",type:"iconhotel"}],p={name:"BookingCreate",components:{IconFont:s,Hotel:i["a"],Tour:l["a"],Restaurant:c["a"],Transport:f["a"]},mounted:function(){this.fetch(this.$route.params.id)},data:function(){return{Category:d,form:null,loading:!1}},methods:{onTitle:function(t){this.$route.meta.title=t.bookingID,this.$parent.getPageMeta()},fetch:function(t){var e=this;this.loading=!0,Object(r["b"])(t).then(function(t){var o=t.result;e.form=o,e.onTitle(e.form),e.$nextTick(function(){e.$refs.form.onFetch(e.form)})}).finally(function(){e.loading=!1})},update:function(t){var e=this;this.loading=!0,Object(r["d"])(t.id,t).then(function(t){t.result;e.$nextTick(function(){e.$refs.form.onUpdate(e.form)})}).finally(function(){e.loading=!1})}}},m=p,g=o("2877"),h=Object(g["a"])(m,n,a,!1,null,null,null);e["default"]=h.exports}}]);