<template>
  <a-card :bordered="true" title="订单列表">
    <div class="table-page-search-wrapper">
      <a-form layout="inline">
        <a-row :gutter="48">
          <a-col :xs="6" :md="8" :sm="16">
            <a-form-item label="Search">
              <a-input
                v-model="queryParam.search"
                placeholder="OrderID, ConfirmID, Variant, Customer, Operator"
              />
            </a-form-item>
          </a-col>
          <a-col :xs="6" :md="8" :sm="16">
            <a-form-item label="Day">
              <a-range-picker :value="day" @change="(value) => day = value"></a-range-picker>
            </a-form-item>
          </a-col>
          <a-col :xs="6" :md="8" :sm="16">
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
      :scroll="{ x: 3050}"
    >
      <span slot="remark" slot-scope="text" style="word-warp:break-word;word-break:break-all">
        <ellipsis :length="200" tooltip>{{ text }}</ellipsis>
      </span>
      <span slot="variant" slot-scope="text" style="word-warp:break-word;word-break:break-all">
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
        <template>
          <router-link :to="{ name: 'OrderDetail', query: data }">详情</router-link>
        </template>
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
      day: undefined,
      queryParam: {
        orderID: undefined,
        confirmID: undefined,
        order_status: undefined,
        pay_status: undefined,
        start_day: undefined,
        end_day: undefined,
        variant__name: undefined,
        variant__product__title: undefined,
        customer__username: undefined,
        operator__username: undefined,
        customer_id: this.$store.getters.userInfo.id
      },
      columns: [
        {
          key: "1",
          title: "订单号",
          dataIndex: "orderID",
          width: 150
        },
        {
          key: "2",
          title: "确认号",
          dataIndex: "confirmID",
          width: 150
        },
        {
          key: "3",
          title: "订单状态",
          dataIndex: "order_status",
          width: 150,
          customRender: (text, row, index) => {
            return <span>{orderStatus[text].label}</span>;
          }
        },
        {
          key: "4",
          title: "产品",
          dataIndex: "variant",
          scopedSlots: { customRender: "variant" },
          width: 250
        },
        {
          key: "5",
          title: "日期",
          dataIndex: "day",
          width: 150
        },
        {
          key: "6",
          title: "时间",
          dataIndex: "time",
          width: 150
        },
        {
          key: "7",
          title: "成人数量",
          dataIndex: "adult_quantity",
          width: 50
        },
        {
          key: "8",
          title: "成人价格",
          dataIndex: "adult_price",
          width: 100
        },
        {
          key: "9",
          title: "儿童数量",
          dataIndex: "child_quantity",
          width: 50
        },
        {
          key: "10",
          title: "儿童价格",
          dataIndex: "child_price",
          width: 100
        },
        {
          key: "18",
          title: "总金额",
          dataIndex: "total_price",
          width: 100
        },
        {
          key: "11",
          title: "客户信息",
          dataIndex: "guest_info",
          scopedSlots: { customRender: "guest_info" },
          width: 400
        },
        {
          key: "12",
          title: "联系方式",
          dataIndex: "guest_contact",
          scopedSlots: { customRender: "guest_contact" },
          width: 400
        },
        {
          key: "14",
          title: "操作员",
          dataIndex: "operator",
          width: 150
        },
        {
          key: "15",
          title: "创建",
          dataIndex: "create_at",
          scopedSlots: { customRender: "create_at" },
          width: 200
        },
        {
          key: "16",
          title: "备注",
          dataIndex: "remark",
          scopedSlots: { customRender: "remark" },
          width: 400
        },
        {
          key: "action",
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
    }
  }
};
</script>
