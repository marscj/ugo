(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-ee898c8a"],{"2b1f":function(e,t,a){"use strict";var r=a("9bfb"),o=a.n(r);o.a},"7a13":function(e,t,a){"use strict";a.r(t);var r=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("a-card",{staticStyle:{width:"100%"},attrs:{tabList:e.tabListNoTitle,activeTabKey:e.noTitleKey},on:{tabChange:function(t){return e.onTabChange(t,"noTitleKey")}}},["index1"===e.noTitleKey?a("order-list"):e._e(),"index2"===e.noTitleKey?a("order-list"):e._e(),"index3"===e.noTitleKey?a("order-list"):e._e(),"index4"===e.noTitleKey?a("order-list"):e._e()],1)},o=[],n=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",{directives:[{name:"action",rawName:"v-action:query",arg:"query"}]},[a("div",{staticClass:"table-page-search-wrapper"},[a("a-form",{attrs:{layout:"inline"}},[a("a-row",{attrs:{gutter:12}},[a("a-col",{attrs:{xs:6,md:6,sm:24}},[a("a-form-item",{attrs:{label:"OrderID"}},[a("a-input",{attrs:{placeholder:""},model:{value:e.queryParam.orderID,callback:function(t){e.$set(e.queryParam,"orderID",t)},expression:"queryParam.orderID"}})],1)],1),a("a-col",{attrs:{xs:6,md:6,sm:24}},[a("a-form-item",{attrs:{label:"Customer"}},[a("a-input",{attrs:{placeholder:""},model:{value:e.queryParam.customer,callback:function(t){e.$set(e.queryParam,"customer",t)},expression:"queryParam.customer"}})],1)],1),a("a-col",{attrs:{xs:6,md:6,sm:24}},[a("a-form-item",{attrs:{label:"Operator"}},[a("a-input",{attrs:{placeholder:""},model:{value:e.queryParam.operator,callback:function(t){e.$set(e.queryParam,"operator",t)},expression:"queryParam.operator"}})],1)],1),a("a-col",{attrs:{xs:6,md:6,sm:24}},[a("a-form-item",{attrs:{label:"Day"}},[a("a-range-picker",{attrs:{value:e.day},on:{change:function(t){return e.day=t}}})],1)],1)],1),a("div",[a("a-collapse",{attrs:{bordered:!1}},[a("a-collapse-panel",{key:"1",staticStyle:{border:"0",overflow:"hidden","margin-bottom":"15px"}},[a("a-row",{attrs:{gutter:12}},[a("a-col",{attrs:{xs:8,md:6,sm:24}},[a("a-form-item",{attrs:{label:"Product"}},[a("a-input",{attrs:{placeholder:""},model:{value:e.queryParam.product,callback:function(t){e.$set(e.queryParam,"product",t)},expression:"queryParam.product"}})],1)],1),a("a-col",{attrs:{xs:8,md:6,sm:24}},[a("a-form-item",{attrs:{label:"Variant"}},[a("a-input",{attrs:{placeholder:""},model:{value:e.queryParam.variant,callback:function(t){e.$set(e.queryParam,"variant",t)},expression:"queryParam.variant"}})],1)],1),a("a-col",{attrs:{xs:8,md:6,sm:24}},[a("a-form-item",{attrs:{label:"OrderStatus"}},[a("a-select",{attrs:{value:e.order_status,filterOption:!1},on:{change:function(t){return e.order_status=t}}},e._l(e.orderStatus,function(t){return a("a-select-option",{key:t.value},[e._v(e._s(t.label))])}),1)],1)],1)],1),a("a-button",{attrs:{type:"primary"},on:{click:function(t){e.exportModal.visible=!0}}},[e._v("Export")])],1)],1)],1)],1),a("a-modal",{attrs:{title:"Export Order"},model:{value:e.exportModal.visible,callback:function(t){e.$set(e.exportModal,"visible",t)},expression:"exportModal.visible"}},[a("template",{slot:"footer"},[a("a-button",{key:"back",on:{click:function(t){e.exportModal.visible=!1}}},[e._v("Return")]),a("a-button",{key:"submit",attrs:{type:"primary"},on:{click:e.exportExcel}},[e._v("Export")])],1),a("a-checkbox-group",{attrs:{options:e.formFiled},model:{value:e.formFiledValue,callback:function(t){e.formFiledValue=t},expression:"formFiledValue"}})],2)],1),a("s-table",{ref:"table",attrs:{size:"default",rowKey:function(e){return e.id},columns:e.book_columns,data:e.loadData,bordered:"",fixed:""},scopedSlots:e._u([{key:"info",fn:function(t,r){return a("span",{},[[a("p",{staticClass:"order-info"},[e._v("产品名称："),a("span",{staticClass:"bold ligth-blue"},[e._v(e._s(r["product"])+" - "+e._s(r["variant"]))])]),a("p",{staticClass:"order-info"},[e._v("执行日期："),a("span",{staticClass:"bold"},[e._v(e._s(r["day"])+" "+e._s(r["time"]))])]),a("p",{staticClass:"order-info"},[e._v("成人数量："),a("span",{staticClass:"bold"},[e._v(e._s(r["adult_quantity"]))])]),r["child_quantity"]>0?a("p",{staticClass:"order-info"},[e._v("儿童数量："),a("span",{staticClass:"bold"},[e._v(e._s(r["adult_quantity"]))])]):e._e(),a("p",{staticClass:"order-info"},[e._v("客人信息："),a("span",{staticClass:"bold"},[e._v(e._s(r["guest_info"])+" "+e._s(r["guest_contact"]))])]),a("p",{staticClass:"order-info"},[e._v("客户备注："),a("span",{staticClass:"bold"},[e._v(e._s(r["guest_remark"]))])]),null!=r["remark"]&&r["remark"].length>0?a("p",{staticClass:"order-info"},[e._v("订单备注："+e._s(r["remark"]))]):e._e()]],2)}},{key:"price",fn:function(t,r){return a("span",{},[[a("p",{staticClass:"order-info"},[e._v("成人："),a("span",{staticClass:"bold"},[e._v(e._s(r["adult_price"])+"$")])]),r["child_quantity"]>0?a("p",{staticClass:"order-info"},[e._v("儿童："),a("span",{staticClass:"bold"},[e._v(e._s(r["child_price"])+"$")])]):e._e(),a("p",{staticClass:"order-info"},[e._v("总价："),a("span",{staticClass:"bold"},[e._v(e._s(r["total"])+"$")])]),a("br"),a("p",{staticClass:"order-info"},[e._v("成人单价："),a("span",{staticClass:"bold"},[e._v(e._s(r["adult_unit_price"])+"$")])]),r["child_quantity"]>0?a("p",{staticClass:"order-info"},[e._v("儿童单价："),a("span",{staticClass:"bold"},[e._v(e._s(r["child_unit_price"])+"$")])]):e._e()]],2)}},{key:"create_at",fn:function(t){return a("span",{},[[a("span",[e._v(e._s(e._f("moment")(t,"YYYY-MM-DD HH:mm")))])]],2)}},{key:"action",fn:function(t,r){return a("span",{},[a("div",{directives:[{name:"action",rawName:"v-action:edit",arg:"edit"}]},[a("router-link",{attrs:{to:{name:"OrderEdit",params:{id:r.id}}}},[e._v("Edit")])],1)])}}])})],1)},l=[],i=(a("7514"),a("2af9")),s=a("f8b7"),d=[{value:-1,label:"全部"},{value:0,label:"新建"},{value:1,label:"订单已确认"},{value:2,label:"出票成功"},{value:3,label:"订单已取消"},{value:4,label:"退款中"},{value:5,label:"已退款"}],u=[{value:"orderID",label:"OrderID",checked:"orderID"},{value:"customer",label:"Customer",checked:"customer"},{value:"product",label:"Product",checked:"product"},{value:"variant",label:"Variant",checked:"variant"},{value:"day",label:"ActionDay",checked:"day"},{value:"time",label:"ActionTime",checked:"time"},{value:"adult_quantity",label:"AdultQuantity",checked:"adult_quantity"},{value:"adult_price",label:"AdultPrice",checked:"adult_price"},{value:"child_quantity",label:"ChildQuantity",checked:"child_quantity"},{value:"child_price",label:"ChildPrice",checked:"child_price"},{value:"total",label:"Total",checked:"total"},{value:"order_status",label:"OrderStatus",checked:"order_status"},{value:"guest_info",label:"GuestInfo",checked:"guest_info"},{value:"guest_contact",label:"GuestContact",checked:"guest_contact"},{value:"guest_remark",label:"GuestRemark",checked:"guest_remark"},{value:"remark",label:"OrderRemark",checked:"remark"},{value:"create_at",label:"CreateAt",checked:"create_at"},{value:"operator",label:"Operator",checked:"operator"}],c={name:"OrderList",components:{STable:i["e"],Ellipsis:i["b"]},created:function(){var e=this;this.debouncedGetAnswer=_.debounce(function(){e.$refs.table.refresh(!0)},1e3),this.formFiledValue=this.formFiled.map(function(e){return e.checked})},watch:{queryParam:{deep:!0,handler:function(e,t){this.debouncedGetAnswer()}},order_status:function(e,t){this.queryParam.order_status=-1==e?void 0:e},day:function(e,t){null!=e&&void 0!=e&&e.length>0?(this.queryParam.start_day=e[0].format("YYYY-MM-DD"),this.queryParam.end_day=e[1].format("YYYY-MM-DD")):(this.queryParam.start_day=void 0,this.queryParam.end_day=void 0)}},data:function(){var e=this;return{orderStatus:d,formFiled:u,formFiledValue:[],day:void 0,order_status:-1,queryParam:{orderID:void 0,order_status:void 0,start_day:void 0,end_day:void 0,variant:void 0,product:void 0,customer:void 0,operator:void 0},exportModal:{visible:!1,loading:!1,filename:"order-list",autoWidth:!0,bookType:"xlsx"},book_columns:[{title:"OrderID",dataIndex:"orderID",width:50},{title:"Customer",dataIndex:"customer",width:120},{title:"Order Info",scopedSlots:{customRender:"info"}},{title:"Price",scopedSlots:{customRender:"price"},width:160},{title:"Create at",dataIndex:"create_at",scopedSlots:{customRender:"create_at"},width:162},{title:"Action",dataIndex:"action",scopedSlots:{customRender:"action"},width:100,fixed:"right"}],loadData:function(t){return Object(s["d"])(Object.assign(t,e.queryParam)).then(function(t){return e.listData=t.result,t.result})},listData:[]}},methods:{handleCreate:function(e){this.$router.push({name:"VariantCreate"})},handleChangeDay:function(e){this.day=e.format("YYYY-MM-DD")},exportExcel:function(){var e=this;a.e("chunk-540ab634").then(a.bind(null,"4bf8d")).then(function(t){var a=e.formatHeader(),r=e.formFiledValue,o=e.listData.data,n=e.formatJson(r,o);t.export_json_to_excel({header:a,data:n,filename:"order-list",autoWidth:!0,bookType:"xlsx"})}),this.exportModal.visible=!1},formatJson:function(e,t){return t.map(function(t){return e.map(function(e){return t[e]})})},formatHeader:function(){var e=this;return this.formFiled.filter(function(t){return e.formFiledValue.find(function(e){return t.value==e})}).map(function(e){return e.value})}}},m=c,f=(a("2b1f"),a("2877")),p=Object(f["a"])(m,n,l,!1,null,null,null),b=p.exports,v={name:"OrderTabs",components:{OrderList:b},data:function(){return{tabListNoTitle:[{key:"index1",tab:"待处理"},{key:"index2",tab:"已确认"},{key:"index3",tab:"出票完成"},{key:"index4",tab:"已取消"}],noTitleKey:"index1"}},methods:{onTabChange:function(e,t){this[t]=e}}},h=v,y=Object(f["a"])(h,r,o,!1,null,null,null);t["default"]=y.exports},"9bfb":function(e,t,a){},f8b7:function(e,t,a){"use strict";a.d(t,"a",function(){return n}),a.d(t,"d",function(){return l}),a.d(t,"c",function(){return i}),a.d(t,"e",function(){return s}),a.d(t,"b",function(){return d});var r=a("365c"),o=a("b775");function n(e){return Object(o["b"])({url:r["a"].checkout,method:"post",data:e})}function l(e){return Object(o["b"])({url:r["a"].order,method:"get",params:e})}function i(e){return Object(o["b"])({url:r["a"].order+"".concat(e,"/"),method:"get"})}function s(e,t){return Object(o["b"])({url:r["a"].order+"".concat(e,"/"),method:"put",data:t})}function d(e){return Object(o["b"])({url:r["a"].order,method:"post",data:e})}}}]);