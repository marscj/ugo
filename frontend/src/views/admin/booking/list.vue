<template >
  <a-card class="table-page-search-wrapper" :bordered="false">
    <template slot="extra">
      <a-form layout="inline">
        <a-row :gutter="16">
          <a-col :span="6">
            <a-form-item label="BookingID">
              <a-input v-model="queryParam.bookingID" placeholder />
            </a-form-item>
          </a-col>
          <a-col :span="6">
            <a-form-item label="OrderID">
              <a-input v-model="queryParam.orderID" />
            </a-form-item>
          </a-col>
          <a-col :span="6">
            <a-form-item label="Booking Date">
              <a-range-picker :value="booking_date" @change="(value) => booking_date = value"></a-range-picker>
            </a-form-item>
          </a-col>
          <div v-if="queryParam.category == 4">
            <a-col :span="6">
              <a-form-item label="CheckIn">
                <a-range-picker :value="start_date" @change="(value) => start_date = value"></a-range-picker>
              </a-form-item>
            </a-col>

            <a-col :span="6">
              <a-form-item label="CheckOut">
                <a-range-picker :value="end_date" @change="(value) => end_date = value"></a-range-picker>
              </a-form-item>
            </a-col>
          </div>

          <div v-else-if="queryParam.category == 3">
            <a-col :span="6">
              <a-form-item label="Start Date">
                <a-range-picker :value="start_date" @change="(value) => start_date = value"></a-range-picker>
              </a-form-item>
            </a-col>

            <a-col :span="6">
              <a-form-item label="End Date">
                <a-range-picker :value="end_date" @change="(value) => end_date = value"></a-range-picker>
              </a-form-item>
            </a-col>
          </div>

          <a-col :span="6" v-else>
            <a-form-item label="Action Date">
              <a-range-picker :value="action_date" @change="(value) => action_date = value"></a-range-picker>
            </a-form-item>
          </a-col>
          
          <a-col :span="6">
            <a-form-item label="Product">
              <a-input v-model="queryParam.search" />
            </a-form-item>
          </a-col>
          <a-col :span="6">
            <a-form-item label="Guide">
              <a-input v-model="queryParam.guide" />
            </a-form-item>
          </a-col>
          <a-col :span="6">
            <a-form-item label="Driver">
              <a-input v-model="queryParam.driver" />
            </a-form-item>
          </a-col>
          <a-col :span="6">
            <a-form-item label="Vehicle">
              <a-input v-model="queryParam.vehicle" />
            </a-form-item>
          </a-col>
          <a-col :span="6">
            <a-form-item label="Officer">
              <a-input v-model="queryParam.officer" />
            </a-form-item>
          </a-col>
          <a-col :span="6">
            <a-form-item label="Operator">
              <a-input v-model="queryParam.operator" />
            </a-form-item>
          </a-col>
          <a-col :span="6">
            <a-form-item label="Status">
              <a-select
                :value="queryParam.status"
                @change="(value) => queryParam.status = value"
                :filterOption="false"
              >
                <a-select-option v-for="d in BookingStatus" :key="d.value">{{d.label}}</a-select-option>
              </a-select>
            </a-form-item>
          </a-col>
        </a-row>

        <a-button type="primary" @click="hanldeSearch">Search & Refresh</a-button>
        <a-button class="buttonStyle" type="primary" @click="exportModal.visible = true">Export</a-button>
      </a-form>
    </template>

    <s-table
      ref="table"
      size="default"
      :rowKey="(item) => item.id"
      :columns="columns"
      :data="loadData"
      bordered
      fixed
    >
      <span slot="action_date" slot-scope="text, data">
        <template>
          <span>{{data.action_date + ' ' + data.action_time | moment('YYYY-MM-DD HH:mm')}}</span>
        </template>
      </span>

      <span slot="hotel_sp" slot-scope="text, data">
        <template>
          <p class="booking-info" v-if="data.sgl">
            SGL:
            <span class="bold ligth-blue">{{data.sgl_price}}</span>
          </p>
          <p class="booking-info" v-if="data.dbl">
            DBL:
            <span class="bold ligth-blue">{{data.dbl_price}}</span>
          </p>
          <p class="booking-info" v-if="data.twn">
            TWN:
            <span class="bold ligth-blue">{{data.twn_price}}</span>
          </p>
          <p class="booking-info" v-if="data.tpl">
            TPL:
            <span class="bold ligth-blue">{{data.tpl_price}}</span>
          </p>
          <p class="booking-info" v-if="data.exb">
            EXB:
            <span class="bold ligth-blue">{{data.exb_price}}</span>
          </p>
        </template>
      </span>

      <span slot="hotel_cp" slot-scope="text, data">
        <template>
          <p class="booking-info" v-if="data.sgl">
            SGL:
            <span class="bold ligth-blue">{{data.sgl_cost_price}}</span>
          </p>
          <p class="booking-info" v-if="data.dbl">
            DBL:
            <span class="bold ligth-blue">{{data.dbl_cost_price}}</span>
          </p>
          <p class="booking-info" v-if="data.twn">
            TWN:
            <span class="bold ligth-blue">{{data.twn_cost_price}}</span>
          </p>
          <p class="booking-info" v-if="data.tpl">
            TPL:
            <span class="bold ligth-blue">{{data.tpl_cost_price}}</span>
          </p>
          <p class="booking-info" v-if="data.exb">
            EXB:
            <span class="bold ligth-blue">{{data.exb_cost_price}}</span>
          </p>
          <p class="booking-info" v-if="data.child_cost_price > 0">
            Child:
            <span class="bold ligth-blue">{{data.child_cost_price}}</span>
          </p>
          <p class="booking-info" v-if="data.tourism_fees > 0">
            Tourism fees:
            <span class="bold ligth-blue">{{data.tourism_fees}}</span>
          </p>
          <p class="booking-info" v-if="data.vat > 0">
            VAT:
            <span class="bold ligth-blue">{{data.vat}}</span>
          </p>
        </template>
      </span>

      <span slot="pax" slot-scope="text, data">
        <template>
          <p class="booking-info">
            Adult:
            <span class="bold ligth-blue">{{data.quantity}}</span>
          </p>
          <p class="booking-info" v-if="data.child_quantity">
            Child:
            <span class="bold ligth-blue">{{data.child_quantity}}</span>
          </p>
          <p class="booking-info" v-if="data.free_quantity">
            Free:
            <span class="bold ligth-blue">{{data.free_quantity}}</span>
          </p>
        </template>
      </span>

      <span slot="sp" slot-scope="text, data">
        <template>
          <p class="booking-info">
            Adult:
            <span class="bold ligth-blue">{{data.price}}</span>
          </p>
          <p class="booking-info" v-if="data.child_quantity">
            Child:
            <span class="bold ligth-blue">{{data.child_price}}</span>
          </p>
        </template>
      </span>

      <span slot="cp" slot-scope="text, data">
        <template>
          <p class="booking-info">
            Adult:
            <span class="bold ligth-blue">{{data.cost_price}}</span>
          </p>
          <p class="booking-info" v-if="data.child_quantity">
            Child:
            <span class="bold ligth-blue">{{data.child_cost_price}}</span>
          </p>
        </template>
      </span>

      <span slot="vat" slot-scope="text, data">
        <template>
          <span class="bold ligth-blue">{{data.vat}}</span>
        </template>
      </span>

      <span slot="total" slot-scope="text, data">
        <template>
          <p class="booking-info" v-if="data.total_price > 0">
            SP:
            <span class="bold ligth-blue">{{data.total_price}}</span>
          </p>
          <p class="booking-info" v-if="data.total_cost_price > 0">
            CP:
            <span class="bold ligth-blue">{{data.total_cost_price}}</span>
          </p>
        </template>
      </span>

      <span slot="source" slot-scope="text, data">
        <template>
          <div class="booking-info" v-if="data.guide">
            Guide:
            <span>{{data.guide}} -</span>
            <span>{{data.guide_mobile}}</span>
          </div>

          <div class="booking-info" v-if="data.driver">
            Driver:
            <span>{{data.driver}} -</span>
            <span>{{data.driver_mobile}}</span>
          </div>

          <div class="booking-info" v-if="data.vehicle">
            Vehicle:
            <span>{{data.vehicle}} -</span>
            <span>{{data.vehicle_model}}</span>
          </div>
        </template>
      </span>

      <span slot="location" slot-scope="text, data">
        <template>
          <p class="booking-info" v-if="data.guide">
            Time:
            <span>{{ data.pick_up_time | moment('MM-DD HH:mm')}}</span>
          </p>
          <p class="booking-info" v-if="data.driver">
            Pick Up:
            <span>{{data.pick_up_address}}</span>
          </p>

          <p class="booking-info" v-if="data.vehicle">
            Drop Off:
            <span>{{data.drop_off_address}}</span>
          </p>
        </template>
      </span>

      <span slot="create_at" slot-scope="text">
        <template>
          <span>{{text | moment('MM-DD HH:mm')}}</span>
        </template>
      </span>

      <span slot="status" slot-scope="text, data">
        <template v-action:edit>
          <span>{{BookingStatus[data.status].label}}</span>
        </template>
      </span>

      <span slot="action" slot-scope="text, data">
        <template v-action:edit>
          <router-link :to="{name: 'BookingEdit', params: {id: data.id}}" target="_blank">detail</router-link>
        </template>
      </span>
    </s-table>
  </a-card>
</template>

<script>
import { STable, Ellipsis } from "@/components";
import { getBookingList } from "@/api/booking";
import {
  RestaurantColumns,
  TourColumns,
  TransportColumns,
  HotelColumns
} from "./colums";
import moment from "moment";

const BookingStatus = [
  { value: 0, label: "All" },
  { value: 1, label: "Inquiry" },
  { value: 2, label: "Confirm" },
  { value: 3, label: "Padding" },
  { value: 4, label: "Email-Sent" },
  { value: 5, label: "OP-Cancelled" },
  { value: 6, label: "OP-Approved" }
];

export default {
  name: "BookingList",
  components: {
    STable,
    Ellipsis
  },
  props: {
    category: {
      type: Number,
      default: 1
    }
  },
  watch: {
    action_date: function(newQuestion, oldQuestion) {
      if (
        newQuestion != null &&
        newQuestion != undefined &&
        newQuestion.length > 0
      ) {
        this.queryParam.action_start_day = newQuestion[0].format("YYYY-MM-DD");
        this.queryParam.action_end_day = newQuestion[1].format("YYYY-MM-DD");
      } else {
        this.queryParam.action_start_day = undefined;
        this.queryParam.action_end_day = undefined;
      }
    },
    booking_date: function(newQuestion, oldQuestion) {
      if (
        newQuestion != null &&
        newQuestion != undefined &&
        newQuestion.length > 0
      ) {
        this.queryParam.booking_start_day = newQuestion[0].format("YYYY-MM-DD");
        this.queryParam.booking_end_day = newQuestion[1].format("YYYY-MM-DD");
      } else {
        this.queryParam.booking_start_day = undefined;
        this.queryParam.booking_end_day = undefined;
      }
    },
    start_date: function(newQuestion, oldQuestion) {
      if (
        newQuestion != null &&
        newQuestion != undefined &&
        newQuestion.length > 0
      ) {
        this.queryParam.start_start_day = newQuestion[0].format("YYYY-MM-DD");
        this.queryParam.start_end_day = newQuestion[1].format("YYYY-MM-DD");
      } else {
        this.queryParam.start_start_day = undefined;
        this.queryParam.start_end_day = undefined;
      }
    },
    end_date: function(newQuestion, oldQuestion) {
      if (
        newQuestion != null &&
        newQuestion != undefined &&
        newQuestion.length > 0
      ) {
        this.queryParam.end_start_day = newQuestion[0].format("YYYY-MM-DD");
        this.queryParam.end_end_day = newQuestion[1].format("YYYY-MM-DD");
      } else {
        this.queryParam.end_start_day = undefined;
        this.queryParam.end_end_day = undefined;
      }
    },
    $route: function(to, from) {
      this.initColunm(to);
      this.$refs.table.refresh();
    }
  },
  created() {
    this.initColunm(this.$route);
  },
  data() {
    return {
      BookingStatus,
      action_date: null,
      booking_date: null,
      start_date: null,
      end_date: null,
      columns: RestaurantColumns,
      queryParam: {
        category: 1,
        search: undefined,
        bookingID: undefined,
        orderID: undefined,
        officer: undefined,
        operator: undefined,
        guide: undefined,
        driver: undefined,
        status: undefined,
        vehicle: undefined,
        booking_start_day: undefined,
        booking_end_day: undefined,
        start_start_day: undefined,
        start_end_day: undefined,
        end_start_day: undefined,
        end_end_day: undefined,
        action_start_day: undefined,
        action_end_day: undefined
      },
      columns: RestaurantColumns,
      loadData: parameter => {
        return getBookingList(Object.assign(parameter, this.queryParam)).then(
          res => {
            return res.result;
          }
        );
      }
    };
  },
  methods: {
    hanldeSearch() {
      this.$refs.table.refresh();
    },
    initColunm(router) {
      if (router.name === "Restaurant") {
        this.columns = RestaurantColumns;
        this.queryParam.category = 1;
      } else if (router.name === "Tour") {
        this.columns = TourColumns;
        this.queryParam.category = 2;
      } else if (router.name === "Transport") {
        this.columns = TransportColumns;
        this.queryParam.category = 3;
      } else if (router.name === "Hotels") {
        this.columns = HotelColumns;
        this.queryParam.category = 4;
      }
    }
  }
};
</script>

<style >
.booking-info {
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

.ant-card-extra {
  width: 100%;
  padding: 16px 0;
  font-size: 14px;
  color: rgba(0, 0, 0, 0.65);
  font-weight: normal;
  margin-left: 0;
}

.ant-card-wider-padding .ant-card-body {
  padding: 24px 12px;
}

.buttonStyle {
  margin: 0px 8px;
}
</style>