<template>
  <div>
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
        <a-input suffix="$" v-model="form.total" disabled/>
      </a-form-item>
      <a-form-item
        label="联系人信息"
        :labelCol="labelCol"
        :wrapperCol="wrapperCol"
      >
        <a-textarea v-model="form.guest_info"/>
      </a-form-item>
      <a-form-item
        label="联系方式"
        :labelCol="labelCol"
        :wrapperCol="wrapperCol"
      >
        <a-textarea v-model="form.guest_contact"/>
      </a-form-item>
      <a-form-item
        label="备注"
        :labelCol="labelCol"
        :wrapperCol="wrapperCol"
      >
        <a-textarea v-model="form.remark"/>
      </a-form-item>
      <a-form-item :wrapperCol="{span: 19, offset: 5}">
        <a-button type="primary" @click="nextStep">下一步</a-button>
      </a-form-item>
    </a-form>
    <a-divider />
  </div>
</template>

<script>
export default {
  name: 'Step1',
  props: {
    form: Object,
    default: {}
  },
  data () {
    return {
      labelCol: { lg: { span: 5 }, sm: { span: 5 } },
      wrapperCol: { lg: { span: 19 }, sm: { span: 19 } },
    }
  },
  methods: {
    nextStep () {
      this.$emit('nextStep')
    }
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
