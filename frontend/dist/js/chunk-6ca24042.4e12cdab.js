(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-6ca24042"],{"0bb4":function(t,n,e){"use strict";e.d(n,"f",function(){return r}),e.d(n,"e",function(){return u}),e.d(n,"g",function(){return a}),e.d(n,"a",function(){return i}),e.d(n,"b",function(){return s}),e.d(n,"d",function(){return d}),e.d(n,"c",function(){return f});var c=e("365c"),o=e("b775");function r(t){return Object(o["b"])({url:c["a"].system_notice,method:"get",params:t})}function u(t){return Object(o["b"])({url:c["a"].system_notice+"".concat(t,"/"),method:"get"})}function a(t,n){return Object(o["b"])({url:c["a"].system_notice+"".concat(t,"/"),method:"put",data:n})}function i(t){return Object(o["b"])({url:c["a"].system_notice,method:"post",data:t})}function s(t){return Object(o["b"])({url:c["a"].system_notice+"".concat(t,"/"),method:"delete"})}function d(t){return Object(o["b"])({url:c["a"].notice,method:"get",params:t})}function f(t){return Object(o["b"])({url:c["a"].notice+"".concat(t,"/"),method:"get"})}},"403b":function(t,n,e){"use strict";e.r(n);var c=function(){var t=this,n=t.$createElement,e=t._self._c||n;return e("a-spin",{attrs:{spinning:t.loading}},[e("a-back-top"),e("a-card",[e("div",{domProps:{innerHTML:t._s(t.data.content)}})])],1)},o=[],r=e("0bb4"),u={loading:!1,mounted:function(){var t=this.$route.params&&this.$route.params.id;this.fetch(t)},data:function(){return{data:{content:""},loading:!1}},methods:{fetch:function(t){var n=this;this.loading=!0,Object(r["c"])(t).then(function(t){n.data=t.result}).finally(function(){n.loading=!1})}}},a=u,i=e("2877"),s=Object(i["a"])(a,c,o,!1,null,null,null);n["default"]=s.exports}}]);