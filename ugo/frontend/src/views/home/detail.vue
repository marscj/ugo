<template>
  <a-card>
    <a-col style="width:524px;min-height:400px;" justify="start">
      <a-carousel arrows autoplay dotsClass="slick-dots slick-thumb">
        <a slot="customPaging" slot-scope="props">
          <img :src="getImgUrl(props.i)" />
        </a>
        <div v-for="item in data.gallery" :key="item.id">
          <img :src="item.image.gallery_square_crop" />
        </div>
      </a-carousel>
    </a-col>
  </a-card>
</template>

<script>
import { getProduct } from '@/api/product'

export default {
  props:{},
  data() {
    return {
      spinning: false,
      data: {
        gallery: []
      },
    }
  },
  mounted() {
    const id = this.$route.params && this.$route.params.id
    this.fetch(id)
  },
  methods: {
    getImgUrl(i) {
      if(this.data && this.data.gallery) {
        return this.data.gallery[i].image.gallery_square_crop
      }
      return ''
    },
    fetch(id) {
      this.spinning = true
      getProduct(id).then((res) => {
        const { result } = res
        this.data = result
        this.description = result.description
        this.$route.meta.title = result.name
        this.$parent.getPageMeta()
        this.extraImage = result.photo.image.medium_square_crop
      }).finally(() => {
        this.spinning = false
      })
    },
  },
}
</script>

<style scoped>

.ant-carousel >>> .slick-dots {
  height: auto
}
.ant-carousel >>> .slick-slide img{
    display: block;
    margin: auto;
    max-width: 100%;
}

.ant-carousel >>> .slick-thumb {
  bottom: -45px;
}
.ant-carousel >>> .slick-thumb li {
  width: 60px;
  height: 45px;
}
.ant-carousel >>> .slick-thumb li img {
  width: 100%;
  height: 100%;
  filter: grayscale(100%);
}
.ant-carousel >>> .slick-thumb li.slick-active img{
    filter: grayscale(0%);
}

.box {
  display: inline-block;
  width: 100px;
  height: 100px;
  background: red;
  color: white;
}

#two {
  position: relative;
  top: 20px;
  left: 20px;
  background: blue;
}
</style>