<template >
  <a-card :loading="loading">
    <a-form :form="form">
      <a-form-item label="CouponID">
        <a-input v-model="form.couponID" disabled />
      </a-form-item>

      <a-form-item label="Product">
        <a-select
          :showSearch="true"
          :showArrow="false"
          :value="product_id"
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

      <a-form-item
        label="Customer"
        :validate-status="help.customer_id == null || help.customer_id === '' ?  null : 'error'"
        :help="help.customer_id"
      >
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

      <a-form-item label="Enable">
        <a-switch v-model="form.enable" checkedChildren="Enable" unCheckedChildren="Disable(禁用)"></a-switch>
      </a-form-item>

      <a-form-item>
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
import {
  deleteCoupon,
  updateCoupon,
  createCoupon,
  getCoupon
} from "@/api/coupon";
import { getProductList, getProduct } from "@/api/backend";
import { getUserList } from "@/api/manage";
import { checkError } from "@/views/utils/error";

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
      product_id: undefined,
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
        id: undefined,
        couponID: undefined,
        enable: true,
        amount: 0.0,
        exp_date: moment(new Date(), "YYYY-MM-DD"),
        description: "",
        variant_id: undefined,
        customer_id: []
      },
      help: {
        variant_id: "",
        customer_id: "",
        exp_date: "",
        amount: ""
      },
      loadingProduct: false,
      loadingCustomer: false
    };
  },
  mounted() {
    this.handleProductSearch = debounce(this.handleProductSearch, 1000);
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
      this.loading = true;
      getCoupon(id)
        .then(res => {
          const { result } = res;
          Object.assign(this.form, result, {
            exp_date: moment(new Date(result.exp_date), "YYYY-MM-DD"),
            customer_id: result.customer.map(f => f.id)
          });
          this.customerOption = result.customer;
          return getProduct(result.variant.product_id);
        })
        .then(res => {
          const { result } = res;
          this.productOption = [result];
          this.variantOption = result.variant;
          this.product_id = result.id;
        })
        .finally(() => {
          this.loading = false;
        });
    },
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
    },
    handleEdit(data) {
      this.form = Object.assign({}, data);
      this.visible = true;
      this.isEdit = true;
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
      this.product_id = value;
      this.form.variant_id = null;
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
      this.form.customer_id = value
    },
    updateForm() {
      var form = {
        enable: this.form.enable,
        amount: Number(this.form.amount),
        exp_date: this.form.exp_date
          ? this.form.exp_date.format("YYYY-MM-DD")
          : undefined,
        description: this.form.description,
        variant_id: this.form.variant_id,
        customer_id: this.form.customer_id
      };
      this.loading = true;
      updateCoupon(this.form.id, form)
        .then(res => {
          this.handleGoBack();
        })
        .catch(error => {
          this.checkError(error);
        })
        .finally(() => {
          this.loading = false;
        });
    },
    createForm() {
      var form = {
        enable: this.form.enable,
        amount: Number(this.form.amount),
        exp_date: this.form.exp_date
          ? this.form.exp_date.format("YYYY-MM-DD")
          : undefined,
        description: this.form.description,
        variant_id: this.form.variant_id,
        customer_id: this.form.customer_id
      };
      this.loading = true;
      createCoupon(form)
        .then(res => {
          this.handleGoBack();
        })
        .catch(error => {
          this.checkError(error);
        })
        .finally(() => {
          this.loading = false;
        });
    },
    checkError(error) {
      var errors = checkError(
        error,
        "variant_id",
        "customer_id",
        "exp_date",
        "amount"
      );
      this.help.variant_id = errors["variant_id"];
      this.help.customer_id = errors["customer_id"];
      this.help.exp_date = errors["exp_date"];
      this.help.amount = errors["amount"];

      for (var key in errors) {
        if (errors[key]) {
          this.$notification["error"]({
            message: key,
            description: errors[key],
            duration: 4
          });
        }
      }
    }
  }
};
</script>