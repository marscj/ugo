<template>
  <a-form :form="form">
    <a-row :gutter="18">
      <a-col :span="6" :offset="3">
        <a-form-item class="form-item" label="Hotel">
          <a-input v-model="form.product" placeholder="Hotel Name"></a-input>
        </a-form-item>
      </a-col>
      <a-col :span="6">
        <a-form-item class="form-item" label="CheckIn Date">
          <a-date-picker v-model="form.start_date" style="width: 100%" />
        </a-form-item>
      </a-col>
      <a-col :span="6">
        <a-form-item class="form-item" label="CheckOut Date">
          <a-date-picker v-model="form.end_date" style="width: 100%" />
        </a-form-item>
      </a-col>
    </a-row>

    <a-row :gutter="18">
      <a-col :span="6" :offset="3">
        <a-form-item class="form-item" label="Booking Date">
          <a-date-picker v-model="form.booking_date" style="width: 100%" format="YYYY-MM-DD" />
        </a-form-item>
      </a-col>
      <a-col :span="6">
        <a-form-item class="form-item" label="Payment Due Date">
          <a-date-picker v-model="form.payment_due_date" style="width: 100%" format="YYYY-MM-DD" />
        </a-form-item>
      </a-col>
      <a-col :span="6">
        <a-form-item class="form-item" label="Room Update">
          <a-date-picker v-model="form.room_update" style="width: 100%" format="YYYY-MM-DD" />
        </a-form-item>
      </a-col>
    </a-row>

    <a-row :gutter="18">
      <a-col :span="6" :offset="3">
        <a-form-item class="form-item" label="Emailed">
          <a-date-picker v-model="form.emailed" style="width: 100%" format="YYYY-MM-DD" />
        </a-form-item>
      </a-col>
      <a-col :span="6">
        <a-form-item class="form-item" label="Cancel Date">
          <a-date-picker v-model="form.cancel_date" style="width: 100%" format="YYYY-MM-DD" />
        </a-form-item>
      </a-col>

      <a-col :span="6">
        <a-form-item class="form-item" label="Status">
          <a-select v-model="form.status" :filterOption="false">
            <a-select-option v-for="data in RoomStatus" :key="data.value">{{data.label}}</a-select-option>
          </a-select>
        </a-form-item>
      </a-col>
    </a-row>

    <a-row :gutter="18">
      <a-col :span="6" :offset="3">
        <a-form-item class="form-item" label="Rooms">
          <a-input-number v-model="form.rooms" :min="0.0" style="width: 100%;" />
        </a-form-item>
      </a-col>
      <a-col :span="6">
        <a-form-item class="form-item" label="Nights">
          <a-input-number v-model="form.nights" :min="0.0" style="width: 100%;" />
        </a-form-item>
      </a-col>

      <a-col :span="6">
        <a-form-item class="form-item" label="Blocked Rooms">
          <a-input v-model="form.blocked_room" disabled />
        </a-form-item>
      </a-col>
    </a-row>

    <a-row :gutter="18">
      <a-col :span="1" :offset="3">
        <a-form-item class="form-item" label="SGL">
          <a-input-number v-model="form.sgl" :min="0" style="width: 100%;" />
        </a-form-item>
      </a-col>
      <a-col :span="2">
        <a-form-item class="form-item" label="SGL/SP">
          <a-input-number
            v-model="form.sgl_price"
            :min="0.0"
            :defaultValue="0.0"
            :precision="2"
            :step="0.5"
            style="width: 100%;"
          />
        </a-form-item>
      </a-col>

      <a-col :span="1">
        <a-form-item class="form-item" label="DBL">
          <a-input-number v-model="form.dbl" :min="0" style="width: 100%;" />
        </a-form-item>
      </a-col>
      <a-col :span="2">
        <a-form-item class="form-item" label="DBL/SP">
          <a-input-number
            v-model="form.dbl_price"
            :min="0.0"
            :defaultValue="0.0"
            :precision="2"
            :step="0.5"
            style="width: 100%;"
          />
        </a-form-item>
      </a-col>

      <a-col :span="1">
        <a-form-item class="form-item" label="TWN">
          <a-input-number v-model="form.twn" :min="0" style="width: 100%;" />
        </a-form-item>
      </a-col>
      <a-col :span="2">
        <a-form-item class="form-item" label="TWN/SP">
          <a-input-number
            v-model="form.twn_price"
            :min="0.0"
            :defaultValue="0.0"
            :precision="2"
            :step="0.5"
            style="width: 100%;"
          />
        </a-form-item>
      </a-col>

      <a-col :span="1">
        <a-form-item class="form-item" label="TPL">
          <a-input-number v-model="form.tpl" :min="0" style="width: 100%;" />
        </a-form-item>
      </a-col>
      <a-col :span="2">
        <a-form-item class="form-item" label="TPL/SP">
          <a-input-number
            v-model="form.tpl_price"
            :min="0.0"
            :defaultValue="0.0"
            :precision="2"
            :step="0.5"
            style="width: 100%;"
          />
        </a-form-item>
      </a-col>

      <a-col :span="1">
        <a-form-item class="form-item" label="EXB">
          <a-input-number v-model="form.exb" :min="0" style="width: 100%;" />
        </a-form-item>
      </a-col>
      <a-col :span="2">
        <a-form-item class="form-item" label="EXB/SP">
          <a-input-number
            v-model="form.exb_price"
            :min="0.0"
            :defaultValue="0.0"
            :precision="2"
            :step="0.5"
            style="width: 100%;"
          />
        </a-form-item>
      </a-col>
      <a-col :span="3">
        <a-form-item class="form-item" label="Total SP">
          <a-input-number v-model="form.total_price" style="width: 100%;" disabled />
        </a-form-item>
      </a-col>
    </a-row>

    <a-row :gutter="18">
      <a-col :span="2" :offset="3">
        <a-form-item class="form-item" label="SGL/CP">
          <a-input-number
            v-model="form.sgl_cost_price"
            :min="0.0"
            :defaultValue="0.0"
            :precision="2"
            :step="0.5"
            style="width: 100%;"
          />
        </a-form-item>
      </a-col>

      <a-col :span="2">
        <a-form-item class="form-item" label="DBL/CP">
          <a-input-number
            v-model="form.dbl_cost_price"
            :min="0.0"
            :defaultValue="0.0"
            :precision="2"
            :step="0.5"
            style="width: 100%;"
          />
        </a-form-item>
      </a-col>

      <a-col :span="2">
        <a-form-item class="form-item" label="TWN/CP">
          <a-input-number
            v-model="form.twn_cost_price"
            :min="0.0"
            :defaultValue="0.0"
            :precision="2"
            :step="0.5"
            style="width: 100%;"
          />
        </a-form-item>
      </a-col>

      <a-col :span="2">
        <a-form-item class="form-item" label="TPL/CP">
          <a-input-number
            v-model="form.tpl_cost_price"
            :min="0.0"
            :defaultValue="0.0"
            :precision="2"
            :step="0.5"
            style="width: 100%;"
          />
        </a-form-item>
      </a-col>

      <a-col :span="2">
        <a-form-item class="form-item" label="EXB/CP">
          <a-input-number
            v-model="form.exb_cost_price"
            :min="0.0"
            :defaultValue="0.0"
            :precision="2"
            :step="0.5"
            style="width: 100%;"
          />
        </a-form-item>
      </a-col>

      <a-col :span="2">
        <a-form-item class="form-item" label="Child/CP">
          <a-input-number
            v-model="form.child_cost_price"
            :min="0.0"
            :defaultValue="0.0"
            :precision="2"
            :step="0.5"
            style="width: 100%;"
          />
        </a-form-item>
      </a-col>

      <a-col :span="2">
        <a-form-item class="form-item" label="Tourism Fees">
          <a-input-number
            v-model="form.tourism_fees"
            :min="0.0"
            :defaultValue="0.0"
            :precision="2"
            :step="0.5"
            style="width: 100%;"
          />
        </a-form-item>
      </a-col>

      <a-col :span="2">
        <a-form-item class="form-item" label="Vat">
          <a-input-number
            v-model="form.vat"
            :min="0.0"
            :defaultValue="0.0"
            :precision="2"
            :step="0.5"
            style="width: 100%;"
          />
        </a-form-item>
      </a-col>

      <a-col :span="2">
        <a-form-item class="form-item" label="Total CP">
          <a-input-number v-model="form.total_cost_price" style="width: 100%;" disabled />
        </a-form-item>
      </a-col>
    </a-row>

    <a-row :gutter="18">
      <a-col :span="9" :offset="3">
        <a-form-item class="form-item" label="Upload/RoomList"></a-form-item>
      </a-col>
      <a-col :span="9" :offset="3">
        <a-form-item class="form-item" label="Upload/ConfList"></a-form-item>
      </a-col>
    </a-row>

    <a-row :gutter="18">
      <a-col :span="18" :offset="3">
        <a-form-item class="form-item" label="Cancellation Policy">
          <a-textarea v-model="form.cancel_policy"></a-textarea>
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
import { createBooking, updateBooking, getBooking } from "@/api/booking";
import moment from "moment";

const RoomStatus = [
  { value: 1, label: "Inquiry" },
  { value: 2, label: "Confirm" },
  { value: 3, label: "Room_Blocked" },
  { value: 4, label: "Email_Sent" },
  { value: 5, label: "OP-Cancelled" },
  { value: 6, label: "Roomlist_Sent" },
  { value: 7, label: "Inquriy_Sent" },
  { value: 8, label: "AC_Paid" },
  { value: 9, label: "AC_Panding" }
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
        this.formatBlockedRooms();
        this.form.total_price =
          Number(this.form.sgl | 0) * Number(this.form.sgl_price | 0) +
          Number(this.form.dbl | 0) * Number(this.form.dbl_price | 0) +
          Number(this.form.twn | 0) * Number(this.form.twn_price | 0) +
          Number(this.form.tpl | 0) * Number(this.form.tpl_price | 0) +
          Number(this.form.exb | 0) * Number(this.form.exb_price | 0);

        this.form.total_cost_price =
          Number(this.form.sgl | 0) * Number(this.form.sgl_cost_price | 0) +
          Number(this.form.dbl | 0) * Number(this.form.dbl_cost_price | 0) +
          Number(this.form.twn | 0) * Number(this.form.twn_cost_price | 0) +
          Number(this.form.tpl | 0) * Number(this.form.tpl_cost_price | 0) +
          Number(this.form.exb | 0) * Number(this.form.exb_cost_price | 0) +
          Number(this.form.child_cost_price | 0) +
          Number(this.form.tourism_fees | 0) +
          Number(this.form.vat | 0);
      }
    }
  },
  data() {
    return {
      RoomStatus,
      loading: false,
      spinning: false,
      form: {
        id: undefined,
        product: "",
        category: 4,
        start_date: null,
        end_date: null,
        booking_date: null,
        payment_due_date: null,
        room_update: null,
        emailed: null,
        cancel_date: null,
        status: 1,
        rooms: 0,
        nights: 0,

        blocked_room: "",
        used_room: "",
        sgl: 0,
        sgl_price: 0.0,
        sgl_cost_price: 0.0,
        dbl: 0,
        dbl_price: 0.0,
        dbl_cost_price: 0.0,
        twn: 0,
        twn_price: 0.0,
        twn_cost_price: 0.0,
        tpl: 0,
        tpl_price: 0.0,
        tpl_cost_price: 0.0,
        exb: 0,
        exb_price: 0.0,
        exb_cost_price: 0.0,
        child_cost_price: 0.0,
        tourism_fees: 0.0,
        vat: 0.0,
        total_price: 0.0,
        total_cost_price: 0.0,
        conf_list: null,
        room_list: null,
        remark: "",
        ref: "",
        order_id: undefined
      }
    };
  },
  methods: {
    formatBlockedRooms() {
      var temp = "";
      if (this.form.sgl) {
        temp = temp.concat("SGL" + "-" + this.form.sgl + " ");
      }
      if (this.form.dbl) {
        temp = temp.concat("DBL" + "-" + this.form.dbl + " ");
      }
      if (this.form.twn) {
        temp = temp.concat("TWN" + "-" + this.form.twn + " ");
      }
      if (this.form.tpl) {
        temp = temp.concat("TPL" + "-" + this.form.tpl + " ");
      }
      if (this.form.exb) {
        temp = temp.concat("EXB" + "-" + this.form.exb + " ");
      }
      this.form.blocked_room = temp;
    },
    initData(data) {
      this.form = Object.assign(this.form, {
        order_id: Number(data.id)
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
          : null,
        payment_due_date: data.payment_due_date
          ? moment(data.payment_due_date, "YYYY-MM-DD")
          : null,
        room_update: data.room_update
          ? moment(data.room_update, "YYYY-MM-DD")
          : null,
        emailed: data.emailed ? moment(data.emailed, "YYYY-MM-DD") : null,
        cancel_date: data.cancel_date
          ? moment(data.cancel_date, "YYYY-MM-DD")
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
          : null,
        payment_due_date: data.payment_due_date
          ? data.payment_due_date.format("YYYY-MM-DD")
          : null,
        room_update: data.room_update
          ? data.room_update.format("YYYY-MM-DD")
          : null,
        emailed: data.emailed ? data.emailed.format("YYYY-MM-DD") : null,
        cancel_date: data.cancel_date
          ? data.cancel_date.format("YYYY-MM-DD")
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