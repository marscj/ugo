(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-4474568d"],{b077:function(t,a,e){"use strict";var r=e("db22"),i=e.n(r);i.a},db22:function(t,a,e){},e03f:function(t,a,e){"use strict";e.r(a);var r=function(){var t=this,a=t.$createElement,e=t._self._c||a;return e("detail",{attrs:{"is-edit":!1}})},i=[],n=e("e8b0"),s={name:"CreateForm",components:{Detail:n["a"]},data:function(){return{description:"新建子产品"}}},l=s,o=e("2877"),u=Object(o["a"])(l,r,i,!1,null,null,null);a["default"]=u.exports},e8b0:function(t,a,e){"use strict";var r,i,n=function(){var t=this,a=t.$createElement,e=t._self._c||a;return e("div",{attrs:{spinning:t.spinning}},[e("div",[e("a-card",{attrs:{title:"订单详情"}},[e("template",{slot:"extra"},[e("a-button-group",[0==t.form.order_status?e("a-button",{on:{click:function(a){return t.changeOrderStatus(1)}}},[t._v("确认")]):t._e(),t.form.order_status<=1?e("a-button",{on:{click:function(a){return t.changeOrderStatus(3)}}},[t._v("取消")]):t._e(),1==t.form.order_status?e("a-button",{on:{click:function(a){return t.changeOrderStatus(2)}}},[t._v("完成")]):t._e(),3==t.form.order_status?e("a-button",{on:{click:function(a){return t.changeOrderStatus(4)}}},[t._v("申请退款")]):t._e(),4==t.form.order_status?e("a-button",{on:{click:function(a){return t.changeOrderStatus(5)}}},[t._v("审核通过")]):t._e(),e("a-button",{on:{click:t.remarkModal.handle}},[t._v("备注")])],1)],1),t.form.order_status<3?e("a-steps",{staticStyle:{margin:"24px 0px 40px 0px"},attrs:{direction:"horizontal",current:t.form.order_status}},[e("a-step",{attrs:{title:"新建"}}),e("a-step",{attrs:{title:"订单已确认,正在出票中"}}),e("a-step",{attrs:{title:"出票完成"}})],1):e("a-steps",{staticStyle:{margin:"24px 0px 40px 0px"},attrs:{direction:"horizontal",current:t.form.order_status-3}},[e("a-step",{attrs:{title:"订单已取消"}}),e("a-step",{attrs:{title:"退款中"}}),e("a-step",{attrs:{title:"已退款"}})],1),e("detail-list",{attrs:{col:4}},[e("detail-list-item",{attrs:{term:"创建人"}},[t._v(t._s(t.form.customer))]),e("detail-list-item",{attrs:{term:"执行时间"}},[t._v(t._s(t.form.time))]),e("detail-list-item",{attrs:{term:"主产品"}},[t._v(t._s(t.form.product))]),e("detail-list-item",{attrs:{term:"成人数量"}},[t._v(t._s(t.form.adult_quantity))]),e("detail-list-item",{attrs:{term:"创建时间"}},[t._v(t._s(t._f("moment")(t.form.create_at)))]),e("detail-list-item",{attrs:{term:"执行日期"}},[t._v(t._s(t.form.day))]),e("detail-list-item",{attrs:{term:"子产品"}},[t._v(t._s(t.form.variant))]),e("detail-list-item",{attrs:{term:"儿童数量"}},[t._v(t._s(t.form.child_quantity))])],1),e("detail-list",{staticClass:"detail-layout",attrs:{col:2}},[e("detail-list-item",{attrs:{term:"客户信息"}},[t._v(t._s(t.form.guest_info))]),e("detail-list-item",{attrs:{term:"联系方式"}},[t._v(t._s(t.form.guest_contact))])],1),e("detail-list",{staticClass:"detail-layout",attrs:{col:1}},[e("detail-list-item",{attrs:{term:"客户备注"}},[t._v(t._s(t.form.guest_remark))])],1),e("detail-list",{staticClass:"detail-layout",attrs:{col:1}},[e("detail-list-item",{attrs:{term:"订单备注"}},[t._v(t._s(t.form.remark))])],1),e("detail-list",{staticClass:"detail-layout",attrs:{col:1}},[e("detail-list-item",{attrs:{term:"操作"}},[t._v(t._s(t.form.operator))])],1),[e("div",{staticClass:"status-list"},[e("div",{staticClass:"text"},[t._v("成人")]),e("div",{staticClass:"heading"},[t._v(t._s(t.form.adult_price)+" $")])]),e("div",{staticClass:"status-list"},[e("div",{staticClass:"text"},[t._v("儿童")]),e("div",{staticClass:"heading"},[t._v(t._s(t.form.child_price)+" $")])])]],2),e("a-card",{attrs:{title:"预定详情"}},[e("template",{slot:"extra"},[e("a-button-group",[e("a-dropdown",[e("a-menu",{attrs:{slot:"overlay"},on:{click:t.handleMenuClick},slot:"overlay"},t._l(t.categoryData,function(a){return e("a-menu-item",{key:a.value},[e("icon-font",{attrs:{type:a.type}}),t._v("\n                "+t._s(a.label)+"\n              ")],1)}),1),e("a-button",{staticStyle:{"margin-left":"8px"}},[t._v("\n              添加\n              "),e("a-icon",{attrs:{type:"down"}})],1)],1)],1)],1)],2)],1),e("a-modal",{attrs:{title:"订单备注"},model:{value:t.remarkModal.visible,callback:function(a){t.$set(t.remarkModal,"visible",a)},expression:"remarkModal.visible"}},[e("a-form",[e("a-form-item",[e("a-textarea",{attrs:{autosize:{minRows:5}},model:{value:t.remarkModal.remark,callback:function(a){t.$set(t.remarkModal,"remark",a)},expression:"remarkModal.remark"}})],1)],1),e("template",{slot:"footer"},[e("a-button",{key:"back",on:{click:function(a){t.remarkModal.visible=!1}}},[t._v("Return")]),e("a-button",{key:"submit",attrs:{type:"primary",loading:t.remarkModal.loading},on:{click:t.remarkModal.submit}},[t._v("Submit")])],1)],2)],1)},s=[],l=e("0c63"),o=e("ac0d"),u=e("680a"),c=e("fa43"),d=c["a"],m=d,f=e("2877"),v=Object(f["a"])(m,r,i,!1,null,null,null),_=v.exports,p=(e("f3b8"),e("f8b7")),b=_.Item,h=l["a"].createFromIconfontCN({scriptUrl:"//at.alicdn.com/t/font_1402881_gsh78a0lnya.js"}),k=[{value:0,label:"新建"},{value:1,label:"订单已确认"},{value:2,label:"出票成功"},{value:3,label:"订单已取消"},{value:4,label:"退款中"},{value:5,label:"已退款"}],g=[{value:1,label:"美食",type:"iconf-30"},{value:2,label:"门票",type:"iconticket"},{value:3,label:"日游",type:"iconlvyou"},{value:4,label:"用车",type:"iconche"},{value:5,label:"酒店",type:"iconhotel"},{value:6,label:"伴手礼",type:"iconliwu1"}],y={name:"OrderDetail",props:{isEdit:{type:Boolean,default:!1}},components:{PageView:u["b"],DetailList:_,DetailListItem:b,IconFont:h},mixins:[o["c"]],data:function(){var t=this;return{orderStatus:k,categoryData:g,form:{order_status:0,adult_quantity:void 0,adult_price:void 0,child_quantity:void 0,child_price:void 0},remarkModal:{visible:!1,loading:!1,remark:"",handle:function(){t.remarkModal.visible=!0,t.remarkModal.loading=!1,t.remarkModal.remark=t.form.remark},submit:function(){t.remarkModal.loading=!0,Object(p["e"])(t.form.id,Object.assign({},t.form,{remark:t.remarkModal.remark})).then(function(a){var e=a.result;t.form=e,t.remarkModal.visible=!1}).finally(function(){t.remarkModal.loading=!1})}},help:{},spinning:!1}},mounted:function(){if(this.isEdit){var t=this.$route.params&&this.$route.params.id;this.fetch(t)}},methods:{fetch:function(t){var a=this;this.spinning=!0,Object(p["c"])(t).then(function(t){var e=t.result;a.form=e,a.initData(e)}).finally(function(){a.spinning=!1})},initData:function(t){this.isEdit&&this.$emit("title",t)},changeOrderStatus:function(t){var a=this;this.spinning=!0,Object(p["e"])(this.form.id,Object.assign({},this.form,{order_status:t})).then(function(t){var e=t.result;a.form=e}).finally(function(){a.spinning=!1})},handleMenuClick:function(t){}}},x=y,M=(e("b077"),Object(f["a"])(x,n,s,!1,null,"f82849a2",null));a["a"]=M.exports},f3b8:function(t,a,e){"use strict";function r(t){if(t&&t.response&&t.response.data&&t.response.data.message){for(var a={},e=arguments.length,r=new Array(e>1?e-1:0),i=1;i<e;i++)r[i-1]=arguments[i];for(var n=0,s=r;n<s.length;n++){var l=s[n];a[l]=t.response.data.message[l]||null}return a}return null}e.d(a,"a",function(){return r})},f8b7:function(t,a,e){"use strict";e.d(a,"a",function(){return n}),e.d(a,"d",function(){return s}),e.d(a,"c",function(){return l}),e.d(a,"e",function(){return o}),e.d(a,"b",function(){return u});var r=e("365c"),i=e("b775");function n(t){return Object(i["b"])({url:r["a"].checkout,method:"post",data:t})}function s(t){return Object(i["b"])({url:r["a"].order,method:"get",params:t})}function l(t){return Object(i["b"])({url:r["a"].order+"".concat(t,"/"),method:"get"})}function o(t,a){return Object(i["b"])({url:r["a"].order+"".concat(t,"/"),method:"put",data:a})}function u(t){return Object(i["b"])({url:r["a"].order,method:"post",data:t})}}}]);