<template>
  <a-card :bordered="true" title="订单列表">
    <div class="table-page-search-wrapper">
      <a-form layout="inline">
        <a-row :gutter="48">
          <a-col :md="8" :sm="16">
            <a-form-item label="Search">
              <a-input v-model="queryParam.search" placeholder="Name or ID" />
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
      <span slot="customer_info" slot-scope="text" style="word-warp:break-word;word-break:break-all">
        <ellipsis :length="160" tooltip>{{ text }}</ellipsis>
      </span>
      <span slot="customer_contact" slot-scope="text" style="word-warp:break-word;word-break:break-all">
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
  data() {
    return {
      orderStatus,
      queryParam: {
        customer_id: this.$store.getters.userInfo.id
      },
      // 表头
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
          scopedSlots: { customRender: 'variant' },
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
          dataIndex: "customer_info",
          scopedSlots: { customRender: 'customer_info' },
          width: 400
        },
        {
          key: "12",
          title: "联系方式",
          dataIndex: "customer_contact",
          scopedSlots: { customRender: 'customer_contact' },
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
          scopedSlots: { customRender: 'create_at' },
          width: 200
        },
        {
          key: "16",
          title: "备注",
          dataIndex: "remark",
          scopedSlots: { customRender: 'remark' },
          width: 400
        },
        {
          key: "action",
          title: "操作",
          dataIndex: "action",
          scopedSlots: { customRender: "action" },
          width: 100,
          fixed: 'right'
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
