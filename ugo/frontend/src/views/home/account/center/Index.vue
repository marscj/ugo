<template>
  <div class="page-header-index-wide page-header-wrapper-grid-content-main">
    <a-row :gutter="24">
      <a-col :md="24" :lg="7">
        <a-card :bordered="true"> 
          <a-form :form="form" layout="vertical" >
            <a-form-item label="用户名:" :labelCol="labelCol" :wrapperCol="wrapperCol" style="margin:0px; padding:0px">{{ form.username }}</a-form-item>
            <a-form-item label="额度:" :labelCol="labelCol" :wrapperCol="wrapperCol" style="margin:0px; padding:0px">{{ form.balance }} $</a-form-item>
          </a-form>
        </a-card>
      </a-col>
      <a-col :md="24" :lg="17">
        <a-card
          style="width:100%"
          :bordered="true"
        >
         <order-list> </order-list>
        </a-card>
      </a-col>
    </a-row>
  </div>
</template>

<script>
import { OrderList } from "./page/list";
export default {
  components: {
    OrderList,
  },
  data() {
    return {
      labelCol: { lg: { span: 5 }, sm: { span: 5 } },
      wrapperCol: { lg: { span: 19 }, sm: { span: 19 } },

      form: Object.assign({}, this.$store.getters.userInfo),
    };
  },
  mounted() {},
  methods: {
  }
};
</script>

<style lang="less" scoped>
.page-header-wrapper-grid-content-main {
  width: 100%;
  height: 100%;
  min-height: 100%;
  transition: 0.3s;

  .account-center-avatarHolder {
    text-align: center;

    .username {
      display: inline-block;
      // color: rgba(0, 0, 0, 0.85);
      font-size: 16px;
      // line-height: 28px;
      font-weight: 500;
      // margin-bottom: 4px;
    }
  }

  .account-center-detail {
    p {
      margin-bottom: 8px;
      padding-left: 26px;
      position: relative;
    }

    i {
      position: absolute;
      height: 14px;
      width: 14px;
      left: 0;
      top: 4px;
    }

    .title {
      background-position: 0 0;
    }
    .group {
      background-position: 0 -22px;
    }
    .address {
      background-position: 0 -44px;
    }
  }
}
</style>
