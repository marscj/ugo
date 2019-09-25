<template>
  <div>
    <a-card class="table-page-search-wrapper" :bordered="false">
      <template slot="extra">
        <a-form layout="inline">
          <a-row :gutter="48">
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
              <a-form-item label="Action Day">
                <a-range-picker :value="day" @change="(value) => day = value"></a-range-picker>
              </a-form-item>
            </a-col>

            <a-col :xs="6" :md="6" :sm="24">
              <a-form-item label="RelatedID">
                <a-input v-model="queryParam.relatedID" placeholder />
              </a-form-item>
            </a-col>
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
              <a-form-item label="Status">
                <a-select
                  :value="order_status"
                  @change="(value) => order_status = value"
                  :filterOption="false"
                >
                  <a-select-option v-for="d in orderStatus" :key="d.value">{{d.label}}</a-select-option>
                </a-select>
              </a-form-item>
            </a-col>
          </a-row>
          <a-button type="primary" @click="activeKey = '2'">Search</a-button>
          <a-button class="buttonStyle" type="primary" @click="exportModal.visible = true">Export</a-button>
        </a-form>
      </template>

      <a-tabs defaultActiveKey="3" :activeKey="activeKey" @change="handleTableChange" >
        <a-tab-pane tab="待处理" :key="0">
          <order-list :queryParam="queryParam"/>
        </a-tab-pane>
        <a-tab-pane tab="已确认" :key="1">
          <order-list />
        </a-tab-pane>
        <a-tab-pane tab="出票完成" :key="2">
          <order-list />
        </a-tab-pane>
        <a-tab-pane tab="已取消" :key="3">
          <order-list />
        </a-tab-pane>
        <a-tab-pane tab="退款中" :key="4">
          <order-list />
        </a-tab-pane>
        <a-tab-pane tab="已退款" :key="5">
          <order-list />
        </a-tab-pane>
        <a-tab-pane tab="全部" :key="-1">
          <order-list />
        </a-tab-pane>
      </a-tabs>
    </a-card>
  </div>
</template>

<script>
import OrderList from "./list";

const orderStatus = [
  { value: -1, label: "全部" },
  { value: 0, label: "待处理" },
  { value: 1, label: "已确认" },
  { value: 2, label: "出票完成" },
  { value: 3, label: "已取消" },
  { value: 4, label: "退款中" },
  { value: 5, label: "已退款" }
];

export default {
  components: {
    OrderList
  },
  watch: {
    order_status: function(newQuestion, oldQuestion) {
      if (newQuestion == -1) {
        this.queryParam.order_status = undefined;
      } else {
        this.queryParam.order_status = newQuestion;
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
    }
  },
  data() {
    return {
      activeKey: 0,
      orderStatus,
      queryParam: {
        orderID: undefined,
        relatedID: undefined,
        order_status: undefined,
        start_day: undefined,
        end_day: undefined,
        variant: undefined,
        product: undefined,
        customer: undefined,
        operator: undefined
      },
      day: undefined,
      order_status: -1,
    };
  },
  methods: {
    handleTableChange(value) {
      this.activeKey = value
    }
  }
};
</script>

<style >
.ant-collapse > .ant-collapse-item > .ant-collapse-header {
  line-height: 22px;
  padding: 12px 0 12px 40px;
  color: #000000d9;
  cursor: pointer;
  position: relative;
  float: right;
  -webkit-transition: all 0.3s;
  transition: all 0.3s;
}

.ant-collapse-content > .ant-collapse-content-box {
  padding: 0px;
}

.ant-card-extra {
  width: 100%;
  padding: 16px 0;
  font-size: 14px;
  color: rgba(0, 0, 0, 0.65);
  font-weight: normal;
  margin-left: 0;
}

.buttonStyle {
  margin: 0px 8px;
}
</style>