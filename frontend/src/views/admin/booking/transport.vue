<template>
  <a-form :form="form">
    <a-row :gutter="18">
      <a-col :span="6" :offset="3">
        <a-form-item class="form-item" label="Itinerary & Vehicle">
          <a-input v-model="form.product" placeholder="Itinerary"></a-input>
        </a-form-item>
      </a-col>
      <a-col :span="6">
        <a-form-item class="form-item" label="Start Date">
          <a-date-picker v-model="form.start_date" style="width: 100%" />
        </a-form-item>
      </a-col>
      <a-col :span="6">
        <a-form-item class="form-item" label="End Date">
          <a-date-picker v-model="form.end_date" style="width: 100%" />
        </a-form-item>
      </a-col>
    </a-row>

    <a-row :gutter="18">
      <a-col :span="9" :offset="3">
        <a-form-item class="form-item" label="Booking Date">
          <a-date-picker v-model="form.booking_date" style="width: 100%" format="YYYY-MM-DD" />
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
        <a-form-item class="form-item" label="Pax">
          <a-input-number v-model="form.quantity" style="width: 100%" :min="1" />
        </a-form-item>
      </a-col>
      <a-col :span="6">
        <a-form-item class="form-item" label="Pax/SP">
          <a-input-number
            v-model="form.price"
            style="width: 100%"
            :min="0.0"
            :defaultValue="0.0"
            :precision="2"
            :step="0.5"
          />
        </a-form-item>
      </a-col>
      <a-col :span="6">
        <a-form-item class="form-item" label="Pax/CP">
          <a-input-number
            v-model="form.cost_price"
            style="width: 100%"
            :min="0.0"
            :defaultValue="0.0"
            :precision="2"
            :step="0.5"
          />
        </a-form-item>
      </a-col>
    </a-row>

    <a-row :gutter="18">
      <a-col :span="9" :offset="3">
        <a-form-item class="form-item" label="Total/SP">
          <a-input-number
            v-model="form.total_price"
            disabled
            style="width: 100%"
            :min="0.0"
            :defaultValue="0.0"
            :precision="2"
            :step="0.5"
          />
        </a-form-item>
      </a-col>
      <a-col :span="9">
        <a-form-item class="form-item" label="Total/CP">
          <a-input-number
            v-model="form.total_cost_price"
            disabled
            style="width: 100%"
            :min="0.0"
            :defaultValue="0.0"
            :precision="2"
            :step="0.5"
          />
        </a-form-item>
      </a-col>
    </a-row>

    <a-row :gutter="18">
      <a-col :span="9" :offset="3">
        <a-form-item class="form-item" label="Vehicle ">
          <a-input v-model="form.vehicle" placeholder="Traffic Plate No."></a-input>
        </a-form-item>
      </a-col>

      <a-col :span="9">
        <a-form-item class="form-item" label="Model">
          <a-input v-model="form.vehicle_model" placeholder="Model Name"></a-input>
        </a-form-item>
      </a-col>
    </a-row>

    <a-row :gutter="18">
      <a-col :span="9" :offset="3">
        <a-form-item class="form-item" label="Driver">
          <a-input v-model="form.driver" placeholder="Name" :min="1" />
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

    <a-row :gutter="18">
      <a-col :span="9" :offset="3">
        <a-form-item class="form-item" label="Itinerary">
          <a-textarea v-model="form.itinerary" :autosize="{minRows: 5}"></a-textarea>
        </a-form-item>
      </a-col>
      <a-col :span="9">
        <a-form-item class="form-item" label="Remark">
          <a-textarea v-model="form.remark" :autosize="{minRows: 5}"></a-textarea>
        </a-form-item>
      </a-col>
    </a-row>

    <a-row :gutter="18">
      <a-col :span="2" :offset="3">
        <a-button v-if="isEdit" type="primary" @click="update">Update</a-button>
        <a-button v-else type="primary" @click="create">Create</a-button>
      </a-col>
      <a-col :span="2" v-if="isEdit">
        <a-dropdown v-if="$auth('Booking.add')">
          <a-menu slot="overlay">
            <a-menu-item v-for="category in Category" :key="category.value">
              <a href="javascript:;" @click="hanldeBooking(category.value)">
                <icon-font :type="category.type" />
                {{category.label}}
              </a>
            </a-menu-item>
          </a-menu>
          <a-button type="primary">Add Related Booking</a-button>
        </a-dropdown>
      </a-col>
    </a-row>
  </a-form>
</template>

<script>
import moment from "moment";

const BookingStatus = [
  { value: 1, label: "Inquiry" },
  { value: 2, label: "Confirm" },
  { value: 3, label: "Padding" },
  { value: 4, label: "Email-Sent" },
  { value: 5, label: "OP-Cancelled" },
  { value: 6, label: "OP-Approved" }
];

import { Icon } from "ant-design-vue";
const IconFont = Icon.createFromIconfontCN({
  scriptUrl: "//at.alicdn.com/t/font_1402881_gsh78a0lnya.js"
});

const Category = [
  { value: 1, label: "Restaurant", type: "iconf-30" },
  { value: 2, label: "Tour", type: "iconticket" },
  // { value: 3, label: "Transport", type: "iconche" },
  { value: 4, label: "Hotel", type: "iconhotel" }
];

export default {
  props: {
    isEdit: {
      type: Boolean,
      default: false
    }
  },
  components : {
    IconFont
  },
  mounted() {
    if (!this.isEdit) {
      this.initData(this.$route.query);
    }
  },
  watch: {
    form: {
      deep: true,
      handler: function(newValue, oldValue) {
        this.form.total_price =
          Number(this.form.quantity || 0) * Number(this.form.price || 0);

        this.form.total_cost_price =
          Number(this.form.quantity || 0) * Number(this.form.cost_price || 0);
      }
    }
  },
  data() {
    return {
      BookingStatus,
      Category,
      form: {
        id: undefined,
        product: "",
        category: 3,
        start_date: null,
        end_date: null,
        booking_date: null,
        supplier: "",
        status: 1,
        quantity: 0,
        price: 0.0,
        cost_price: 0.0,
        total_price: 0.0,
        total_cost_price: 0.0,
        vehicle_model: null,
        vehicle_no: null,
        driver: null,
        driver_mobile: null,
        guide: null,
        guide_mobile: null,
        remark: "",
        ref: "",
        order_id: undefined
      }
    };
  },
  methods: {
    initData(data) {
      this.form = Object.assign(this.form, {
        product: data.product + " - " + data.variant,
        start_date: data.day ? moment(data.day, "YYYY-MM-DD") : null,
        booking_date: data.create_at
          ? moment(data.create_at, "YYYY-MM-DD")
          : null,
        quantity: Number(data.adult_quantity),
        price: Number(data.adult_price),
        total_price: Number(data.total),
        operator: data.operator,
        order_id: Number(data.orderID)
      });
    },
    updateDateTime(data) {
      return {
        start_date: data.start_date
          ? moment(data.start_date, "YYYY-MM-DD")
          : null,
        end_date: data.end_date ? moment(data.end_date, "YYYY-MM-DD") : null,
        booking_date: data.booking_date
          ? moment(data.booking_date, "YYYY-MM-DD")
          : null
      };
    },
    translateDate(data) {
      return {
        start_date: data.start_date
          ? data.start_date.format("YYYY-MM-DD")
          : null,
        end_date: data.end_date ? data.end_date.format("YYYY-MM-DD") : null,
        booking_date: data.booking_date
          ? data.booking_date.format("YYYY-MM-DD")
          : null
      };
    },
    onFetch(data) {
      this.form = Object.assign(data, this.updateDateTime(data));
    },
    create() {
      var form = Object.assign({}, this.form, this.translateDate(this.form));
      this.$emit("create", form);
    },
    update() {
      var form = Object.assign({}, this.form, this.translateDate(this.form));
      this.$emit("update", form);
    },
    onUpdate(data) {
      this.form = Object.assign(data, this.updateDateTime(data));
    },
    hanldeBooking(value) {
      let routeUrl = this.$router.resolve({
        name: "BookingCreate",
        query: Object.assign({ type: value }, {
          product: '',
          variant: '',
          create_at: this.form.booking_date ? this.form.booking_date.format("YYYY-MM-DD") : null,
          adult_quantity: this.form.quantity,
          child_quantity: 0,
          adult_price: 0.0,
          child_price: 0.0,
          total: 0.0,
          operator: this.form.operator,
          orderID: this.form.order_id
        })
      });
      window.open(routeUrl.href, "_blank");
    }
  }
};
</script>

<style >
.form-item {
  margin-bottom: 16px;
  color: red;
}
</style>