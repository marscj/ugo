<template>
  <div v-action:query>
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
        <a-checkbox-group v-model="formFiledValue" :options="formFiled"></a-checkbox-group>
      </a-modal>
    </div>

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
            产品名称：
            <span class="bold ligth-blue">{{data['product']}} - {{data['variant']}}</span>
          </p>
          <p class="order-info">
            执行日期：
            <span class="bold">{{data['day']}} {{data['time']}}</span>
          </p>
          <p class="order-info">
            成人数量：
            <span class="bold">{{data['adult_quantity']}}</span>
          </p>
          <p class="order-info" v-if="data['child_quantity'] > 0">
            儿童数量：
            <span class="bold">{{data['adult_quantity']}}</span>
          </p>
          <p class="order-info">
            客人信息：
            <span class="bold">{{data['guest_info']}} {{data['guest_contact']}}</span>
          </p>
          <p class="order-info">
            客户备注：
            <span class="bold">{{data['guest_remark']}}</span>
          </p>
          <p
            class="order-info"
            v-if="data['remark'] != null && data['remark'].length > 0"
          >订单备注：{{data['remark']}}</p>
        </template>
      </span>

      <span slot="price" slot-scope="text, data">
        <template>
          <p class="order-info">
            成人：
            <span class="bold">{{data['adult_price']}}$</span>
          </p>
          <p class="order-info" v-if="data['child_quantity'] > 0">
            儿童：
            <span class="bold">{{data['child_price']}}$</span>
          </p>
          <p class="order-info">
            总价：
            <span class="bold">{{data['total']}}$</span>
          </p>
          <br />
          <p class="order-info">
            成人单价：
            <span class="bold">{{data['adult_unit_price']}}$</span>
          </p>
          <p class="order-info" v-if="data['child_quantity'] > 0">
            儿童单价：
            <span class="bold">{{data['child_unit_price']}}$</span>
          </p>
        </template>
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
  </div>
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

const formFiled = [
  { value: "orderID", label: "OrderID", checked: "orderID" },
  { value: "customer", label: "Customer", checked: "customer" },
  { value: "product", label: "Product", checked: "product" },
  { value: "variant", label: "Variant", checked: "variant" },
  { value: "day", label: "ActionDay", checked: "day" },
  { value: "time", label: "ActionTime", checked: "time" },
  {
    value: "adult_quantity",
    label: "AdultQuantity",
    checked: "adult_quantity"
  },
  { value: "adult_price", label: "AdultPrice", checked: "adult_price" },
  {
    value: "child_quantity",
    label: "ChildQuantity",
    checked: "child_quantity"
  },
  { value: "child_price", label: "ChildPrice", checked: "child_price" },
  { value: "total", label: "Total", checked: "total" },
  { value: "order_status", label: "OrderStatus", checked: "order_status" },
  { value: "guest_info", label: "GuestInfo", checked: "guest_info" },
  { value: "guest_contact", label: "GuestContact", checked: "guest_contact" },
  { value: "guest_remark", label: "GuestRemark", checked: "guest_remark" },
  { value: "remark", label: "OrderRemark", checked: "remark" },
  { value: "create_at", label: "CreateAt", checked: "create_at" },
  { value: "operator", label: "Operator", checked: "operator" }
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

    this.formFiledValue = this.formFiled.map(f => f.checked);
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
      orderStatus,
      formFiled,
      formFiledValue: [],
      day: undefined,
      order_status: -1,
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
      exportModal: {
        visible: false,
        loading: false,
        filename: "order-list",
        autoWidth: true,
        bookType: "xlsx"
      },
      // 表头
      book_columns: [
        {
          title: "OrderID",
          dataIndex: "orderID",
          width: 50
        },
        {
          title: "RelatedID",
          dataIndex: "relatedID",
          width: 50
        },
        {
          title: "Customer",
          dataIndex: "customer",
          width: 120
        },
        {
          title: "Order Info",
          scopedSlots: { customRender: "info" }
        },
        {
          title: "Price",
          scopedSlots: { customRender: "price" },
          width: 160
        },
        {
          title: "Create at",
          dataIndex: "create_at",
          scopedSlots: { customRender: "create_at" },
          width: 162
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
        const header = this.formatHeader();
        const filterVal = this.formFiledValue;
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
    },
    formatHeader() {
      return this.formFiled
        .filter(f => {
          return this.formFiledValue.find(f1 => f.value == f1);
        })
        .map(f => f.value);
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
