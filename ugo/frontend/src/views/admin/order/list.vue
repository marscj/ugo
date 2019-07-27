<template>
  <a-card :bordered="false">
    <div class="table-page-search-wrapper">
      <a-form layout="inline">
        <a-row :gutter="48">
          <a-col :md="8" :sm="16">
            <a-form-item label="Search">
              <a-input v-model="queryParam.search" placeholder="Name or ID" />
            </a-form-item>
          </a-col>
        </a-row>
      </a-form>
    </div>

    <s-table
      ref="table"
      size="default"
      :rowKey="(item) => item.id"
      :columns="columns"
      :data="loadData"
      bordered
      :scroll="{ x: 2800}"
    >
      <span slot="create_at" slot-scope="text">
        <template>
          <span>{{text | moment('YYYY-MM-DD HH:mm')}}</span>
        </template>
      </span>
      <span slot="action" slot-scope="text, data">
        <template>
          <router-link :to="{ name: 'OrderEdit', params: { id: data.id } }">Edit</router-link>
        </template>
      </span>
    </s-table>
  </a-card>
</template>

<script>
import { STable } from "@/components";
import { getOrderList } from "@/api/order";

export default {
  name: "VariantList",
  components: {
    STable
  },
  data() {
    return {
      // 查询参数
      queryParam: {},
      // 表头
      columns: [
        {
          key: "#",
          title: "#",
          dataIndex: "id",
          fixed: 'left',
          width: 100
        },
        {
          key: "1",
          title: "OrderID",
          dataIndex: "orderID",
          fixed: 'left',
          width: 150
        },
        {
          key: "2",
          title: "ConfirmID",
          dataIndex: "confirmID",
          width: 150
        },
        {
          key: "3",
          title: "Status",
          dataIndex: "status",
          width: 150,
          customRender: (text, row, index) => {
            switch (text) {
              case 0:
                return <span>新建</span>;
              case 1:
                return <span>订单已确认</span>;
              case 2:
                return <span>等待</span>;
              case 3:
                return <span>订单已取消</span>;
            }
          }
        },
        {
          key: "4",
          title: "Day",
          dataIndex: "day",
          width: 150
        },
        {
          key: "5",
          title: "Time",
          dataIndex: "time",
          width: 150
        },
        {
          key: "6",
          title: "Customer Info",
          dataIndex: "customer_info",
          width: 150
        },
        {
          key: "7",
          title: "Customer Contact",
          dataIndex: "customer_contact",
          width: 150
        },
        {
          key: "8",
          title: "Adult Quantity",
          dataIndex: "adult_quantity",
          width: 150
        },
        {
          key: "9",
          title: "Adult Price",
          dataIndex: "adult_price",
          width: 150
        },
        {
          key: "10",
          title: "Child Quantity",
          dataIndex: "child_quantity",
          width: 150
        },
        {
          key: "11",
          title: "Child Price",
          dataIndex: "child_price",
          width: 150
        },
        {
          key: "12",
          title: "Remark",
          dataIndex: "remark",
          width: 150
        },
        {
          key: "13",
          title: "Variant",
          dataIndex: "variant",
          width: 250
        },
        {
          key: "14",
          title: "Customer",
          dataIndex: "customer",
          width: 150
        },
        {
          key: "15",
          title: "Operator",
          dataIndex: "operator",
          width: 150
        },
        {
          key: "16",
          title: "Create at",
          dataIndex: "create_at",
          scopedSlots: { customRender: 'create_at' },
          width: 250
        },
        {
          key: "action",
          title: "操作",
          dataIndex: "action",
          scopedSlots: { customRender: "action" },
          width: 100,
          fixed: 'right'
        }
      ],
      loadData: parameter => {
        return getOrderList(Object.assign(parameter, this.queryParam)).then(
          res => {
            return res.result;
          }
        );
      }
    };
  },
  methods: {
    handleCreate(data) {
      this.$router.push({
        name: "VariantCreate"
      });
    }
  }
};
</script>
