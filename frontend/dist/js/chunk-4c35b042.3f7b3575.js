(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-4c35b042"],{e03f:function(t,a,e){"use strict";e.r(a);var r=function(){var t=this,a=t.$createElement,e=t._self._c||a;return e("detail",{attrs:{"is-edit":!1}})},n=[],o=e("e8b0"),i={name:"CreateForm",components:{Detail:o["a"]},data:function(){return{description:"新建子产品"}}},l=i,s=e("2877"),u=Object(s["a"])(l,r,n,!1,null,null,null);a["default"]=u.exports},e8b0:function(t,a,e){"use strict";var r=function(){var t=this,a=t.$createElement,e=t._self._c||a;return e("a-spin",{attrs:{spinning:t.spinning}},[e("a-form",{attrs:{form:t.form}},[e("a-row",{attrs:{gutter:16}},[e("a-col",{attrs:{span:16}},[e("a-card",[e("a-form-item",{attrs:{label:"Day(日期)"}},[e("a-input",{attrs:{disabled:""},model:{value:t.form.day,callback:function(a){t.$set(t.form,"day",a)},expression:"form.day"}})],1),e("a-form-item",{attrs:{label:"Time(时间)"}},[e("a-input",{attrs:{disabled:""},model:{value:t.form.time,callback:function(a){t.$set(t.form,"time",a)},expression:"form.time"}})],1),e("a-form-item",{attrs:{label:"Adult Quantity(成人票数量)"}},[e("a-input",{attrs:{disabled:""},model:{value:t.form.adult_quantity,callback:function(a){t.$set(t.form,"adult_quantity",a)},expression:"form.adult_quantity"}})],1),e("a-form-item",{attrs:{label:"Adult Price(成人票总价格)"}},[e("a-input",{attrs:{disabled:""},model:{value:t.form.adult_price,callback:function(a){t.$set(t.form,"adult_price",a)},expression:"form.adult_price"}})],1),e("a-form-item",{attrs:{label:"Child Quantity(儿童票数量)"}},[e("a-input",{attrs:{disabled:""},model:{value:t.form.child_quantity,callback:function(a){t.$set(t.form,"child_quantity",a)},expression:"form.child_quantity"}})],1),e("a-form-item",{attrs:{label:"Child Price(儿童票总价格)"}},[e("a-input",{attrs:{disabled:""},model:{value:t.form.child_price,callback:function(a){t.$set(t.form,"child_price",a)},expression:"form.child_price"}})],1),e("a-form-item",{attrs:{label:"Total Price(总价格)"}},[e("a-input",{attrs:{disabled:""},model:{value:t.form.total_price,callback:function(a){t.$set(t.form,"total_price",a)},expression:"form.total_price"}})],1),e("a-form-item",{attrs:{label:"Customer Info(客户信息)"}},[e("a-textarea",{attrs:{disabled:""},model:{value:t.form.customer_info,callback:function(a){t.$set(t.form,"customer_info",a)},expression:"form.customer_info"}})],1),e("a-form-item",{attrs:{label:"Customer Contact(客户联系方式)"}},[e("a-textarea",{attrs:{disabled:""},model:{value:t.form.customer_contact,callback:function(a){t.$set(t.form,"customer_contact",a)},expression:"form.customer_contact"}})],1),e("a-form-item",{attrs:{label:"ConfirmID"}},[e("a-input",{model:{value:t.form.confirmID,callback:function(a){t.$set(t.form,"confirmID",a)},expression:"form.confirmID"}})],1),e("a-form-item",{attrs:{label:"Remark"}},[e("a-textarea",{model:{value:t.form.remark,callback:function(a){t.$set(t.form,"remark",a)},expression:"form.remark"}})],1)],1),e("div",{staticStyle:{position:"relative","margin-top":"20px"}},[e("a-button",{staticStyle:{"margin-right":"20px"},attrs:{type:"primary","html-type":"submit"},on:{click:t.handleSubmit}},[t._v("Submit")]),e("a-button",{on:{click:t.handleGoBack}},[t._v("Return")])],1)],1),e("a-col",{attrs:{span:8}},[e("a-card",[e("a-form-item",{attrs:{label:"OrderID"}},[e("a-input",{attrs:{disabled:""},model:{value:t.form.orderID,callback:function(a){t.$set(t.form,"orderID",a)},expression:"form.orderID"}})],1),e("a-form-item",{attrs:{label:"Order Status"}},[e("a-select",{attrs:{value:t.form.order_status,filterOption:!1},on:{change:t.handleOrderStatusChange}},t._l(t.orderStatus,function(a){return e("a-select-option",{key:a.value},[t._v(t._s(a.label))])}),1)],1),e("a-form-item",{attrs:{label:"Pay Status"}},[e("a-select",{attrs:{value:t.form.pay_status,filterOption:!1},on:{change:t.handlePayStatusChange}},t._l(t.payStatus,function(a){return e("a-select-option",{key:a.value},[t._v(t._s(a.label))])}),1)],1),e("a-form-item",{attrs:{label:"Customer"}},[e("a-input",{attrs:{disabled:""},model:{value:t.form.customer,callback:function(a){t.$set(t.form,"customer",a)},expression:"form.customer"}})],1),e("a-form-item",{attrs:{label:"Operator"}},[e("a-input",{attrs:{disabled:""},model:{value:t.form.operator,callback:function(a){t.$set(t.form,"operator",a)},expression:"form.operator"}})],1),e("a-form-item",{attrs:{label:"Create at"}},[[e("span",[t._v(t._s(t._f("moment")(t.form.create_at,"YYYY-MM-DD HH:mm")))])]],2),e("a-form-item",{attrs:{label:"Change at"}},[[e("span",[t._v(t._s(t._f("moment")(t.form.change_at,"YYYY-MM-DD HH:mm")))])]],2)],1)],1)],1)],1)],1)},n=[],o=e("f3b8"),i=e("f8b7"),l=[{value:0,label:"新建"},{value:1,label:"订单已确认"},{value:2,label:"出票成功"},{value:3,label:"出票失败"},{value:4,label:"订单已取消"}],s=[{value:0,label:"未支付"},{value:1,label:"部分支付"},{value:2,label:"全部付清"},{value:3,label:"部分退款"},{value:4,label:"全部退款"}],u={name:"OrderDetail",props:{isEdit:{type:Boolean,default:!1}},data:function(){return{orderStatus:l,payStatus:s,form:{order_status:0,pay_status:0,adult_quantity:void 0,adult_price:void 0,child_quantity:void 0,child_price:void 0},help:{},spinning:!1}},created:function(){if(this.isEdit){var t=this.$route.params&&this.$route.params.id;this.fetch(t)}},methods:{handleGoBack:function(){this.$router.go(-1)},fetch:function(t){var a=this;this.spinning=!0,Object(i["c"])(t).then(function(t){var e=t.result;a.form=e,a.initData(e)}).finally(function(){a.spinning=!1})},updateForm:function(t){var a=this;this.spinning=!0,Object(i["e"])(this.$route.params.id,t).then(function(t){t.result;a.handleGoBack()}).catch(function(t){a.checkError(t)}).finally(function(){a.spinning=!1})},createForm:function(t){var a=this;this.spinning=!0,Object(i["b"])(t).then(function(t){t.result;a.handleGoBack()}).catch(function(t){a.checkError(t)}).finally(function(){a.spinning=!1})},checkError:function(t){var a=Object(o["a"])(t);for(var e in this.help={},a)a[e]&&this.$notification["error"]({message:e,description:a[e],duration:4})},initData:function(t){this.isEdit&&this.$emit("title",t)},handleOrderStatusChange:function(t){this.form.order_status=t},handlePayStatusChange:function(t){this.form.pay_status=t},handleSubmit:function(){this.isEdit?this.updateForm(this.form):this.createForm(this.form)}}},c=u,m=e("2877"),f=Object(m["a"])(c,r,n,!1,null,null,null);a["a"]=f.exports},f3b8:function(t,a,e){"use strict";function r(t){if(t&&t.response&&t.response.data&&t.response.data.message){for(var a={},e=arguments.length,r=new Array(e>1?e-1:0),n=1;n<e;n++)r[n-1]=arguments[n];for(var o=0,i=r;o<i.length;o++){var l=i[o];a[l]=t.response.data.message[l]||null}return a}return null}e.d(a,"a",function(){return r})},f8b7:function(t,a,e){"use strict";e.d(a,"a",function(){return o}),e.d(a,"d",function(){return i}),e.d(a,"c",function(){return l}),e.d(a,"e",function(){return s}),e.d(a,"b",function(){return u});var r=e("365c"),n=e("b775");function o(t){return Object(n["b"])({url:r["a"].checkout,method:"post",data:t})}function i(t){return Object(n["b"])({url:r["a"].order,method:"get",params:t})}function l(t){return Object(n["b"])({url:r["a"].order+"".concat(t,"/"),method:"get"})}function s(t,a){return Object(n["b"])({url:r["a"].order+"".concat(t,"/"),method:"put",data:a})}function u(t){return Object(n["b"])({url:r["a"].order,method:"post",data:t})}}}]);