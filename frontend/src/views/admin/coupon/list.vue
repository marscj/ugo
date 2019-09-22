<template>
  <a-card :bordered="false" v-action:query>
    <div class="table-page-search-wrapper">
      <a-form layout="inline">
        <a-row :gutter="48">
          <a-col :md="8" :sm="16">
            <a-form-item label="Product">
              <a-input v-model="queryParam.search" />
            </a-form-item>
          </a-col>
        </a-row>
      </a-form>
    </div>

    <div class="table-operator">
      <a-button v-action:add type="primary" icon="plus" @click="handleCreate">Add</a-button>
    </div>

    <s-table
      ref="table"
      size="default"
      :rowKey="(item) => item.id"
      :columns="columns"
      :data="loadData"
      bordered
    >
      <span slot="product" slot-scope="text, data">
        <template>
          <span>{{data['variant.product.title']}} - {{data['variant.name']}}</span>
        </template>
      </span>

      <span slot="action" slot-scope="text, data">
        <a v-action:edit @click="handleEdit(data)">Edit</a>
      </span>
    </s-table>

    <a-modal v-model="formModal.visible">
      <a-form :form="formModal.data">
        <a-form-item
          :labelCol="formModal.labelCol"
          :wrapperCol="formModal.wrapperCol"
          label="CouponID"
          validateStatus="success"
        >
          <a-input v-model="formModal.data.id" disabled />
        </a-form-item>

        <a-form-item
          :labelCol="formModal.labelCol"
          :wrapperCol="formModal.wrapperCol"
          label="Product"
        >
          <a-select
            showSearch
            :value="formModal.product"
            :defaultActiveFirstOption="false"
            :showArrow="false"
            :filterOption="false"
            allowClear
            @search="handleProductSearch"
            @change="handleProductChange"
            notFoundContent="Not Found."
            style="width:200px;"
          >
            <a-select-option
              v-for="d in formModal.productOption"
              :key="d.id"
              :value="d.id"
            >{{d.title}}</a-select-option>
          </a-select>
        </a-form-item>

        <a-form-item
          :labelCol="formModal.labelCol"
          :wrapperCol="formModal.wrapperCol"
          label="Variant"
          :validate-status="formModal.help.variant_id == null || formModal.help.variant_id === '' ?  null : 'error'"
          :help="formModal.help.variant_id"
          v-if="formModal.variantOption.length > 0"
        >
          <a-select
            :value="formModal.variant"
            allowClear
            @change="handleVariantChange"
            :notFoundContent="null"
            style="width:200px;"
          >
            <a-select-option
              v-for="d in formModal.variantOption"
              :key="d.id"
              :value="d.id"
            >{{d.name}}</a-select-option>
          </a-select>
        </a-form-item>

        <a-form-item
          :labelCol="formModal.labelCol"
          :wrapperCol="formModal.wrapperCol"
          label="Exp Date"
          :required="true"
          :validate-status="formModal.help.exp_date == null || formModal.help.exp_date === '' ?  null : 'error'"
          :help="formModal.help.exp_date"
        >
          <a-date-picker v-model="formModal.data.exp_date" />
        </a-form-item>

        <a-form-item
          :labelCol="formModal.labelCol"
          :wrapperCol="formModal.wrapperCol"
          label="Amount"
          :required="true"
          :validate-status="formModal.help.amount == null || formModal.help.amount === '' ?  null : 'error'"
          :help="formModal.help.amount"
        >
          <a-input-number
            v-model="formModal.data.amount"
            :min="0.0"
            :defaultValue="0.0"
            :precision="2"
            :step="0.5"
            style="width:200px;"
          />
        </a-form-item>

        <a-form-item
          :labelCol="formModal.labelCol"
          :wrapperCol="formModal.wrapperCol"
          label="Enable"
          :required="true"
        >
          <a-switch
            v-model="formModal.data.enable"
            checkedChildren="Enable"
            unCheckedChildren="Disable(禁用)"
          ></a-switch>
        </a-form-item>

        <template slot="footer">
          <a-button key="back" @click="visible=false">Return</a-button>
          <a-button
            key="submit"
            type="primary"
            :loading="formModal.loading"
            @click="formModal.isEdit ? updateForm() : createForm()"
          >Submit</a-button>
        </template>
      </a-form>
    </a-modal>
  </a-card>
</template>

<script>
import {
  getCouponList,
  deleteCoupon,
  updateCoupon,
  createCoupon
} from "@/api/coupon";

import { getProductList, getProduct } from "@/api/backend";

import { STable } from "@/components";

import moment from "moment";

let timeout;

export default {
  name: "CouponList",
  components: {
    STable
  },
  created: function() {
    this.debouncedGetAnswer = _.debounce(() => {
      console.log("abc");
    }, 1000);
  },
  data() {
    return {
      queryParam: {},
      columns: [
        {
          title: "Product",
          scopedSlots: { customRender: "product" },
          width: 120
        },
        {
          title: "Action",
          dataIndex: "action",
          width: "140px",
          scopedSlots: { customRender: "action" }
        }
      ],
      formModal: {
        visible: false,
        loading: false,
        isEdit: false,
        product: undefined,
        variant: undefined,
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
        data: {
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
        }
      },
      loadData: parameter => {
        return getCouponList(Object.assign(parameter, this.queryParam)).then(
          res => {
            return res.result;
          }
        );
      }
    };
  },
  methods: {
    handleCreate() {
      this.formModal.data = {
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
      this.formModal.visible = true;
      this.formModal.isEdit = false;
    },
    handleEdit(data) {
      this.formModal.data = Object.assign({}, data);
      this.formModal.visible = true;
      this.formModal.isEdit = true;
    },
    handleProductSearch(value) {
      var _this = this;

      if (timeout) {
        clearTimeout(timeout);
        timeout = null;
      }

      function fake(callback) {
        getProductList({ search: value }).then(res => {
          const { result } = res;
          _this.formModal.productOption = result;
        });
      }

      timeout = setTimeout(fake, 1000);
    },
    handleProductChange(value) {
      this.formModal.product = value;
      this.formModal.variant = null;
      this.formModal.variantOption = [];
      if (value) {
        getProduct(value).then(res => {
          const { result } = res;
          this.formModal.variantOption = result.variant;
        });
      }
    },
    handleVariantChange(value) {
      this.formModal.variant = value;
    },
    updateForm() {

    },
    createForm() {

    }
  }
};
</script>