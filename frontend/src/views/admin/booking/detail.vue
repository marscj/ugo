<template>
  <a-spin :spinning="loading">
    <a-card title="Base">
      <a-form :form="data">
        <a-row :gutter="18">
          <a-col :span="9" :offset="3">
            <a-form-item class="form-item" label="Product">
              <a-input v-model="form.product" placeholder="Product"></a-input>
            </a-form-item>
          </a-col>
          <a-col :span="9">
            <a-form-item class="form-item" label="Variant">
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
              <a-time-picker v-model="form.action_time" style="width: 100%" />
            </a-form-item>
          </a-col>
        </a-row>

        <a-row :gutter="18">
          <a-col :span="9" :offset="3">
            <a-form-item class="form-item" label="Booking Date">
              <a-date-picker
                v-model="form.booking_date"
                style="width: 100%"
                format="YYYY-MM-DD HH:mm:ss"
                showTime
              />
            </a-form-item>
          </a-col>
          <a-col :span="9">
            <a-form-item class="form-item" label="Status">
              <a-time-picker v-model="form.status" style="width: 100%" />
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
          <a-col :span="4" :offset="3">
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
          <a-col :span="4">
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
          <a-col :span="6">
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

        <a-row :gutter="18">
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

        <a-row :gutter="18">
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

        <a-row :gutter="18">
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

        <a-row></a-row>

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
import moment from "moment";

export default {
  props: {
    isEdit: {
      type: Boolean,
      default: false
    }
  },
  created() {
    if (!this.isEdit) {
      this.initData();
    }
  },
  data() {
    return {
      loading: false,
      form: {
        id: undefined,
        product: undefined,
        variant: undefined,
        action_day: moment(new Date(), "YYYY-MM-DD"),
        action_time: moment(new Date(), "HH:mm:ss"),
        booking_date: moment(new Date(), "YYYY-MM-DD HH:mm:ss"),
        adult_quantity: 0,
        child_quantity: 0,
        free_quantity: 0,
        adult_price: 0.0,
        child_price: 0.0,
        total_price: 0.0,
        adult_cost_pirce: 0.0,
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
        order_id: undefined
      }
    };
  },
  methods: {
    initData() {
      var data = this.$route.query;

      this.form = {
        product: data.product,
        variant: data.variant,
        category: data.category,
        action_day: moment(data.day, "YYYY-MM-DD"),
        action_time: moment(data.time, "HH:mm:ss"),
        booking_date: moment(data.create_at, "YYYY-MM-DD HH:mm:ss"),
        adult_quantity: data.adult_quantity,
        child_quantity: data.child_quantity,
        adult_price: data.adult_price,
        child_price: data.child_price,
        total_price: data.total,
        order_id: data.id
      };
    },
    create() {
      var form = Object.assign({}, this.form, {
        action_day: this.form.action_day.format("YYYY-MM-DD"),
        action_time: this.form.action_time.format("HH:mm:ss"),
        booking_date: this.form.booking_date.format("YYYY-MM-DD HH:mm:ss"),
        pick_up_time: this.form.pick_up_time.format("YYYY-MM-DD HH:mm:ss")
      });

      createBooking(form)
        .then(res => {
          return this.refresh(false);
        })
        .finally(() => {
          this.visible = false;
          this.loading = false;
        });
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
  margin-bottom: 15px;
}
</style>