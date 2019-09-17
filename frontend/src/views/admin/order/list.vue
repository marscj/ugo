<template>
  <a-card :bordered="false" v-action:query>
    <div class="table-page-search-wrapper">
      <a-form layout="inline">
        <a-row :gutter="12">
          <a-col :xs="6" :md="6" :sm="24">
            <a-form-item label="OrderID">
              <a-input v-model="queryParam.orderID" placeholder />
            </a-form-item>
          </a-col>
          <a-col :xs="6" :md="6" :sm="24">
            <a-form-item label="Customer">
              <a-input v-model="queryParam.customer" placeholder />
            </a-form-item>
          </a-col>
          <a-col :xs="6" :md="6" :sm="24">
            <a-form-item label="Operator">
              <a-input v-model="queryParam.operator" placeholder />
            </a-form-item>
          </a-col>
          <a-col :xs="6" :md="6" :sm="24">
            <a-form-item label="Day">
              <a-range-picker :value="day" @change="(value) => day = value"></a-range-picker>
            </a-form-item>
          </a-col>
        </a-row>

        <div>
          <a-collapse :bordered="false">
            <a-collapse-panel key="1" style="border: 0; overflow: hidden; margin-bottom: 15px;">
              <a-row :gutter="12">
                <a-col :xs="8" :md="6" :sm="24">
                  <a-form-item label="Product">
                    <a-input v-model="queryParam.product" placeholder />
                  </a-form-item>
                </a-col>
                <a-col :xs="8" :md="6" :sm="24">
                  <a-form-item label="Variant">
                    <a-input v-model="queryParam.variant" placeholder />
                  </a-form-item>
                </a-col>
                <a-col :xs="8" :md="6" :sm="24">
                  <a-form-item label="OrderStatus">
                    <a-select
                      :value="order_status"
                      @change="(value) => order_status = value"
                      :filterOption="false"
                    >
                      <a-select-option v-for="d in orderStatus" :key="d.value">{{d.label}}</a-select-option>
                    </a-select>
                  </a-form-item>
                </a-col>
                <a-col :xs="8" :md="6" :sm="24">
                  <a-form-item label="PayStatus">
                    <a-select
                      :value="pay_status"
                      @change="(value) => pay_status = value"
                      :filterOption="false"
                    >
                      <a-select-option v-for="d in payStatus" :key="d.value">{{d.label}}</a-select-option>
                    </a-select>
                  </a-form-item>
                </a-col>
              </a-row>
              <a-button type="primary" @click="exportModal.visible = true">Export</a-button>
            </a-collapse-panel>
          </a-collapse>
        </div>
      </a-form>

      <a-modal v-model="exportModal.visible" title="Export Order">
        <template slot="footer">
          <a-button key="back" @click="exportModal.visible=false">Return</a-button>
          <a-button key="submit" type="primary" @click="exportExcel">Export</a-button>
        </template>
        <a-checkbox-group :options="formFiled" :defaultValue="formFiled.map((f)=> f.checked)"></a-checkbox-group>
      </a-modal>
    </div>

    <s-table
      ref="table"
      size="default"
      :rowKey="(item) => item.id"
      :columns="columns"
      :data="loadData"
      bordered
      fixed
      :scroll="{ x: 3450}"
    >
      <span slot="guest_remark" slot-scope="text" style="word-warp:break-word;word-break:break-all">
        <ellipsis :length="200" tooltip>{{ text }}</ellipsis>
      </span>
      <span slot="variant" slot-scope="text" style="word-warp:break-word;word-break:break-all">
        <ellipsis :length="60" tooltip>{{ text }}</ellipsis>
      </span>
      <span slot="product" slot-scope="text" style="word-warp:break-word;word-break:break-all">
        <ellipsis :length="60" tooltip>{{ text }}</ellipsis>
      </span>
      <span slot="guest_info" slot-scope="text" style="word-warp:break-word;word-break:break-all">
        <ellipsis :length="160" tooltip>{{ text }}</ellipsis>
      </span>
      <span
        slot="guest_contact"
        slot-scope="text"
        style="word-warp:break-word;word-break:break-all"
      >
        <ellipsis :length="160" tooltip>{{ text }}</ellipsis>
      </span>
      <span slot="create_at" slot-scope="text">
        <template>
          <span>{{text | moment('YYYY-MM-DD HH:mm')}}</span>
        </template>
      </span>
      <span slot="action" slot-scope="text, data">
        <div v-action:edit>
          <router-link :to="{ name: 'OrderEdit', params: { id: data.id } }">Edit</router-link>
        </div>
      </span>
    </s-table>
  </a-card>
</template>

<script>
import { STable, Ellipsis } from "@/components";
import { getOrderList } from "@/api/order";

const orderStatus = [
  { value: -1, label: "全部" },
  { value: 0, label: "新建" },
  { value: 1, label: "订单已确认" },
  { value: 2, label: "出票成功" },
  { value: 3, label: "订单已取消" },
  { value: 4, label: "退款中" },
  { value: 5, label: "已退款" }
];

const payStatus = [
  { value: -1, label: "全部" },
  { value: 0, label: "未支付" },
  { value: 1, label: "部分支付" },
  { value: 2, label: "全部付清" },
  { value: 3, label: "部分退款" },
  { value: 4, label: "全部退款" }
];

export default {
  name: "OrderList",
  components: {
    STable,
    Ellipsis
  },
  created: function() {
    this.debouncedGetAnswer = _.debounce(() => {
      this.$refs.table.refresh(true);
    }, 1000);
  },
  watch: {
    queryParam: {
      deep: true,
      handler: function(newQuestion, oldQuestion) {
        this.debouncedGetAnswer();
      }
    },
    order_status: function(newQuestion, oldQuestion) {
      if (newQuestion == -1) {
        this.queryParam.order_status = undefined;
      } else {
        this.queryParam.order_status = newQuestion;
      }
      // this.$refs.table.refresh(true);
    },
    pay_status: function(newQuestion, oldQuestion) {
      if (newQuestion == -1) {
        this.queryParam.pay_status = undefined;
      } else {
        this.queryParam.pay_status = newQuestion;
      }
      // this.$refs.table.refresh(true);
    },
    day: function(newQuestion, oldQuestion) {
      if (
        newQuestion != null &&
        newQuestion != undefined &&
        newQuestion.length > 0
      ) {
        this.queryParam.start_day = newQuestion[0].format("YYYY-MM-DD");
        this.queryParam.end_day = newQuestion[1].format("YYYY-MM-DD");
      } else {
        this.queryParam.start_day = undefined;
        this.queryParam.end_day = undefined;
      }
      // this.$refs.table.refresh(true);
    }
  },
  data() {
    return {
      orderStatus,
      payStatus,
      formFiled: [
        { value: "orderID", label: "OrderID", checked: 'orderID' },
        { value: "customer", label: "Customer", checked: 'customer' },
        { value: "product", label: "Product", checked: 'product' },
        { value: "variant", label: "Variant", checked: 'variant' },
        { value: "day", label: "ActionDay", checked: 'day' },
        { value: "time", label: "ActionTime", checked: 'time' },
        { value: "adult_quantity", label: "AdultQuantity", checked: 'adult_quantity' },
        { value: "adult_price", label: "AdultPrice", checked: 'adult_price' },
        { value: "child_quantity", label: "ChildQuantity", checked: 'child_quantity' },
        { value: "child_price", label: "ChildPrice", checked: 'child_price' },
        { value: "total", label: "Total", checked: 'total' },
        { value: "order_status", label: "OrderStatus", checked: 'order_status' },
        { value: "pay_status", label: "PayStatus", checked: 'pay_status' },
        { value: "guest_info", label: "GuestInfo", checked: 'guest_info' },
        { value: "guest_contact", label: "GuestContact", checked: 'guest_contact' },
        { value: "guest_remark", label: "GuestRemark", checked: 'guest_remark' },
        { value: "remark", label: "OrderRemark", checked: 'remark' },
        { value: "create_at", label: "CreateAt", checked: 'create_at' },
        { value: "operator", label: "Operator", checked: 'operator' }
      ],
      day: undefined,
      order_status: -1,
      pay_status: -1,
      queryParam: {
        orderID: undefined,
        order_status: undefined,
        pay_status: undefined,
        start_day: undefined,
        end_day: undefined,
        variant: undefined,
        product: undefined,
        customer: undefined,
        operator: undefined
      },
      exportModal: {
        visible: false,
        loading: false,
        filename: "order-list",
        autoWidth: true,
        bookType: "xlsx"
      },
      // 表头
      columns: [
        {
          title: "OrderID",
          dataIndex: "orderID",
          fixed: "left",
          width: 150
        },
        {
          title: "Customer",
          dataIndex: "customer",
          width: 150
        },
        {
          title: "Product",
          dataIndex: "product",
          scopedSlots: { customRender: "product" },
          width: 250
        },
        {
          title: "Variant",
          dataIndex: "variant",
          scopedSlots: { customRender: "variant" },
          width: 250
        },
        {
          title: "ActionDay",
          dataIndex: "day",
          width: 150
        },
        {
          title: "ActionTime",
          dataIndex: "time",
          width: 150
        },
        {
          title: "AdultQuantity",
          dataIndex: "adult_quantity",
          width: 50
        },
        {
          title: "AdultPrice",
          dataIndex: "adult_price",
          width: 100
        },
        {
          title: "ChildQuantity",
          dataIndex: "child_quantity",
          width: 50
        },
        {
          title: "ChildPrice",
          dataIndex: "child_price",
          width: 100
        },
        {
          title: "Total",
          dataIndex: "total",
          width: 100
        },
        {
          title: "OrderStatus",
          dataIndex: "order_status",
          width: 150,
          customRender: (text, row, index) => {
            return (
              <span>{orderStatus.find(res => res.value == text).label}</span>
            );
          }
        },
        {
          title: "PayStatus",
          dataIndex: "pay_status",
          width: 150,
          customRender: (text, row, index) => {
            return (
              <span>{payStatus.find(res => res.value == text).label}</span>
            );
          }
        },
        {
          title: "GuestInfo",
          dataIndex: "guest_info",
          scopedSlots: { customRender: "guest_info" },
          width: 400
        },
        {
          title: "GuestContact",
          dataIndex: "guest_contact",
          scopedSlots: { customRender: "guest_contact" },
          width: 400
        },
        {
          title: "Create at",
          dataIndex: "create_at",
          scopedSlots: { customRender: "create_at" },
          width: 200
        },
        {
          title: "Guest Remark",
          dataIndex: "guest_remark",
          scopedSlots: { customRender: "guest_remark" },
          width: 400
        },
        {
          title: "Operator",
          dataIndex: "operator",
          width: 150
        },
        {
          title: "Action",
          dataIndex: "action",
          scopedSlots: { customRender: "action" },
          width: 100,
          fixed: "right"
        }
      ],
      loadData: parameter => {
        return getOrderList(Object.assign(parameter, this.queryParam)).then(
          res => {
            this.listData = res.result;
            return res.result;
          }
        );
      },
      listData: []
    };
  },
  methods: {
    handleCreate(data) {
      this.$router.push({
        name: "VariantCreate"
      });
    },
    handleChangeDay(value) {
      this.day = value.format("YYYY-MM-DD");
    },
    exportExcel() {
      import("@/vendor/Export2Excel").then(excel => {
        const header = this.formFiled.map((f) => f.label);
        const filterVal = this.formFiled.map((f) => f.checked);
        const list = this.listData.data;
        const data = this.formatJson(filterVal, list);
        excel.export_json_to_excel({
          header: header,
          data,
          filename: "order-list",
          autoWidth: true,
          bookType: "xlsx"
        });
      });
      this.exportModal.visible = false;
    },
    formatJson(filterVal, jsonData) {
      return jsonData.map(v =>
        filterVal.map(j => {
          return v[j];
        })
      );
    }
  }
};
</script>

<style >
.ant-collapse > .ant-collapse-item > .ant-collapse-header {
  line-height: 22px;
  padding: 12px 0 12px 40px;
  color: rgba(0, 0, 0, 0.85);
  cursor: pointer;
  position: relative;
  float: right;
  -webkit-transition: all 0.3s;
  transition: all 0.3s;
}
.ant-collapse-content > .ant-collapse-content-box {
  padding: 0px;
}
</style>
