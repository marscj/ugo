(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-3054d83a"],{"2b1f":function(t,a,e){"use strict";var r=e("9bfb"),s=e.n(r);s.a},"51f0":function(t,a,e){"use strict";var r=e("ca16"),s=e.n(r);s.a},"7a13":function(t,a,e){"use strict";e.r(a);var r=function(){var t=this,a=t.$createElement,e=t._self._c||a;return e("div",[e("a-card",{staticClass:"table-page-search-wrapper",attrs:{bordered:!1}},[e("template",{slot:"extra"},[e("a-form",{attrs:{layout:"inline"}},[e("a-row",{attrs:{gutter:48}},[e("a-col",{attrs:{xs:6,md:6,sm:24}},[e("a-form-item",{attrs:{label:"OrderID"}},[e("a-input",{attrs:{placeholder:""},model:{value:t.queryParam.orderID,callback:function(a){t.$set(t.queryParam,"orderID",a)},expression:"queryParam.orderID"}})],1)],1),e("a-col",{attrs:{xs:6,md:6,sm:24}},[e("a-form-item",{attrs:{label:"Customer"}},[e("a-input",{attrs:{placeholder:""},model:{value:t.queryParam.customer,callback:function(a){t.$set(t.queryParam,"customer",a)},expression:"queryParam.customer"}})],1)],1),e("a-col",{attrs:{xs:6,md:6,sm:24}},[e("a-form-item",{attrs:{label:"Operator"}},[e("a-input",{attrs:{placeholder:""},model:{value:t.queryParam.operator,callback:function(a){t.$set(t.queryParam,"operator",a)},expression:"queryParam.operator"}})],1)],1),e("a-col",{attrs:{xs:6,md:6,sm:24}},[e("a-form-item",{attrs:{label:"Action Day"}},[e("a-range-picker",{attrs:{value:t.day},on:{change:function(a){return t.day=a}}})],1)],1),e("a-col",{attrs:{xs:6,md:6,sm:24}},[e("a-form-item",{attrs:{label:"RelatedID"}},[e("a-input",{attrs:{placeholder:""},model:{value:t.queryParam.relatedID,callback:function(a){t.$set(t.queryParam,"relatedID",a)},expression:"queryParam.relatedID"}})],1)],1),e("a-col",{attrs:{xs:8,md:6,sm:24}},[e("a-form-item",{attrs:{label:"Product"}},[e("a-input",{attrs:{placeholder:""},model:{value:t.queryParam.product,callback:function(a){t.$set(t.queryParam,"product",a)},expression:"queryParam.product"}})],1)],1),e("a-col",{attrs:{xs:8,md:6,sm:24}},[e("a-form-item",{attrs:{label:"Variant"}},[e("a-input",{attrs:{placeholder:""},model:{value:t.queryParam.variant,callback:function(a){t.$set(t.queryParam,"variant",a)},expression:"queryParam.variant"}})],1)],1),e("a-col",{attrs:{xs:8,md:6,sm:24}},[e("a-form-item",{attrs:{label:"Status"}},[e("a-select",{attrs:{value:t.order_status,filterOption:!1},on:{change:function(a){return t.order_status=a}}},t._l(t.orderStatus,function(a){return e("a-select-option",{key:a.value},[t._v(t._s(a.label))])}),1)],1)],1)],1),e("a-button",{attrs:{type:"primary"},on:{click:t.hanldeSearch}},[t._v("Search & Refresh")]),e("a-button",{staticClass:"buttonStyle",attrs:{type:"primary"},on:{click:t.hanldeClean}},[t._v("Clean")]),e("a-button",{staticClass:"buttonStyle",attrs:{type:"primary"},on:{click:function(a){t.exportModal.visible=!0}}},[t._v("Export")])],1)],1),e("a-tabs",{attrs:{defaultActiveKey:0,activeKey:t.activeKey,animated:!1},on:{change:t.handleTableChange}},t._l(t.orderStatus,function(a){return e("a-tab-pane",{key:a.value,attrs:{tab:a.label}},[e("order-list",{ref:"orders",refInFor:!0,attrs:{queryParam:t.queryParam,status:a.value}})],1)}),1)],2)],1)},s=[],n=(e("7514"),function(){var t=this,a=t.$createElement,e=t._self._c||a;return e("div",{directives:[{name:"action",rawName:"v-action:query",arg:"query"}]},[e("s-table",{ref:"table",attrs:{size:"default",rowKey:function(t){return t.id},columns:t.book_columns,data:t.loadData,bordered:"",fixed:""},scopedSlots:t._u([{key:"info",fn:function(a,r){return e("span",{},[[e("p",{staticClass:"order-info"},[t._v("\n          产品名称:\n          "),e("span",{staticClass:"bold ligth-blue"},[t._v("【"+t._s(r["product"])+" - "+t._s(r["variant"])+"】")])]),e("p",{staticClass:"order-info"},[t._v("\n          执行日期:\n          "),e("span",{staticClass:"bold"},[t._v(t._s(t._f("moment")(r["day"]+" "+r["time"],"YYYY-MM-DD HH:mm")))])]),e("p",{staticClass:"order-info"},[t._v("\n          成人数量:\n          "),e("span",{staticClass:"bold"},[t._v(t._s(r["adult_quantity"]))])]),r["child_quantity"]>0?e("p",{staticClass:"order-info"},[t._v("\n          儿童数量:\n          "),e("span",{staticClass:"bold"},[t._v(t._s(r["adult_quantity"]))])]):t._e(),e("p",{staticClass:"order-info"},[t._v("\n          客人信息:\n          "),e("span",{staticClass:"bold"},[t._v(t._s(r["guest_info"])+" "+t._s(r["guest_contact"]))])]),e("p",{staticClass:"order-info"},[t._v("\n          客户备注:\n          "),e("span",{staticClass:"bold"},[t._v(t._s(r["guest_remark"]))])]),null!=r["remark"]&&r["remark"].length>0?e("p",{staticClass:"order-info"},[t._v("订单备注:"+t._s(r["remark"]))]):t._e()]],2)}},{key:"price",fn:function(a,r){return e("span",{},[[e("p",{staticClass:"order-info"},[t._v("\n          成人:\n          "),e("span",{staticClass:"bold"},[t._v(t._s(r["adult_price"])+"$")])]),r["child_quantity"]>0?e("p",{staticClass:"order-info"},[t._v("\n          儿童:\n          "),e("span",{staticClass:"bold"},[t._v(t._s(r["child_price"])+"$")])]):t._e(),e("p",{staticClass:"order-info"},[t._v("\n          优惠:\n          "),e("span",{staticClass:"bold"},[t._v(t._s(r["offer"])+"$")])]),e("p",{staticClass:"order-info"},[t._v("\n          总价:\n          "),e("span",{staticClass:"bold"},[t._v(t._s(r["total"])+"$")])]),e("br"),e("p",{staticClass:"order-info"},[t._v("\n          成人单价:\n          "),e("span",{staticClass:"bold"},[t._v(t._s(r["adult_unit_price"])+"$")])]),r["child_quantity"]>0?e("p",{staticClass:"order-info"},[t._v("\n          儿童单价:\n          "),e("span",{staticClass:"bold"},[t._v(t._s(r["child_unit_price"])+"$")])]):t._e()]],2)}},{key:"payment",fn:function(a){return e("span",{},t._l(a.payment,function(a){return e("div",{key:a.id},[e("p",{staticClass:"order-info"},[t._v("\n          金额:\n          "),e("span",{staticClass:"bold"},[t._v(t._s(a.total)+"$")])]),e("p",{staticClass:"order-info"},[t._v("\n          捕捉金额:\n          "),e("span",{staticClass:"bold"},[t._v(t._s(a.captured)+"$")])]),e("p",{staticClass:"order-info"},[t._v("\n          状态:\n          "),e("span",{staticClass:"bold"},[t._v(t._s(t.payStatus[a.status].label))])]),e("p",{staticClass:"order-info"},[t._v("\n          动作:\n          "),e("span",{staticClass:"bold"},[t._v(t._s(t.payActions[a.action].label))])]),e("p",{staticClass:"order-info"},[t._v("\n          客户余额:\n          "),e("span",{staticClass:"bold"},[t._v(t._s(a.customer_balance)+"$")])])])}),0)}},{key:"create_at",fn:function(a){return e("span",{},[[e("span",[t._v(t._s(t._f("moment")(a,"MM-DD HH:mm")))])]],2)}},{key:"action",fn:function(a,r){return e("span",{},[e("div",{directives:[{name:"action",rawName:"v-action:edit",arg:"edit"}]},[e("router-link",{attrs:{to:{name:"OrderEdit",params:{id:r.id}}}},[t._v("Edit")])],1)])}}])})],1)}),o=[],i=(e("c5f6"),e("2af9")),l=e("f8b7"),u=[{value:0,label:"未支付"},{value:1,label:"部分支付"},{value:2,label:"全部付清"},{value:3,label:"退款中"},{value:4,label:"部分退款"},{value:5,label:"全部退款"}],d=[{value:0,label:"捕捉"},{value:1,label:"退款"},{value:2,label:"充值"}],c={name:"OrderList",components:{STable:i["e"],Ellipsis:i["b"]},props:{queryParam:{type:Object,default:void 0},status:{type:Number,default:0}},data:function(){var t=this;return{payStatus:u,payActions:d,book_columns:[{title:"OrderID",dataIndex:"orderID",width:"50px"},{title:"RelatedID",dataIndex:"relatedID",width:"50px"},{title:"Customer",dataIndex:"customer",width:"100px"},{title:"Order Info",scopedSlots:{customRender:"info"}},{title:"Payment",scopedSlots:{customRender:"payment"},width:"180px"},{title:"Price",scopedSlots:{customRender:"price"},width:"140px"},{title:"Create",dataIndex:"create_at",scopedSlots:{customRender:"create_at"},width:"50px"},{title:"Action",dataIndex:"action",scopedSlots:{customRender:"action"},width:"50px",fixed:"right"}],loadData:function(a){return Object(l["d"])(Object.assign(a,t.queryParam)).then(function(a){return t.listData=a.result,a.result})},listData:[]}},methods:{handleCreate:function(t){this.$router.push({name:"OrderCreate"})},refresh:function(){this.$refs.table.refresh()}}},p=c,f=(e("2b1f"),e("2877")),m=Object(f["a"])(p,n,o,!1,null,null,null),v=m.exports,_=[{value:0,label:"待处理"},{value:1,label:"已确认"},{value:2,label:"出票完成"},{value:3,label:"已取消"},{value:4,label:"退款中"},{value:5,label:"已退款"},{value:-1,label:"全部"}],b={components:{OrderList:v},watch:{order_status:function(t,a){this.queryParam.order_status=-1==t?void 0:t},day:function(t,a){null!=t&&void 0!=t&&t.length>0?(this.queryParam.start_day=t[0].format("YYYY-MM-DD"),this.queryParam.end_day=t[1].format("YYYY-MM-DD")):(this.queryParam.start_day=void 0,this.queryParam.end_day=void 0)},activeKey:function(t,a){this.queryParam.order_status=-1==t?void 0:t}},data:function(){return{activeKey:0,orderStatus:_,queryParam:{orderID:void 0,relatedID:void 0,order_status:0,start_day:void 0,end_day:void 0,variant:void 0,product:void 0,customer:void 0,operator:void 0},day:void 0,order_status:-1}},methods:{refresh:function(){var t=this;this.$refs.orders.find(function(a){return a.status==t.activeKey}).refresh()},handleTableChange:function(t){var a=this;this.activeKey=t,this.$refs.orders.find(function(t){return t.status==a.activeKey})?this.$nextTick(function(){return a.refresh()}):this.hanldeClean()},hanldeClean:function(){var t=this;this.queryParam={orderID:void 0,relatedID:void 0,order_status:this.activeKey,start_day:void 0,end_day:void 0,variant:void 0,product:void 0,customer:void 0,operator:void 0},this.$nextTick(function(){return t.refresh()})},hanldeSearch:function(){this.refresh()}}},y=b,h=(e("51f0"),Object(f["a"])(y,r,s,!1,null,null,null));a["default"]=h.exports},"9bfb":function(t,a,e){},ca16:function(t,a,e){},f8b7:function(t,a,e){"use strict";e.d(a,"a",function(){return n}),e.d(a,"d",function(){return o}),e.d(a,"c",function(){return i}),e.d(a,"e",function(){return l}),e.d(a,"b",function(){return u});var r=e("365c"),s=e("b775");function n(t){return Object(s["b"])({url:r["a"].checkout,method:"post",data:t})}function o(t){return Object(s["b"])({url:r["a"].order,method:"get",params:t})}function i(t){return Object(s["b"])({url:r["a"].order+"".concat(t,"/"),method:"get"})}function l(t,a){return Object(s["b"])({url:r["a"].order+"".concat(t,"/"),method:"put",data:a})}function u(t){return Object(s["b"])({url:r["a"].order,method:"post",data:t})}}}]);