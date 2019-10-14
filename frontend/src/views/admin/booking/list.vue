<template >
  <a-card class="table-page-search-wrapper" :bordered="false">
    <template slot="extra">
      <a-form layout="inline">
        <a-row :gutter="48">
          <a-col :xs="6" :md="6" :sm="24">
            <a-form-item label="OrderID">
              <a-input v-model="queryParam.orderID" placeholder />
            </a-form-item>
          </a-col>
          <a-col :xs="6" :md="6" :sm="24">
            <a-form-item label="Customer">
              <a-input v-model="queryParam.customer" placeholder />
            </a-form-item>
          </a-col>
          <a-col :xs="6" :md="6" :sm="24">
            <a-form-item label="Operator">
              <a-input v-model="queryParam.operator" placeholder />
            </a-form-item>
          </a-col>
          <a-col :xs="6" :md="6" :sm="24">
            <a-form-item label="Action Day">
              <a-range-picker :value="day" @change="(value) => day = value"></a-range-picker>
            </a-form-item>
          </a-col>

          <a-col :xs="6" :md="6" :sm="24">
            <a-form-item label="RelatedID">
              <a-input v-model="queryParam.relatedID" placeholder />
            </a-form-item>
          </a-col>
          <a-col :xs="8" :md="6" :sm="24">
            <a-form-item label="Product">
              <a-input v-model="queryParam.product" placeholder />
            </a-form-item>
          </a-col>
          <a-col :xs="8" :md="6" :sm="24">
            <a-form-item label="Variant">
              <a-input v-model="queryParam.variant" placeholder />
            </a-form-item>
          </a-col>
          <a-col :xs="8" :md="6" :sm="24">
            <a-form-item label="Status">
              <a-select
                :value="order_status"
                @change="(value) => order_status = value"
                :filterOption="false"
              >
                <a-select-option v-for="d in orderStatus" :key="d.value">{{d.label}}</a-select-option>
              </a-select>
            </a-form-item>
          </a-col>
        </a-row>

        <a-button type="primary" @click="hanldeSearch">Search & Refresh</a-button>
        <a-button class="buttonStyle" type="primary" @click="hanldeClean">Clean</a-button>
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
          <span>{{data['action_date'] + ' ' + data['action_time'] | moment('YYYY-MM-DD HH:mm')}}</span>
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
          <p class="booking-info">
            SP:
            <span class="bold ligth-blue">{{data.total_price}}</span>
          </p>
          <p class="booking-info">
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

      <span slot="action" slot-scope="text, data">
        <template v-action:edit>
          <router-link :to="{name: 'BookingEdit', params: {id: data.id}}" target="_blank" > detail</router-link>
        </template>
      </span>
    </s-table>
  </a-card>
</template>

<script>
import { STable, Ellipsis } from "@/components";
import { getBookingList } from "@/api/booking";
import moment from "moment";

export default {
  name: "BookingList",
  components: {
    STable,
    Ellipsis
  },
  data() {
    const RestaurantColumns = [
      {
        title: "BookingID",
        dataIndex: "bookingID",
        width: "100px"
      },
      {
        title: "OrderID",
        dataIndex: "order_id",
        width: "100px"
      },
      {
        title: "Restaurant & Meal",
        dataIndex: "product",
        width: "180px"
      },
      {
        title: "Action Date",
        scopedSlots: { customRender: "action_date" },
        width: "130px"
      },
      {
        title: "Pax",
        scopedSlots: { customRender: "pax" },
        width: "80px"
      },
      {
        title: "SP",
        scopedSlots: { customRender: "sp" },
        width: "110px"
      },
      {
        title: "CP",
        scopedSlots: { customRender: "cp" },
        width: "110px"
      },
      {
        title: "Vat",
        scopedSlots: { customRender: "vat" },
        width: "80px"
      },
      {
        title: "Total",
        scopedSlots: { customRender: "total" },
        width: "110px"
      },
      {
        title: "Source",
        scopedSlots: { customRender: "source" },
        width: "120px"
      },
      {
        title: "Remarks",
        dataIndex: "remark"
      },
      {
        title: "Offer",
        dataIndex: "offer",
        width: "50px"
      },
      {
        title: "Operator",
        dataIndex: "operator",
        width: "50px"
      },
      {
        title: "Create",
        dataIndex: "create_at",
        scopedSlots: { customRender: "create_at" },
        width: "40px"
      },
      {
        title: "Action",
        dataIndex: "action",
        scopedSlots: { customRender: "action" },
        width: "60px",
        fixed: "right"
      }
    ];

    return {
      queryParam: {},
      columns: RestaurantColumns,
      loadData: parameter => {
        return getBookingList(Object.assign(parameter, this.queryParam)).then(
          res => {
            return res.result;
          }
        );
      }
    };
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
</style>