<template>
  <a-card :bordered="false" v-action:query>
    <div class="table-page-search-wrapper">
      <a-form layout="inline">
        <a-row :gutter="48">
          <a-col :xs="6" :md="5" :sm="16">
            <a-form-item label="Search">
              <a-input
                v-model="queryParam.search"
                placeholder="OrderID, ConfirmID, Variant, Customer, Operator"
              />
            </a-form-item>
          </a-col>
          <a-col :xs="6" :md="5" :sm="16">
            <a-form-item label="Day">
              <a-range-picker :value="day" @change="(value) => day = value"></a-range-picker>
            </a-form-item>
          </a-col>
          <a-col :xs="6" :md="5" :sm="16">
            <a-form-item label="Order Status">
              <a-select
                :value="queryParam.order_status"
                @change="(value) => queryParam.order_status = value"
                :filterOption="false"
              >
                <a-select-option v-for="d in orderStatus" :key="d.value">{{d.label}}</a-select-option>
              </a-select>
            </a-form-item>
          </a-col>
          <a-col :xs="6" :md="5" :sm="16">
            <a-form-item label="Pay Status">
              <a-select
                :value="queryParam.pay_status"
                @change="(value) => queryParam.pay_status = value"
                :filterOption="false"
              >
                <a-select-option v-for="d in payStatus" :key="d.value">{{d.label}}</a-select-option>
              </a-select>
            </a-form-item>
          </a-col>
        </a-row>
      </a-form>
    </div>

    <s-table
      ref="table"
      size="default"
      :rowKey="(item) => item.id"
      :columns="columns"
      :data="loadData"
      bordered
      fixed
      :scroll="{ x: 3550}"
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
      <span
        slot="guest_info"
        slot-scope="text"
        style="word-warp:break-word;word-break:break-all"
      >
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
  { value: 0, label: "新建" },
  { value: 1, label: "订单已确认" },
  { value: 2, label: "出票成功" },
  { value: 3, label: "出票失败" },
  { value: 4, label: "订单已取消" }
];

const payStatus = [
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
      this.$refs.table.refresh(true);
    }
  },
  data() {
    return {
      orderStatus,
      payStatus,
      day: undefined,
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
      // 表头
      columns: [
        {
          key: "#",
          title: "#",
          dataIndex: "id",
          fixed: "left",
          width: 100
        },
        {
          title: "OrderID",
          dataIndex: "orderID",
          fixed: "left",
          width: 150
        },
        {
          title: "OrderStatus",
          dataIndex: "order_status",
          width: 150,
          customRender: (text, row, index) => {
            return <span>{orderStatus[text].label}</span>;
          }
        },
        {
          title: "PayStatus",
          dataIndex: "pay_status",
          width: 150,
          customRender: (text, row, index) => {
            return <span>{payStatus[text].label}</span>;
          }
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
          title: "Day",
          dataIndex: "day",
          width: 150
        },
        {
          title: "Time",
          dataIndex: "time",
          width: 150
        },
        {
          title: "Adult Quantity",
          dataIndex: "adult_quantity",
          width: 50
        },
        {
          title: "Adult Price",
          dataIndex: "adult_price",
          width: 100
        },
        {
          title: "Child Quantity",
          dataIndex: "child_quantity",
          width: 50
        },
        {
          title: "Child Price",
          dataIndex: "child_price",
          width: 100
        },
        {
          title: "Total",
          dataIndex: "total",
          width: 100
        },
        {
          title: "Guest Info",
          dataIndex: "guest_info",
          scopedSlots: { customRender: "guest_info" },
          width: 400
        },
        {
          title: "Guest Contact",
          dataIndex: "guest_contact",
          scopedSlots: { customRender: "guest_contact" },
          width: 400
        },
        {
          key: "13",
          title: "Customer",
          dataIndex: "customer",
          width: 150
        },
        {
          title: "Operator",
          dataIndex: "operator",
          width: 150
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
          title: "操作",
          dataIndex: "action",
          scopedSlots: { customRender: "action" },
          width: 100,
          fixed: "right"
        }
      ],
      loadData: parameter => {
        return getOrderList(Object.assign(parameter, this.queryParam)).then(
          res => {
            return res.result;
          }
        );
      }
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
    }
  }
};
</script>
