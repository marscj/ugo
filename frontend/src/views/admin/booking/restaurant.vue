<template>
  <a-form :form="form">
    <a-row :gutter="18">
      <a-col :span="6" :offset="3">
        <a-form-item class="form-item" label="Restaurant&Meal">
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
        <a-form-item class="form-item" label="Adult/Pax">
          <a-input-number v-model="form.quantity" style="width: 100%" :min="1" />
        </a-form-item>
      </a-col>
      <a-col :span="6">
        <a-form-item class="form-item" label="Child/Pax">
          <a-input-number v-model="form.child_quantity" style="width: 100%" :min="0" />
        </a-form-item>
      </a-col>
      <a-col :span="6">
        <a-form-item class="form-item" label="Free/Pax">
          <a-input-number v-model="form.free_quantity" style="width: 100%" :min="0" />
        </a-form-item>
      </a-col>
    </a-row>

    <a-row :gutter="18">
      <a-col :span="6" :offset="3">
        <a-form-item class="form-item" label="Adult/SP">
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
        <a-form-item class="form-item" label="Child/SP">
          <a-input-number
            v-model="form.child_price"
            style="width: 100%"
            :min="0.0"
            :defaultValue="0.0"
            :precision="2"
            :step="0.5"
          />
        </a-form-item>
      </a-col>
      <a-col :span="6">
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
    </a-row>

    <a-row :gutter="18">
      <a-col :span="4" :offset="3">
        <a-form-item class="form-item" label="Adult/CP">
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
      <a-col :span="4">
        <a-form-item class="form-item" label="Child/CP">
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
      <a-col :span="6">
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

    <a-row :gutter="18">
      <a-col :span="9" :offset="3">
        <a-button v-if="isEdit" type="primary" @click="update" >Update</a-button>
        <a-button v-else type="primary" @click="create" >Create</a-button>
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
    }
  },
  watch: {
    form: {
      deep: true,
      handler: function(newValue, oldValue) {
        this.form.total_price =
          Number(this.form.quantity | 0) * Number(this.form.price | 0) +
          Number(this.form.child_quantity | 0) *
            Number(this.form.child_price | 0);

        this.form.total_cost_price =
          Number(this.form.quantity | 0) * Number(this.form.cost_price | 0) +
          Number(this.form.child_quantity | 0) *
            Number(this.form.child_cost_price | 0) +
          Number(this.form.vat | 0);
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
        category: 1,
        action_date: null,
        action_time: null,
        booking_date: null,
        status: 1,
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
        product: data.product + ' - ' + data.variant,
        action_date: data.day ? moment(data.day, "YYYY-MM-DD") : null,
        action_time: data.time ? moment(data.time, "HH:mm") : null,
        booking_date: data.create_at
          ? moment(data.create_at, "YYYY-MM-DD")
          : null,
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
          : null
      };
    },
    translateDate(data) {
      return {
        action_date: data.action_date
          ? data.action_date.format("YYYY-MM-DD")
          : null,
        action_time: data.action_time ? data.action_time.format("HH:mm") : null,
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