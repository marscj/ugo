(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-16cfc87e"],{"0552":function(t,e,a){},2013:function(t,e,a){"use strict";a.r(e);var r=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("detail",{attrs:{"is-edit":!0},on:{title:t.onTitle}})},i=[],l=a("e8b0"),n={name:"CreateForm",components:{Detail:l["a"]},data:function(){return{description:""}},methods:{onTitle:function(t){this.$route.meta.title=t.orderID}}},s=n,o=a("2877"),u=Object(o["a"])(s,r,i,!1,null,null,null);e["default"]=u.exports},e8b0:function(t,e,a){"use strict";var r,i,l=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",[a("div",[a("a-card",{attrs:{title:"订单详情"}},[a("template",{slot:"extra"},[a("a-button-group",[0==t.form.order_status?a("a-button",{on:{click:function(e){return t.changeOrderStatus(1)}}},[t._v("确认")]):t._e(),t.form.order_status<=1?a("a-button",{on:{click:function(e){return t.changeOrderStatus(3)}}},[t._v("取消")]):t._e(),1==t.form.order_status?a("a-button",{on:{click:function(e){return t.changeOrderStatus(2)}}},[t._v("完成")]):t._e(),3==t.form.order_status?a("a-button",{on:{click:function(e){return t.changeOrderStatus(4)}}},[t._v("申请退款")]):t._e(),4==t.form.order_status?a("a-button",{on:{click:function(e){return t.changeOrderStatus(5)}}},[t._v("审核通过")]):t._e(),a("a-button",{on:{click:t.remarkModal.handle}},[t._v("备注")])],1)],1),t.form.order_status<3?a("a-steps",{staticStyle:{margin:"24px 0px 40px 0px"},attrs:{direction:"horizontal",current:t.form.order_status}},[a("a-step",{attrs:{title:"新建"}}),a("a-step",{attrs:{title:"订单已确认,正在出票中"}}),a("a-step",{attrs:{title:"出票完成"}})],1):a("a-steps",{staticStyle:{margin:"24px 0px 40px 0px"},attrs:{direction:"horizontal",current:t.form.order_status-3}},[a("a-step",{attrs:{title:"订单已取消"}}),a("a-step",{attrs:{title:"退款中"}}),a("a-step",{attrs:{title:"已退款"}})],1),a("detail-list",{attrs:{col:4}},[a("detail-list-item",{attrs:{term:"创建人"}},[t._v(t._s(t.form.customer))]),a("detail-list-item",{attrs:{term:"执行时间"}},[t._v(t._s(t.form.time))]),a("detail-list-item",{attrs:{term:"主产品"}},[t._v(t._s(t.form.product))]),a("detail-list-item",{attrs:{term:"成人数量"}},[t._v(t._s(t.form.adult_quantity))]),a("detail-list-item",{attrs:{term:"创建时间"}},[t._v(t._s(t._f("moment")(t.form.create_at)))]),a("detail-list-item",{attrs:{term:"执行日期"}},[t._v(t._s(t.form.day))]),a("detail-list-item",{attrs:{term:"子产品"}},[t._v(t._s(t.form.variant))]),a("detail-list-item",{attrs:{term:"儿童数量"}},[t._v(t._s(t.form.child_quantity))])],1),a("detail-list",{staticClass:"detail-layout",attrs:{col:2}},[a("detail-list-item",{attrs:{term:"客户信息"}},[t._v(t._s(t.form.guest_info))]),a("detail-list-item",{attrs:{term:"联系方式"}},[t._v(t._s(t.form.guest_contact))])],1),a("detail-list",{staticClass:"detail-layout",attrs:{col:1}},[a("detail-list-item",{attrs:{term:"客户备注"}},[t._v(t._s(t.form.guest_remark))])],1),a("detail-list",{staticClass:"detail-layout",attrs:{col:1}},[a("detail-list-item",{attrs:{term:"订单备注"}},[t._v(t._s(t.form.remark))])],1),a("detail-list",{staticClass:"detail-layout",attrs:{col:1}},[a("detail-list-item",{attrs:{term:"操作"}},[t._v(t._s(t.form.operator))])],1),[a("div",{staticClass:"status-list"},[a("div",{staticClass:"text"},[t._v("成人")]),a("div",{staticClass:"heading"},[t._v(t._s(t.form.adult_price)+" $")])]),a("div",{staticClass:"status-list"},[a("div",{staticClass:"text"},[t._v("儿童")]),a("div",{staticClass:"heading"},[t._v(t._s(t.form.child_price)+" $")])])]],2),a("a-card",{attrs:{title:"预定详情"}},[a("template",{slot:"extra"},[a("a-button-group",[a("a-dropdown",[a("a-menu",{attrs:{slot:"overlay"},on:{click:t.handleMenuClick},slot:"overlay"},t._l(t.categoryData,function(e){return a("a-menu-item",{key:e.value},[a("icon-font",{attrs:{type:e.type}}),t._v("\n                "+t._s(e.label)+"\n              ")],1)}),1),a("a-button",{staticStyle:{"margin-left":"8px"}},[t._v("\n              添加\n              "),a("a-icon",{attrs:{type:"down"}})],1)],1)],1)],1)],2)],1),a("a-modal",{attrs:{title:"订单备注"},model:{value:t.remarkModal.visible,callback:function(e){t.$set(t.remarkModal,"visible",e)},expression:"remarkModal.visible"}},[a("a-form",[a("a-form-item",[a("a-textarea",{attrs:{autosize:{minRows:5}},model:{value:t.remarkModal.remark,callback:function(e){t.$set(t.remarkModal,"remark",e)},expression:"remarkModal.remark"}})],1)],1),a("template",{slot:"footer"},[a("a-button",{key:"back",on:{click:function(e){t.remarkModal.visible=!1}}},[t._v("Return")]),a("a-button",{key:"submit",attrs:{type:"primary",loading:t.remarkModal.loading},on:{click:t.remarkModal.submit}},[t._v("Submit")])],1)],2)],1)},n=[],s=a("0c63"),o=a("ac0d"),u=a("680a"),c=a("fa43"),d=c["a"],m=d,f=a("2877"),v=Object(f["a"])(m,r,i,!1,null,null,null),_=v.exports,p=(a("f3b8"),a("f8b7")),b=_.Item,h=s["a"].createFromIconfontCN({scriptUrl:"//at.alicdn.com/t/font_1402881_gsh78a0lnya.js"}),k=[{value:0,label:"新建"},{value:1,label:"订单已确认"},{value:2,label:"出票成功"},{value:3,label:"订单已取消"},{value:4,label:"退款中"},{value:5,label:"已退款"}],g=[{value:0,label:"未支付"},{value:1,label:"部分支付"},{value:2,label:"全部付清"},{value:3,label:"部分退款"},{value:4,label:"全部退款"}],y=[{value:1,label:"美食",type:"iconf-30"},{value:2,label:"门票",type:"iconticket"},{value:3,label:"日游",type:"iconlvyou"},{value:4,label:"用车",type:"iconche"},{value:5,label:"酒店",type:"iconhotel"},{value:6,label:"伴手礼",type:"iconliwu1"}],x={name:"OrderDetail",props:{isEdit:{type:Boolean,default:!1}},components:{PageView:u["b"],DetailList:_,DetailListItem:b,IconFont:h},mixins:[o["c"]],data:function(){var t=this;return{orderStatus:k,payStatus:g,categoryData:y,form:{order_status:0,pay_status:0,adult_quantity:void 0,adult_price:void 0,child_quantity:void 0,child_price:void 0},remarkModal:{visible:!1,loading:!1,remark:"",handle:function(){t.remarkModal.visible=!0,t.remarkModal.loading=!1,t.remarkModal.remark=t.form.remark},submit:function(){t.remarkModal.loading=!0,Object(p["e"])(t.form.id,Object.assign({},t.form,{remark:t.remarkModal.remark})).then(function(e){var a=e.result;t.form=a,t.remarkModal.visible=!1}).finally(function(){t.remarkModal.loading=!1})}},help:{},spinning:!1}},mounted:function(){if(this.isEdit){var t=this.$route.params&&this.$route.params.id;this.fetch(t)}},methods:{fetch:function(t){var e=this;this.spinning=!0,Object(p["c"])(t).then(function(t){var a=t.result;e.form=a,e.initData(a)}).finally(function(){e.spinning=!1})},initData:function(t){this.isEdit&&this.$emit("title",t)},changeOrderStatus:function(t){var e=this;this.spinning=!0,Object(p["e"])(this.form.id,Object.assign({},this.form,{order_status:t})).then(function(t){var a=t.result;e.form=a}).finally(function(){e.spinning=!1})},handleMenuClick:function(t){}}},M=x,O=(a("fecc"),Object(f["a"])(M,l,n,!1,null,"09e19434",null));e["a"]=O.exports},f3b8:function(t,e,a){"use strict";function r(t){if(t&&t.response&&t.response.data&&t.response.data.message){for(var e={},a=arguments.length,r=new Array(a>1?a-1:0),i=1;i<a;i++)r[i-1]=arguments[i];for(var l=0,n=r;l<n.length;l++){var s=n[l];e[s]=t.response.data.message[s]||null}return e}return null}a.d(e,"a",function(){return r})},f8b7:function(t,e,a){"use strict";a.d(e,"a",function(){return l}),a.d(e,"d",function(){return n}),a.d(e,"c",function(){return s}),a.d(e,"e",function(){return o}),a.d(e,"b",function(){return u});var r=a("365c"),i=a("b775");function l(t){return Object(i["b"])({url:r["a"].checkout,method:"post",data:t})}function n(t){return Object(i["b"])({url:r["a"].order,method:"get",params:t})}function s(t){return Object(i["b"])({url:r["a"].order+"".concat(t,"/"),method:"get"})}function o(t,e){return Object(i["b"])({url:r["a"].order+"".concat(t,"/"),method:"put",data:e})}function u(t){return Object(i["b"])({url:r["a"].order,method:"post",data:t})}},fecc:function(t,e,a){"use strict";var r=a("0552"),i=a.n(r);i.a}}]);