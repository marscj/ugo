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
      <a-button type="primary" icon="plus" @click="handleCreate">New</a-button>
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
          <img v-if="data.photo" :src="data.photo.image.thumbnail" alt='photo'>
        </template>
      </span>
      <span slot="action" slot-scope="text, data">
        <template>
          <router-link :to="{ name: 'ProductEdit', params: { id: data.id } }">Edit</router-link>
        </template>
      </span>
    </s-table>
  </a-card>
</template>

<script>
import moment from 'moment'
import { STable } from '@/components'
import { getVariantList } from '@/api/product'

export default {
  name: 'VariantList',
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
          width: 40,
        },
        {
          title: 'Product ID',
          dataIndex: 'productID',
          width: 120,
        },
        {
          title: 'Category',
          dataIndex: 'category.name',
        },
        {
          title: 'Title',
          dataIndex: 'title',
        },
        {
          title: 'Location',
          dataIndex: 'location',
        },
        {
          title: 'Photo',
          width: 200,
          scopedSlots: { customRender: 'photo' }
        },
        {
          title: '操作',
          dataIndex: 'action',
          width: '150px',
          scopedSlots: { customRender: 'action' }
        }
      ],
      loadData: parameter => {
        return getVariantList(Object.assign(parameter, this.queryParam))
          .then(res => {
            return res.result
          })
      },
    }
  },
  methods: {
    handleCreate (data) {
      this.$router.push({
        name: 'ProductCreate'
      })
    }
  }
}
</script>
