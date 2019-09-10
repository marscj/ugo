<template>
  <page-view :title="`单号：` + form.orderID">
    <div>
      <a-card :bordered="false" title="订单详情">
        <template slot="extra">
          <a-button-group>
            <a-button>确认</a-button>
            <a-button>取消</a-button>
            <a-button>备注</a-button>
          </a-button-group>
        </template>

        <a-steps
          style="margin: 24px 0px 40px 0px;"
          :direction="isMobile() && 'vertical' || 'horizontal'"
          :current="form.orderStatus"
        >
          <a-step title="新建" />
          <a-step title="订单已确认,正在出票中" />
          <a-step title="出票完成" />
        </a-steps>

        <detail-list :col="4">
          <detail-list-item term="创建人">{{form.customer}}</detail-list-item>
          <detail-list-item term="执行时间">{{form.time}}</detail-list-item>
          <detail-list-item term="主产品">{{form.product}}</detail-list-item>
          <detail-list-item term="成人数量">{{form.adult_quantity}}</detail-list-item>
          <detail-list-item term="创建时间">{{form.create_at | moment()}}</detail-list-item>
          <detail-list-item term="执行日期">{{form.day}}</detail-list-item>
          <detail-list-item term="子产品">{{form.variant}}</detail-list-item>
          <detail-list-item term="儿童数量">{{form.child_quantity}}</detail-list-item>
        </detail-list>

        <detail-list :col="2" class="detail-layout">
          <detail-list-item term="客户信息">{{form.guest_info}}</detail-list-item>
          <detail-list-item term="联系方式">{{form.guest_contact}}</detail-list-item>
        </detail-list>

        <detail-list :col="2" class="detail-layout">
          <detail-list-item term="客户备注">{{form.guest_remark}}</detail-list-item>
          <detail-list-item term="订单备注">{{form.guest_remark}}</detail-list-item>
        </detail-list>
        <detail-list :col="1" class="detail-layout">
          <detail-list-item term="操作">{{form.operator}}</detail-list-item>
        </detail-list>
      </a-card>

      <a-card title="预定详情">
        <template slot="extra">
          <a-button-group>
            <a-button>添加预定</a-button>
            <a-button>出票完成</a-button>
          </a-button-group>
        </template>
      </a-card>
    </div>

    <a-modal visible="" title="订单备注">
      <a-form>
        <a-form-item>
          <a-textarea v-model="form.remark" :autosize="{minRows: 5}"></a-textarea>
        </a-form-item>
      </a-form>
    </a-modal>

  </page-view>
</template>

<script>
import { mixinDevice } from "@/utils/mixin";
import { PageView } from "@/layouts";
import DetailList from "@/components/tools/DetailList";
import { checkError } from "@/views/utils/error";
import { getOrder, updateOrder, createOrder } from "@/api/order";

const DetailListItem = DetailList.Item;

const orderStatus = [
  { value: 0, label: "新建" },
  { value: 1, label: "订单已确认" },
  { value: 2, label: "出票成功" },
  { value: 3, label: "出票失败" },
  { value: 4, label: "订单已取消" }
];

const payStatus = [
  { value: 0, label: "未支付" },
  { value: 1, label: "部分支付" },
  { value: 2, label: "全部付清" },
  { value: 3, label: "部分退款" },
  { value: 4, label: "全部退款" }
];

export default {
  name: "OrderDetail",
  props: {
    isEdit: {
      type: Boolean,
      default: false
    }
  },
  components: {
    PageView,
    DetailList,
    DetailListItem
  },
  mixins: [mixinDevice],
  data() {
    return {
      orderStatus,
      payStatus,
      form: {
        order_status: 0,
        pay_status: 0,
        adult_quantity: undefined,
        adult_price: undefined,
        child_quantity: undefined,
        child_price: undefined
      },
      help: {},
      spinning: false
    };
  },
  created() {
    if (this.isEdit) {
      const id = this.$route.params && this.$route.params.id;
      this.fetch(id);
    }
  },
  methods: {
    fetch(id) {
      this.spinning = true;
      getOrder(id)
        .then(res => {
          const { result } = res;
          this.form = result;
        })
        .finally(() => {
          this.spinning = false;
        });
    }
  }
};
</script>

<style lang="less" scoped>
.detail-layout {
  margin-left: 0px;
}
.text {
  color: rgba(0, 0, 0, 0.45);
}

.heading {
  color: rgba(0, 0, 0, 0.85);
  font-size: 20px;
}

.no-data {
  color: rgba(0, 0, 0, 0.25);
  text-align: center;
  line-height: 64px;
  font-size: 16px;

  i {
    font-size: 24px;
    margin-right: 16px;
    position: relative;
    top: 3px;
  }
}

.mobile {
  .detail-layout {
    margin-left: unset;
  }
  .text {
    text-align: right;
  }
  .status-list {
    text-align: right;
  }
}
</style>