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
            <a-form-item label="Category">
              <a-select v-model="category">
                <a-select-option v-for="d in categoryData" :key="d.value">{{d.label}}</a-select-option>
              </a-select>
            </a-form-item>
          </a-col>
          <a-col :md="8" :sm="16">
            <a-form-item label="Status">
              <a-select v-model="status">
                <a-select-option v-for="d in statusData" :key="d.value">{{d.label}}</a-select-option>
              </a-select>
            </a-form-item>
          </a-col>
        </a-row>
      </a-form>
    </div>

    <div class="table-operator">
      <a-button v-action:add type="primary" icon="plus" @click="handleCreate">Add</a-button>

      <a-button
        v-if="selectedRowKeys.length > 0"
        v-action:edit
        type="default"
        icon="unlock"
        @click="listProductEnable(true)"
      >上架</a-button>
      <a-button
        v-if="selectedRowKeys.length > 0"
        v-action:edit
        type="default"
        icon="lock"
        @click="listProductEnable(false)"
      >下架</a-button>
      <a-button
        v-if="selectedRowKeys.length > 0"
        v-action:delete
        type="danger"
        icon="delete"
        @click="listProductDelete"
      >删除</a-button>
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
          <img v-if="data.photo" :src="data.photo.image.thumbnail" alt="photo" />
        </template>
      </span>
      <span slot="action" slot-scope="text, data">
        <template>
          <router-link v-action:edit :to="{ name: 'ProductEdit', params: { id: data.id } }">Edit</router-link>
          <a-divider v-action:edit type="vertical" />
        </template>
        <a-dropdown v-if="$auth('Product.edit')|| $auth('Product.delete')">
          <a class="ant-dropdown-link">More</a>
          <a-menu slot="overlay">
            <a-menu-item>
              <a v-action:edit @click="updateProduct(data, true)">上架</a>
              <a v-action:edit @click="updateProduct(data, false)">下架</a>
              <a v-action:delete @click="handleDelete(data)">删除</a>
            </a-menu-item>
          </a-menu>
        </a-dropdown>
      </span>
    </s-table>
  </a-card>
</template>

<script>
import { STable } from "@/components";
import {
  getProductList,
  deleteProduct,
  listProductDelete,
  listProductEnable,
  updateProduct
} from "@/api/product";

const categoryData = [
  { value: 0, label: "全部" },
  { value: 1, label: "美食" },
  { value: 2, label: "门票" },
  { value: 3, label: "日游" },
  { value: 4, label: "用车" },
  { value: 5, label: "酒店" },
  { value: 6, label: "伴手礼" }
];

const statusData = [
  { value: 0, label: "全部" },
  { value: 1, label: "上架" },
  { value: 2, label: "下架" }
];

export default {
  name: "ProductList",
  components: {
    STable
  },
  created: function() {
    this.debouncedGetAnswer = _.debounce(() => {
      this.$refs.table.refresh(true);
    }, 1000);
  },
  watch: {
    category: function(newQuestion, oldQuestion) {
      if (newQuestion == 0) {
        this.queryParam.category = undefined;
      } else {
        this.queryParam.category = newQuestion;
      }
      this.$refs.table.refresh(true);
    },
    status: function(newQuestion, oldQuestion) {
      if (newQuestion == 0) {
        this.queryParam.status = undefined;
      } else {
        this.queryParam.status = newQuestion == 1;
      }
      this.$refs.table.refresh(true);
    },
    "queryParam.search": function(newQuestion, oldQuestion) {
      this.debouncedGetAnswer();
    },
    selectedRowKeys: function(_new, _old) {
      this.ids = _new.join(",");
    }
  },
  data() {
    return {
      category: 0,
      status: 0,
      categoryData,
      statusData,
      queryParam: {
        search: undefined,
        category: null,
        status: null
      },
      columns: [
        {
          title: "#",
          dataIndex: "id",
          width: 40
        },
        {
          title: "Product ID",
          dataIndex: "productID",
          width: 120
        },
        {
          title: "Category",
          dataIndex: "category",
          customRender: (text, index, row) => {
            return <span>{categoryData[text].label}</span>;
          }
        },
        {
          title: "Title",
          dataIndex: "title",
          width: 200
        },
        {
          title: "SubTitle",
          dataIndex: "subtitle"
        },
        {
          title: "Location",
          dataIndex: "location"
        },
        {
          title: "Photo",
          width: 100,
          scopedSlots: { customRender: "photo" }
        },
        {
          title: "Status",
          dataIndex: "status",
          width: "80px",
          customRender: (text, row, index) => {
            if (text) {
              return <span>上架</span>;
            } else {
              return <span>下架</span>;
            }
          }
        },
        {
          title: "操作",
          dataIndex: "action",
          width: "140px",
          scopedSlots: { customRender: "action" }
        }
      ],
      loadData: parameter => {
        return getProductList(Object.assign(parameter, this.queryParam)).then(
          res => {
            return res.result;
          }
        );
      },
      selectedRowKeys: [],
      selectedRows: [],
      options: {
        alert: {
          show: false,
          clear: () => {
            this.selectedRowKeys = [];
          }
        },
        rowSelection: {
          selectedRowKeys: this.selectedRowKeys,
          onChange: this.onSelectChange
        }
      },
      ids: null
    };
  },
  methods: {
    handleCreate(data) {
      this.$router.push({
        name: "ProductCreate"
      });
    },
    handleDelete(data) {
      var _this = this;

      _this.$confirm({
        title: "alert",
        content: `Are you sure delete ${data.title}?`,
        okText: "delete",
        okType: "danger",
        cancelText: "cancle",
        onOk() {
          _this.$refs.table.localLoading = true;
          return deleteProduct(data.id)
            .then(res => {
              _this.onClear();
              _this.$refs.table.refresh(true);
            })
            .finally(() => {
              _this.$refs.table.localLoading = false;
            });
        }
      });
    },
    onSelectChange(selectedRowKeys, selectedRows) {
      this.selectedRowKeys = selectedRowKeys;
      this.selectedRows = selectedRows;
    },
    onClear() {
      this.options.alert.clear();
      this.$refs.table.clearSelected();
    },
    listProductDelete() {
      var _this = this;

      _this.$confirm({
        title: "alert",
        content: `Are you sure delete?`,
        okText: "delete",
        okType: "danger",
        cancelText: "cancle",
        onOk() {
          _this.$refs.table.localLoading = true;
          listProductDelete({ ids: _this.ids })
            .then(res => {
              _this.onClear();
              return _this.$refs.table.refresh(true);
            })
            .finally(() => {
              _this.$refs.table.localLoading = false;
            });
        }
      });
    },
    listProductEnable(enable) {
      this.$refs.table.localLoading = true;
      listProductEnable({ ids: this.ids, enable: enable ? 1 : 0 })
        .then(res => {
          this.onClear();
          return this.$refs.table.refresh(true);
        })
        .finally(() => {
          this.$refs.table.localLoading = false;
        });
    },
    updateProduct(data, enable) {
      var _data = Object.assign({}, data, { status: enable });
      this.$refs.table.localLoading = true;
      updateProduct(data.id, _data)
        .then(res => {
          this.onClear();
          return this.$refs.table.refresh(true);
        })
        .finally(() => {
          this.$refs.table.localLoading = false;
        });
    }
  }
};
</script>
