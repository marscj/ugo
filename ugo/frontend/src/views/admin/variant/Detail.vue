<template>
  <a-spin :spinning="spinning">
    <a-card title="Base">
      <a-form :form="form">
        <a-form-item label="Status" :required="true">
          <a-switch checkedChildren="上架" unCheckedChildren="下架" :checked="form.status" disabled />
        </a-form-item>
        <a-form-item
          label="Product(主产品)"
          :required="true"
          :validate-status="help.product_id == null || help.product_id === '' ?  null : 'error'"
          :help="help.product_id"
        >
          <a-select
            showSearch
            :value="form.product_id"
            placeholder="Product name"
            :defaultActiveFirstOption="false"
            :showArrow="false"
            :filterOption="false"
            @search="handleProductSearch"
            @change="handleProductChange"
            notFoundContent="没有找到"
          >
            <a-select-option v-for="d in productOption" :key="d.id">{{d.name}}</a-select-option>
          </a-select>
        </a-form-item>
        <a-form-item
          label="Name"
          :required="true"
          :validate-status="help.name == null || help.name === '' ?  null : 'error'"
          :help="help.name"
        >
          <a-input v-model="form.name"></a-input>
        </a-form-item>
        <a-form-item
          label="VariantID"
          :required="true"
          :validate-status="help.variantID == null || help.variantID === '' ?  null : 'error'"
          :help="help.variantID"
        >
          <a-input v-model="form.variantID"></a-input>
        </a-form-item>
        <a-form-item
          label="SKU"
          :required="true"
          :validate-status="help.sku == null || help.sku === '' ?  null : 'error'"
          :help="help.sku"
        >
          <a-input v-model="form.sku"></a-input>
        </a-form-item>
        <a-form-item label="Adult Status(成人票)" :required="true">
          <a-switch
            checkedChildren="上架"
            unCheckedChildren="下架"
            :checked="form.adult_status"
            @change="handleAdultChange"
          />
        </a-form-item>
        <a-form-item
          label="Adult Desc"
          :validate-status="help.adult_desc == null || help.adult_desc === '' ?  null : 'error'"
          :help="help.adult_desc"
          v-if="form.adult_status"
        >
          <a-input v-model="form.adult_desc"></a-input>
        </a-form-item>
        <!-- <a-form-item
          label="Adult Quantity"
          :required="true"
          :validate-status="help.adult_quantity == null || help.adult_quantity === '' ?  null : 'error'"
          :help="help.adult_quantity"
          v-if="form.adult_status"
        >
          <a-input-number
            v-model="form.adult_quantity"
            :min="1"
            :max="9999"
            :defaultValue="1"
            style="width:200px;"
          />
        </a-form-item>-->
        <a-form-item
          label="Adult Price(default price)"
          :required="true"
          :validate-status="help.adult_price == null || help.adult_price === '' ?  null : 'error'"
          :help="help.adult_price"
          v-if="form.adult_status"
        >
          <a-input-number
            v-model="form.adult_price"
            :min="0.0"
            :max="99999.99"
            :defaultValue="0.0"
            :precision="2"
            :step="0.5"
            style="width:200px;"
          />
        </a-form-item>
        <a-form-item label="Child Status(儿童票)" :required="true">
          <a-switch
            checkedChildren="上架"
            unCheckedChildren="下架"
            :checked="form.child_status"
            @change="handleChildChange"
          />
        </a-form-item>
        <a-form-item
          label="Child Desc"
          :validate-status="help.child_desc == null || help.child_desc === '' ?  null : 'error'"
          :help="help.child_desc"
          v-if="form.child_status"
        >
          <a-input v-model="form.child_desc"></a-input>
        </a-form-item>
        <!-- <a-form-item
          label="Child Quantity"
          :required="true"
          :validate-status="help.child_quantity == null || help.child_quantity === '' ?  null : 'error'"
          :help="help.child_quantity"
          v-if="form.child_status"
        >
          <a-input-number
            v-model="form.child_quantity"
            :min="1"
            :max="9999"
            :defaultValue="1"
            style="width:200px;"
          />
        </a-form-item>-->
        <a-form-item
          label="Child Price(default price)"
          :required="true"
          :validate-status="help.child_price == null || help.child_price === '' ?  null : 'error'"
          :help="help.child_price"
          v-if="form.child_status"
        >
          <a-input-number
            v-model="form.child_price"
            :min="0.0"
            :max="99999.99"
            :defaultValue="0.0"
            :precision="2"
            :step="0.5"
            style="width:200px;"
          />
        </a-form-item>
      </a-form>
    </a-card>

    <a-row style="margin-top:20px">
      <a-col span="2">
        <a-button type="primary" html-type="submit" @click="handleSubmit">Submit</a-button>
      </a-col>
      <a-col span="2">
        <a-button @click="handleGoBack">Return</a-button>
      </a-col>
    </a-row>
  </a-spin>
</template>

<script>
import { checkError } from "@/views/utils/error";
import { getVariant, updateVariant, createVariant } from "@/api/variant";
import { getProductList } from "@/api/product";

export default {
  name: "ProductDetail",
  props: {
    isEdit: {
      type: Boolean,
      default: false
    }
  },
  data() {
    return {
      form: {
        status: false,
        product_id: undefined,
        adult_status: false,
        adult_desc: undefined,
        adult_quantity: undefined,
        adult_price: undefined,
        child_status: false,
        child_desc: undefined,
        child_quantity: undefined,
        child_price: undefined
      },
      price: [],
      help: {},
      productOption: [],
      spinning: false,
      columns: [
        {
          title: '#',
          dataIndex: 'id',
          width: 40,
        },
        {
          title: "User",
          dataIndex: "user",
        },
        {
          title: "Current Lev",
          dataIndex: "curLev",
        },
        {
          title: "Lev1",
          dataIndex: "lve1",
        },
        {
          title: "Lev2",
          dataIndex: "lve2",
        },
        {
          title: "Lev3",
          dataIndex: "lve3",
        },
        {
          title: "Lev4",
          dataIndex: "lve4",
        },
        {
          title: "Lev5",
          dataIndex: "lve5",
        }
      ]
    };
  },
  created() {
    this.handleProductSearch(null);
    if (this.isEdit) {
      const id = this.$route.params && this.$route.params.id;
      this.fetch(id);
    }
  },
  methods: {
    handleGoBack() {
      this.$router.go(-1);
    },
    fetch(id) {
      this.spinning = true;
      getVariant(id)
        .then(res => {
          const { result } = res;
          this.form = result;
          this.product = result.product.id;
        })
        .finally(() => {
          this.spinning = false;
        });
    },
    updateForm(data) {
      this.spinning = true;
      updateVariant(this.$route.params.id, data)
        .then(res => {
          const { result } = res;
          this.handleGoBack();
        })
        .catch(error => {
          this.checkError(error);
        })
        .finally(() => {
          this.spinning = false;
        });
    },
    createForm(data) {
      this.spinning = true;
      createVariant(data)
        .then(res => {
          const { result } = res;
          this.$router.replace({
            name: "VariantEdit",
            params: { id: result.id }
          });
        })
        .catch(error => {
          this.checkError(error);
        })
        .finally(() => {
          this.spinning = false;
        });
    },
    handleProductSearch(value) {
      getProductList({ search: value }).then(res => {
        const { result } = res;
        this.productOption = result;
      });
    },
    handleProductChange(value) {
      this.form.product_id = value;
    },
    handleAdultChange(value) {
      this.form.adult_status = value;
      this.handleStatusChange();
    },
    handleChildChange(value) {
      this.form.child_status = value;
      this.handleStatusChange();
    },
    checkError(error) {
      var errors = checkError(
        error,
        "status",
        "variantID",
        "name",
        "sku",
        "adult_status",
        "adult_desc",
        "adult_quantity",
        "adult_price",
        "child_status",
        "child_desc",
        "child_quantity",
        "child_price",
        "product_id"
      );

      this.help = {
        status: errors["category"],
        variantID: errors["variantID"],
        name: errors["name"],
        sku: errors["sku"],
        adult_status: errors["adult_status"],
        adult_desc: errors["adult_desc"],
        adult_quantity: errors["adult_quantity"],
        adult_price: errors["adult_price"],
        child_status: errors["child_status"],
        child_desc: errors["child_desc"],
        child_quantity: errors["child_quantity"],
        child_price: errors["child_price"],
        product_id: errors["product_id"]
      };

      for (var key in errors) {
        if (errors[key]) {
          this.$notification["error"]({
            message: key,
            description: errors[key],
            duration: 4
          });
        }
      }
    },
    initData(data) {
      if (this.isEdit) {
        this.$route.meta.title = data.name;
        this.$emit("title");
      }
    },
    handleSubmit() {
      if (this.isEdit) {
        this.updateForm(this.form);
      } else {
        this.createForm(this.form);
      }
    },
    handleStatusChange() {
      if (this.form.adult_status || this.form.child_status) {
        this.form.status = true;
      } else {
        this.form.status = false;
      }
    },
    handleNewPrice() {
      this.$refs.modal.add({
        variant_id: this.form.id
      })
    },
    handleCreatePrice (value) {
      this.price.push(value)
    },  
    handleUpdatePrice (value) {
      this.price = this.price.map(function (f) {
        if (f && f.id === value.id) {
          return value
        } 
        return f
      })
    },
    getPrice() {
      this.spinning = true
      getPriceList().then((res) => {
        const { result } = res
        this.price = result
      })
      .finally(() => {
        this.spinning = false
      })
    },
    handleDeletePrice (value) {
      this.getPrice()
    }
  }
};
</script>
