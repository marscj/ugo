<template>
  <div>
    <a-form :form="form" style="max-width: 500px; margin: 40px auto 0;">
      <a-form-item
        label="主产品名称"
        :labelCol="labelCol"
        :wrapperCol="wrapperCol"
        :required="true"
        class="stepFormText"
      ><span class="bold">{{ form.product }}</span></a-form-item>
      <a-form-item
        label="子产品名称"
        :labelCol="labelCol"
        :wrapperCol="wrapperCol"
        :required="true"
        class="stepFormText"
      ><span class="bold">{{ form.variant }}</span></a-form-item>
      <a-form-item
        label="日期"
        :labelCol="labelCol"
        :wrapperCol="wrapperCol"
        :required="true"
        class="stepFormText"
      ><span class="bold">{{ form.day }}</span></a-form-item>
      <a-form-item
        label="时间"
        :labelCol="labelCol"
        :wrapperCol="wrapperCol"
        :required="true"
        class="stepFormText"
      ><span class="bold">{{ form.time }}</span></a-form-item>
      <a-form-item
        label="成人数量"
        :labelCol="labelCol"
        :wrapperCol="wrapperCol"
        :required="true"
        class="stepFormText"
        v-if="form.adult_quantity > 0"
      ><span class="bold">{{ form.adult_quantity }}</span></a-form-item>
      <a-form-item
        label="成人金额"
        :labelCol="labelCol"
        :wrapperCol="wrapperCol"
        :required="true"
        class="stepFormText"
        v-if="form.adult_quantity > 0"
      ><span class="bold">{{ form.adult_price }} $</span></a-form-item>
      <a-form-item
        label="儿童数量"
        :labelCol="labelCol"
        :wrapperCol="wrapperCol"
        :required="true"
        class="stepFormText"
        v-if="form.child_quantity > 0"
      ><span class="bold">{{ form.child_quantity }}</span></a-form-item>
      <a-form-item
        label="儿童金额"
        :labelCol="labelCol"
        :wrapperCol="wrapperCol"
        :required="true"
        class="stepFormText"
        v-if="form.child_quantity > 0"
      ><span class="bold">{{ form.child_price }} $</span></a-form-item>
      <a-form-item
        label="优惠金额"
        :labelCol="labelCol"
        :wrapperCol="wrapperCol"
        :required="true"
        class="stepFormText"
      ><span class="bold">{{ form.offer }} $</span></a-form-item>
      <a-form-item
        label="总金额"
        :labelCol="labelCol"
        :wrapperCol="wrapperCol"
        :required="true"
        class="stepFormText"
      ><span class="bold">{{ form.total }} $</span></a-form-item>
      <a-form-item
        label="UGO关联单号"
        :labelCol="labelCol"
        :wrapperCol="wrapperCol"
        class="stepFormText"
      ><span class="bold">{{ form.relatedID }}</span></a-form-item>
      <a-form-item
        label="客户关联单号"
        :labelCol="labelCol"
        :wrapperCol="wrapperCol"
        class="stepFormText"
      ><span class="bold">{{ form.guest_relatedID }}</span></a-form-item>
      <a-form-item
        label="联系人信息"
        :labelCol="labelCol"
        :wrapperCol="wrapperCol"
        class="stepFormText"
      ><span class="bold">{{ form.guest_info }}</span></a-form-item>
      <a-form-item
        label="联系方式"
        :labelCol="labelCol"
        :wrapperCol="wrapperCol"
        class="stepFormText"
      ><span class="bold">{{ form.guest_contact }}</span></a-form-item>
      <a-form-item
        label="客户备注"
        :labelCol="labelCol"
        :wrapperCol="wrapperCol"
        class="stepFormText"
      ><span class="bold">{{ form.guest_remark }}</span></a-form-item>
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
      createOrder(this.form)
        .then(res => {
          const { result } = res;
          this.result.data = result;
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
        "variant",
        "relatedID"
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
  margin-bottom: 0px;

  .ant-form-item-label,
  .ant-form-item-control {
    line-height: 22px;
  }
}

.bold {
  font-weight:bold;
}

.money {
  font-family: "Helvetica Neue", sans-serif;
  font-weight: 500;
  font-size: 20px;
  line-height: 14px;
}
</style>
