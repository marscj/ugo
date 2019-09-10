<template>
  <page-view v-if="form.orderID" :title="`单号：` + form.orderID">
    <div>
      <a-card title="订单详情">
        <template slot="extra">
          <a-button-group>
            <a-button v-if="form.order_status == 0" @click="changeOrderStatus(1)">确认</a-button>
            <a-button v-if="form.order_status <= 1" @click="changeOrderStatus(3)">取消</a-button>
            <a-button v-if="form.order_status == 1" @click="changeOrderStatus(2)">完成</a-button>
            <a-button v-if="form.order_status == 3" @click="changeOrderStatus(4)">申请退款</a-button>
            <a-button v-if="form.order_status == 4" @click="changeOrderStatus(5)">审核通过</a-button>
            <a-button @click="remarkModal.handle">备注</a-button>
          </a-button-group>
        </template>

        <a-steps
          v-if="form.order_status < 3"
          style="margin: 24px 0px 40px 0px;"
          direction="horizontal"
          :current="form.order_status"
        >
          <a-step title="新建" />
          <a-step title="订单已确认,正在出票中" />
          <a-step title="出票完成" />
        </a-steps>
        <a-steps
          v-else
          style="margin: 24px 0px 40px 0px;"
          direction="horizontal"
          :current="form.order_status - 3"
        >
          <a-step title="订单已取消" />
          <a-step title="退款中" />
          <a-step title="已退款" />
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

        <detail-list :col="1" class="detail-layout">
          <detail-list-item term="客户备注">{{form.guest_remark}}</detail-list-item>
        </detail-list>
        <detail-list :col="1" class="detail-layout">
          <detail-list-item term="订单备注">{{form.remark}}</detail-list-item>
        </detail-list>
        <detail-list :col="1" class="detail-layout">
          <detail-list-item term="操作">{{form.operator}}</detail-list-item>
        </detail-list>

        <template>
          <div class="status-list" >
            <div class="text">成人</div>
            <div class="heading">{{form.adult_price}} $</div>
          </div>
          <div class="status-list">
            <div class="text">儿童</div>
            <div class="heading">{{form.child_price}} $</div>
          </div>
        </template>
      </a-card>

      <a-card title="预定详情">
        <template slot="extra">
          <a-button-group>
            <a-dropdown>
              <a-menu slot="overlay" @click="handleMenuClick">
                <a-menu-item v-for="data in categoryData" :key="data.value">
                  <icon-font :type="data.type" />
                  {{data.label}}
                </a-menu-item>
              </a-menu>
              <a-button style="margin-left: 8px">
                添加
                <a-icon type="down" />
              </a-button>
            </a-dropdown>
          </a-button-group>
        </template>
      </a-card>
    </div>

    <a-modal v-model="remarkModal.visible" title="订单备注">
      <a-form>
        <a-form-item>
          <a-textarea v-model="remarkModal.remark" :autosize="{minRows: 5}"></a-textarea>
        </a-form-item>
      </a-form>
      <template slot="footer">
        <a-button key="back" @click="remarkModal.visible=false">Return</a-button>
        <a-button
          key="submit"
          type="primary"
          :loading="remarkModal.loading"
          @click="remarkModal.submit"
        >Submit</a-button>
      </template>
    </a-modal>
  </page-view>
</template>

<script>
import { Icon } from "ant-design-vue";
import { mixinDevice } from "@/utils/mixin";
import { PageView } from "@/layouts";
import DetailList from "@/components/tools/DetailList";
import { checkError } from "@/views/utils/error";
import { getOrder, updateOrder, createOrder } from "@/api/order";

const DetailListItem = DetailList.Item;

const IconFont = Icon.createFromIconfontCN({
  scriptUrl: "//at.alicdn.com/t/font_1402881_gsh78a0lnya.js"
});

const orderStatus = [
  { value: 0, label: "新建" },
  { value: 1, label: "订单已确认" },
  { value: 2, label: "出票成功" },
  { value: 3, label: "订单已取消" },
  { value: 4, label: "退款中" },
  { value: 5, label: "已退款" }
];

const payStatus = [
  { value: 0, label: "未支付" },
  { value: 1, label: "部分支付" },
  { value: 2, label: "全部付清" },
  { value: 3, label: "部分退款" },
  { value: 4, label: "全部退款" }
];

const categoryData = [
  { value: 1, label: "美食", type: "iconf-30" },
  { value: 2, label: "门票", type: "iconticket" },
  { value: 3, label: "日游", type: "iconlvyou" },
  { value: 4, label: "用车", type: "iconche" },
  { value: 5, label: "酒店", type: "iconhotel" },
  { value: 6, label: "伴手礼", type: "iconliwu1" }
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
    DetailListItem,
    IconFont
  },
  mixins: [mixinDevice],
  data() {
    return {
      orderStatus,
      payStatus,
      categoryData,
      form: {
        order_status: 0,
        pay_status: 0,
        adult_quantity: undefined,
        adult_price: undefined,
        child_quantity: undefined,
        child_price: undefined
      },
      remarkModal: {
        visible: false,
        loading: false,
        remark: "",
        handle: () => {
          this.remarkModal.visible = true;
          this.remarkModal.loading = false;
          this.remarkModal.remark = this.form.remark;
        },
        submit: () => {
          this.remarkModal.loading = true;
          updateOrder(
            this.form.id,
            Object.assign({}, this.form, { remark: this.remarkModal.remark })
          )
            .then(res => {
              const { result } = res;
              this.form = result;
              this.remarkModal.visible = false;
            })
            .finally(() => {
              this.remarkModal.loading = false;
            });
        }
      },
      help: {},
      spinning: false
    };
  },
  mounted() {
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
    },
    changeOrderStatus(status) {
      this.spinning = true;
      updateOrder(
        this.form.id,
        Object.assign({}, this.form, { order_status: status })
      )
        .then(res => {
          const { result } = res;
          this.form = result;
        })
        .finally(() => {
          this.spinning = false;
        });
    },
    handleMenuClick(e) {}
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

.status-list {
  text-align: right;
  float: right;
  width: 160px;
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

.icons-list .anticon {
  margin-right: 6px;
  font-size: 24px;
}
</style>