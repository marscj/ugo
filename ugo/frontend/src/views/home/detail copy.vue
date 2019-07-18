<template>
  <div class="detail_main">
    <div class="detail_main_wrap basefix">
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
              <span class="detail_dest detail_dest_more" id="detail_dest">有UgoDubai提供</span>
            </span>
          </div>
          <div class="detail_top_line"></div>
        </div>
      </div>

      <div class="detail-booking-mod">
        <div class="booking-mod-top">
          <div class="booking-media-left">
            <div class="attraction_calendar_wrap">
              <a-calendar :fullscreen="false" />
            </div>
          </div>
          <div class="booking-media-right" >
            <div class="detail-booking-info-box">
              <ul class="detail-booking-info" style="margin: 0; padding: 0;">
                <li>
                  <label>
                    <span class>选择套餐</span>
                  </label>
                  <div class="right">
                    <div class="choose-wrap">
                      <a
                        data-df="1"
                        data-disable="indisable"
                        data-attid="207"
                        data-vname="海底餐厅午餐四道式"
                        data-vid="191700"
                        href="javascript:;"
                        class="focus"
                      >
                        <!-- react-text: 750 -->
                        海底餐厅午餐四道式
                        <!-- /react-text -->
                        <i></i>
                      </a>
                      <a
                        data-df="1"
                        data-disable="indisable"
                        data-attid="207"
                        data-vname="海底餐厅晚餐四道式"
                        data-vid="191800"
                        href="javascript:;"
                        class
                      >
                        <!-- react-text: 752 -->
                        海底餐厅晚餐四道式
                        <!-- /react-text -->
                      </a>
                      <a
                        data-df="1"
                        data-disable="indisable"
                        data-attid="207"
                        data-vname="天空餐厅午餐四道式"
                        data-vid="197200"
                        href="javascript:;"
                        class
                      >
                        <!-- react-text: 754 -->
                        天空餐厅午餐四道式
                        <!-- /react-text -->
                      </a>
                      <a
                        data-df="1"
                        data-disable="indisable"
                        data-attid="207"
                        data-vname="池畔餐厅午餐自助"
                        data-vid="197300"
                        href="javascript:;"
                        class
                      >
                        <!-- react-text: 756 -->
                        池畔餐厅午餐自助
                        <!-- /react-text -->
                      </a>
                      <a
                        data-df="1"
                        data-disable="indisable"
                        data-attid="207"
                        data-vname="日落小食下午茶套餐"
                        data-vid="197500"
                        href="javascript:;"
                        class
                      >
                        <!-- react-text: 758 -->
                        日落小食下午茶套餐
                        <!-- /react-text -->
                      </a>
                      <a
                        data-df="1"
                        data-disable="indisable"
                        data-attid="207"
                        data-vname="JUNSUI餐厅午餐自助"
                        data-vid="197600"
                        href="javascript:;"
                        class
                      >
                        <!-- react-text: 760 -->
                        JUNSUI餐厅午餐自助
                        <!-- /react-text -->
                      </a>
                      <a
                        data-df="1"
                        data-disable="indisable"
                        data-attid="207"
                        data-vname="天空餐厅晚餐四道式"
                        data-vid="197700"
                        href="javascript:;"
                        class
                      >
                        <!-- react-text: 762 -->
                        天空餐厅晚餐四道式
                        <!-- /react-text -->
                      </a>
                      <a
                        data-df="1"
                        data-disable="indisable"
                        data-attid="207"
                        data-vname="池畔餐厅晚餐自助"
                        data-vid="197800"
                        href="javascript:;"
                        class
                      >
                        <!-- react-text: 764 -->
                        池畔餐厅晚餐自助
                        <!-- /react-text -->
                      </a>
                      <a
                        data-df="1"
                        data-disable="indisable"
                        data-attid="207"
                        data-vname="JUNSUI餐厅晚餐自助"
                        data-vid="198000"
                        href="javascript:;"
                        class
                      >
                        <!-- react-text: 766 -->
                        JUNSUI餐厅晚餐自助
                        <!-- /react-text -->
                      </a>
                    </div>
                  </div>
                </li>
                <li style="position: relative;">
                  <label>
                    <span class>选择使用日期时间</span>
                  </label>
                  <div class="right">
                    <div class="date-wrapper">
                      <div class="date-box">
                        <a-date-picker />
                        <a-time-picker style="margin-left: 5px">
                          <a-button slot="addon" size="small" type="primary">Ok</a-button>
                        </a-time-picker>
                      </div>
                    </div>
                  </div>
                </li>
                <li>
                  <label>
                    <span class>人数</span>
                  </label>
                  <div class="right">
                    <div class="instruction-list">
                      <div class="instruction-item">
                        <div class="item-left">
                          <p style="margin-bottom:0px">
                            成人
                            <span class="text-grey">10周岁（含）以上</span>
                          </p>
                          <p class="price">
                            单价
                            <em>¥975</em>
                          </p>
                        </div>
                        <div class="item-right">
                          <span class="num-box">
                            <a
                              data-disable="indisable"
                              data-vname="成人"
                              data-vid="3700"
                              class="copies-cut"
                              href="javascript:;"
                              role="cut"
                            ></a>
                            <input
                              type="text"
                              min="1"
                              max="9999"
                              value="1"
                              class="copies-num"
                              role="copy"
                            />
                            <a
                              data-disable="indisable"
                              data-vname="成人"
                              data-vid="3700"
                              class="copies-add"
                              href="javascript:;"
                              role="add"
                            ></a>
                          </span>
                        </div>
                      </div>
                      <div class="instruction-item">
                        <div class="item-left">
                          <p style="margin-bottom:0px">
                            儿童
                            <span class="text-grey">3周岁（含）-9周岁（含）</span>
                          </p>
                          <p class="price">
                            单价
                            <em>¥528</em>
                          </p>
                        </div>
                        <div class="item-right">
                          <span class="num-box">
                            <a
                              data-disable="indisable"
                              data-vname="儿童"
                              data-vid="3800"
                              class="copies-cut disable"
                              href="javascript:;"
                              role="cut"
                            ></a>
                            <input
                              type="text"
                              min="1"
                              max="9999"
                              value="0"
                              class="copies-num"
                              role="copy"
                            />
                            <a
                              data-disable="indisable"
                              data-vname="儿童"
                              data-vid="3800"
                              class="copies-add"
                              href="javascript:;"
                              role="add"
                            ></a>
                          </span>
                        </div>
                      </div>
                    </div>
                    <div></div>
                  </div>
                </li>
              </ul>
            </div>
            <div class="booking-mod-bottom">
              <a class="booking-btn">立即预订</a>
              <div class="booking-price-wrap booking-price-wrap-nodesc" style="top: 0px;">
                <p class="selling-price">
                  总价
                  <span>
                    <dfn>
                      ¥
                      <i class="selling-price-text" style="font-style: inherit;">1050</i>
                    </dfn>
                  </span>
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="basefix">
      <div class="detail_main_wrap" v-html="data.content"></div>
    </div>
  </div>
</template>

<script>
import { getProduct } from "@/api/product";
import moment from "moment";

export default {
  props: {},
  data() {
    return {
      spinning: false,
      data: {
        gallery: []
      }
    };
  },
  mounted() {
    const id = this.$route.params && this.$route.params.id;
    this.fetch(id);
  },
  methods: {
    getImgUrl(i) {
      if (this.data && this.data.gallery) {
        return this.data.gallery[i].image.gallery_square_crop;
      }
      return "";
    },
    fetch(id) {
      this.spinning = true;
      getProduct(id)
        .then(res => {
          const { result } = res;
          this.data = result;
          this.description = result.description;
          this.$route.meta.title = result.name;
          this.$parent.getPageMeta();
          this.extraImage = result.photo.image.medium_square_crop;
        })
        .finally(() => {
          this.spinning = false;
        });
    },
    getListData(value) {
      let listData;
      switch (value.date()) {
        case 8:
          listData = [
            {
              type: "warning",
              content: "Y1004"
            }
          ];
          break;
        default:
      }
      return listData || [];
    },

    getMonthData(value) {
      if (value.month() === 8) {
        return 1394;
      }
    }
  }
};
</script>

<style scoped>
.detail_main {
  width: 100%;
  margin: 0 auto;
  background: #f2f5f7;
  padding-bottom: 40px;
}

.detail_main_wrap {
  background: #fff;
  border: 1px solid #ddd;
  padding: 29px;
  position: relative;
  margin-bottom: 18px;
  font-size: 12px;
  font-family: microsoft yahei, simsun, sans-serif;
}

.basefix:after {
  clear: both;
  content: " ";
  display: block;
  height: 0;
  overflow: hidden;
}

.detail_media_left {
  height: 348px;
}

.detail_media_right {
  position: absolute;
  top: 30px;
  right: 30px;
  width: 591px;
  float: right;
  font-family: Microsoft YaHei !important;
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
  font: 400 22px microsoft yahei, simsun, sans-serif;
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
  width: 100%;
  padding-top: 16px;
}

.detail-booking-mod .booking-media-left {
  display: inline-block;
  width: 500px;
  vertical-align: top;
}

.detail-booking-mod .booking-media-right {
  position: relative;
  right: -48px;
  width: 590px;
  top: -120px; 
  margin-bottom: -120px;
}

.detail-booking-mod .booking-media-right {
  display: inline-block;
}

.detail-booking-mod .detail-booking-info li {
  margin-bottom: 18px;
  display: flex;
}

.detail-booking-mod .detail-booking-info li .error-tip {
  padding-left: 142px;
  font-size: 12px;
  color: #ff5d37;
  font-family: PingFangSC-Semibold;
}

.detail-booking-mod .detail-booking-info li .act-error-tip {
  color: #ff5d37;
  font-family: PingFangSC-Semibold;
}

.detail-booking-mod .detail-booking-info label {
  display: inline-block;
  width: 114px;
  height: 100%;
  min-height: 28px;
  line-height: 28px;
  font-size: 12px;
  color: #333;
  margin-right: 5px;
}

.detail-booking-mod .detail-booking-info label span {
  display: inline-block;
}

.detail-booking-mod .detail-booking-info label .extr-tip {
  display: block;
  padding-right: 16px;
  line-height: 20px;
  font-size: 10px;
  color: #2680ff;
}

.detail-booking-mod .detail-booking-info .right {
  display: inline-block;
  line-height: 28px;
  font-size: 12px;
  width: 418px;
  float: right;
}

.detail-booking-mod .detail-booking-info .bookinglimit {
  line-height: 2;
  margin-bottom: 10px;
}

.detail-booking-mod .detail-booking-info .right .data-ctrl {
  float: left;
  margin-right: 12px;
}

.detail-booking-mod .detail-booking-info .right .data-ctrl input {
  height: 28px;
  padding: 0;
  margin-top: -4px;
  text-indent: 8px;
  font-size: 14px;
  line-height: 28px/9;
  vertical-align: middle;
  outline: 0;
  box-shadow: none;
  border: 1px solid #ccc;
  font-family: microsoft yahei;
}

.detail-booking-mod .detail-booking-info .right .data-ctrl .select-date {
  width: 173px;
  background: url(https://pages.c-ctrip.com/activity/online/detail_caculate.png)
    148px -216px no-repeat;
  color: #333;
}

.detail-booking-mod .detail-booking-info .right .data-ctrl .focus {
  background-position: 148px -241px;
  border-color: #45c3da;
  color: #45c3da;
}

.detail-booking-mod .detail-booking-info .right .date-tip {
  font-size: 14px;
  color: #333;
}

.detail-booking-mod .detail-booking-info .right .choose-wrap {
  position: relative;
}

.detail-booking-mod .detail-booking-info .right .choose-wrap a {
  display: inline-block;
  min-width: 10px;
  border: 1px solid #ccc;
  text-align: left;
  margin-right: 10px;
  margin-bottom: 8px;
  border-radius: 4px;
  color: #333;
  padding: 5px 10px;
  max-width: 380px;
}

.detail-booking-mod .detail-booking-info .right .choose-wrap a:hover {
  border: 1px solid #2680ff;
}

.detail-booking-mod .detail-booking-info .right .choose-wrap a:last-child {
  margin-right: 0;
}

.detail-booking-mod .detail-booking-info .right .choose-wrap .focus {
  border: 1px solid #2680ff;
  position: relative;
}

.detail-booking-mod .detail-booking-info .right .choose-wrap i {
  display: block;
  position: absolute;
  border-bottom: 12px solid #2680ff;
  border-left: 14px solid transparent;
  width: 0;
  height: 0;
  bottom: 0;
  right: 0;
}

.detail-booking-mod .detail-booking-info .right .choose-wrap i:after {
  position: absolute;
  content: "";
  background-image: url(//pages.c-ctrip.com/activity/online/detail_icon_all_new.png);
  background-position: -598px -297px;
  width: 10px;
  height: 8px;
  left: -9px;
  top: 4.3px;
}

.detail-booking-mod .detail-booking-info .right .choose-wrap .disable {
  background-color: #f6f6f6;
  color: #d5d5d5;
}

.detail-booking-mod .detail-booking-info .right .choose-wrap .disable:hover {
  cursor: not-allowed;
}

.detail-booking-mod .detail-booking-info .instruction-list {
  padding-left: 0;
  margin-top: 3px
}

.detail-booking-mod .detail-booking-info .instruction-item {
  min-height: 28px;
  margin-bottom: 10px;
}

.detail-booking-mod .detail-booking-info .instruction-item .item-left {
  display: inline-block;
  max-width: 310px;
  vertical-align: sub;
}

.detail-booking-mod .detail-booking-info .instruction-item .item-left p {
  display: block;
  max-width: 300px;
  color: #333;
}

.detail-booking-mod
  .detail-booking-info
  .instruction-item
  .item-left
  .text-grey {
  color: #9b9b9b !important;
  margin-left: 12px;
}

.detail-booking-mod .detail-booking-info .instruction-item .item-left .price {
  color: #ff6913;
  line-height: 18px;
}

.detail-booking-mod .detail-booking-info .instruction-item .item-left .limit {
  font-size: 12px;
  color: #999;
  line-height: 18px;
}

.detail-booking-mod
  .detail-booking-info
  .instruction-item
  .item-left
  .price
  em {
  font-size: 14px;
  font-weight: 400;
  font-style: normal;
  margin-left: 3px;
}

.detail-booking-mod
  .detail-booking-info
  .instruction-item
  .item-left
  .price-tip {
  font-size: 12px;
  line-height: 20px;
}

.detail-booking-mod
  .detail-booking-info
  .instruction-item
  .item-left
  .price-tip
  dfn {
  margin-right: 5px;
}

.detail-booking-mod .detail-booking-info .instruction-item .item-right {
  float: right;
}

.detail-booking-mod .detail-booking-info .instruction-item .num-box {
  display: inline-block;
  border: 1px solid #2680ff;
  height: 26px;
  overflow: hidden;
  vertical-align: middle;
  box-sizing: border-box;
  margin-bottom: 4px;
}

.detail-booking-mod .detail-booking-info .instruction-item .num-box a:hover {
  background-color: #2680ff;
}

.detail-booking-mod .detail-booking-info .instruction-item .num-box a.disable {
  background-color: #f3f3f3;
  cursor: default;
}

.detail-booking-mod .detail-booking-info .instruction-item .num-box .copies-add,
.detail-booking-mod
  .detail-booking-info
  .instruction-item
  .num-box
  .copies-cut {
  background: url(//pages.c-ctrip.com/activity/online/detail_icon_all_new.png)
    no-repeat #2680ff;
  display: inline-block;
  height: 26px;
  width: 26px;
  vertical-align: top;
}

.detail-booking-mod
  .detail-booking-info
  .instruction-item
  .num-box
  .copies-cut {
  background-position: 6px -289px;
}

.detail-booking-mod
  .detail-booking-info
  .instruction-item
  .num-box
  .copies-add {
  background-position: 8px -319px;
}

.detail-booking-mod
  .detail-booking-info
  .instruction-item
  .num-box
  .copies-num {
  color: #000;
  height: 23px;
  width: 48px;
  text-align: center;
  text-indent: 0;
  vertical-align: middle;
  border: none;
  outline: 0;
  font-size: 12px;
}

.detail-booking-mod .detail-booking-info .instruction-item .num-box.disable {
  border-color: #dfe2e4;
}

.detail-booking-mod .detail-booking-info .instruction-item .num-box.disable a {
  background-color: #dfe2e4;
  cursor: default;
}

.detail-booking-mod .booking-mod-bottom {
  padding-top: 20px;
  border-top: 1px dashed #d1d1d1;
}

.booking-btn {
  display: inline-block;
  width: 178px;
  height: 50px;
  background: linear-gradient(90deg, #ffa900 0, #ff7201 100%);
  background: -ms-linear-gradient(90deg, #ffa900 0, #ff7201 100%);
  filter: progid:DXImageTransform.Microsoft.Gradient(startColorstr="#FFA900", endColorstr="#FFA900", gradientType="1");
  color: #fff;
  font-size: 26px;
  line-height: 50px;
  text-align: center;
  border-radius: 5px;
  cursor: pointer;
  float: right;
}

.booking-btn:hover {
  background: #f2590d;
  border-color: #d54100;
  color: #fff;
}

.booking-price-wrap {
  display: inline-block;
  margin-right: 29px;
  float: right;
  font-size: 14px;
}

.booking-price-wrap-nodesc {
  margin-top: 10px !important;
  position: relative;
}

.booking-price-wrap p {
  display: block;
  text-align: right;
}

.booking-price-wrap .selling-price {
  color: #333;
}

.booking-price-wrap .selling-price dfn {
  color: #ff6913;
  font-size: 32px;
}

.booking-price-wrap .selling-price span {
  margin-left: 6px;
  font-size: 24px;
  height: 32px;
  line-height: 32px;
}

.booking-price-wrap .suggest-price {
  color: #f2590d;
}

.booking-price-wrap .suggest-price span {
  margin-left: 10px;
}

.booking-price-wrap .suggest-price dfn {
  font-size: 18px;
}

.ant-carousel >>> .slick-dots {
  height: auto;
}

.ant-carousel >>> .slick-slide img {
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

.ant-carousel >>> .slick-thumb li.slick-active img {
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

.ul {
  display: block;
  list-style-type: disc;
  margin-block-start: 1em;
  margin-block-end: 1em;
  margin-inline-start: 0px;
  margin-inline-end: 0px;
  padding-inline-start: 40px;
}

.right {
  line-height: normal !important;
}

.a {
  text-decoration: none !important;
}

a {
  color: #0065bb;
  text-decoration: none;
  outline: 0;
}

p {
    margin-top: 100;
    margin-bottom: 1em;
}
</style>
