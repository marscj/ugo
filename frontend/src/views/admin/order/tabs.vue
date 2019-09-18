<template>
  <a-card
    style="width:100%"
    :tabList="tabListNoTitle"
    :activeTabKey="noTitleKey"
    @tabChange="key => onTabChange(key, 'noTitleKey')"
  >
    <order-list v-if="noTitleKey === 'index1'" />
    <order-list v-if="noTitleKey === 'index2'" />
    <order-list v-if="noTitleKey === 'index3'" />
    <order-list v-if="noTitleKey === 'index4'" />
  </a-card>
</template>

<script>
import OrderList from "./list";

export default {
  name: "OrderTabs",
  components: { OrderList },
  data() {
    return {
      tabListNoTitle: [
        {
          key: "index1",
          tab: "待处理"
        },
        {
          key: "index2",
          tab: "已确认"
        },
        {
          key: "index3",
          tab: "出票完成"
        },
        {
          key: "index4",
          tab: "已取消"
        }
      ],
      noTitleKey: "index1"
    };
  },
  methods: {
    onTabChange(key, type) {
      this[type] = key;
    }
  }
};
</script>