<template>
  <div>
    <a-form :form="form" style="max-width: 500px; margin: 40px auto 0;">
      <a-form-item label="主产品名称" :labelCol="labelCol" :wrapperCol="wrapperCol" :required="true">
        <a-input v-model="form.product" disabled />
      </a-form-item>
      <a-form-item label="子产品名称" :labelCol="labelCol" :wrapperCol="wrapperCol" :required="true">
        <a-input v-model="form.variant" disabled />
      </a-form-item>
      <a-form-item label="日期" :labelCol="labelCol" :wrapperCol="wrapperCol" :required="true">
        <a-input v-model="form.day" disabled />
      </a-form-item>
      <a-form-item label="时间" :labelCol="labelCol" :wrapperCol="wrapperCol" :required="true">
        <a-input v-model="form.time" disabled />
      </a-form-item>
      <a-form-item
        label="成人数量"
        :labelCol="labelCol"
        :wrapperCol="wrapperCol"
        :required="true"
        v-if="form.adult_quantity > 0"
      >
        <a-input v-model="form.adult_quantity" disabled />
      </a-form-item>
      <a-form-item
        label="成人金额"
        :labelCol="labelCol"
        :wrapperCol="wrapperCol"
        :required="true"
        v-if="form.adult_quantity > 0"
      >
        <a-input suffix="$" v-model="form.adult_price" disabled />
      </a-form-item>
      <a-form-item
        label="儿童数量"
        :labelCol="labelCol"
        :wrapperCol="wrapperCol"
        :required="true"
        v-if="form.child_quantity > 0"
      >
        <a-input v-model="form.child_quantity" disabled />
      </a-form-item>
      <a-form-item
        label="儿童金额"
        :labelCol="labelCol"
        :wrapperCol="wrapperCol"
        :required="true"
        v-if="form.child_quantity > 0"
      >
        <a-input suffix="$" v-model="form.child_price" disabled />
      </a-form-item>
      <a-form-item label="优惠金额" :labelCol="labelCol" :wrapperCol="wrapperCol" :required="true">
        <a-spin :spinning="spinning">
          <a-input suffix="$" v-model="form.offer" disabled />
        </a-spin>
      </a-form-item>
      <a-form-item label="总金额" :labelCol="labelCol" :wrapperCol="wrapperCol" :required="true">
        <a-spin :spinning="spinning">
          <a-input suffix="$" v-model="form.total" disabled />
        </a-spin>
      </a-form-item>
      <a-form-item label="优惠券序列号" :labelCol="labelCol" :wrapperCol="wrapperCol">
        <a-input v-model="form.couponID" @change="handleCoupon" />
      </a-form-item>
      <a-form-item label="UGO关联单号" :labelCol="labelCol" :wrapperCol="wrapperCol">
        <a-input v-model="form.relatedID" />
      </a-form-item>
      <a-form-item label="客户关联单号" :labelCol="labelCol" :wrapperCol="wrapperCol">
        <a-input v-model="form.guest_relatedID" />
      </a-form-item>
      <a-form-item label="联系人信息" :labelCol="labelCol" :wrapperCol="wrapperCol">
        <a-textarea v-model="form.guest_info" />
      </a-form-item>
      <a-form-item label="联系方式" :labelCol="labelCol" :wrapperCol="wrapperCol">
        <a-textarea v-model="form.guest_contact" />
      </a-form-item>
      <a-form-item label="客户备注" :labelCol="labelCol" :wrapperCol="wrapperCol">
        <a-textarea v-model="form.guest_remark" />
      </a-form-item>
      <a-form-item :wrapperCol="{span: 19, offset: 5}">
        <a-button type="primary" :loading="loading" @click="handleBook(true)">下一步</a-button>
      </a-form-item>
    </a-form>
    <a-divider />
  </div>
</template>

<script>
import { checkout } from "@/api/order";
import { checkError } from "@/views/utils/error";
import debounce from "lodash/debounce";

export default {
  name: "Step1",
  props: {
    form: {
      type: Object,
      default: {}
    },
    result: {
      type: Object,
      default: {}
    }
  },
  data() {
    this.handleCoupon = debounce(this.handleCoupon, 1200);
    return {
      labelCol: { lg: { span: 5 }, sm: { span: 5 } },
      wrapperCol: { lg: { span: 19 }, sm: { span: 19 } },
      loading: false,
      spinning: false
    };
  },
  methods: {
    handleBook(value) {
      this.spinning = true;
      checkout({
        day: this.form.day,
        time: this.form.time,
        adult_quantity: this.form.adult_quantity,
        child_quantity: this.form.child_quantity,
        variantID: this.form.variantID,
        relatedID: this.form.relatedID,
        couponID: this.form.couponID
      })
        .then(res => {
          const { result } = res;
          Object.assign(this.form, result);
          if (value) {
            this.$emit("nextStep");
          }
        })
        .catch(error => {
          this.checkError(error);
          if (error && error.response) {
            if (error.response.status == 401) {
              // this.$router.push({name: 'UserLogin'})
            }
          }
        })
        .finally(() => {
          this.spinning = false;
        });
    },
    checkError(error) {
      var errors = checkError(
        error,
        "customer",
        "adult_quantity",
        "child_quantity",
        "variant",
        "relatedID",
        "couponID"
      );

      for (var key in errors) {
        if (errors[key]) {
          this.$notification["error"]({
            message: errors[key],
            duration: 4
          });
        }
      }
    },
    handleCoupon(value) {
      this.handleBook(false);
    },
    nextStep() {
      this.$emit("nextStep");
    }
  }
};
</script>
