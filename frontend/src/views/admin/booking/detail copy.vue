<template>
  <a-spin :spinning="loading">
    <a-card>
      <div slot="title">
        <a-dropdown :disabled="isEdit">
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
      </div>

      <div slot="extra">
        <a-button v-if="isEdit" type="primary" @click="update">Update</a-button>
        <a-button v-else type="primary" @click="create">Create</a-button>
      </div>

      <a-form :form="form">
        <a-row :gutter="18">
          <a-col :span="9" :offset="3">
            <a-form-item class="form-item" :label="productLabel">
              <a-input v-model="form.product"></a-input>
            </a-form-item>
          </a-col>
          <a-col :span="9">
            <a-form-item class="form-item" :label="variantLabel">
              <a-input v-model="form.variant"></a-input>
            </a-form-item>
          </a-col>
        </a-row>

        <a-row :gutter="18" v-if="form.category == 3">
          <a-col :span="9" :offset="3">
            <a-form-item class="form-item" label="Start Date">
              <a-date-picker v-model="form.start_date" style="width: 100%" />
            </a-form-item>
          </a-col>
          <a-col :span="9">
            <a-form-item class="form-item" label="End Date">
              <a-date-picker v-model="form.end_date" style="width: 100%" />
            </a-form-item>
          </a-col>
        </a-row>

        <a-row :gutter="18" v-else-if="form.category == 5">
          <a-col :span="9" :offset="3">
            <a-form-item class="form-item" label="CheckIn Date">
              <a-date-picker v-model="form.start_date" style="width: 100%" />
            </a-form-item>
          </a-col>
          <a-col :span="9">
            <a-form-item class="form-item" label="CheckOut Date">
              <a-date-picker v-model="form.end_date" style="width: 100%" />
            </a-form-item>
          </a-col>
        </a-row>

        <a-row :gutter="18" v-else>
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
              <a-date-picker v-model="form.booking_day" style="width: 100%" format="YYYY-MM-DD" />
            </a-form-item>
          </a-col>
          <a-col :span="9">
            <a-form-item class="form-item" label="Status" @change="() => {}">
              <a-select v-model="form.status" :filterOption="false" v-if="form.category == 5">
                <a-select-option v-for="data in RoomStatus" :key="data.value">{{data.label}}</a-select-option>
              </a-select>

              <a-select v-model="form.status" :filterOption="false" v-else>
                <a-select-option v-for="data in BookingStatus" :key="data.value">{{data.label}}</a-select-option>
              </a-select>
            </a-form-item>
          </a-col>
        </a-row>

        <a-row :gutter="18" v-if="form.category == 1 || form.category == 2">
          <a-col :span="6" :offset="3">
            <a-form-item class="form-item" label="Adult Quantity">
              <a-input-number v-model="form.quantity" style="width: 100%" :min="1" />
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

        <a-row :gutter="18" v-if="form.category == 1 || form.category == 2">
          <a-col :span="6" :offset="3">
            <a-form-item class="form-item" label="Adult Price">
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

        <a-row :gutter="18" v-if="form.category == 1 || form.category == 2">
          <a-col :span="6" :offset="3">
            <a-form-item class="form-item" label="Adult Cost Price">
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

        <a-row :gutter="18" v-else-if="form.category == 3 || form.category == 4">
          <a-col :span="6" :offset="3">
            <a-form-item class="form-item" label="Quantity">
              <a-input-number v-model="form.quantity" style="width: 100%" :min="1" />
            </a-form-item>
          </a-col>
          <a-col :span="6">
            <a-form-item class="form-item" label="Price">
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
            <a-form-item class="form-item" label="Cost Price">
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

        <a-row :gutter="18" v-if="form.category == 2 || form.category == 4">
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

        <a-row :gutter="18" v-if="form.category == 2 || form.category == 3 || form.category == 4">
          <a-col :span="9" :offset="3">
            <a-form-item class="form-item" label="Vehicle Model">
              <a-input v-model="form.vehicle_model" placeholder="Model"></a-input>
            </a-form-item>
          </a-col>

          <a-col :span="9">
            <a-form-item class="form-item" label="Number">
              <a-input v-model="form.vehicle_number" placeholder="Traffic Plate No."></a-input>
            </a-form-item>
          </a-col>
        </a-row>

        <a-row
          :gutter="18"
          v-if="form.category == 2 || form.category == 3 || form.category == 4"
        >
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

        <a-row :gutter="18" v-if="form.category == 3">
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

        <a-row v-if="form.category == 2">
          <a-col :span="18" :offset="3">
            <a-form-item class="form-item" label="Supplier">
              <a-input v-model="form.supplier"></a-input>
            </a-form-item>
          </a-col>
        </a-row>

        <a-row :gutter="18">
          <a-col :span="9" v-if="form.category == 3 || form.category == 4" :offset="3">
            <a-form-item class="form-item" label="Itinerary">
              <a-textarea v-model="form.ref" :autosize="{minRows: 5}"></a-textarea>
            </a-form-item>
          </a-col>
          <a-col :span="9" v-else :offset="3">
            <a-form-item class="form-item" label="Ref">
              <a-textarea v-model="form.ref" :autosize="{minRows: 5}"></a-textarea>
            </a-form-item>
          </a-col>
          <a-col :span="9">
            <a-form-item class="form-item" label="Remark">
              <a-textarea v-model="form.remark" :autosize="{minRows: 5}"></a-textarea>
            </a-form-item>
          </a-col>
        </a-row>
      </a-form>
    </a-card>
  </a-spin>
</template>

<script>
import { Icon } from "ant-design-vue";
import { createBooking, updateBooking, getBooking } from "@/api/booking";
import moment from "moment";

const IconFont = Icon.createFromIconfontCN({
  scriptUrl: "//at.alicdn.com/t/font_1402881_gsh78a0lnya.js"
});

const BookingStatus = [
  { value: 1, label: "Inquiry" },
  { value: 2, label: "Confirm" },
  { value: 3, label: "Padding" },
  { value: 4, label: "Email-Sent" },
  { value: 5, label: "OP-Cancelled" },
  { value: 6, label: "OP-Approved" }
];

const RoomStatus = [
  { value: 1, label: "Inquiry" },
  { value: 2, label: "Confirm" },
  { value: 3, label: "Room_Blocked" },
  { value: 4, label: "Email_Sent" },
  { value: 5, label: "OP-Cancelled" },
  { value: 6, label: "Roomlist_Sent" },
  { value: 7, label: "Inquriy_Sent" },
  { value: 8, label: "AC_Paid" },
  { value: 9, label: "AC_Panding" },
];

const Category = [
  { value: 1, label: "Restaurant", type: "iconf-30" },
  { value: 2, label: "Tour", type: "iconticket" },
  { value: 3, label: "Transport", type: "iconche" },
  { value: 4, label: "Car", type: "iconche" },
  { value: 5, label: "Hotel", type: "iconhotel" },
  { value: 6, label: "Gift", type: "iconliwu1" }
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
  mounted() {
    if (!this.isEdit) {
      this.initData(this.$route.query);
    } else {
      this.fetch(this.$route.params.id);
    }
  },
  watch: {
    "form.category": function(newValue, oldValue) {
      this.updateLabel(newValue);
    }
  },
  data() {
    return {
      BookingStatus,
      RoomStatus,
      Category,
      loading: false,
      productLabel: "Product",
      variantLabel: "Variant",
      form: {
        id: undefined,
        product: null,
        variant: null,
        status: 1,
        category: 1,
        action_day: null,
        action_time: null,
        booking_day: null,
        start_date: null,
        end_date: null,
        quantity: 0,
        child_quantity: 0,
        free_quantity: 0,
        price: 0.0,
        child_price: 0.0,
        total_price: 0.0,
        cost_price: 0.0,
        child_cost_price: 0.0,
        total_cost_price: 0.0,
        vat: 0.0,
        pick_up_time: null,
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
    initData(data) {
      this.form = Object.assign(this.form, {
        product: data.product,
        variant: data.variant,
        category: Number(data.category),
        action_day: moment(data.day, "YYYY-MM-DD"),
        action_time: moment(data.time, "HH:mm:ss"),
        booking_day: moment(data.create_at, "YYYY-MM-DD"),
        start_date: moment(data.day),
        end_date: moment(data.day),
        quantity: Number(data.adult_quantity),
        child_quantity: Number(data.child_quantity),
        price: Number(data.adult_price),
        child_price: Number(data.child_price),
        total_price: Number(data.total),
        order_id: Number(data.id)
      });
      this.$nextTick(() => {
        this.updateLabel(Number(data.category));
      });
    },
    updateDateTime(data) {
      return {
        action_day: moment(data.action_day, "YYYY-MM-DD"),
        action_time: moment(data.action_time, "HH:mm:ss"),
        booking_day: moment(data.booking_day, "YYYY-MM-DD"),
        pick_up_time: moment(data.pick_up_time, "YYYY-MM-DD"),
        start_date: moment(data.pick_up_time, "YYYY-MM-DD"),
        end_date: moment(data.pick_up_time, "YYYY-MM-DD")
      };
    },
    updateLabel(newValue) {
      if (newValue == 1) {
        this.productLabel = "Restaurant";
        this.variantLabel = "Meal";
      } else if (newValue == 2) {
        this.productLabel = "Product";
        this.variantLabel = "Variant";
      } else if (newValue == 3) {
        this.productLabel = "Trip";
        this.variantLabel = "Line";
      } else if (newValue == 4) {
        this.productLabel = "Itinerary";
        this.variantLabel = "Vehicle Model";
      } else if (newValue == 5) {
        this.productLabel = "Hotel";
        this.variantLabel = "Used Rooms";
      } else if (newValue == 6) {
        this.productLabel = "Product";
        this.variantLabel = "Variant";
      }
    },
    fetch(id) {
      this.loading = true;
      getBooking(id)
        .then(res => {
          const { result } = res;
          this.form = Object.assign(result, this.updateDateTime(result));
        })
        .finally(() => {
          this.loading = false;
        });
    },
    create() {
      var form = Object.assign({}, this.form, {
        action_day: this.form.action_day
          ? this.form.action_day.format("YYYY-MM-DD")
          : undefined,
        action_time: this.form.action_time
          ? this.form.action_time.format("HH:mm:ss")
          : undefined,
        booking_day: this.form.booking_day
          ? this.form.booking_day.format("YYYY-MM-DD")
          : undefined,
        pick_up_time: this.form.pick_up_time
          ? this.form.pick_up_time.format("YYYY-MM-DD HH:mm:ss")
          : undefined,
        start_date: this.form.start_date
          ? this.form.start_date.format("YYYY-MM-DD")
          : undefined,
        end_date: this.form.end_date
          ? this.form.end_date.format("YYYY-MM-DD")
          : undefined
      });

      this.loading = true;

      createBooking(form)
        .then(res => {
          const { id } = res.result;
          this.$router.replace({ name: "BookingEdit", params: { id } });
        })
        .finally(() => {
          this.loading = false;
        });
    },
    update() {
      var form = Object.assign({}, this.form, {
        action_day: this.form.action_day
          ? this.form.action_day.format("YYYY-MM-DD")
          : undefined,
        action_time: this.form.action_time
          ? this.form.action_time.format("HH:mm:ss")
          : undefined,
        booking_day: this.form.booking_day
          ? this.form.booking_day.format("YYYY-MM-DD")
          : undefined,
        pick_up_time: this.form.pick_up_time
          ? this.form.pick_up_time.format("YYYY-MM-DD HH:mm:ss")
          : undefined,
        start_date: this.form.start_date
          ? this.form.start_date.format("YYYY-MM-DD")
          : undefined,
        end_date: this.form.end_date
          ? this.form.end_date.format("YYYY-MM-DD")
          : undefined
      });

      this.loading = true;

      updateBooking(this.form.id, form)
        .then(res => {
          this.form = Object.assign(result, this.updateDateTime(result));
        })
        .finally(() => {
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
.form-item {
  margin-bottom: 16px;
  color: red;
}
</style>