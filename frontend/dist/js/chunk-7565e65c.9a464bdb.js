(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-7565e65c","chunk-31d7ed90"],{"149c":function(t,e,a){"use strict";var n=a("7001"),i=a.n(n);i.a},"2bec":function(t,e,a){"use strict";a.r(e);var n=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("list-view",{attrs:{loading:t.loading,data:t.data,align:"center"},on:{onClick:t.onClick,onSearch:t.onSearch}})},i=[],r=a("9847"),s=a("c78b"),c=a("c4c8"),o={components:{ListView:r["a"],PageView:s["default"]},data:function(){return{data:[],loading:!1,description:" ",extraImage:a("76d3")}},mounted:function(){this.fetch(null)},methods:{fetch:function(t){var e=this;this.loading=!0,Object(c["c"])({category:1,search:t,sorter:"-id"}).then(function(t){var a=t.result;e.data=a}).finally(function(){e.loading=!1})},onClick:function(t){this.$router.push({name:"FoodDetail",params:{id:t.id}})},onSearch:function(t){this.fetch(t)}}},l=o,u=a("2877"),d=Object(u["a"])(l,n,i,!1,null,null,null);e["default"]=d.exports},7001:function(t,e,a){},"76d3":function(t,e,a){t.exports=a.p+"assets/food.c4beca73.svg"},9847:function(t,e,a){"use strict";var n=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",[a("div",{staticStyle:{"margin-bottom":"25px"}},[a("div",{staticClass:"page-menu-search"},[a("a-input-search",{staticStyle:{width:"80%","max-width":"522px"},attrs:{placeholder:"请输入...",size:"large",enterButton:"搜索"},on:{search:t.handleSearch}})],1)]),a("a-list",{attrs:{grid:{gutter:24,lg:3,md:3,sm:2,xs:1},dataSource:t.data,loading:t.loading},scopedSlots:t._u([{key:"renderItem",fn:function(e){return a("a-list-item",{staticStyle:{"margin-bottom":"20px"},on:{click:function(a){return t.handleClick(e)}}},[[a("a-card",{staticStyle:{width:"100%"},attrs:{hoverable:!0,bordered:!1}},[e.photo?a("img",{attrs:{slot:"cover",alt:e.name,src:e.photo.image.large_square_crop},slot:"cover"}):t._e(),a("a-divider"),a("a-card-meta",{attrs:{title:e.title}},[a("div",{staticStyle:{"margin-bottom":"5px",height:"45px"},attrs:{slot:"description"},slot:"description"},[t._v(t._s(e.subtitle))])])],1)]],2)}}])})],1)},i=[],r={props:{loading:{type:Boolean,default:!1},data:{type:Array,default:!1}},methods:{handleClick:function(t){this.$emit("onClick",t)},handleSearch:function(t){this.$emit("onSearch",t)}}},s=r,c=a("2877"),o=Object(c["a"])(s,n,i,!1,null,null,null);e["a"]=o.exports},c4c8:function(t,e,a){"use strict";a.d(e,"e",function(){return r}),a.d(e,"d",function(){return s}),a.d(e,"f",function(){return c}),a.d(e,"a",function(){return o}),a.d(e,"c",function(){return l}),a.d(e,"b",function(){return u});var n=a("365c"),i=a("b775");function r(t){return Object(i["b"])({url:n["a"].system_product,method:"get",params:t})}function s(t){return Object(i["b"])({url:n["a"].system_product+"".concat(t,"/"),method:"get"})}function c(t,e){return Object(i["b"])({url:n["a"].system_product+"".concat(t,"/"),method:"put",data:e})}function o(t){return Object(i["b"])({url:n["a"].system_product,method:"post",data:t})}function l(t){return Object(i["b"])({url:n["a"].product,method:"get",params:t})}function u(t){return Object(i["b"])({url:n["a"].product+"".concat(t,"/"),method:"get"})}},c78b:function(t,e,a){"use strict";a.r(e);var n=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{style:t.$route.meta.hiddenHeaderContent?null:"margin: -24px -24px 0px;"},[t.$route.meta.hiddenHeaderContent?t._e():a("page-header",{attrs:{title:t.pageTitle,logo:t.logo,avatar:t.avatar}},[t._t("action",null,{slot:"action"}),t._t("headerContent",null,{slot:"content"}),!this.$slots.headerContent&&t.description?a("div",{attrs:{slot:"content"},slot:"content"},[a("p",{staticStyle:{"font-size":"14px",color:"rgba(0,0,0,.65)"}},[t._v(t._s(t.description))]),a("div",{staticClass:"link"},[t._l(t.linkList,function(e,n){return[a("a",{key:n,attrs:{href:e.href}},[a("a-icon",{attrs:{type:e.icon}}),a("span",[t._v(t._s(e.title))])],1)]})],2)]):t._e(),t._t("extra",[a("div",{staticClass:"extra-img"},["undefined"!==typeof t.extraImage?a("img",{attrs:{src:t.extraImage}}):t._e()])],{slot:"extra"}),a("div",{attrs:{slot:"pageMenu"},slot:"pageMenu"},[t.search?a("div",{staticClass:"page-menu-search"},[a("a-input-search",{staticStyle:{width:"80%","max-width":"522px"},attrs:{placeholder:"请输入...",size:"large",enterButton:"搜索"}})],1):t._e(),t.tabs&&t.tabs.items?a("div",{staticClass:"page-menu-tabs"},[a("a-tabs",{attrs:{tabBarStyle:{margin:0},activeKey:t.tabs.active()},on:{change:t.tabs.callback}},t._l(t.tabs.items,function(t){return a("a-tab-pane",{key:t.key,attrs:{tab:t.title}})}),1)],1):t._e()])],2),a("div",{staticClass:"content"},[a("div",{staticClass:"page-header-index-wide"},[t._t("default",[t.multiTab?a("keep-alive",[a("router-view",{ref:"content"})],1):a("router-view",{ref:"content"})])],2)])],1)},i=[],r=(a("386d"),a("cebc")),s=a("2f62"),c=a("2c82"),o={name:"PageView",components:{PageHeader:c["a"]},props:{avatar:{type:String,default:null},title:{type:[String,Boolean],default:!0},logo:{type:String,default:null},directTabs:{type:Object,default:null}},data:function(){return{pageTitle:null,description:null,linkList:[],extraImage:void 0,search:!1,tabs:{}}},computed:Object(r["a"])({},Object(s["d"])({multiTab:function(t){return t.app.multiTab}})),mounted:function(){this.tabs=this.directTabs,this.getPageMeta()},updated:function(){this.getPageMeta()},methods:{getPageMeta:function(){this.pageTitle="string"!==typeof this.title&&this.title?this.$route.meta.title:this.title;var t=this.$refs.content;t&&(t.pageMeta?Object.assign(this,t.pageMeta):(this.description=t.description,this.linkList=t.linkList,this.extraImage=t.extraImage,this.search=!0===t.search,this.tabs=t.tabs))}}},l=o,u=(a("149c"),a("2877")),d=Object(u["a"])(l,n,i,!1,null,"a084ab12",null);e["default"]=d.exports}}]);