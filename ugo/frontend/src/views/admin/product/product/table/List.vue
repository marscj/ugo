<template>
  <div>
    <div class="table-page-search-wrapper">
      <a-form layout="inline">
        <a-row :gutter="48">
          <a-col :md="8" :sm="16">
            <a-form-item label="Search">
              <a-input v-model="queryParam.search" placeholder="Name or ID" />
            </a-form-item>
          </a-col>
          <a-col :md="8" :sm="16">
            <a-form-item label="Category">
              <a-select v-model="queryParam.category" placeholder="请选择" default-value="0">
                <a-select-option value="0">全部</a-select-option>
                <a-select-option value="1">关闭</a-select-option>
                <a-select-option value="2">运行中</a-select-option>
              </a-select>
            </a-form-item>
          </a-col>
        </a-row>
      </a-form>
    </div>

    <div class="table-operator">
      <a-button type="primary" icon="plus" @click="handleEdit()">新建</a-button>
    </div>

    <s-table
      ref="table"
      size="default"
      rowKey="key"
      :columns="columns"
      :data="loadData"
    >
      <span slot="serial" slot-scope="text, record, index">
        {{ index + 1 }}
      </span>
      <span slot="action" slot-scope="text, record">
        <template>
          <a @click="handleEdit(record)">Edit</a>
          <a-divider type="vertical" />
        </template>
      </span>
    </s-table>
  </div>
</template>

<script>
import moment from 'moment'
import { STable } from '@/components'
import { getProductList } from '@/api/product'

export default {
  name: 'TableList',
  components: {
    STable
  },
  data () {
    return {
      mdl: {},
      // 查询参数
      queryParam: {},
      // 表头
      columns: [
        {
          title: '#',
          scopedSlots: { customRender: 'id' }
        },
        {
          title: 'Product ID',
          dataIndex: 'productID'
        },
        {
          title: 'description',
          dataIndex: 'description'
        },
        {
          title: 'photo',
          dataIndex: 'image'
        },
        {
          title: '操作',
          dataIndex: 'action',
          width: '150px',
          scopedSlots: { customRender: 'action' }
        }
      ],
      loadData: parameter => {
        return getProductList(Object.assign(parameter, this.queryParam))
          .then(res => {
            return res.result
          })
      },
    }
  },
  created () {

  },
  methods: {

    handleEdit (record) {
      this.$emit('onEdit', record)
    },
    handleOk () {

    },
  }
}
</script>
