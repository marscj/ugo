<template>
  <a-card :bordered="false" v-action:query>
    <div class="table-page-search-wrapper">
      <a-form layout="inline">
        <a-row :gutter="48">
          <a-col :md="8" :sm="16">
            <a-form-item label="Search">
              <a-input v-model="queryParam.search" placeholder="Title or Product ID" />
            </a-form-item>
          </a-col>
          <a-col :md="8" :sm="16">
            <a-form-item label="Category" >
              <a-select v-model="category">
                <a-select-option v-for="d in categoryData" :key="d.value">{{d.label}}</a-select-option>
              </a-select>
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
      <a-button v-action:add type="primary" icon="plus" @click="handleCreate">Add</a-button>

      <a-button v-if="selectedRowKeys.length > 0" v-action:edit type="default" icon="unlock" @click="handleCreate">Unlock</a-button>
      <a-button v-if="selectedRowKeys.length > 0" v-action:edit type="dashed" icon="lock" @click="handleCreate">Lock</a-button>
      <a-button v-if="selectedRowKeys.length > 0" v-action:delete type="danger" icon="delete" @click="handleCreate">Delete</a-button>
    </div>

    <s-table
      ref="table"
      size="default"
      :rowKey="(item) => item.id"
      :columns="columns"
      :data="loadData"
      :alert="options.alert"
      :rowSelection="options.rowSelection"
      bordered
    >
      <span slot="photo" slot-scope="data">
        <template>
          <img v-if="data.photo" :src="data.photo.image.thumbnail" alt='photo'>
        </template>
      </span>
      <span slot="action" slot-scope="text, data">
        <template>
          <router-link v-action:edit :to="{ name: 'ProductEdit', params: { id: data.id } }">Edit</router-link>
          <a-divider v-action:edit type="vertical" />
          <a v-action:delete @click="handleDelete(data)">Delete</a>
        </template>
      </span>
    </s-table>
  </a-card>
</template>

<script>
import { STable } from '@/components'
import { getProductList, deleteProduct } from '@/api/product'

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
  created: function () {
    this.debouncedGetAnswer = _.debounce(() => {this.$refs.table.refresh(true)}, 1000)
  },
  watch: {
    category: function (newQuestion, oldQuestion) {
      if (newQuestion == 0) {
        this.queryParam.category = undefined
      } else {
        this.queryParam.category = newQuestion
      }
      this.$refs.table.refresh(true)
    },
    'queryParam.status': function (newQuestion, oldQuestion) {
      this.$refs.table.refresh(true)
    },
    'queryParam.search': function (newQuestion, oldQuestion) {
      this.debouncedGetAnswer()
    },
  },
  data () {
    return {
      category: 0,
      categoryData,
      // 查询参数
      queryParam: {
        search: undefined,
        category: null,
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
          title: 'Product ID',
          dataIndex: 'productID',
          width: 120,
        },
        {
          title: 'Category',
          dataIndex: 'category',
          customRender: (text, index, row) => {
            return <span>{categoryData[text].label}</span>;
          }
        },
        {
          title: 'Title',
          dataIndex: 'title',
          width: 200,
        },
        {
          title: 'SubTitle',
          dataIndex: 'subtitle',
        },
        {
          title: 'Location',
          dataIndex: 'location',
        },
        {
          title: 'Sort ID',
          dataIndex: 'sort_by',
          width: 100
        },
        {
          title: 'Photo',
          width: 200,
          scopedSlots: { customRender: 'photo' }
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
          width: '120px',
          scopedSlots: { customRender: 'action' }
        }
      ],
      loadData: parameter => {
        return getProductList(Object.assign(parameter, this.queryParam))
          .then(res => {
            return res.result
          })
      },
      selectedRowKeys: [],
      selectedRows: [],
      options: {
        alert: { show: true, clear: () => { this.selectedRowKeys = [] } },
        rowSelection: {
          selectedRowKeys: this.selectedRowKeys,
          onChange: this.onSelectChange
        }
      }
    }
  },
  methods: {
    handleCreate (data) {
      this.$router.push({
        name: 'ProductCreate'
      })
    },
    handleDelete(data) {
      var _this = this
      this.$confirm({
        title: 'alert',
        content: `Are you sure delete ${data.title}?`,
        okText: 'delete',
        okType: 'danger',
        cancelText: 'cancle',
        onOk () {
          return deleteProduct(data.id).then((res) => {
            _this.$refs.table.refresh(true);
          })
        },
      })
    },
    onSelectChange (selectedRowKeys, selectedRows) {
      this.selectedRowKeys = selectedRowKeys
      this.selectedRows = selectedRows
    },
  }
}
</script>
