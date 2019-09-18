<template>
  <a-spin :spinning="loading" >
    <a-form style="margin: 40px auto 0;">
      <result title="操作成功" :is-success="true" style="max-width: 560px;">
        <div class="information">
          <a-form-item
          label="主产品名称"
          :labelCol="labelCol"
          :wrapperCol="wrapperCol"
        >
          <span class="bold">{{ result.data.product }} - {{result.data.variant}}</span>
        </a-form-item>
        <a-form-item
          label="订单号"
          :labelCol="labelCol"
          :wrapperCol="wrapperCol"
        >{{ result.data.orderID }}</a-form-item>
        <a-form-item
          label="关联单号"
          :labelCol="labelCol"
          :wrapperCol="wrapperCol"
          v-if="result.data.relatedID"
        >{{ result.data.relatedID }}</a-form-item>
        <a-form-item
          label="总金额"
          :labelCol="labelCol"
          :wrapperCol="wrapperCol"
        >{{ result.data.total }} $</a-form-item>
        <a-form-item
          label="账户余额"
          :labelCol="labelCol"
          :wrapperCol="wrapperCol"
        >{{ userInfo.balance }} $</a-form-item>
        </div>
        <div slot="action">
          <a-button type="primary" @click="finish">返回首页</a-button>
          <a-button style="margin-left: 8px" @click="toOrderList">查看订单</a-button>
        </div>
      </result>
    </a-form>
  </a-spin>
</template>

<script>
import { Result } from "@/components";
import { getInfo } from '@/api/login'

export default {
  name: "Step3",
  components: {
    Result
  },
  props: {
    result: {
      type: Object,
      default: {}
    }
  },
  mounted() {
    this.loading = true
    this.$store.dispatch('GetInfo').then((res) => {
      const { result } = res;
      this.userInfo = result
    }).finally(() => {
      this.loading = false
    })
  },
  data() {
    return {
      labelCol: { lg: { span: 5 }, sm: { span: 5 } },
      wrapperCol: { lg: { span: 19 }, sm: { span: 19 } },
      userInfo: {},
      loading: false
    };
  },
  methods: {
    finish() {
      this.$emit("finish");
    },
    toOrderList() {
      this.$router.push({ name: "UserAccount" });
    }
  }
};
</script>
<style lang="less" scoped>
.information {
  line-height: 22px;

  .ant-row:not(:last-child) {
    margin-bottom: 0px;
  }
}
</style>
