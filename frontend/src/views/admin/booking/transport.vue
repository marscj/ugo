<template>
  <a-spin :spinning="spinning">
    <a-form :form="form">
      <a-row :gutter="18">
        <a-col :span="6" :offset="3">
          <a-form-item class="form-item" label="Product">
            <a-input v-model="form.product" placeholder="Product Name"></a-input>
          </a-form-item>
        </a-col>
        <a-col :span="6">
          <a-form-item class="form-item" label="Action Date">
            <a-date-picker v-model="form.action_date" style="width: 100%" />
          </a-form-item>
        </a-col>
        <a-col :span="6">
          <a-form-item class="form-item" label="Action Time">
            <a-time-picker v-model="form.action_time" style="width: 100%" format="HH:mm" />
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
        <a-col :span="6" >
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
        <a-col :span="9" >
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
        <a-col :span="9" :offset="3">
          <a-button v-if="isEdit" type="primary" @click="update" :loading="loading">Update</a-button>
          <a-button v-else type="primary" @click="create" :loading="loading">Create</a-button>
        </a-col>
      </a-row>
    </a-form>
  </a-spin>
</template>

<script>
import { createBooking, updateBooking, getBooking } from "@/api/booking";
import moment from "moment";

const BookingStatus = [
  { value: 1, label: "Inquiry" },
  { value: 2, label: "Confirm" },
  { value: 3, label: "Padding" },
  { value: 4, label: "Email-Sent" },
  { value: 5, label: "OP-Cancelled" },
  { value: 6, label: "OP-Approved" }
];

export default {
  props: {
    isEdit: {
      type: Boolean,
      default: false
    }
  },
  mounted() {
    if (!this.isEdit) {
      this.initData(this.$route.query);
    } else {
      this.fetch(this.$route.params.id);
    }
  },
  watch: {
    form: {
      deep: true,
      handler: function(newValue, oldValue) {
        this.form.total_price =
          Number(this.form.quantity | 0) * Number(this.form.price | 0);

        this.form.total_cost_price =
          Number(this.form.quantity | 0) * Number(this.form.cost_price | 0);
      }
    }
  },
  data() {
    return {
      BookingStatus,
      loading: false,
      spinning: false,
      form: {
        id: undefined,
        product: "",
        category: 3,
        action_date: null,
        action_time: null,
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
        product: data.product,
        action_date: data.day ? moment(data.day, "YYYY-MM-DD") : null,
        action_time: data.time ? moment(data.time, "HH:mm") : null,
        booking_date: data.create_at ? moment(data.create_at, "YYYY-MM-DD") : null,
        quantity: data.adult_quantity,
        child_quantity: data.child_quantity,
        price: data.adult_price,
        child_price: data.child_price,
        total_price: data.total,
        order_id: Number(data.id)
      });
    },
    updateDateTime(data) {
      return {
        action_date: data.action_date
          ? moment(data.action_date, "YYYY-MM-DD")
          : null,
        action_time: data.action_time
          ? moment(data.action_time, "HH:mm")
          : null,
        booking_date: data.booking_date
          ? moment(data.booking_date, "YYYY-MM-DD")
          : null,
      };
    },
    translateDate(data) {
      return {
        action_date: data.action_date ? data.action_date.format("YYYY-MM-DD") : null,
        action_time: data.action_time ? data.action_time.format("HH:mm") : null,
        booking_date: data.booking_date ? data.booking_date.format("YYYY-MM-DD") : null,
      };
    },
    fetch(id) {
      this.spinning = true;
      getBooking(id)
        .then(res => {
          const { result } = res;
          this.form = Object.assign(result, this.updateDateTime(result));
          this.$emit("onTitle", this.form);
        })
        .finally(() => {
          this.spinning = false;
        });
    },
    create() {
      var form = Object.assign({}, this.form, this.translateDate(this.form));

      this.loading = true;

      createBooking(form)
        .then(res => {
          const { id } = res.result;
          this.$router.replace({
            name: "BookingEdit",
            params: { id },
            query: { category: 3 }
          });
        })
        .finally(() => {
          this.loading = false;
        });
    },
    update() {
      var form = Object.assign({}, this.form, this.translateDate(this.form));

      this.loading = true;

      updateBooking(this.form.id, form)
        .then(res => {
          this.form = Object.assign(result, this.updateDateTime(result));
        })
        .finally(() => {
          this.loading = false;
        });
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