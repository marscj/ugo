<template>
  <a-modal
    key="formkey"
    :title="title"
    :visible="visible"
    :confirmLoading="confirmLoading"
    @ok="handleSubmit"
    @cancel="visible=false"
  >
    <template slot="footer">
      <a-button key="back" @click="visible=false">Return</a-button>
      <a-button key="submit" :type="submitButton.type" @click="handleSubmit">{{submitButton.name}}</a-button>
    </template>

    <a-spin :spinning="confirmLoading">
      <a-form :form="form">
        <a-form-item label="ID" :labelCol="labelCol" :wrapperCol="wrapperCol">
          <a-input v-decorator="['id']" :disabled="true" />
        </a-form-item>
        <a-form-item label="Variant ID:" :labelCol="labelCol" :wrapperCol="wrapperCol">
          <a-input v-decorator="['variant_id']" :disabled="true" />
        </a-form-item>
        <a-form-item
          label="User"
          :labelCol="labelCol"
          :wrapperCol="wrapperCol"
        >
          <a-select
            v-decorator="[
                'user_id',
                {rules: [{ required: true, message: 'Please select user.' }]}
            ]"
            placeholder="Please select a user"
          >
            <a-select-option v-for="data in userOption" :key="data.id">{{data.username}}</a-select-option>
          </a-select>
        </a-form-item>
        <a-form-item
          label="Current Lev"
          :labelCol="labelCol"
          :wrapperCol="wrapperCol"
          :validate-status="validate['curLev'] != null ? 'error' : null"
          :help="validate['curLev']"
        >
          <a-input-number
            :min="1"
            :max="5"
            v-decorator="['curLev', {rules: [{required: true}], initialValue: 1}]"
          />
        </a-form-item>
        <a-form-item
          label="Lev1"
          :labelCol="labelCol"
          :wrapperCol="wrapperCol"
          :validate-status="validate['lev1'] != null ? 'error' : null"
          :help="validate['lev1']"
        >
          <a-input-number
            :min="0.0"
            :max="99999.99"
            :precision="2"
            :step="0.5"
            v-decorator="['lev1', {rules: [{required: true}], initialValue: 0.0}]"
          />
        </a-form-item>
        <a-form-item
          label="Lev2"
          :labelCol="labelCol"
          :wrapperCol="wrapperCol"
          :validate-status="validate['lev2'] != null ? 'error' : null"
          :help="validate['lev2']"
        >
          <a-input-number
            :min="0.0"
            :max="99999.99"
            :precision="2"
            :step="0.5"
            v-decorator="['lev2', {rules: [{required: true}], initialValue: 0.0}]"
          />
        </a-form-item>
        <a-form-item
          label="Lev3"
          :labelCol="labelCol"
          :wrapperCol="wrapperCol"
          :validate-status="validate['lev3'] != null ? 'error' : null"
          :help="validate['lev3']"
        >
          <a-input-number
            :min="0.0"
            :max="99999.99"
            :precision="2"
            :step="0.5"
            v-decorator="['lev3', {rules: [{required: true}], initialValue: 0.0}]"
          />
        </a-form-item>
        <a-form-item
          label="Lev4"
          :labelCol="labelCol"
          :wrapperCol="wrapperCol"
          :validate-status="validate['lev4'] != null ? 'error' : null"
          :help="validate['lev4']"
        >
          <a-input-number
            :min="0.0"
            :max="99999.99"
            :precision="2"
            :step="0.5"
            v-decorator="['lev4', {rules: [{required: true}], initialValue: 0.0}]"
          />
        </a-form-item>
        <a-form-item
          label="Lev5"
          :labelCol="labelCol"
          :wrapperCol="wrapperCol"
          :validate-status="validate['lev5'] != null ? 'error' : null"
          :help="validate['lev5']"
        >
          <a-input-number
            :min="0.0"
            :max="99999.99"
            :precision="2"
            :step="0.5"
            v-decorator="['lev5', {rules: [{required: true}], initialValue: 0.0}]"
          />
        </a-form-item>
      </a-form>
    </a-spin>
  </a-modal>
</template>