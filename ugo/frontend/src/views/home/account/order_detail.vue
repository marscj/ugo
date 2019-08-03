<template>
  <a-card title="订单详情">
    <a-form :form="form" style="max-width: 500px; margin: 40px auto 0;">
      <a-form-item
        label="主产品名称"
        :labelCol="labelCol"
        :wrapperCol="wrapperCol"
        :required="true"
      >
        <a-input v-model="form.product" disabled/>
      </a-form-item>
      <a-form-item
        label="子产品名称"
        :labelCol="labelCol"
        :wrapperCol="wrapperCol"
        :required="true"
      >
        <a-input v-model="form.variant" disabled/>
      </a-form-item>
      <a-form-item
        label="日期"
        :labelCol="labelCol"
        :wrapperCol="wrapperCol"
        :required="true"
      >
        <a-input v-model="form.day" disabled />
      </a-form-item>
      <a-form-item
        label="时间"
        :labelCol="labelCol"
        :wrapperCol="wrapperCol"
        :required="true"
      >
        <a-input v-model="form.time" disabled />
      </a-form-item>
      <a-form-item
        label="成人数量"
        :labelCol="labelCol"
        :wrapperCol="wrapperCol"
        :required="true"
        v-if="form.adult_quantity > 0"
      >
        <a-input v-model="form.adult_quantity" disabled/>
      </a-form-item>
      <a-form-item
        label="成人金额"
        :labelCol="labelCol"
        :wrapperCol="wrapperCol"
        :required="true"
        v-if="form.adult_quantity > 0"
      >
        <a-input suffix="$" v-model="form.adult_price" disabled/>
      </a-form-item>
      <a-form-item
        label="儿童数量"
        :labelCol="labelCol"
        :wrapperCol="wrapperCol"
        :required="true"
        v-if="form.child_quantity > 0"
      >
        <a-input v-model="form.child_quantity" disabled/>
      </a-form-item>
      <a-form-item
        label="儿童金额"
        :labelCol="labelCol"
        :wrapperCol="wrapperCol"
        :required="true"
        v-if="form.child_quantity > 0"
      >
        <a-input suffix="$" v-model="form.child_price" disabled/>
      </a-form-item>
      <a-form-item
        label="总金额"
        :labelCol="labelCol"
        :wrapperCol="wrapperCol"
        :required="true"
      >
        <a-input suffix="$" v-model="form.total_price" disabled/>
      </a-form-item>
      <a-form-item
        label="联系人信息"
        :labelCol="labelCol"
        :wrapperCol="wrapperCol"
      >
        <a-textarea v-model="form.customer_info"/>
      </a-form-item>
      <a-form-item
        label="联系方式"
        :labelCol="labelCol"
        :wrapperCol="wrapperCol"
      >
        <a-textarea v-model="form.customer_contact"/>
      </a-form-item>
      <a-form-item
        label="备注"
        :labelCol="labelCol"
        :wrapperCol="wrapperCol"
      >
        <a-textarea v-model="form.remark"/>
      </a-form-item>
      <a-form-item :wrapperCol="{span: 19, offset: 5}">
        <a-button type="primary" @click="submit">提交</a-button>
        <a-button style="margin-left: 8px" @click="back">返回</a-button>
      </a-form-item>
    </a-form>
  </a-card>
</template>

<script>
import { updateOrder } from "@/api/order";
import { checkError } from "@/views/utils/error";
export default {
  name: 'OrderDetail',
  data () {
    return {
      form: this.$route.query,
      labelCol: { lg: { span: 5 }, sm: { span: 5 } },
      wrapperCol: { lg: { span: 19 }, sm: { span: 19 } },
    }
  },
  methods: {
    submit() {
      this.loading = true;
      updateOrder(this.form.id, this.form)
        .then(res => {
          const { result } = res;
          this.$router.go(-1)
        })
        .catch(error => {
          this.checkError(error);
        })
        .finally(() => {
          this.loading = false;
        });
    },
    back() {
      this.$router.go(-1)
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
  }
}
</script>

<style lang="less" scoped>
.step-form-style-desc {
  padding: 0 56px;
  color: rgba(0,0,0,.45);

  h3 {
    margin: 0 0 12px;
    color: rgba(0,0,0,.45);
    font-size: 16px;
    line-height: 32px;
  }

  h4 {
    margin: 0 0 4px;
    color: rgba(0,0,0,.45);
    font-size: 14px;
    line-height: 22px;
  }

  p {
    margin-top: 0;
    margin-bottom: 12px;
    line-height: 22px;
  }
}
</style>
