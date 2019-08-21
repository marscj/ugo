<template>
  <a-spin :spinning="spinning">
    <div class="detail_main">
      <div class="detail_main_wrap">
        <div class="detail_main_left">
          <div class="detail_gallery">
            <a-carousel arrows autoplay dotsClass="slick-dots slick-thumb">
              <a slot="customPaging" slot-scope="props">
                <img :src="getImgUrl(props.i)" />
              </a>
              <div v-for="item in data.gallery" :key="item.id">
                <img :src="item.image.gallery_square_crop" />
              </div>
            </a-carousel>
          </div>
          <div class="detail_calendar">
            <a-calendar
              :value="day"
              :fullscreen="false"
              @change="handleDay"
              :disabledDate="disabledDate"
            />
          </div>
        </div>
        <div class="detail_main_right">
          <div class="detail_info">
            <h1>{{data.title}}</h1>
            <dl class="detail_dominance">
              <dt>产品特色</dt>
              <div class="editor-content" v-html="data.special" />
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
                <span class="detail_dest detail_dest_more" id="detail_dest">由UgoDubai提供</span>
              </span>
            </div>
            <div class="detail_top_line"></div>
          </div>
          <div class="detail-booking-mod">
            <div class="detail-booking-info-box">
              <ul class="detail-booking-info" style="margin: 0; padding: 0;">
                <li>
                  <label>
                    <span class>选择套餐</span>
                  </label>
                  <div class="right">
                    <div class="choose-wrap">
                      <a
                        href="javascript:;"
                        :class="variant == data ? data.status ? 'focus' : null : data.status ? null : 'disable' "
                        v-for="data in data.variant"
                        :key="data.id"
                        @click="handleVariant(data)"
                      >
                        {{data.name}}
                        <i v-if="variant==data" />
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
                        <a-date-picker
                          :value="day"
                          @change="handleDay"
                          :disabledDate="disabledDate"
                        />
                        <a-time-picker :value="time" style="margin-left: 8px" @change="handleTime" />
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
                            <span class="text-grey" v-if="variant">{{variant.adult_desc}}</span>
                          </p>
                          <p v-if="variant" class="price">
                            单价
                            <em>${{variant.adult_price}}</em>
                          </p>
                        </div>
                        <div class="item-right">
                          <a-input-number
                            v-model="adult_quantity"
                            :min="0"
                            :max="9999"
                            :precision="0"
                            :disabled="variant ? !variant.adult_status : true"
                          />
                        </div>
                      </div>
                      <div class="instruction-item">
                        <div class="item-left">
                          <p style="margin-bottom:0px">
                            儿童
                            <span class="text-grey" v-if="variant">{{variant.child_desc}}</span>
                          </p>
                          <p v-if="variant" class="price">
                            单价
                            <em>${{variant.child_price}}</em>
                          </p>
                        </div>
                        <div class="item-right">
                          <a-input-number
                            v-model="child_quantity"
                            :min="0"
                            :max="9999"
                            :precision="0"
                            :disabled="variant ? !variant.child_status : true"
                          />
                        </div>
                      </div>
                    </div>
                  </div>
                </li>
              </ul>
            </div>
            <div class="booking-mod-bottom">
              <a-button type="primary" class="booking-btn" :disabled="!canbook" @click="handleBook">立即预订</a-button>
              <div class="booking-price-wrap booking-price-wrap-nodesc" style="top: 0px;">
                <p class="selling-price">
                  总价
                  <span>
                    <dfn>
                      $
                      <i class="selling-price-text" style="font-style: inherit;">{{total_price}}</i>
                    </dfn>
                  </span>
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="detail_main_wrap" v-html="data.content"></div>
    </div>
  </a-spin>
</template>

<script>
import { getProduct } from "@/api/product";
import { checkout } from "@/api/order";
import { checkError } from "@/views/utils/error";
import moment from "moment";

export default {
  data() {
    return {
      spinning: false,
      data: {
        gallery: []
      },
      variant: null,
      day: moment(new Date(), "YYYY-MM-DD"),
      time: moment("12:00:00", "HH:mm:ss"),
      adult_quantity: 0,
      adult_price: 0.0,
      child_quantity: 0,
      child_price: 0.0,
      total_price: 0.0,
      canbook: false
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
          this.description = result.subtitle;
          this.$route.meta.title = result.title;
          this.$parent.getPageMeta();
          this.extraImage = result.photo.image.medium_square_crop;
        })
        .finally(() => {
          this.spinning = false;
        });
    },
    handleVariant(data) {
      if (data.status) {
        this.variant = data;
        this.adult_quantity = 0;
        this.child_quantity = 0;
      }
    },
    handleDay(value) {
      if (value) {
        this.day = value;
      } else {
        this.day = moment();
      }
    },
    handleTime(value) {
      if (value) {
        this.time = value;
      } else {
        this.time = moment("12:00:00", "HH:mm:ss");
      }
    },
    handleBook() {
      this.spinning = true
      checkout({
        day: this.day.format("YYYY-MM-DD"),
        time: this.time.format("HH:mm:ss"),
        adult_quantity: this.adult_quantity,
        adult_price: this.adult_price,
        child_quantity: this.child_quantity,
        child_price: this.child_price,
        variant_id: this.variant.id,
      }).then(res => {
        const { result } = res
        this.$router.push({name: 'Checkout', query: result})
      }).catch((error) => {
        this.checkError(error)
        if (error && error.response) {
          if (error.response.status == 401) {
            // this.$router.push({name: 'UserLogin'})
          }
        }
      }).finally(() => {
        this.spinning = false
      });
    },
    checkError(error) {
      var errors = checkError(
        error,
        "customer",
        "adult_quantity",
        "child_quantity",
        "adult_price",
        "child_price",
        "variant"
      );

      for (var key in errors) {
        if (errors[key]) {
          this.$notification["error"]({
            message: errors[key],
            duration: 4
          });
        }
      }
    },
    handleCanBook() {
      if (
        (this.adult_quantity > 0 || this.child_quantity > 0) &&
        this.day &&
        this.time
      ) {
        this.canbook = true;
      } else {
        this.canbook = false;
      }
    },
    toDecimal(num) {
      let tar = parseFloat(num);
      if (isNaN(tar)) {
        return;
      }
      return Math.round(num * 100) / 100;
    },
    disabledDate(value) {
      return value.diff(moment(new Date()).format("YYYY-MM-DD")) <= 0;
    }
  },
  watch: {
    adult_quantity(value) {
      this.adult_price = this.toDecimal(this.variant.adult_price * value);
      this.handleCanBook();
    },
    child_quantity(value) {
      this.child_price = this.toDecimal(this.variant.child_price * value);
      this.handleCanBook();
    },
    adult_price(value) {
      this.total_price = this.toDecimal(value + this.child_price);
    },
    child_price(value) {
      this.total_price = this.toDecimal(this.adult_price + value);
    },
    day(value) {
      this.handleCanBook();
    },
    time(value) {
      this.handleCanBook();
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
  padding: 20px;
  margin-bottom: 18px;
  overflow: hidden;
  font-size: 12px;
  font-family: microsoft yahei, simsun, sans-serif;
}

.detail_main_left {
  float: left;
  width: 45%;
  min-width: 300px;
}

.detail_gallery {
  height: 350px;
}

.detail_calendar {
  border: 1px solid #d9d9d9;
}

.detail_main_right {
  float: right;
  width: 52%;
}

.detail_info h1 {
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

.detail_address {
  vertical-align: middle;
  position: relative;
  line-height: 26px;
  font-family: Microsoft YaHei;
  font-size: 12px;
  color: #333;
  clear: both;
  height: 26px;
}

.detail_address .detail_txt span.aline {
  display: inline-block;
  width: 114px;
  margin-right: 5px;
  height: 15px;
  *height: auto;
  font-family: Microsoft YaHei;
  font-size: 12px;
  color: #333;
}

.detail_top_line {
  border-bottom: 1px dashed #dfdfdf;
  width: 100%;
  padding-top: 10px;
}

.basefix:after {
  clear: both;
  content: " ";
  display: block;
  height: 0;
  overflow: hidden;
}

.detail-booking-mod {
  background-color: #fff;
  width: 100%;
  padding-top: 16px;
}

.detail-booking-mod .detail-booking-info-box {
  display: inline-block;
}

.detail-booking-mod .detail-booking-info li {
  margin-bottom: 18px;
  display: flex;
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

.detail-booking-mod .detail-booking-info .right {
  display: inline-block;
  line-height: 28px;
  font-size: 12px;
  width: 418px;
}

.detail-booking-mod .detail-booking-info .bookinglimit {
  line-height: 2;
  margin-bottom: 10px;
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
  margin-top: 3px;
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

.detail-booking-mod .booking-mod-bottom {
  padding-top: 20px;
  border-top: 1px dashed #d1d1d1;
}

.booking-btn {
  width: 178px;
  height: 50px;
  font-size: 26px;
  line-height: 50px;
  text-align: center;
  border-radius: 5px;
  cursor: pointer;
  float: right;
}

.booking-price-wrap {
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
