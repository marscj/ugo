<template>
  <div>
    <div class="detail_main_wrap basefix" style="height: 845px">
      <div class="detail_media_left">
        <div class="attraction_photo_wrap">
          <a-carousel arrows autoplay dotsClass="slick-dots slick-thumb">
            <a slot="customPaging" slot-scope="props">
              <img :src="getImgUrl(props.i)" />
            </a>
            <div v-for="item in data.gallery" :key="item.id">
              <img :src="item.image.gallery_square_crop" />
            </div>
          </a-carousel>
        </div>
      </div>

      <div class="detail_media_right">
        <div class="detail_media_info">
          <h1>迪拜旅游七星帆船酒店天空/海底/池畔自助餐/JUNSUI自助餐/餐厅午餐晚餐下午茶预定可选</h1>
          <dl class="detail_dominance">
            <dt>产品特色</dt>
            <div class="editor-content" v-html="data.subtitle" />
          </dl>
          
          <div class="detail_address">
            <span class="detail_txt">
              <span class="aline">所在地</span>
              <span class="detail_dest detail_dest_more" id="detail_dest">迪拜</span>
            </span>
          </div>
        </div>
      </div>
    </div>
    <div class="detail_main_wrap" v-html="data.content"></div>
  </div>
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

.detail_main_wrap {
    background: #fff;
    border: 1px solid #ddd;
    padding: 29px;
    position: relative;
    margin-bottom: 18px;
}

.basefix:after, .layoutfix:after {
    clear: both;
    content: '.';
    display: block;
    height: 0;
    overflow: hidden;
}

.detail_media_left{
  height:348px;
  float: left;
}

.detail_media_right {
    position: absolute;
    top: 30px;
    right: 30px;
    width: 591px;
    float: right;
    font-family: Microsoft YaHei!important;
}

.attraction_photo_wrap {
    width: 500px;
}

.detail_media_info .detail_address {
    vertical-align: middle;
    position: relative;
    line-height: 26px;
    font-family: Microsoft YaHei;
    font-size: 12px;
    color: #333;
    clear: both;
    height: 26px;
}

.detail_media_info .detail_address .detail_txt span.aline {
    display: inline-block;
    width: 114px;
    margin-right: 5px;
    float: left;
    height: 15px;
    *height: auto;
    font-family: Microsoft YaHei;
    font-size: 12px;
    color: #333;
}

.detail_media_info h1 {
    font: 400 22px microsoft yahei,simsun,sans-serif;
    word-wrap: break-word;
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 2;
    overflow: hidden;
    padding-bottom: 15px;
    display: block;
    font-family: Microsoft YaHei;
    color: #333;
}

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

.detail_dominance {
    zoom: 1;
    margin: 8px 0;
    line-height: 1.8;
    position: relative;
    border: 1px dashed #2680ff;
    padding: 17px 14px 4px 14px;
    border-radius: 10px;
}
.detail_dominance dt {
    background: #2680ff;
    border-radius: 0 100px 100px 0;
    color: #fff;
    width: 90px;
    text-align: center;
    height: 20px;
    line-height: 20px;
    position: absolute;
    left: -2px;
    top: -8px;
    font-size: 12px;
}
.detail_dominance ul {
    position: relative;
    padding-left: 18px;
    zoom: 1;
    color: #333;
    word-wrap: break-word;
    font-size: 14px;
}

</style>