<template >
  <a-card :loading="loading">
    <a-form :form="form">
      <a-form-item label="CouponID">
        <a-input v-model="form.id" disabled />
      </a-form-item>

      <a-form-item label="Product">
        <a-select
          :showSearch="true"
          :showArrow="false"
          :value="product"
          :filterOption="false"
          @search="handleProductSearch"
          @change="handleProductChange"
          :notFoundContent="loadingProduct ? undefined : null"
        >
          <a-spin v-if="loadingProduct" slot="notFoundContent" size="small" />
          <a-select-option v-for="d in productOption" :key="d.id" :value="d.id">{{d.title}}</a-select-option>
        </a-select>
      </a-form-item>

      <a-form-item
        label="variant"
        :validate-status="help.variant_id == null || help.variant_id === '' ?  null : 'error'"
        :help="help.variant_id"
        v-if="variantOption.length > 0"
      >
        <a-select
          :value="form.variant_id"
          allowClear
          @change="handleVariantChange"
          :notFoundContent="null"
        >
          <a-select-option v-for="d in variantOption" :key="d.id" :value="d.id">{{d.name}}</a-select-option>
        </a-select>
      </a-form-item>

      <a-form-item label="Customer">
        <a-select
          mode="multiple"
          :showSearch="true"
          :showArrow="false"
          :value="form.customer_id"
          :filterOption="false"
          @search="handleCustomerSearch"
          @change="handleCustomerChange"
          :notFoundContent="loadingCustomer ? undefined : null"
        >
          <a-spin v-if="loadingCustomer" slot="notFoundContent" size="small" />
          <a-select-option v-for="d in customerOption" :key="d.id" :value="d.id">{{d.username}}</a-select-option>
        </a-select>
      </a-form-item>

      <a-form-item
        label="Exp Date"
        :required="true"
        :validate-status="help.exp_date == null || help.exp_date === '' ?  null : 'error'"
        :help="help.exp_date"
      >
        <a-date-picker v-model="form.exp_date" />
      </a-form-item>

      <a-form-item
        label="Amount"
        :required="true"
        :validate-status="help.amount == null || help.amount === '' ?  null : 'error'"
        :help="help.amount"
      >
        <a-input-number
          v-model="form.amount"
          :min="0.0"
          :defaultValue="0.0"
          :precision="2"
          :step="0.5"
          style="width:200px;"
        />
      </a-form-item>

      <a-form-item label="Enable" :required="true">
        <a-switch v-model="form.enable" checkedChildren="Enable" unCheckedChildren="Disable(禁用)"></a-switch>
      </a-form-item>

      <a-form-item >
        <template>
          <a-button key="back" @click="visible=false">Return</a-button>
          <a-button
            key="submit"
            type="primary"
            :loading="loading"
            :style="{ marginLeft: '8px'}"
            @click="isEdit ? updateForm() : createForm()"
          >Submit</a-button>
        </template>
      </a-form-item>
    </a-form>
  </a-card>
</template>

<script>
import { deleteCoupon, updateCoupon, createCoupon } from "@/api/coupon";
import { getProductList, getProduct } from "@/api/backend";
import { getUserList } from "@/api/manage";
import moment from "moment";
import debounce from "lodash/debounce";

export default {
  name: "CouponDetail",
  props: {
    isEdit: {
      type: Boolean,
      default: false
    }
  },
  data() {
    return {
      visible: false,
      loading: false,
      product: undefined,
      productOption: [],
      variantOption: [],
      customerOption: [],
      labelCol: {
        xs: { span: 24 },
        sm: { span: 5 }
      },
      wrapperCol: {
        xs: { span: 24 },
        sm: { span: 16 }
      },
      form: {
        couponID: undefined,
        enable: true,
        amount: 0.0,
        exp_date: moment(new Date(), "YYYY-MM-DD"),
        description: "",
        variant_id: undefined,
        customer_id: []
      },
      help: {
        couponID: "",
        enable: "",
        amount: "",
        exp_date: "",
        description: "",
        variant_id: "",
        customer_id: ""
      },
      loadingProduct: false,
      loadingCustomer: false
    };
  },
  mounted() {
    this.handleProductSearch = debounce(this.handleProductSearch, 1000);
  },
  methods: {
    handleCreate() {
      this.form = {
        couponID: undefined,
        enable: true,
        amount: 0.0,
        exp_date: moment(new Date(), "YYYY-MM-DD"),
        description: "",
        variant_id: undefined,
        customer_id: []
      };
      this.product = null;
      this.variant = null;
      this.visible = true;
      this.isEdit = false;
      this.getUserList();
    },
    handleEdit(data) {
      this.form = Object.assign({}, data);
      this.visible = true;
      this.isEdit = true;
      this.getUserList();
    },
    getUserList() {
      if (this.customerOption.length == 0) {
        getUserList().then(res => {
          const { result } = res;
          this.customerOption = result;
        });
      }
    },
    handleProductSearch(value) {
      this.loadingProduct = true;
      getProductList({ search: value })
        .then(res => {
          const { result } = res;
          this.productOption = result;
        })
        .finally(() => {
          this.loadingProduct = false;
        });
    },
    handleProductChange(value) {
      this.product = value;
      this.variant = null;
      this.variantOption = [];
      if (value) {
        getProduct(value).then(res => {
          const { result } = res;
          this.variantOption = result.variant;
        });
      }
    },
    handleVariantChange(value) {
      this.form.variant_id = value;
    },
    handleCustomerSearch(value) {
      this.loadingCustomer = true;
      getUserList({ search: value })
        .then(res => {
          const { result } = res;
          this.customerOption = result;
        })
        .finally(() => {
          this.loadingCustomer = false;
        });
    },
    handleCustomerChange(value) {
      Object.assign(this.form.customer_id, value);
    },
    updateForm() {},
    createForm() {
      var form = {
        enable: this.form.enable,
        amount: Number(this.form.amount),
        exp_date: this.form.exp_date.format("YYYY-MM-DD"),
        description: this.form.description,
        variant_id: this.form.variant_id,
        customer_id: this.form.customer_id
      };
      createCoupon(form).then(res => {});
    }
  }
};
</script>