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
          
          <a-button type="primary" @click="hanldeSearch">Search & Refresh</a-button>
          <a-button class="buttonStyle" type="primary" @click="exportModal.visible = true">Export</a-button>
        </a-form>
      </template>

      <a-tabs
        :defaultActiveKey="0"
        :activeKey="activeKey"
        @change="handleTableChange"
        :animated="false"
      >
        <a-tab-pane v-for="tab in orderStatus" :tab="tab.label" :key="tab.value">
          <order-list :queryParam="queryParam" :status="tab.value" ref="orders" />
        </a-tab-pane>
      </a-tabs>
    </a-card>
  </div>
</template>

<script>
import OrderList from "./list";

const orderStatus = [
  { value: 0, label: "New" },
  { value: 1, label: "Confirm" },
  { value: 2, label: "Complete" },
  { value: 3, label: "Cancel" },
  // { value: 4, label: "退款中" },
  { value: 5, label: "Refund" },
  { value: -1, label: "All" }
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
    },
    activeKey: function(newQuestion, oldQuestion) {
      if (newQuestion == -1) {
        this.queryParam.order_status = undefined;
      } else {
        this.queryParam.order_status = newQuestion;
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
        order_status: 0,
        start_day: undefined,
        end_day: undefined,
        variant: undefined,
        product: undefined,
        customer: undefined,
        operator: undefined
      },
      day: undefined,
      order_status: -1
    };
  },
  methods: {
    refresh() {
      this.$refs.orders.find(f => f.status == this.activeKey).refresh();
    },
    handleTableChange(value) {
      this.activeKey = value;
      if (this.$refs.orders.find(f => f.status == this.activeKey)) {
        this.$nextTick(() =>
          this.refresh()
        );
      } else {
        this.hanldeClean()
      }
    },
    hanldeClean() {
      this.queryParam = {
        orderID: undefined,
        relatedID: undefined,
        order_status: this.activeKey,
        start_day: undefined,
        end_day: undefined,
        variant: undefined,
        product: undefined,
        customer: undefined,
        operator: undefined
      },
      this.$nextTick(() =>
        this.refresh()
      );
    },
    hanldeSearch() {
      this.refresh();
    }
  }
};
</script>

<style >

.ant-card-extra {
  width: 100%;
  padding: 16px 0;
  font-size: 14px;
  color: rgba(0, 0, 0, 0.65);
  font-weight: normal;
  margin-left: 0;
}

.ant-card-wider-padding .ant-card-body {
    padding: 24px 12px;
}

.buttonStyle {
  margin: 0px 8px;
}
</style>