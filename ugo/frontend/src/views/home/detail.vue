<template>
  <div>
    <div class="detail_main_wrap basefix" >
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
            <h1>{{data.name}}</h1>
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
            <div class="detail_address">
              <span class="detail_txt">
                <span class="aline">开发商</span>
                <span class="detail_dest detail_dest_more" id="detail_dest">有UgoduBubai提供</span>
              </span>
            </div>
            <div class="detail_top_line"></div>
          </div>
        </div>

        <div class="detail-booking-mod" >
          <div class="booking-mod-top">
            <div class="booking-media-left">
              <div class="attraction_calendar_wrap">
                <a-calendar :fullscreen="false" />
              </div>
            </div>
            <div class="booking-media-right" style="top: 360px; padding-top: 18px;">
              <div class="detail-booking-info-box">
                <div class="detail-booking-info-box ">
                  <ul class="detail-booking-info">
                    <li><label><span class=""><!-- react-text: 754 -->选择<!-- /react-text --><!-- react-text: 755 -->套餐<!-- /react-text --><!-- react-text: 756 --> &nbsp; <!-- /react-text --></span></label><div class="right"><div class="choose-wrap"><a data-df="1" data-disable="disable" data-attid="207" data-vname="海底餐厅午餐四道式" data-vid="191700" href="javascript:;" class="disable "><!-- react-text: 760 -->海底餐厅午餐四道式<!-- /react-text --></a><a data-df="1" data-disable="indisable" data-attid="207" data-vname="海底餐厅晚餐四道式" data-vid="191800" href="javascript:;" class=" "><!-- react-text: 762 -->海底餐厅晚餐四道式<!-- /react-text --></a><a data-df="1" data-disable="indisable" data-attid="207" data-vname="天空餐厅午餐四道式" data-vid="197200" href="javascript:;" class=" "><!-- react-text: 764 -->天空餐厅午餐四道式<!-- /react-text --></a><a data-df="1" data-disable="indisable" data-attid="207" data-vname="池畔餐厅午餐自助" data-vid="197300" href="javascript:;" class=" "><!-- react-text: 766 -->池畔餐厅午餐自助<!-- /react-text --></a><a data-df="1" data-disable="indisable" data-attid="207" data-vname="日落小食下午茶套餐" data-vid="197500" href="javascript:;" class=" "><!-- react-text: 768 -->日落小食下午茶套餐<!-- /react-text --></a><a data-df="1" data-disable="indisable" data-attid="207" data-vname="JUNSUI餐厅午餐自助" data-vid="197600" href="javascript:;" class=" "><!-- react-text: 770 -->JUNSUI餐厅午餐自助<!-- /react-text --></a><a data-df="1" data-disable="indisable" data-attid="207" data-vname="天空餐厅晚餐四道式" data-vid="197700" href="javascript:;" class=" "><!-- react-text: 772 -->天空餐厅晚餐四道式<!-- /react-text --></a><a data-df="1" data-disable="indisable" data-attid="207" data-vname="池畔餐厅晚餐自助" data-vid="197800" href="javascript:;" class=" focus"><!-- react-text: 774 -->池畔餐厅晚餐自助<!-- /react-text --><i></i></a><a data-df="1" data-disable="indisable" data-attid="207" data-vname="JUNSUI餐厅晚餐自助" data-vid="198000" href="javascript:;" class=" "><!-- react-text: 776 -->JUNSUI餐厅晚餐自助<!-- /react-text --></a></div></div></li>
                    <li style="position: relative;"><label><span class=""><!-- react-text: 780 -->选择<!-- /react-text --><!-- react-text: 781 -->使用日期<!-- /react-text --><!-- react-text: 782 --> &nbsp; <!-- /react-text --></span></label><div class="right"><div class="date-wrapper"><div class="date-box"><span class="date-input">2019-07-27</span><i class="icon-date"></i></div><span class="date-box-tip">最晚18:00前可订出行当天产品（当地时间）</span></div></div><div class="price-date-small "><div><div class="price-date-wrapper"><div class="calendar small"><div class="calendar-wrap"><div class="calendar-switch-month"><div class="calendar-switch-arrow-left disable"><!-- react-text: 796 --> <!-- /react-text --><i></i><!-- react-text: 798 --> <!-- /react-text --></div><div class="calendar-switch-arrow-right "><!-- react-text: 800 --> <!-- /react-text --><i></i><!-- react-text: 802 --> <!-- /react-text --></div><div class="calendar-switch-month-txt"><!-- react-text: 804 -->2019<!-- /react-text --><!-- react-text: 805 -->年<!-- /react-text --><!-- react-text: 806 -->07<!-- /react-text --><!-- react-text: 807 -->月<!-- /react-text --></div></div><ul class="calendar-title"><li>日</li><li>一</li><li>二</li><li>三</li><li>四</li><li>五</li><li>六</li></ul><div class="calendar-body"><table class="calendar-right"><tbody><tr><td data-disable="disable" data-index="none" data-day="" class=" "><a href="javascript:;" class="" style="cursor: not-allowed;"><span class="date "></span></a></td><td data-disable="disable" data-index="none" data-day="1" class=" "><a href="javascript:;" class="" style="cursor: not-allowed;"><span class="date ">1</span></a></td><td data-disable="disable" data-index="none" data-day="2" class=" "><a href="javascript:;" class="" style="cursor: not-allowed;"><span class="date ">2</span></a></td><td data-disable="disable" data-index="none" data-day="3" class=" "><a href="javascript:;" class="" style="cursor: not-allowed;"><span class="date ">3</span></a></td><td data-disable="disable" data-index="none" data-day="4" class=" "><a href="javascript:;" class="" style="cursor: not-allowed;"><span class="date ">4</span></a></td><td data-disable="disable" data-index="none" data-day="5" class=" "><a href="javascript:;" class="" style="cursor: not-allowed;"><span class="date ">5</span></a></td><td data-disable="disable" data-index="none" data-day="6" class=" "><a href="javascript:;" class="" style="cursor: not-allowed;"><span class="date ">6</span></a></td></tr><tr><td data-disable="disable" data-index="none" data-day="7" class=" "><a href="javascript:;" class="" style="cursor: not-allowed;"><span class="date ">7</span></a></td><td data-disable="disable" data-index="none" data-day="8" class=" "><a href="javascript:;" class="" style="cursor: not-allowed;"><span class="date ">8</span></a></td><td data-disable="disable" data-index="none" data-day="9" class=" "><a href="javascript:;" class="" style="cursor: not-allowed;"><span class="date ">9</span></a></td><td data-disable="disable" data-index="none" data-day="10" class=" "><a href="javascript:;" class="" style="cursor: not-allowed;"><span class="date ">10</span></a></td><td data-disable="disable" data-index="none" data-day="11" class=" "><a href="javascript:;" class="" style="cursor: not-allowed;"><span class="date ">11</span></a></td><td data-disable="disable" data-index="none" data-day="12" class=" "><a href="javascript:;" class="" style="cursor: not-allowed;"><span class="date ">12</span></a></td><td data-disable="disable" data-index="none" data-day="13" class=" "><a href="javascript:;" class="" style="cursor: not-allowed;"><span class="date ">13</span></a></td></tr><tr><td data-disable="disable" data-index="none" data-day="14" class=" "><a href="javascript:;" class="" style="cursor: not-allowed;"><span class="date ">14</span></a></td><td data-disable="indisable" data-index="2019-07-15" data-day="15" class=" on"><a href="javascript:;" class="" style=""><span class="date ">15</span></a></td><td data-disable="indisable" data-index="2019-07-16" data-day="16" class=" on"><a href="javascript:;" class="" style=""><span class="date ">今天</span></a></td><td data-disable="indisable" data-index="2019-07-17" data-day="17" class=" on"><a href="javascript:;" class="" style=""><span class="date ">17</span></a></td><td data-disable="indisable" data-index="2019-07-18" data-day="18" class=" on"><a href="javascript:;" class="" style=""><span class="date ">18</span></a></td><td data-disable="indisable" data-index="2019-07-19" data-day="19" class=" on"><a href="javascript:;" class="" style=""><span class="date ">19</span></a></td><td data-disable="indisable" data-index="2019-07-20" data-day="20" class=" on"><a href="javascript:;" class="" style=""><span class="date ">20</span></a></td></tr><tr><td data-disable="indisable" data-index="2019-07-21" data-day="21" class=" on"><a href="javascript:;" class="" style=""><span class="date ">21</span></a></td><td data-disable="indisable" data-index="2019-07-22" data-day="22" class=" on"><a href="javascript:;" class="" style=""><span class="date ">22</span></a></td><td data-disable="indisable" data-index="2019-07-23" data-day="23" class=" on"><a href="javascript:;" class="" style=""><span class="date ">23</span></a></td><td data-disable="indisable" data-index="2019-07-24" data-day="24" class=" on"><a href="javascript:;" class="" style=""><span class="date ">24</span></a></td><td data-disable="indisable" data-index="2019-07-25" data-day="25" class=" on"><a href="javascript:;" class="" style=""><span class="date ">25</span></a></td><td data-disable="indisable" data-index="2019-07-26" data-day="26" class=" on"><a href="javascript:;" class="" style=""><span class="date ">26</span></a></td><td data-disable="indisable" data-index="2019-07-27" data-day="27" class="active on"><a href="javascript:;" class="a_active" style=""><span class="date span_active">27</span></a></td></tr><tr><td data-disable="indisable" data-index="2019-07-28" data-day="28" class=" on"><a href="javascript:;" class="" style=""><span class="date ">28</span></a></td><td data-disable="indisable" data-index="2019-07-29" data-day="29" class=" on"><a href="javascript:;" class="" style=""><span class="date ">29</span></a></td><td data-disable="indisable" data-index="2019-07-30" data-day="30" class=" on"><a href="javascript:;" class="" style=""><span class="date ">30</span></a></td><td data-disable="indisable" data-index="2019-07-31" data-day="31" class=" on"><a href="javascript:;" class="" style=""><span class="date ">31</span></a></td><td data-disable="disable" data-index="none" data-day="" class=" "><a href="javascript:;" class="" style="cursor: not-allowed;"><span class="date "></span></a></td><td data-disable="disable" data-index="none" data-day="" class=" "><a href="javascript:;" class="" style="cursor: not-allowed;"><span class="date "></span></a></td><td data-disable="disable" data-index="none" data-day="" class=" "><a href="javascript:;" class="" style="cursor: not-allowed;"><span class="date "></span></a></td></tr><tr><td data-disable="disable" data-index="none" data-day="" class=" "><a href="javascript:;" class="" style="cursor: not-allowed;"><span class="date "></span></a></td><td data-disable="disable" data-index="none" data-day="" class=" "><a href="javascript:;" class="" style="cursor: not-allowed;"><span class="date "></span></a></td><td data-disable="disable" data-index="none" data-day="" class=" "><a href="javascript:;" class="" style="cursor: not-allowed;"><span class="date "></span></a></td><td data-disable="disable" data-index="none" data-day="" class=" "><a href="javascript:;" class="" style="cursor: not-allowed;"><span class="date "></span></a></td><td data-disable="disable" data-index="none" data-day="" class=" "><a href="javascript:;" class="" style="cursor: not-allowed;"><span class="date "></span></a></td><td data-disable="disable" data-index="none" data-day="" class=" "><a href="javascript:;" class="" style="cursor: not-allowed;"><span class="date "></span></a></td><td data-disable="disable" data-index="none" data-day="" class=" "><a href="javascript:;" class="" style="cursor: not-allowed;"><span class="date "></span></a></td></tr></tbody></table></div></div></div><div class="tips_custom small"><div><label>您选择的是当地时间。</label></div></div></div><!-- react-empty: 1256 --></div></div></li>
                    <li><label><span class="">人数</span></label><div class="right"><div class="bookinglimit"></div><div class="instruction-list"><div class="instruction-item"><div class="item-left"><p><!-- react-text: 963 -->成人<!-- /react-text --><span class="text-grey">10周岁（含）以上</span></p><p class="price"><!-- react-text: 1908 -->单价<!-- /react-text --><em><!-- react-text: 1910 -->¥<!-- /react-text --><!-- react-text: 1911 -->975<!-- /react-text --></em></p></div><div class="item-right"><span class="num-box"><a data-disable="indisable" data-vname="成人" data-vid="3700" class="copies-cut   " href="javascript:;" role="cut"></a><input type="text" min="1" max="9999" value="1" class="copies-num" role="copy"><a data-disable="indisable" data-vname="成人" data-vid="3700" class="copies-add   " href="javascript:;" role="add"></a></span></div></div><div class="instruction-item"><div class="item-left"><p><!-- react-text: 973 -->儿童<!-- /react-text --><span class="text-grey">3周岁（含）-9周岁（含）</span></p><p class="price"><!-- react-text: 1913 -->单价<!-- /react-text --><em><!-- react-text: 1915 -->¥<!-- /react-text --><!-- react-text: 1916 -->528<!-- /react-text --></em></p></div><div class="item-right"><span class="num-box "><a data-disable="indisable" data-vname="儿童" data-vid="3800" class="copies-cut disable  " href="javascript:;" role="cut"></a><input type="text" min="1" max="9999" value="0" class="copies-num" role="copy"><a data-disable="indisable" data-vname="儿童" data-vid="3800" class="copies-add   " href="javascript:;" role="add"></a></span></div></div></div><div></div></div></li>
                  </ul>
                </div>
              </div>
              <div class="booking-mod-bottom">
                <a class=" booking-btn">立即预订</a>
                <div class="booking-price-wrap booking-price-wrap-nodesc" style="top: 0px;">
                  <p class="selling-price">
                    总价
                    <span>
                      <dfn>
                        ¥ 
                        <i class="selling-price-text" style="font-style: inherit;">
                          1050
                        </i>
                      </dfn>
                    </span>
                  </p>
                </div>
              </div>
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
    getListData(value) {
      let listData;
      switch (value.date()) {
        case 8:
          listData = [
            { type: 'warning', content: 'Y1004' },
          ]; break;
        default:
      }
      return listData || [];
    },

    getMonthData(value) {
      if (value.month() === 8) {
        return 1394;
      }
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

.attraction_calendar_wrap {
  width: 500px;
  border: 1px solid #d9d9d9;
  position: relative;
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

.detail_top_line {
    border-bottom: 1px dashed #dfdfdf;
    width: 100%;
    padding-top: 10px;
}

.detail-booking-mod {
    background-color: #fff;
    zoom: 1;
    width: 100%;
    padding-top: 16px;
}

.detail-booking-mod .booking-media-left {
    display: inline-block;
    width: 500px;
    vertical-align: top;
}

.detail-booking-mod .booking-media-right {
    position: absolute;
    right: 30px;
    display: inline-block;
    width: 590px;
}

.detail-booking-mod .booking-mod-bottom {
    padding-top: 20px;
    border-top: 1px dashed #d1d1d1;
}

.booking-btn {
    display: inline-block;
    width: 178px;
    height: 50px;
    background: linear-gradient(90deg,#ffa900 0,#ff7201 100%);
    background: -ms-linear-gradient(90deg,#ffa900 0,#ff7201 100%);
    filter: progid:DXImageTransform.Microsoft.Gradient(startColorstr="#FFA900", endColorstr="#FFA900", gradientType="1");
    color: #fff;
    font-size: 26px;
    line-height: 50px;
    text-align: center;
    border-radius: 5px;
    cursor: pointer;
    float: right;
}

.booking-price-wrap-nodesc {
    margin-top: 10px!important;
    position: relative;
}

.booking-price-wrap {
    display: inline-block;
    margin-right: 29px;
    float: right;
    font-size: 14px;
}

.booking-price-wrap .selling-price {
    color: #333;
}

.booking-price-wrap .selling-price span {
    margin-left: 6px;
    font-size: 24px;
    height: 32px;
    line-height: 32px;
}

.booking-price-wrap .selling-price dfn {
    color: #ff6913;
    font-size: 32px;
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