<template>
  <a-card
    style="width:100%"
    :tabList="tabListNoTitle"
    :activeTabKey="noTitleKey"
    @tabChange="key => onTabChange(key, 'noTitleKey')"
  >
    <order-list v-if="noTitleKey === '1'" />
    <order-list v-if="noTitleKey === '2'" />
    <order-list v-if="noTitleKey === '3'" />
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
          key: "1",
          tab: "待处理"
        },
        {
          key: "2",
          tab: "已确认"
        },
        {
          key: "3",
          tab: "出票完成"
        },
        {
          key: "4",
          tab: "已取消"
        }
      ],
      key: "1",
      noTitleKey: "1"
    };
  },
  methods: {
    onTabChange (key, type) {
      this[type] = key
    },
  }
};
</script>