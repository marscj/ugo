<template>
  <a-spin :spinning="spinning">
    <a-form :form="form">
      <a-row :gutter="16">
        <a-col :span="16">
          <a-card>
            <a-form-item label="Day(日期)">
              <a-input v-model="form.day" disabled></a-input>
            </a-form-item>
            <a-form-item label="Time(时间)">
              <a-input v-model="form.time" disabled></a-input>
            </a-form-item>
            <a-form-item label="Adult Quantity(成人票数量)">
              <a-input v-model="form.adult_quantity" disabled></a-input>
            </a-form-item>
            <a-form-item label="Adult Price(成人票总价格)">
              <a-input v-model="form.adult_price" disabled></a-input>
            </a-form-item>
            <a-form-item label="Child Quantity(儿童票数量)">
              <a-input v-model="form.child_quantity" disabled></a-input>
            </a-form-item>
            <a-form-item label="Child Price(儿童票总价格)">
              <a-input v-model="form.child_price" disabled></a-input>
            </a-form-item>
            <a-form-item label="Total Price(总价格)">
              <a-input v-model="form.total" disabled></a-input>
            </a-form-item>
            <a-form-item label="Guest Info(客户信息)">
              <a-textarea v-model="form.guest_info" autosize disabled></a-textarea>
            </a-form-item>
            <a-form-item label="Guest Contact(客户联系方式)">
              <a-textarea v-model="form.guest_contact" autosize disabled></a-textarea>
            </a-form-item>
            <a-form-item label="Guest Remark">
              <a-textarea v-model="form.guest_remark" autosize disabled></a-textarea>
            </a-form-item>
            <a-form-item label="Order Remark">
              <a-textarea v-model="form.remark" :autosize="{minRows: 5}"></a-textarea>
            </a-form-item>
          </a-card>
          <div style="position:relative; margin-top:20px">
            <a-button type="primary" html-type="submit" @click="handleSubmit" style="margin-right:20px">Submit</a-button>
            <a-button @click="handleGoBack">Return</a-button>
          </div>
        </a-col>
        <a-col :span="8">
          <a-card>
            <a-form-item label="OrderID">
              <a-input v-model="form.orderID" disabled></a-input>
            </a-form-item>
            <a-form-item label="Order Status">
              <a-select :value="form.order_status"  @change="handleOrderStatusChange" :filterOption="false">
                <a-select-option v-for="d in orderStatus" :key="d.value">{{d.label}}</a-select-option>
              </a-select>
            </a-form-item>
            <a-form-item label="Customer">
              <a-input v-model="form.customer" disabled></a-input>
            </a-form-item>
            <a-form-item label="Operator">
              <a-input v-model="form.operator" disabled></a-input>
            </a-form-item>
            <a-form-item label="Create at">
              <template>
                <span>{{form.create_at | moment('YYYY-MM-DD HH:mm')}}</span>
              </template>
            </a-form-item>
            <a-form-item label="Change at">
              <template>
                <span>{{form.change_at | moment('YYYY-MM-DD HH:mm')}}</span>
              </template>
            </a-form-item>
          </a-card>
        </a-col>
      </a-row>
    </a-form>
  </a-spin>
</template>

<script>
import { checkError } from "@/views/utils/error";
import { getOrder, updateOrder, createOrder } from "@/api/order";

const orderStatus = [
  { value: 0, label: "新建" },
  { value: 1, label: "订单已确认" },
  { value: 2, label: "出票成功" },
  { value: 3, label: "订单已取消" },
  { value: 4, label: "退款中" },
  { value: 5, label: "已退款" }
];

export default {
  name: "OrderDetail",
  props: {
    isEdit: {
      type: Boolean,
      default: false
    }
  },
  data() {
    return {
      orderStatus,
      form: {
        order_status: 0,
        adult_quantity: undefined,
        adult_price: undefined,
        child_quantity: undefined,
        child_price: undefined
      },
      help: {},
      spinning: false
    };
  },
  created() {
    if (this.isEdit) {
      const id = this.$route.params && this.$route.params.id;
      this.fetch(id);
    }
  },
  methods: {
    handleGoBack() {
      this.$router.go(-1);
    },
    fetch(id) {
      this.spinning = true;
      getOrder(id)
        .then(res => {
          const { result } = res;
          this.form = result;
          this.initData(result);
        })
        .finally(() => {
          this.spinning = false;
        });
    },
    updateForm(data) {
      this.spinning = true;
      updateOrder(this.$route.params.id, data)
        .then(res => {
          const { result } = res;
          this.handleGoBack();
        })
        .catch(error => {
          this.checkError(error);
        })
        .finally(() => {
          this.spinning = false;
        });
    },
    createForm(data) {
      this.spinning = true;
      createOrder(data)
        .then(res => {
          const { result } = res;
          this.handleGoBack();
        })
        .catch(error => {
          this.checkError(error);
        })
        .finally(() => {
          this.spinning = false;
        });
    },
    checkError(error) {
      var errors = checkError(
        error,
      );

      this.help = {};

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
    initData(data) {
      if (this.isEdit) {
        // this.$route.meta.title = data.product;
        // this.description = data.variant;
        this.$emit("title", data);
      }
    },
    handleOrderStatusChange(value) {
      this.form.order_status = value
    },
    handleSubmit() {
      if (this.isEdit) {
        console.log(this.form, '==========')
        this.updateForm(this.form);
      } else {
        this.createForm(this.form);
      }
    }
  }
};
</script>
