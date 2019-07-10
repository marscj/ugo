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
      :rowKey="(item) => item.id"
      :columns="columns"
      :data="loadData"
      bordered
    >
      <span slot="photo" slot-scope="data">
        <template>
          <img v-if="data.image != null && data.image.length > 0" :src="data.image.find((f) => {
            return f.flag === 'icon'
          }).image.thumbnail" alt='photo'>
        </template>
      </span>
      <span slot="action" slot-scope="text, data">
        <template>
          <a @click="handleEdit(data)">Edit</a>
        </template>
      </span>
    </s-table>
  </div>
</template>

<script>
import { STable } from '@/components'
import { getSourceList } from '@/api/source'

export default {
  name: 'SourceList',
  components: {
    STable
  },
  data () {
    return {
      // 查询参数
      queryParam: {},
      // 表头
      columns: [
        {
          title: '#',
          dataIndex: 'id',
          width: 80
        },
        {
          title: 'Title',
          dataIndex: 'productID',
          width: 120
        },
        {
          title: 'Description',
          width: 120,
          dataIndex: 'description'
        },
        {
          title: 'description',
          dataIndex: 'description'
        },
        {
          title: '操作',
          dataIndex: 'action',
          width: '150px',
          scopedSlots: { customRender: 'action' }
        }
      ],
      loadData: parameter => {
        return getSourceList(Object.assign(parameter, this.queryParam))
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
