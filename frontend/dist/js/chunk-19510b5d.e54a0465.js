(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-19510b5d"],{"0bb4":function(t,n,e){"use strict";e.d(n,"e",function(){return a}),e.d(n,"d",function(){return o}),e.d(n,"f",function(){return c}),e.d(n,"a",function(){return s}),e.d(n,"c",function(){return l}),e.d(n,"b",function(){return u});var i=e("365c"),r=e("b775");function a(t){return Object(r["b"])({url:i["a"].system_notice,method:"get",params:t})}function o(t){return Object(r["b"])({url:i["a"].system_notice+"".concat(t,"/"),method:"get"})}function c(t,n){return Object(r["b"])({url:i["a"].system_notice+"".concat(t,"/"),method:"put",data:n})}function s(t){return Object(r["b"])({url:i["a"].system_notice,method:"post",data:t})}function l(t){return Object(r["b"])({url:i["a"].notice,method:"get",params:t})}function u(t){return Object(r["b"])({url:i["a"].notice+"".concat(t,"/"),method:"get"})}},a0ab:function(t,n,e){"use strict";e.r(n);var i=function(){var t=this,n=t.$createElement,e=t._self._c||n;return e("detail",{attrs:{"is-edit":!0},on:{title:t.onTitle}})},r=[],a=e("a8ea"),o={name:"CreateForm",components:{Detail:a["a"]},data:function(){return{description:"编辑公告"}},methods:{onTitle:function(t){this.description=t.variant,this.pageTitle=t.product,this.$parent.getPageMeta()}}},c=o,s=e("2877"),l=Object(s["a"])(c,i,r,!1,null,null,null);n["default"]=l.exports},a8ea:function(t,n,e){"use strict";var i=function(){var t=this,n=t.$createElement,e=t._self._c||n;return e("a-spin",{attrs:{spinning:t.spinning}},[e("a-card",[e("a-form",{attrs:{form:t.form}},[e("a-form-item",{attrs:{label:"Title",required:!0,"validate-status":null==t.help.title||""===t.help.title?null:"error",help:t.help.title}},[e("a-input",{model:{value:t.form.title,callback:function(n){t.$set(t.form,"title",n)},expression:"form.title"}})],1),e("a-form-item",{attrs:{label:"SubTitle",required:!0,"validate-status":null==t.help.subtitle||""===t.help.subtitle?null:"error",help:t.help.subtitle}},[e("a-textarea",{attrs:{rows:5},model:{value:t.form.subtitle,callback:function(n){t.$set(t.form,"subtitle",n)},expression:"form.subtitle"}})],1),e("a-form-item",{attrs:{label:"Content",required:!0,"validate-status":null==t.help.content||""===t.help.content?null:"error",help:t.help.content}},[e("div",{staticClass:"components-container"},[e("div",[e("tinymce",{attrs:{height:500},model:{value:t.form.content,callback:function(n){t.$set(t.form,"content",n)},expression:"form.content"}})],1)])])],1),e("a-row",[e("a-col",{attrs:{span:"2"}},[e("a-button",{attrs:{type:"primary","html-type":"submit"},on:{click:t.handleSubmit}},[t._v("Submit")])],1),e("a-col",{attrs:{span:"2"}},[e("a-button",{on:{click:t.handleGoBack}},[t._v("Return")])],1)],1)],1)],1)},r=[],a=e("8256"),o=e("f3b8"),c=e("0bb4"),s={name:"EditDetail",components:{Tinymce:a["a"]},props:{isEdit:{type:Boolean,default:!1}},data:function(){return{form:{title:"",subtitle:"",content:""},help:{},spinning:!1}},created:function(){if(this.isEdit){var t=this.$route.params&&this.$route.params.id;this.fetch(t)}},methods:{handleGoBack:function(){this.$router.go(-1)},fetch:function(t){var n=this;this.spinning=!0,Object(c["d"])(t).then(function(t){var e=t.result;n.form=e,n.initData(e)}).finally(function(){n.spinning=!1})},updateForm:function(t){var n=this;this.spinning=!0,Object(c["f"])(this.$route.params.id,t).then(function(t){t.result;n.handleGoBack()}).catch(function(t){n.checkError(t)}).finally(function(){n.spinning=!1})},createForm:function(t){var n=this;this.spinning=!0,Object(c["a"])(t).then(function(t){t.result;n.handleGoBack()}).catch(function(t){n.checkError(t)}).finally(function(){n.spinning=!1})},checkError:function(t){var n=Object(o["a"])(t,"title","subtitle","content");for(var e in this.help={title:n["title"],subtitle:n["subtitle"],content:n["content"]},n)n[e]&&this.$notification["error"]({message:e,description:n[e],duration:4})},initData:function(t){this.isEdit&&this.$emit("title",t)},handleSubmit:function(){console.log(this.form,"======="),this.isEdit?this.updateForm(this.form):this.createForm(this.form)}}},l=s,u=e("2877"),f=Object(u["a"])(l,i,r,!1,null,null,null);n["a"]=f.exports}}]);