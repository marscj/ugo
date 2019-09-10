<template>
  <div>
    <a-back-top />
    <div style="margin-bottom:25px;">
      <div class="page-menu-search">
        <a-input-search
          style="width: 80%; max-width: 522px;"
          placeholder="请输入..."
          size="large"
          enterButton="搜索"
          v-model="search"
          @search="handleSearch"
        />
      </div>
    </div>
    <a-list
      :grid="{gutter: 24, lg: 3, md: 3, sm: 2, xs: 1}"
      :dataSource="data.data"
      :loading="loading"
      :pagination="pagination"
      size="large"
    >
      <a-list-item
        slot="renderItem"
        slot-scope="item"
        style="margin-bottom:20px;"
        key="item.id"
        @click="handleClick(item)"
      >
        <template>
          <a-card :hoverable="true" style="width: 100%" :bordered="false">
            <img
              :alt="item.name"
              :src="item.photo.image.large_square_crop"
              slot="cover"
              v-if="item.photo"
            />
            <a-divider></a-divider>
            <a-card-meta :title="item.title">
              <div style="margin-bottom:5px; height:45px" slot="description">{{ item.subtitle }}</div>
            </a-card-meta>
          </a-card>
        </template>
      </a-list-item>
    </a-list>
  </div>
</template>

<script>
export default {
  props: {
    loading: {
      type: Boolean,
      default: false
    },
    data: {
      type: Object,
      default: null
    }
  },
  mounted() {
    this.$emit("onFetch", this.search, this.pagination);
  },
  watch: {
    data: function(newValue, old) {
      if (newValue) {
        this.pagination.total = newValue.totalCount
      }
    }
  },
  data() {
    return {
      pagination: {
        onChange: (page) => {
          this.pagination.pageNo = page
          window.scrollTo(0,0);
          this.$emit("onFetch", this.search, this.pagination);
        },
        pageNo: 1,
        pageSize: 12
      },
      search: null,
    };
  },
  methods: {
    handleClick(row) {
      this.$emit("onClick", row);
    },
    handleSearch(value) {
      this.pagination.pageNo = 1
      this.$emit("onSearch", value, this.pagination);
    }
  }
};
</script>
