<template>
  <a-card :bordered="false" v-action:query>
    <div class="table-page-search-wrapper">
      <a-form layout="inline">
        <a-row :gutter="48">
          <a-col :md="8" :sm="16">
            <a-form-item label="Product">
              <a-input v-model="queryParam.search" />
            </a-form-item>
          </a-col>
        </a-row>
      </a-form>
    </div>

    <div class="table-operator">
      <a-button v-action:add type="primary" icon="plus" @click="handleCreate">Add</a-button>
    </div>

    <s-table
      ref="table"
      size="default"
      :rowKey="(item) => item.id"
      :columns="columns"
      :data="loadData"
      bordered
    >
      <span slot="product" slot-scope="text">
        <template>
          <span>{{text}}</span>
        </template>
      </span>

      <span slot="variant" slot-scope="text">
        <template>
          <span>{{text}}</span>
        </template>
      </span>

      <span slot="status" slot-scope="text">
        <a-checkbox :checked="text" disabled />
      </span>

      <span slot="exp_date" slot-scope="text">
        <span>{{text | moment('YYYY-MM-DD')}}</span>
      </span>

      <span slot="action" slot-scope="text, data">
        <a v-action:edit @click="handleEdit(data)">Edit</a>
      </span>
    </s-table>
  </a-card>
</template>

<script>
import { getCouponList } from "@/api/coupon";

import { getProductList, getProduct } from "@/api/backend";
import { getUserList } from "@/api/manage";

import { STable } from "@/components";

export default {
  name: "CouponList",
  components: {
    STable
  },
  data() {
    return {
      queryParam: {},
      columns: [
        {
          title: "Product",
          dataIndex: "variant.product",
          scopedSlots: { customRender: "product" },
        },
        {
          title: "Variant",
          dataIndex: "variant.name",
          scopedSlots: { customRender: "variant" },
        },
        {
          title: "Description",
          dataIndex: "description",
        },
        {
          title: "Amount",
          dataIndex: "amount",
          width: '100px',
        },
        {
          title: "Status",
          dataIndex: "enable",
          scopedSlots: { customRender: "status" },
          width: '100px',
        },
        {
          title: "ExpDate",
          dataIndex: "exp_date",
          scopedSlots: { customRender: "exp_date" },
          width: '120px',
        },
        {
          title: "Action",
          dataIndex: "action",
          width: '10%',
          scopedSlots: { customRender: "action" }
        }
      ],
      formModal: {
        
      },
      loadData: parameter => {
        return getCouponList(Object.assign(parameter, this.queryParam)).then(
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
        name: "CouponCreate"
      });
    },
  }
};
</script>