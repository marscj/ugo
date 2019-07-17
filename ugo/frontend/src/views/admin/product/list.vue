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
            <a-form-item label="Category" >
              <a-select v-model="queryParam.category">
                <a-select-option v-for="d in categoryData" :key="d.value">{{d.label}}</a-select-option>
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
import { STable } from '@/components'
import { getProductList } from '@/api/product'

const categoryData = [
  { value: 0, label: '全部' },
  { value: 1, label: '美食' },
  { value: 2, label: '门票' },
  { value: 3, label: '日游' },
  { value: 4, label: '用车' },
  { value: 5, label: '酒店' },
  { value: 6, label: '伴手礼' },
]

export default {
  name: 'ProductList',
  components: {
    STable
  },
  data () {
    return {
      categoryData,
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
          dataIndex: 'category',
          customRender: (text, index, row) => {
            return <span href="javascript:;">{categoryData[text].label}</span>;
          }
        },
        {
          title: 'Name',
          dataIndex: 'name',
          width: 140,
        },
        {
          title: 'Description',
          dataIndex: 'description',
          width: 200,
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
        return getProductList(Object.assign(parameter, this.queryParam))
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
