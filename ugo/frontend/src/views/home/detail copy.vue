<template>
  <div class="detail_main_wrap" style="height: 845px">
    <div class="detail_media_left">
      <a-carousel arrows autoplay dotsClass="slick-dots slick-thumb">
          <a slot="customPaging" slot-scope="props">
            <img :src="getImgUrl(props.i)" />
          </a>
          <div v-for="item in data.gallery" :key="item.id">
            <img :src="item.image.gallery_square_crop" />
          </div>
        </a-carousel>
    </div>
    <div class="detail_media_right" data-reactid="54"><div data-reactid="55"><div class="detail_media_info" data-reactid="56"><h1 data-reactid="57"><!-- react-text: 58 -->迪拜旅游七星帆船酒店天空/海底/池畔自助餐/JUNSUI自助餐/餐厅午餐晚餐下午茶预定可选<!-- /react-text --></h1><dl class="detail_dominance" data-reactid="59"><dt data-reactid="60">产品特色</dt><dd data-reactid="61"><i data-reactid="62"></i><p data-reactid="63">身边就是蓝色的海底，珊瑚水草小鱼。让您仿佛置身于童话里</p></dd><dd data-reactid="64"><i data-reactid="65"></i><p data-reactid="66">体验“高高在上”的餐厅，边吃饭边俯瞰整个棕榈岛</p></dd><dd data-reactid="67"><i data-reactid="68"></i><p data-reactid="69">位于水池旁边，全透明的玻璃面朝大海，阳光满屋</p></dd></dl><div class="detail-proinfo-li-box " data-reactid="70"><div class="detail_grade " style="min-width:150px;background-color:#FFFBF5;padding-left:15px;" data-reactid="71"><span class="price_text" style="margin-right:10px;" data-reactid="72"><dfn class="price_language" data-reactid="73">¥</dfn><strong style="font-family:ArialMT;" data-reactid="74">415</strong><!-- react-text: 75 -->起<!-- /react-text --></span><div class="detail_wifi_info more_layer ttd-flex ttd-vertical-center" style="margin-bottom:-8px;" data-reactid="76"><span class="item ellipsis" style="max-width:108px;" data-reactid="77"><span data-reactid="78"><span style="cursor:pointer;vertical-align:middle;" data-reactid="79"><span style="color:#A4A4A4;padding-right:5px;" data-reactid="80"><span style="text-decoration:line-through;" data-reactid="81"><!-- react-text: 82 -->¥<!-- /react-text --><!-- react-text: 83 -->999<!-- /react-text --></span><span class="wifi_title" style="text-decoration:underline;" data-reactid="84">价格说明</span></span></span></span></span><span class="price_line" style="display:inline-block;margin-left:33px;height:22px;width:1px;opacity:0.4;border-right:1px dotted #979797;" data-reactid="85"></span></div><span class="saleInfo" style="display:flex;" data-reactid="86"><div class="point_text" style="cursor:pointer;" data-reactid="87"><p class="amount" data-reactid="88"><!-- react-text: 89 -->4.4<!-- /react-text --><!-- react-text: 90 -->分<!-- /react-text --></p><p class="text" data-reactid="91">评分</p></div><div class="point_text" style="cursor:pointer;" data-reactid="92"><p class="amount" data-reactid="93">8</p><p class="text" data-reactid="94">累计评价</p></div><div class="point_text" data-reactid="95"><p class="amount" data-reactid="96"><!-- react-text: 97 -->43<!-- /react-text --><!-- react-text: 98 -->份<!-- /react-text --></p><p class="text" data-reactid="99">月销</p></div></span><section class="collectionContainer" data-reactid="100"><span id="favorite" class="favorite" data-reactid="101"><i class="icon_favorite" title="收藏" data-reactid="102"></i><!-- react-text: 103 -->收藏 <!-- /react-text --></span></section></div></div><div class="detail_address" data-reactid="104"><span class="detail_txt" data-reactid="105"><span class="aline" data-reactid="106">所在地</span><span class="detail_dest detail_dest_more" id="detail_dest" data-reactid="107">迪拜</span></span></div><div class="detail_address" data-reactid="108"><span class="detail_txt" data-reactid="109"><span class="aline" data-reactid="110">零售商</span><span class="detail_dest" data-reactid="111"><span data-reactid="112">由</span><a class="vendor-store" data-reactid="113">迪拜中洲假期</a><span data-reactid="114">直售，并提供咨询/预订/售后服务</span></span></span></div><div class="detail_top_line" data-reactid="115"></div></div></div></div>
  </div>
  <!--<a-card>
     <a-row type="flex" justify="space-between">
      <a-col span="12" style="width:524px;min-height:400px;">
        <a-carousel arrows autoplay dotsClass="slick-dots slick-thumb">
          <a slot="customPaging" slot-scope="props">
            <img :src="getImgUrl(props.i)" />
          </a>
          <div v-for="item in data.gallery" :key="item.id">
            <img :src="item.image.gallery_square_crop" />
          </div>
        </a-carousel>
      </a-col>
      <a-col span="12" style="width:567px;min-height:400px;">
        <h1>
          伊斯坦布尔4
        </h1>
        <dl class="detail_dominance">
          <dt>
            产品特色
          </dt>
          <ul>
            <li>身边就是蓝色的海底，珊瑚水草小鱼。让您仿佛置身于童话里</li>
            <li>体验&ldquo;高高在上&rdquo;的餐厅，边吃饭边俯瞰整个棕榈岛】</li>
            <li>体验&ldquo;高高在上&rdquo;的餐厅，边吃饭边俯瞰整个棕榈岛】</li>
          </ul>
        </dl>
      </a-col>
    </a-row> 
  </a-card>-->
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

.detail_media_right {
    position: absolute;
    top: 30px;
    right: 30px;
    width: 591px;
    font-family: Microsoft YaHei!important;
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