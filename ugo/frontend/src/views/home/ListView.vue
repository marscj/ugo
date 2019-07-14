<template>
  <div >
    <div slot="pageMenu" style="margin-bottom:25px;">
      <div class="page-menu-search">
        <a-input-search
          style="width: 80%; max-width: 522px;"
          placeholder="请输入..."
          size="large"
          enterButton="搜索"
        />
      </div>
    </div>
    <a-list
      :grid="{gutter: 24, lg: 2, md: 2, sm: 1, xs: 1}"
      :dataSource="data"
      :loading="loading"
    >
      <a-list-item slot="renderItem" slot-scope="item" style="margin-bottom:20px;">
        <template >
          <a-card 
          :hoverable="true" 
          style="width: 80%"
          :bordered="false"
          >
            <img
              :alt="item.title"
              :src="item.photo.image.large_square_crop"
              style="height: 400px"
              slot="cover"
              v-if="item.photo"
            />
            <a-divider></a-divider>
            <a-card-meta :title="item.title">
              <div style="margin-bottom:5px; height:45px" slot="description">{{ item.title }}</div>
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
      type: Array,
      default: false
    }
  },
}
</script>
