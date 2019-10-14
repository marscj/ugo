<template>
  <div>
    <a-spin v-action:query :spinning="loading">
      <s-table
        ref="table"
        size="default"
        :rowKey="(item) => item.id"
        :columns="order_columns"
        :data="loadData"
        bordered
        fixed
      >
        <span slot="order" slot-scope="text, data">
          <template>
            <p class="order-info">
              产品名称:
              <span class="bold ligth-blue">【{{data['product']}} - {{data['variant']}}】</span>
            </p>
            <p class="order-info">
              执行日期:
              <span
                class="bold"
              >{{data['day'] + ' ' + data['time'] | moment('YYYY-MM-DD HH:mm')}}</span>
            </p>
            <p class="order-info">
              成人数量:
              <span class="bold">{{data['adult_quantity']}}</span>
            </p>
            <p class="order-info" v-if="data['child_quantity'] > 0">
              儿童数量:
              <span class="bold">{{data['child_quantity']}}</span>
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
            <p class="order-info">
              修改:
              <span class="bold">{{pay.change_at | moment('YYYY-MM-DD HH:mm')}}</span>
            </p>
            <p class="order-info">
              说明:
              <span class="bold">{{pay.description}}</span>
            </p>
            <p>
              <a-popconfirm
                title="Are you sure to do this?"
                @confirm="paymentRefund(pay)"
                okText="Yes"
                cancelText="No"
                v-if="$auth('Payment.edit') && pay.status == 3"
              >
                <a href="javascript:;">Confrim</a>
              </a-popconfirm>
            </p>
          </div>
        </span>

        <span slot="booking" slot-scope="data">
          <div v-for="booking in data.booking" :key="booking.id">
            <router-link
              :to="{name: 'BookingEdit', params: {id: booking.id}}"
              target="_blank"
            >{{booking.bookingID}}</router-link>
          </div>
        </span>

        <span slot="create_at" slot-scope="text">
          <template>
            <span>{{text | moment('MM-DD HH:mm')}}</span>
          </template>
        </span>

        <span slot="action" slot-scope="text, data">
          <template v-action:edit>
            <div v-if="status == 0">
              <a
                v-if="$auth('Order.edit')"
                href="javascript:;"
                @click="changeOrderStatus(data, 1)"
              >confirm</a>
              <br />
              <a-popconfirm
                title="Are you sure cancel?"
                @confirm="changeOrderStatus(data, 3)"
                okText="Yes"
                cancelText="No"
                v-if="$auth('Order.edit')"
              >
                <a href="javascript:;">cancel</a>
              </a-popconfirm>
            </div>
            <div v-if="status == 1">
              <a-dropdown v-if="$auth('Booking.add')">
                <a-menu slot="overlay">
                  <a-menu-item v-for="category in Category" :key="category.value">
                    <a href="javascript:;" @click="hanldeBooking(category.value, data)">
                      <icon-font :type="category.type" />
                      {{category.label}}
                    </a>
                  </a-menu-item>
                </a-menu>
                <a href="javascript:;">booking</a>
              </a-dropdown>
              <br />
              <a
                v-if="$auth('Order.edit')"
                href="javascript:;"
                @click="changeOrderStatus(data, 2)"
              >complete</a>
            </div>
            <div v-if="status == 2"></div>
            <div v-if="status == 3">
              <a v-if="$auth('Payment.add')" href="javascript:;" @click="refund.handle(data)">refund</a>
              <br />
              <a
                v-if="$auth('Order.edit') | $auth('Payment.edit')"
                href="javascript:;"
                @click="changeOrderStatus(data, 5)"
              >complete</a>
            </div>
            <div v-if="status == 5"></div>
            <div>
              <a href="javascript:;" @click="remark.handle(data)">remark</a>
            </div>
          </template>
        </span>
      </s-table>
    </a-spin>

    <a-modal v-model="refund.visible" title="Refund Form">
      <a-form>
        <a-form-item :labelCol="labelCol" :wrapperCol="wrapperCol" label="Amount" :required="true">
          <a-input-number
            v-model="refund.form.amount"
            :min="0.0"
            :max="refund.data.total"
            :defaultValue="0.0"
            :precision="2"
            :step="0.5"
            style="width:200px;"
          />
        </a-form-item>
        <a-form-item :labelCol="labelCol" :wrapperCol="wrapperCol" label="Description">
          <a-textarea v-model="refund.form.description" :autosize="{minRows: 3}"></a-textarea>
        </a-form-item>
      </a-form>
      <template slot="footer">
        <a-button key="back" @click="refund.visible=false">Return</a-button>
        <a-button
          key="submit"
          type="primary"
          :loading="refund.loading"
          @click="refund.submit"
        >Submit</a-button>
      </template>
    </a-modal>

    <a-modal v-model="remark.visible" title="Remark">
      <a-form>
        <a-form-item>
          <a-textarea v-model="remark.data.remark" :autosize="{minRows: 5}"></a-textarea>
        </a-form-item>
      </a-form>
      <template slot="footer">
        <a-button key="back" @click="remark.visible=false">Return</a-button>
        <a-button
          key="submit"
          type="primary"
          :loading="remark.loading"
          @click="remark.submit"
        >Submit</a-button>
      </template>
    </a-modal>
  </div>
</template>

<script>
import { STable, Ellipsis } from "@/components";
import { getOrderList, updateOrder, orderRefund } from "@/api/order";

import { paymentRefund } from "@/api/payment";
import { checkError } from "@/views/utils/error";

import moment from "moment";

import { Icon } from "ant-design-vue";
const IconFont = Icon.createFromIconfontCN({
  scriptUrl: "//at.alicdn.com/t/font_1402881_gsh78a0lnya.js"
});

const payStatus = [
  { value: 0, label: "未支付" },
  { value: 1, label: "部分支付" },
  { value: 2, label: "全部付清" },
  { value: 3, label: "退款中" },
  { value: 4, label: "部分退款" },
  { value: 5, label: "全部退款" }
];

const payActions = [
  { value: 0, label: "扣费" },
  { value: 1, label: "退款" },
  { value: 2, label: "充值" }
];

const Category = [
  { value: 1, label: "Restaurant", type: "iconf-30" },
  { value: 2, label: "Tour", type: "iconticket" },
  { value: 3, label: "Transport", type: "iconche" },
  { value: 4, label: "Hotel", type: "iconhotel" }
];

export default {
  name: "OrderList",
  components: {
    STable,
    Ellipsis,
    IconFont
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
      loading: false,
      Category,
      payStatus,
      payActions,
      labelCol: {
        xs: { span: 24 },
        sm: { span: 5 }
      },
      wrapperCol: {
        xs: { span: 24 },
        sm: { span: 16 }
      },
      order_columns: [
        {
          title: "OrderID",
          dataIndex: "orderID",
          width: "50px"
        },
        {
          title: "RelatedID",
          dataIndex: "relatedID",
          width: "50px"
        },
        {
          title: "Customer",
          dataIndex: "customer",
          width: "100px"
        },
        {
          title: "Order Info",
          scopedSlots: { customRender: "order" }
        },
        {
          title: "Price",
          scopedSlots: { customRender: "price" },
          width: "140px"
        },
        {
          title: "Payment",
          scopedSlots: { customRender: "payment" },
          width: "180px"
        },
        {
          title: "Booking",
          scopedSlots: { customRender: "booking" },
          width: "110px"
        },
        {
          title: "Operator",
          dataIndex: "operator",
          width: "50px"
        },
        {
          title: "Create",
          dataIndex: "create_at",
          scopedSlots: { customRender: "create_at" },
          width: "40px"
        },
        {
          title: "Action",
          dataIndex: "action",
          scopedSlots: { customRender: "action" },
          width: "90px",
          fixed: "right"
        }
      ],
      loadData: parameter => {
        return getOrderList(Object.assign(parameter, this.queryParam)).then(
          res => {
            return res.result;
          }
        );
      },
      refund: {
        loading: false,
        visible: false,
        handle: data => {
          this.refund.visible = true;
          this.refund.data = data;
          this.refund.form.amount = data.total;
          this.refund.form.description = "";
        },
        data: {
          total: undefined
        },
        form: {
          amount: 0.0,
          description: ""
        },
        submit: () => {
          this.refund.loading = true;
          orderRefund(this.refund.data.id, this.refund.form)
            .then(res => {
              return this.refresh(false);
            })
            .catch(error => this.checkError(error))
            .finally(() => {
              this.refund.loading = false;
              this.refund.visible = false;
            });
        }
      },
      remark: {
        loading: false,
        visible: false,

        handle: data => {
          this.remark.visible = true;
          this.remark.data = Object.assign({}, data);
        },

        data: {
          id: undefined,
          remark: undefined
        },

        submit: () => {
          this.remark.loading = true;
          updateOrder(this.remark.data.id, this.remark.data)
            .then(res => {
              return this.refresh(false);
            })
            .finally(() => {
              this.remark.visible = false;
              this.remark.loading = false;
            });
        }
      }
    };
  },
  methods: {
    refresh(value = true) {
      this.$refs.table.refresh(value);
    },
    changeOrderStatus(data, status) {
      this.loading = true;
      updateOrder(data.id, Object.assign({}, data, { order_status: status }))
        .then(res => {
          return this.refresh(false);
        })
        .finally(() => {
          this.loading = false;
        });
    },
    paymentRefund(data) {
      this.loading = true;
      paymentRefund(data.id)
        .then(res => {
          return this.refresh(false);
        })
        .finally(() => (this.loading = false));
    },
    checkError(error) {
      var errors = checkError(error, "amount");

      for (var key in errors) {
        if (errors[key]) {
          this.$notification["error"]({
            message: key,
            description: errors[key],
            duration: 4
          });
        }
      }
    },
    hanldeBooking(value, data) {
      let routeUrl = this.$router.resolve({
        name: "BookingCreate",
        query: Object.assign({ type: value }, data)
      });
      window.open(routeUrl.href, "_blank");
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
  color: #2f54eb;
}

.ant-table-tbody > tr > td,
.ant-table-thead > tr > th {
  padding: 12px 8px;
  font-size: 12px;
}

.form-item {
  margin-bottom: 0px;
}
</style>
