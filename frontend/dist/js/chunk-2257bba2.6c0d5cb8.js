(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-2257bba2"],{"419a":function(t,e,a){"use strict";a.r(e);var r=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("detail",{attrs:{"is-edit":!0},on:{title:t.onTitle}})},n=[],i=a("daae"),l={name:"CreateForm",components:{Detail:i["a"]},data:function(){return{description:"编辑子产品"}},methods:{onTitle:function(){this.$parent.getPageMeta()}}},u=l,c=a("2877"),o=Object(c["a"])(u,r,n,!1,null,null,null);e["default"]=o.exports},"7aa0":function(t,e,a){"use strict";a.d(e,"d",function(){return i}),a.d(e,"c",function(){return l}),a.d(e,"g",function(){return u}),a.d(e,"a",function(){return c}),a.d(e,"b",function(){return o}),a.d(e,"e",function(){return d}),a.d(e,"f",function(){return s});var r=a("365c"),n=a("b775");function i(t){return Object(n["b"])({url:r["a"].variant,method:"get",params:t})}function l(t){return Object(n["b"])({url:r["a"].variant+"".concat(t,"/"),method:"get"})}function u(t,e){return Object(n["b"])({url:r["a"].variant+"".concat(t,"/"),method:"put",data:e})}function c(t){return Object(n["b"])({url:r["a"].variant,method:"post",data:t})}function o(t){return Object(n["b"])({url:r["a"].variant+"".concat(t,"/"),method:"delete"})}function d(t){return Object(n["b"])({url:r["a"].variant+"delete/",method:"delete",params:t})}function s(t){return Object(n["b"])({url:r["a"].variant+"enable/",method:"post",params:t})}},c4c8:function(t,e,a){"use strict";a.d(e,"d",function(){return i}),a.d(e,"c",function(){return l}),a.d(e,"g",function(){return u}),a.d(e,"a",function(){return c}),a.d(e,"b",function(){return o}),a.d(e,"e",function(){return d}),a.d(e,"f",function(){return s});var r=a("365c"),n=a("b775");function i(t){return Object(n["b"])({url:r["a"].product,method:"get",params:t})}function l(t){return Object(n["b"])({url:r["a"].product+"".concat(t,"/"),method:"get"})}function u(t,e){return Object(n["b"])({url:r["a"].product+"".concat(t,"/"),method:"put",data:e})}function c(t){return Object(n["b"])({url:r["a"].product,method:"post",data:t})}function o(t){return Object(n["b"])({url:r["a"].product+"".concat(t,"/"),method:"delete"})}function d(t){return Object(n["b"])({url:r["a"].product+"delete/",method:"delete",params:t})}function s(t){return Object(n["b"])({url:r["a"].product+"enable/",method:"post",params:t})}},daae:function(t,e,a){"use strict";var r=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("a-spin",{attrs:{spinning:t.spinning}},[a("a-card",{attrs:{title:"Base"}},[a("a-form",{attrs:{form:t.form}},[a("a-form-item",{attrs:{label:"Status",required:!0}},[a("a-switch",{attrs:{checkedChildren:"上架",unCheckedChildren:"下架",checked:t.form.status,disabled:""}})],1),a("a-form-item",{attrs:{label:"Product(主产品)",required:!0,"validate-status":null==t.help.product_id||""===t.help.product_id?null:"error",help:t.help.product_id}},[a("a-select",{attrs:{showSearch:"",value:t.form.product_id,placeholder:"Product name",defaultActiveFirstOption:!1,showArrow:!1,filterOption:!1,notFoundContent:"没有找到"},on:{search:t.handleProductSearch,change:t.handleProductChange}},t._l(t.productOption,function(e){return a("a-select-option",{key:e.id},[t._v(t._s(e.title))])}),1)],1),a("a-form-item",{attrs:{label:"Name",required:!0,"validate-status":null==t.help.name||""===t.help.name?null:"error",help:t.help.name}},[a("a-input",{model:{value:t.form.name,callback:function(e){t.$set(t.form,"name",e)},expression:"form.name"}})],1),a("a-form-item",{attrs:{label:"VariantID",required:!0,"validate-status":null==t.help.variantID||""===t.help.variantID?null:"error",help:t.help.variantID}},[a("a-input",{model:{value:t.form.variantID,callback:function(e){t.$set(t.form,"variantID",e)},expression:"form.variantID"}})],1),a("a-form-item",{attrs:{label:"SKU",required:!0,"validate-status":null==t.help.sku||""===t.help.sku?null:"error",help:t.help.sku}},[a("a-input",{model:{value:t.form.sku,callback:function(e){t.$set(t.form,"sku",e)},expression:"form.sku"}})],1),a("a-form-item",{attrs:{label:"Sort ID","validate-status":null==t.help.sort_by||""===t.help.sort_by?null:"error",help:t.help.sort_by}},[a("a-input",{model:{value:t.form.sort_by,callback:function(e){t.$set(t.form,"sort_by",e)},expression:"form.sort_by"}})],1),a("a-form-item",{attrs:{label:"Adult Status(成人票)",required:!0}},[a("a-switch",{attrs:{checkedChildren:"上架",unCheckedChildren:"下架",checked:t.form.adult_status},on:{change:t.handleAdultChange}})],1),t.form.adult_status?a("a-form-item",{attrs:{label:"Adult Desc( 成人票说明 例如: 12周岁（含）以上 )","validate-status":null==t.help.adult_desc||""===t.help.adult_desc?null:"error",help:t.help.adult_desc}},[a("a-input",{model:{value:t.form.adult_desc,callback:function(e){t.$set(t.form,"adult_desc",e)},expression:"form.adult_desc"}})],1):t._e(),t.form.adult_status?a("a-form-item",{attrs:{label:"Adult Price",required:!0,"validate-status":null==t.help.adult_price||""===t.help.adult_price?null:"error",help:t.help.adult_price}},[a("div",t._l(t.form.adult_price,function(e,r){return a("div",{key:r,staticStyle:{display:"inline-block","padding-left":"6px","padding-right":"6px"}},[a("div",[a("span",[t._v(t._s("Level "+(r+1)))])]),a("a-input-number",{staticStyle:{width:"200px"},attrs:{placeholder:"Input Level "+(r+1)+" price",min:0,defaultValue:0,precision:2,step:.5},model:{value:t.form.adult_price[r],callback:function(e){t.$set(t.form.adult_price,r,e)},expression:"form.adult_price[index]"}})],1)}),0)]):t._e(),a("a-form-item",{attrs:{label:"Child Status(儿童票)",required:!0}},[a("a-switch",{attrs:{checkedChildren:"上架",unCheckedChildren:"下架",checked:t.form.child_status},on:{change:t.handleChildChange}})],1),t.form.child_status?a("a-form-item",{attrs:{label:"Child Desc( 儿童票说明 例如: 4周岁（含）-11周岁（含）)","validate-status":null==t.help.child_desc||""===t.help.child_desc?null:"error",help:t.help.child_desc}},[a("a-input",{model:{value:t.form.child_desc,callback:function(e){t.$set(t.form,"child_desc",e)},expression:"form.child_desc"}})],1):t._e(),t.form.child_status?a("a-form-item",{attrs:{label:"Child Price",required:!0,"validate-status":null==t.help.child_price||""===t.help.child_price?null:"error",help:t.help.child_price}},[a("div",t._l(t.form.child_price,function(e,r){return a("div",{key:r,staticStyle:{display:"inline-block","padding-right":"8px"}},[a("div",[a("span",[t._v(t._s("Level "+(r+1)))])]),a("a-input-number",{staticStyle:{width:"200px"},attrs:{placeholder:"Input Level "+(r+1)+" price",min:0,defaultValue:0,precision:2,step:.5},model:{value:t.form.child_price[r],callback:function(e){t.$set(t.form.child_price,r,e)},expression:"form.child_price[index]"}})],1)}),0)]):t._e()],1)],1),a("a-row",{staticStyle:{"margin-top":"20px"}},[a("a-col",{attrs:{span:"2"}},[a("a-button",{attrs:{type:"primary","html-type":"submit"},on:{click:t.handleSubmit}},[t._v("Submit")])],1),a("a-col",{attrs:{span:"2"}},[a("a-button",{on:{click:t.handleGoBack}},[t._v("Return")])],1)],1)],1)},n=[],i=(a("7f7f"),a("f3b8")),l=a("7aa0"),u=a("c4c8"),c={name:"ProductDetail",props:{isEdit:{type:Boolean,default:!1}},data:function(){var t=this;return{form:{status:!1,product_id:void 0,adult_status:!1,adult_desc:void 0,adult_quantity:void 0,adult_price:[100,100,100,100,100],child_status:!1,child_desc:void 0,child_quantity:void 0,child_price:[100,100,100,100,100]},price:[],help:{},productOption:[],spinning:!1,columns:[{title:"Lev1",dataIndex:function(){return t.form.child_price[0]}},{title:"Lev2",dataIndex:function(){return t.form.child_price[1]}},{title:"Lev3",dataIndex:function(){return t.form.child_price[2]}},{title:"Lev4",dataIndex:function(){return t.form.child_price[3]}},{title:"Lev5",dataIndex:function(){return t.form.child_price[4]}}]}},created:function(){if(this.handleProductSearch(null),this.isEdit){var t=this.$route.params&&this.$route.params.id;this.fetch(t)}},methods:{handleGoBack:function(){this.$router.go(-1)},fetch:function(t){var e=this;this.spinning=!0,Object(l["c"])(t).then(function(t){var a=t.result;e.form=a,e.product=a.product.id}).finally(function(){e.spinning=!1})},updateForm:function(t){var e=this;this.spinning=!0,Object(l["g"])(this.$route.params.id,t).then(function(t){t.result;e.handleGoBack()}).catch(function(t){e.checkError(t)}).finally(function(){e.spinning=!1})},createForm:function(t){var e=this;this.spinning=!0,Object(l["a"])(t).then(function(t){t.result;e.handleGoBack()}).catch(function(t){e.checkError(t)}).finally(function(){e.spinning=!1})},handleProductSearch:function(t){var e=this;Object(u["d"])({search:t}).then(function(t){var a=t.result;e.productOption=a})},handleProductChange:function(t){this.form.product_id=t},handleAdultChange:function(t){this.form.adult_status=t,this.handleStatusChange()},handleChildChange:function(t){this.form.child_status=t,this.handleStatusChange()},checkError:function(t){var e=Object(i["a"])(t,"status","variantID","name","sku","sort_by","adult_status","adult_desc","adult_quantity","adult_price","child_status","child_desc","child_quantity","child_price","product_id");for(var a in this.help={status:e["status"],variantID:e["variantID"],name:e["name"],sku:e["sku"],sort_by:e["sort_by"],adult_status:e["adult_status"],adult_desc:e["adult_desc"],adult_quantity:e["adult_quantity"],adult_price:e["adult_price"],child_status:e["child_status"],child_desc:e["child_desc"],child_quantity:e["child_quantity"],child_price:e["child_price"],product_id:e["product_id"]},e)e[a]&&this.$notification["error"]({message:a,description:e[a],duration:4})},initData:function(t){this.isEdit&&(this.$route.meta.title=t.name,this.$emit("title"))},handleSubmit:function(){this.isEdit?this.updateForm(this.form):this.createForm(this.form)},handleStatusChange:function(){this.form.adult_status||this.form.child_status?this.form.status=!0:this.form.status=!1}}},o=c,d=a("2877"),s=Object(d["a"])(o,r,n,!1,null,null,null);e["a"]=s.exports},f3b8:function(t,e,a){"use strict";function r(t){if(t&&t.response&&t.response.data&&t.response.data.message){for(var e={},a=arguments.length,r=new Array(a>1?a-1:0),n=1;n<a;n++)r[n-1]=arguments[n];for(var i=0,l=r;i<l.length;i++){var u=l[i];e[u]=t.response.data.message[u]||null}return e}return null}a.d(e,"a",function(){return r})}}]);