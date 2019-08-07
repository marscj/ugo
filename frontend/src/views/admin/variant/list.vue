<template>
  <a-card :bordered="false" v-action:query>
    <div class="table-page-search-wrapper">
      <a-form layout="inline">
        <a-row :gutter="48">
          <a-col :md="8" :sm="16">
            <a-form-item label="Search">
              <a-input v-model="queryParam.search" placeholder="Name, Product, VariantID, SKU" />
            </a-form-item>
          </a-col>
          <a-col :md="8" :sm="16">
            <a-form-item label="Status" >
              <a-checkbox :checked="queryParam.status" @change="queryParam.status=!queryParam.status">上架</a-checkbox>
            </a-form-item>
          </a-col>
        </a-row>
      </a-form>
    </div>

    <div class="table-operator">
      <a-button v-action:add type="primary" icon="plus" @click="handleCreate">New</a-button>
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
        <div v-action:edit>
          <router-link :to="{ name: 'VariantEdit', params: { id: data.id } }">Edit</router-link>
        </div>
      </span>
    </s-table>
  </a-card>
</template>

<script>
import { STable } from '@/components'
import { getVariantList } from '@/api/variant'

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
  name: 'VariantList',
  components: {
    STable
  },
  created: function () {
    this.debouncedGetAnswer = _.debounce(() => {this.$refs.table.refresh(true)}, 1000)
  },
  watch: {
    'queryParam.status': function (newQuestion, oldQuestion) {
      this.$refs.table.refresh(true)
    },
    'queryParam.search': function (newQuestion, oldQuestion) {
      this.debouncedGetAnswer()
    },
  },
  data () {
    return {
      categoryData,
      queryParam: {
        search: undefined,
        status: true,
      },
      // 表头
      columns: [
        {
          title: '#',
          dataIndex: 'id',
          width: 40,
        },
        {
          title: 'Name',
          dataIndex: 'name'
        },
        {
          title: 'Product',
          dataIndex: 'product',
        },
        
        {
          title: 'Category',
          dataIndex: 'category',
          customRender: (text, index, row) => {
            return <span>{categoryData[text].label}</span>;
          }
        },
        {
          title: 'VariantID',
          dataIndex: 'variantID'
        },
        {
          title: 'SKU',
          dataIndex: 'sku'
        },
        {
          title: 'Status',
          dataIndex: 'status',
          width: '80px',
          customRender: (text, row, index) => {
            if(text) {
              return <span>上架</span>; 
            } else {
              return <span>下架</span>;
            }
          }
        },
        {
          title: '操作',
          dataIndex: 'action',
          width: '80px',
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
        name: 'VariantCreate'
      })
    }
  }
}
</script>