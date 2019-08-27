<template>
  <div>
    <a-form :form="form" style="max-width: 500px; margin: 40px auto 0;">
      <a-form-item
        label="主产品名称"
        :labelCol="labelCol"
        :wrapperCol="wrapperCol"
        :required="true"
      >{{ form.product }}</a-form-item>
      <a-form-item
        label="子产品名称"
        :labelCol="labelCol"
        :wrapperCol="wrapperCol"
        :required="true"
      >{{ form.variant }}</a-form-item>
      <a-form-item
        label="日期"
        :labelCol="labelCol"
        :wrapperCol="wrapperCol"
        :required="true"
      >{{ form.day }}</a-form-item>
      <a-form-item
        label="时间"
        :labelCol="labelCol"
        :wrapperCol="wrapperCol"
        :required="true"
      >{{ form.time }}</a-form-item>
      <a-form-item
        label="成人数量"
        :labelCol="labelCol"
        :wrapperCol="wrapperCol"
        :required="true"
        v-if="form.adult_quantity > 0"
      >{{ form.adult_quantity }}</a-form-item>
      <a-form-item
        label="成人金额"
        :labelCol="labelCol"
        :wrapperCol="wrapperCol"
        :required="true"
        v-if="form.adult_quantity > 0"
      >{{ form.adult_price }} $</a-form-item>
      <a-form-item
        label="儿童数量"
        :labelCol="labelCol"
        :wrapperCol="wrapperCol"
        :required="true"
        v-if="form.child_quantity > 0"
      >{{ form.child_quantity }}</a-form-item>
      <a-form-item
        label="儿童金额"
        :labelCol="labelCol"
        :wrapperCol="wrapperCol"
        :required="true"
        v-if="form.child_quantity > 0"
      >{{ form.child_price }} $</a-form-item>
      <a-form-item
        label="总金额"
        :labelCol="labelCol"
        :wrapperCol="wrapperCol"
        :required="true"
      >{{ form.total }} $</a-form-item>
      <a-form-item
        label="联系人信息"
        :labelCol="labelCol"
        :wrapperCol="wrapperCol"
      >{{ form.guest_info }}</a-form-item>
      <a-form-item
        label="联系方式"
        :labelCol="labelCol"
        :wrapperCol="wrapperCol"
      >{{ form.guest_contact }}</a-form-item>
      <a-form-item label="客户备注" :labelCol="labelCol" :wrapperCol="wrapperCol">{{ form.guest_remark }}</a-form-item>
      <a-form-item :wrapperCol="{span: 19, offset: 5}">
        <a-button :loading="loading" type="primary" @click="nextStep">提交</a-button>
        <a-button style="margin-left: 8px" @click="prevStep">上一步</a-button>
      </a-form-item>
    </a-form>
  </div>
</template>

<script>
import { createOrder } from "@/api/order";
import { checkError } from "@/views/utils/error";
export default {
  name: "Step2",
  props: {
    form: Object,
    default: {}
  },
  data() {
    return {
      labelCol: { lg: { span: 5 }, sm: { span: 5 } },
      wrapperCol: { lg: { span: 19 }, sm: { span: 19 } },
      loading: false,
      timer: 0
    };
  },
  methods: {
    nextStep() {
      this.loading = true;
      console.log(this.form, '-------')
      createOrder(this.form)
        .then(res => {
          const { result } = res;
          this.$emit("nextStep");
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
        "customer",
        "adult_quantity",
        "child_quantity",
        "variant"
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
    prevStep() {
      this.$emit("prevStep");
    }
  },
  beforeDestroy() {
    clearTimeout(this.timer);
  }
};
</script>

<style lang="less" scoped>
.stepFormText {
  margin-bottom: 24px;

  .ant-form-item-label,
  .ant-form-item-control {
    line-height: 22px;
  }
}
</style>
