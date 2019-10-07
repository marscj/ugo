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
              <a-input v-model="form.variant" placeholder="Variant"></a-input>
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
              <a-date-picker v-model="form.booking_day" style="width: 100%" format="YYYY-MM-DD" />
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

        <a-row :gutter="18" v-if="isEdit">
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

        <a-row :gutter="18" v-if="form.category == 1">
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

        <a-row :gutter="18" v-if="form.category == 1 && isEdit">
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

        <a-row :gutter="18" v-if="form.category == 1 && isEdit">
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

        <a-row :gutter="18" v-if="isEdit">
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

        <a-row v-if="isEdit">
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
          <a-col :span="9" v-if="isEdit">
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
import { createBooking, updateBooking, getBooking } from "@/api/booking";
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
  { value: 1, label: "Tour", type: "iconticket" },
  { value: 2, label: "Restaurant", type: "iconf-30" },
  { value: 3, label: "Hotel", type: "iconhotel" },
  { value: 4, label: "Car", type: "iconche" },
  { value: 5, label: "Gift", type: "iconliwu1" }
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
      this.initData(this.$route.query);
    } else {
      this.fetch(this.$route.params.id);
    }
  },
  watch: {
    "form.category": function(newValue, oldValue) {
      if (newValue == 1) {
        this.productLabel = "Product";
        this.variantLabel = "Variant";
      } else if (newValue == 2) {
        this.productLabel = "Restaurant";
        this.variantLabel = "Meal";
      } else if (newValue == 3) {
        this.productLabel = "Hotel";
        this.variantLabel = "Room";
      } else if (newValue == 4) {
        this.productLabel = "Itinerary";
        this.variantLabel = "Vehicle Model";
      } else if (newValue == 5) {
        this.productLabel = "Product";
        this.variantLabel = "Variant";
      }
    }
  },
  data() {
    return {
      BookingStatus,
      Category,
      loading: false,
      productLabel: "Product",
      variantLabel: "Variant",
      form: {
        id: undefined,
        product: undefined,
        variant: undefined,
        status: 1,
        category: 1,
        action_day: moment(new Date(), "YYYY-MM-DD"),
        action_time: moment(new Date(), "HH:mm:ss"),
        booking_day: moment(new Date(), "YYYY-MM-DD"),
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
    initData(data) {
      var category = Number(data.category);

      if (data.category == 1) {
        category = 2
      } else if (data.category == 2) {
        category = 1
      } else if (date.category == 3) {
        category = 1
      } else if (data.category == 4) {
        category = 4
      } else if (data.category == 5) {
        category = 3
      } else if (data.category == 6) {
        category = 5
      }

      this.form = Object.assign(this.form, {
        product: data.product,
        variant: data.variant,
        category: category,
        action_day: moment(data.day, "YYYY-MM-DD"),
        action_time: moment(data.time, "HH:mm:ss"),
        booking_day: moment(data.create_at, "YYYY-MM-DD"),
        adult_quantity: Number(data.adult_quantity),
        child_quantity: Number(data.child_quantity),
        adult_price: Number(data.adult_price),
        child_price: Number(data.child_price),
        total_price: Number(data.total),
        order_id: Number(data.id)
      });
    },
    updateDateTime(data) {
      return {
        action_day: moment(data.action_day, "YYYY-MM-DD"),
        action_time: moment(data.action_time, "HH:mm:ss"),
        booking_day: moment(data.booking_day, "YYYY-MM-DD"),
        pick_up_time: moment(data.pick_up_time, "YYYY-MM-DD")
      };
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