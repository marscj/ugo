<template>
  <div >
    <div >
      <a-list
        :grid="{gutter: 24, lg: 2, md: 1, sm: 1, xs: 1}"
        :dataSource="data"
        :loading="loading"
      >
        <a-list-item slot="renderItem" slot-scope="item">
          <template >
          <a-card :hoverable="true" style="width: 240px">
            <img
              :alt="item.title"
              :src="item.photo.image.medium_square_crop"
              slot="cover"
              v-if="item.photo"
            />
            <a-card-meta>
              <div style="margin-bottom: 3px" slot="title">{{ item.title }}</div>
            </a-card-meta>
          </a-card>
          </template>
        </a-list-item>
      </a-list>
    </div>
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
