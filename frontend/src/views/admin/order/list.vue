<template>
  <div v-action:query>
    <s-table
      ref="table"
      size="default"
      :rowKey="(item) => item.id"
      :columns="book_columns"
      :data="loadData"
      bordered
      fixed
    >
      <span slot="info" slot-scope="text, data">
        <template>
          <p class="order-info">
            产品名称:
            <span class="bold ligth-blue">【{{data['product']}} - {{data['variant']}}】</span>
          </p>
          <p class="order-info">
            执行日期:
            <span class="bold">{{data['day'] + ' ' + data['time'] | moment('YYYY-MM-DD HH:mm')}}</span>
          </p>
          <p class="order-info">
            成人数量:
            <span class="bold">{{data['adult_quantity']}}</span>
          </p>
          <p class="order-info" v-if="data['child_quantity'] > 0">
            儿童数量:
            <span class="bold">{{data['adult_quantity']}}</span>
          </p>
          <p class="order-info">
            客人信息:
            <span class="bold">{{data['guest_info']}} {{data['guest_contact']}}</span>
          </p>
          <p class="order-info">
            客户备注:
            <span class="bold">{{data['guest_remark']}}</span>
          </p>
          <p
            class="order-info"
            v-if="data['remark'] != null && data['remark'].length > 0"
          >订单备注:{{data['remark']}}</p>
        </template>
      </span>

      <span slot="price" slot-scope="text, data">
        <template>
          <p class="order-info">
            成人:
            <span class="bold">{{data['adult_price']}}$</span>
          </p>
          <p class="order-info" v-if="data['child_quantity'] > 0">
            儿童:
            <span class="bold">{{data['child_price']}}$</span>
          </p>
          <p class="order-info">
            优惠:
            <span class="bold">{{data['offer']}}$</span>
          </p>
          <p class="order-info">
            总价:
            <span class="bold">{{data['total']}}$</span>
          </p>
          <br />
          <p class="order-info">
            成人单价:
            <span class="bold">{{data['adult_unit_price']}}$</span>
          </p>
          <p class="order-info" v-if="data['child_quantity'] > 0">
            儿童单价:
            <span class="bold">{{data['child_unit_price']}}$</span>
          </p>
        </template>
      </span>

      <span slot="payment" slot-scope="data">
        <div v-for="pay in data.payment" :key="pay.id">
           <p class="order-info">
            金额:
            <span class="bold">{{pay.total}}$</span>
          </p>
          <p class="order-info">
            捕捉金额:
            <span class="bold">{{pay.captured}}$</span>
          </p>
          <p class="order-info">
            状态:
            <span class="bold">{{payStatus[pay.status].label}}</span>
          </p>
          <p class="order-info">
            动作:
            <span class="bold">{{payActions[pay.action].label}}</span>
          </p>
          <p class="order-info">
            客户余额:
            <span class="bold">{{pay.customer_balance}}$</span>
          </p>
        </div>
      </span>

      <span slot="create_at" slot-scope="text">
        <template>
          <span>{{text | moment('MM-DD HH:mm')}}</span>
        </template>
      </span>
      <span slot="action" slot-scope="text, data">
        <div v-action:edit>
          <router-link :to="{ name: 'OrderEdit', params: { id: data.id } }">Edit</router-link>
        </div>
      </span>
    </s-table>
  </div>
</template>

<script>
import { STable, Ellipsis } from "@/components";
import { getOrderList } from "@/api/order";

const payStatus = [
  { value: 0, label: "未支付" },
  { value: 1, label: "部分支付" },
  { value: 2, label: "全部付清" },
  { value: 3, label: "退款中" },
  { value: 4, label: "部分退款" },
  { value: 5, label: "全部退款" },
];

const payActions = [
  { value: 0, label: "捕捉" },
  { value: 1, label: "退款" },
  { value: 2, label: "充值" },
];

export default {
  name: "OrderList",
  components: {
    STable,
    Ellipsis
  },
  props: {
    queryParam: {
      type: Object,
      default: undefined
    },
    status: {
      type: Number,
      default: 0
    }
  },
  data() {
    return {
      payStatus,
      payActions,
      // 表头
      book_columns: [
        {
          title: "OrderID",
          dataIndex: "orderID",
          width: '50px'
        },
        {
          title: "RelatedID",
          dataIndex: "relatedID",
          width: '50px'
        },
        {
          title: "Customer",
          dataIndex: "customer",
          width: '100px'
        },
        {
          title: "Order Info",
          scopedSlots: { customRender: "info" }
        },
        {
          title: "Payment",
          scopedSlots: { customRender: "payment" },
          width: '180px'
        },
        {
          title: "Price",
          scopedSlots: { customRender: "price" },
          width: '140px'
        },
        {
          title: "Create",
          dataIndex: "create_at",
          scopedSlots: { customRender: "create_at" },
          width: '50px'
        },
        {
          title: "Action",
          dataIndex: "action",
          scopedSlots: { customRender: "action" },
          width: '50px',
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
        name: "OrderCreate"
      });
    },
    refresh() {
      this.$refs.table.refresh()
    }
  }
};
</script>

<style >
.order-info {
  margin: 0;
}

.bold {
  font-weight: bold;
}

.ligth-blue {
  color: #2F54EB
}

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
