<template>
  <a-spin :spinning="loading">
    <a-card >
      <template slot="title">
        <a-button type="primary">Create</a-button>
      </template>
      <template slot="extra">
        <a-button-group>
          <a-dropdown>
            <a-menu slot="overlay" @click="handleMenuClick">
              <a-menu-item v-for="data in Category" :key="data.value">
                <icon-font :type="data.type" />
                {{data.label}}
              </a-menu-item>
            </a-menu>
            <a-button style="margin-left: 8px">
              {{Category[form.category - 1].label}}
              <a-icon type="down" />
            </a-button>
          </a-dropdown>
        </a-button-group>
      </template>

      <a-form :form="form">
        <a-row :gutter="18">
          <a-col :span="form.category == 1 ? 6 : 9" :offset="3">
            <a-form-item class="form-item" label="Product">
              <a-input v-model="form.product" placeholder="Product"></a-input>
            </a-form-item>
          </a-col>
          <a-col :span="form.category == 1 ? 6 : 9">
            <a-form-item class="form-item" label="Variant">
              <a-input v-model="form.variant" placeholder="Variant"></a-input>
            </a-form-item>
          </a-col>
          <a-col :span="6" v-if="form.category == 1">
            <a-form-item class="form-item" label="Meal">
              <a-select v-model="form.meal" :filterOption="false">
                <a-select-option v-for="data in MealPeriod" :key="data.value">{{data.label}}</a-select-option>
              </a-select>
            </a-form-item>
          </a-col>
        </a-row>

        <a-row :gutter="18">
          <a-col :span="9" :offset="3">
            <a-form-item class="form-item" label="Action Day">
              <a-date-picker v-model="form.action_day" style="width: 100%" />
            </a-form-item>
          </a-col>
          <a-col :span="9">
            <a-form-item class="form-item" label="Action Time">
              <a-time-picker v-model="form.action_time" style="width: 100%" format="HH:mm" />
            </a-form-item>
          </a-col>
        </a-row>

        <a-row :gutter="18">
          <a-col :span="9" :offset="3">
            <a-form-item class="form-item" label="Booking Date">
              <a-date-picker
                v-model="form.booking_date"
                style="width: 100%"
                format="YYYY-MM-DD HH:mm"
                :showTime="{ format: 'HH:mm' }"
              />
            </a-form-item>
          </a-col>
          <a-col :span="9">
            <a-form-item class="form-item" label="Status" @change="() => {}">
              <a-select v-model="form.status" :filterOption="false">
                <a-select-option v-for="data in BookingStatus" :key="data.value">{{data.label}}</a-select-option>
              </a-select>
            </a-form-item>
          </a-col>
        </a-row>

        <a-row :gutter="18">
          <a-col :span="6" :offset="3">
            <a-form-item class="form-item" label="Adult Quantity">
              <a-input-number
                v-model="form.adult_quantity"
                style="width: 100%"
                placeholder="Adult"
                :min="1"
              />
            </a-form-item>
          </a-col>
          <a-col :span="6">
            <a-form-item class="form-item" label="Child Quantity">
              <a-input-number
                v-model="form.child_quantity"
                style="width: 100%"
                placeholder="Child"
                :min="0"
              />
            </a-form-item>
          </a-col>
          <a-col :span="6">
            <a-form-item class="form-item" label="Free Quantity">
              <a-input-number
                v-model="form.free_quantity"
                style="width: 100%"
                placeholder="Free"
                :min="0"
              />
            </a-form-item>
          </a-col>
        </a-row>

        <a-row :gutter="18">
          <a-col :span="6" :offset="3">
            <a-form-item class="form-item" label="Adult Price">
              <a-input-number
                v-model="form.adult_price"
                style="width: 100%"
                placeholder="Adult"
                :min="0.0"
                :defaultValue="0.0"
                :precision="2"
                :step="0.5"
              />
            </a-form-item>
          </a-col>
          <a-col :span="6">
            <a-form-item class="form-item" label="Child Price">
              <a-input-number
                v-model="form.child_price"
                style="width: 100%"
                placeholder="Child"
                :min="0.0"
                :defaultValue="0.0"
                :precision="2"
                :step="0.5"
              />
            </a-form-item>
          </a-col>
          <a-col :span="6">
            <a-form-item class="form-item" label="Total Price">
              <a-input-number
                v-model="form.total_price"
                style="width: 100%"
                placeholder="Free"
                :min="0.0"
                :defaultValue="0.0"
                :precision="2"
                :step="0.5"
              />
            </a-form-item>
          </a-col>
        </a-row>

        <a-row :gutter="18">
          <a-col :span="6" :offset="3">
            <a-form-item class="form-item" label="Adult Cost Price">
              <a-input-number
                v-model="form.adult_cost_price"
                style="width: 100%"
                :min="0.0"
                :defaultValue="0.0"
                :precision="2"
                :step="0.5"
              />
            </a-form-item>
          </a-col>
          <a-col :span="6">
            <a-form-item class="form-item" label="Child Cost Price">
              <a-input-number
                v-model="form.child_cost_price"
                style="width: 100%"
                :min="0.0"
                :defaultValue="0.0"
                :precision="2"
                :step="0.5"
              />
            </a-form-item>
          </a-col>
          <a-col :span="4">
            <a-form-item class="form-item" label="Total Cost Price">
              <a-input-number
                v-model="form.total_cost_price"
                style="width: 100%"
                :min="0.0"
                :defaultValue="0.0"
                :precision="2"
                :step="0.5"
              />
            </a-form-item>
          </a-col>
          <a-col :span="2">
            <a-form-item class="form-item" label="Vat">
              <a-input-number
                v-model="form.vat"
                style="width: 100%"
                :min="0.0"
                :defaultValue="0.0"
                :precision="2"
                :step="0.5"
              />
            </a-form-item>
          </a-col>
        </a-row>

        <a-row :gutter="18" v-if="form.category == 2">
          <a-col :span="6" :offset="3">
            <a-form-item class="form-item" label="Pickup Time">
              <a-date-picker
                v-model="form.pick_up_time"
                format="YYYY-MM-DD HH:mm:ss"
                showTime
                placeholder="Pickup Time"
                style="width: 100%;"
              ></a-date-picker>
            </a-form-item>
          </a-col>
          <a-col :span="6">
            <a-form-item class="form-item" label="Pickup Address">
              <a-input v-model="form.pick_up_address" placeholder="Pickup Address"></a-input>
            </a-form-item>
          </a-col>

          <a-col :span="6">
            <a-form-item class="form-item" label="Dropoff Address">
              <a-input v-model="form.drop_off_address" placeholder="Dropoff Address"></a-input>
            </a-form-item>
          </a-col>
        </a-row>

        <a-row :gutter="18" v-if="form.category == 2">
          <a-col :span="9" :offset="3">
            <a-form-item class="form-item" label="Vehicle">
              <a-input v-model="form.vehicle_model" placeholder="Model"></a-input>
            </a-form-item>
          </a-col>

          <a-col :span="9">
            <a-form-item class="form-item" label="Number">
              <a-input v-model="form.vehicle_number" placeholder="Traffic Plate No."></a-input>
            </a-form-item>
          </a-col>
        </a-row>

        <a-row :gutter="18" v-if="form.category == 2">
          <a-col :span="9" :offset="3">
            <a-form-item class="form-item" label="Driver">
              <a-input v-model="form.dirver" placeholder="Name" :min="1" />
            </a-form-item>
          </a-col>

          <a-col :span="9">
            <a-form-item class="form-item" label="Mobile">
              <a-input v-model="form.driver_mobile" placeholder="Moblie" :min="0" />
            </a-form-item>
          </a-col>
        </a-row>

        <a-row :gutter="18">
          <a-col :span="9" :offset="3">
            <a-form-item class="form-item" label="Tourguide">
              <a-input v-model="form.guide" placeholder="Name" :min="1" />
            </a-form-item>
          </a-col>

          <a-col :span="9">
            <a-form-item class="form-item" label="Mobile">
              <a-input v-model="form.guide_mobile" placeholder="Moblie" :min="0" />
            </a-form-item>
          </a-col>
        </a-row>

        <a-row>
          <a-col :span="18" offset="3">
            <a-form-item class="form-item" label="Supplier">
              <a-input v-model="form.supplier"></a-input>
            </a-form-item>
          </a-col>
        </a-row>

        <a-row :gutter="18">
          <a-col :span="9" :offset="3">
            <a-form-item class="form-item" label="Remark">
              <a-textarea v-model="form.remark" :autosize="{minRows: 5}"></a-textarea>
            </a-form-item>
          </a-col>
          <a-col :span="9">
            <a-form-item class="form-item" label="Ref">
              <a-textarea v-model="form.ref" :autosize="{minRows: 5}"></a-textarea>
            </a-form-item>
          </a-col>
        </a-row>
      </a-form>
    </a-card>
  </a-spin>
</template>

<script>
import { Icon } from "ant-design-vue";
import { createBooking } from "@/api/booking";
import moment from "moment";

const IconFont = Icon.createFromIconfontCN({
  scriptUrl: "//at.alicdn.com/t/font_1402881_gsh78a0lnya.js"
});

const BookingStatus = [
  { value: 1, label: "Inquiry" },
  { value: 2, label: "Confirm" },
  { value: 3, label: "Padding" },
  { value: 4, label: "Sent-Email" },
  { value: 5, label: "OP-Cancel" },
  { value: 6, label: "OP_Approved" }
];

const Category = [
  { value: 1, label: "Food", type: "iconf-30" },
  { value: 2, label: "Ticket", type: "iconticket" },
  { value: 3, label: "Trip", type: "iconlvyou" },
  { value: 4, label: "Car", type: "iconche" },
  { value: 5, label: "Hotel", type: "iconhotel" },
  { value: 6, label: "Gift", type: "iconliwu1" }
];

const MealPeriod = [
  { value: 1, label: "Breakfast" },
  { value: 2, label: "Lunch" },
  { value: 3, label: "Dinner" },
  { value: 4, label: "Afternoon Tea" }
];

export default {
  props: {
    isEdit: {
      type: Boolean,
      default: false
    }
  },
  components: {
    IconFont
  },
  created() {
    if (!this.isEdit) {
      this.initData();
    }
  },
  data() {
    return {
      BookingStatus,
      Category,
      MealPeriod,
      loading: false,
      form: {
        id: undefined,
        product: undefined,
        variant: undefined,
        status: 1,
        category: 1,
        meal: 1,
        action_day: moment(new Date(), "YYYY-MM-DD"),
        action_time: moment(new Date(), "HH:mm:ss"),
        booking_date: moment(new Date(), "YYYY-MM-DD HH:mm:ss"),
        adult_quantity: 0,
        child_quantity: 0,
        free_quantity: 0,
        adult_price: 0.0,
        child_price: 0.0,
        total_price: 0.0,
        adult_cost_price: 0.0,
        child_cost_price: 0.0,
        total_cost_price: 0.0,
        vat: 0.0,
        pick_up_time: moment(new Date(), "YYYY-MM-DD HH:mm:ss"),
        pick_up_address: "",
        drop_off_address: "",
        vehicle: "",
        vehicle_number: "",
        driver: "",
        driver_mobile: "",
        guide: "",
        guide_mobile: "",
        remark: "",
        ref: "",
        supplier: "",
        order_id: undefined
      }
    };
  },
  methods: {
    initData() {
      var data = this.$route.query;

      this.form = Object.assign(this.form, {
        product: data.product,
        variant: data.variant,
        category: Number(data.category),
        action_day: moment(data.day, "YYYY-MM-DD"),
        action_time: moment(data.time, "HH:mm"),
        booking_date: moment(data.create_at, "YYYY-MM-DD HH:mm"),
        adult_quantity: Number(data.adult_quantity),
        child_quantity: Number(data.child_quantity),
        adult_price: Number(data.adult_price),
        child_price: Number(data.child_price),
        total_price: Number(data.total),
        order_id: Number(data.id)
      });
    },
    create() {
      var form = Object.assign({}, this.form, {
        action_day: this.form.action_day.format("YYYY-MM-DD"),
        action_time: this.form.action_time.format("HH:mm"),
        booking_date: this.form.booking_date.format("YYYY-MM-DD HH:mm"),
        pick_up_time: this.form.pick_up_time.format("YYYY-MM-DD HH:mm")
      });

      createBooking(form)
        .then(res => {
          return this.refresh(false);
        })
        .finally(() => {
          this.visible = false;
          this.loading = false;
        });
    },
    handleMenuClick(e) {
      this.form.category = e.key;
    }
  }
};
</script>

<style >
.order-info {
  margin: 0;
}

.bold {
  font-weight: bold;
}

.ligth-blue {
  color: #2f54eb;
}

.ant-table-tbody > tr > td,
.ant-table-thead > tr > th {
  padding: 12px 8px;
  font-size: 12px;
}

.form-item {
  margin-bottom: 16px;
}
</style>