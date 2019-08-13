(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-fac61110"],{3910:function(a,r,e){"use strict";e.r(r);var t=function(){var a=this,r=a.$createElement,e=a._self._c||r;return e("a-card",{attrs:{title:"订单详情"}},[e("a-form",{staticStyle:{"max-width":"500px",margin:"40px auto 0"},attrs:{form:a.form}},[e("a-form-item",{attrs:{label:"订单号",labelCol:a.labelCol,wrapperCol:a.wrapperCol}},[e("a-input",{attrs:{disabled:""},model:{value:a.form.orderID,callback:function(r){a.$set(a.form,"orderID",r)},expression:"form.orderID"}})],1),e("a-form-item",{attrs:{label:"主产品名称",labelCol:a.labelCol,wrapperCol:a.wrapperCol}},[e("a-input",{attrs:{disabled:""},model:{value:a.form.product,callback:function(r){a.$set(a.form,"product",r)},expression:"form.product"}})],1),e("a-form-item",{attrs:{label:"子产品名称",labelCol:a.labelCol,wrapperCol:a.wrapperCol}},[e("a-input",{attrs:{disabled:""},model:{value:a.form.variant,callback:function(r){a.$set(a.form,"variant",r)},expression:"form.variant"}})],1),e("a-form-item",{attrs:{label:"日期",labelCol:a.labelCol,wrapperCol:a.wrapperCol}},[e("a-input",{attrs:{disabled:""},model:{value:a.form.day,callback:function(r){a.$set(a.form,"day",r)},expression:"form.day"}})],1),e("a-form-item",{attrs:{label:"时间",labelCol:a.labelCol,wrapperCol:a.wrapperCol}},[e("a-input",{attrs:{disabled:""},model:{value:a.form.time,callback:function(r){a.$set(a.form,"time",r)},expression:"form.time"}})],1),a.form.adult_quantity>0?e("a-form-item",{attrs:{label:"成人数量",labelCol:a.labelCol,wrapperCol:a.wrapperCol}},[e("a-input",{attrs:{disabled:""},model:{value:a.form.adult_quantity,callback:function(r){a.$set(a.form,"adult_quantity",r)},expression:"form.adult_quantity"}})],1):a._e(),a.form.adult_quantity>0?e("a-form-item",{attrs:{label:"成人金额",labelCol:a.labelCol,wrapperCol:a.wrapperCol}},[e("a-input",{attrs:{suffix:"$",disabled:""},model:{value:a.form.adult_price,callback:function(r){a.$set(a.form,"adult_price",r)},expression:"form.adult_price"}})],1):a._e(),a.form.child_quantity>0?e("a-form-item",{attrs:{label:"儿童数量",labelCol:a.labelCol,wrapperCol:a.wrapperCol}},[e("a-input",{attrs:{disabled:""},model:{value:a.form.child_quantity,callback:function(r){a.$set(a.form,"child_quantity",r)},expression:"form.child_quantity"}})],1):a._e(),a.form.child_quantity>0?e("a-form-item",{attrs:{label:"儿童金额",labelCol:a.labelCol,wrapperCol:a.wrapperCol}},[e("a-input",{attrs:{suffix:"$",disabled:""},model:{value:a.form.child_price,callback:function(r){a.$set(a.form,"child_price",r)},expression:"form.child_price"}})],1):a._e(),e("a-form-item",{attrs:{label:"总金额",labelCol:a.labelCol,wrapperCol:a.wrapperCol}},[e("a-input",{attrs:{suffix:"$",disabled:""},model:{value:a.form.total_price,callback:function(r){a.$set(a.form,"total_price",r)},expression:"form.total_price"}})],1),e("a-form-item",{attrs:{label:"状态",labelCol:a.labelCol,wrapperCol:a.wrapperCol}},[e("a-input",{attrs:{defaultValue:a.orderStatus[a.form.order_status].label,disabled:""}})],1),e("a-form-item",{attrs:{label:"确认号",labelCol:a.labelCol,wrapperCol:a.wrapperCol}},[e("a-input",{attrs:{disabled:""},model:{value:a.form.confirmID,callback:function(r){a.$set(a.form,"confirmID",r)},expression:"form.confirmID"}})],1),e("a-form-item",{attrs:{label:"联系人信息",labelCol:a.labelCol,wrapperCol:a.wrapperCol}},[e("a-textarea",{model:{value:a.form.customer_info,callback:function(r){a.$set(a.form,"customer_info",r)},expression:"form.customer_info"}})],1),e("a-form-item",{attrs:{label:"联系方式",labelCol:a.labelCol,wrapperCol:a.wrapperCol}},[e("a-textarea",{model:{value:a.form.customer_contact,callback:function(r){a.$set(a.form,"customer_contact",r)},expression:"form.customer_contact"}})],1),e("a-form-item",{attrs:{label:"备注",labelCol:a.labelCol,wrapperCol:a.wrapperCol}},[e("a-textarea",{model:{value:a.form.remark,callback:function(r){a.$set(a.form,"remark",r)},expression:"form.remark"}})],1),e("a-form-item",{attrs:{wrapperCol:{span:19,offset:5}}},[e("a-button",{attrs:{type:"primary"},on:{click:a.submit}},[a._v("提交")]),e("a-button",{staticStyle:{"margin-left":"8px"},on:{click:a.back}},[a._v("返回")])],1)],1)],1)},l=[],o=e("f8b7"),n=e("f3b8"),i=[{value:0,label:"新建"},{value:1,label:"订单已确认"},{value:2,label:"出票成功"},{value:3,label:"出票失败"},{value:4,label:"订单已取消"}],s={name:"OrderDetail",data:function(){return{form:Object.assign({},this.$route.query),orderStatus:i,labelCol:{lg:{span:5},sm:{span:5}},wrapperCol:{lg:{span:19},sm:{span:19}}}},methods:{submit:function(){var a=this;this.loading=!0,Object(o["e"])(this.form.id,this.form).then(function(r){r.result;a.$router.go(-1)}).catch(function(r){a.checkError(r)}).finally(function(){a.loading=!1})},back:function(){this.$router.go(-1)},checkError:function(a){var r=Object(n["a"])(a,"customer","adult_quantity","child_quantity","variant");for(var e in r)r[e]&&this.$notification["error"]({message:r[e],duration:4})},handleOrderStatusChange:function(a){this.form.order_status=a}}},u=s,c=(e("c9e5"),e("2877")),f=Object(c["a"])(u,t,l,!1,null,"605442d3",null);r["default"]=f.exports},"3da0":function(a,r,e){},c9e5:function(a,r,e){"use strict";var t=e("3da0"),l=e.n(t);l.a},f3b8:function(a,r,e){"use strict";function t(a){if(a&&a.response&&a.response.data&&a.response.data.message){for(var r={},e=arguments.length,t=new Array(e>1?e-1:0),l=1;l<e;l++)t[l-1]=arguments[l];for(var o=0,n=t;o<n.length;o++){var i=n[o];r[i]=a.response.data.message[i]||null}return r}return null}e.d(r,"a",function(){return t})},f8b7:function(a,r,e){"use strict";e.d(r,"a",function(){return o}),e.d(r,"d",function(){return n}),e.d(r,"c",function(){return i}),e.d(r,"e",function(){return s}),e.d(r,"b",function(){return u});var t=e("365c"),l=e("b775");function o(a){return Object(l["b"])({url:t["a"].checkout,method:"post",data:a})}function n(a){return Object(l["b"])({url:t["a"].order,method:"get",params:a})}function i(a){return Object(l["b"])({url:t["a"].order+"".concat(a,"/"),method:"get"})}function s(a,r){return Object(l["b"])({url:t["a"].order+"".concat(a,"/"),method:"put",data:r})}function u(a){return Object(l["b"])({url:t["a"].order,method:"post",data:a})}}}]);