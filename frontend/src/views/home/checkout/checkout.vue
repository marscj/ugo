<template>
  <a-card :bordered="false">
    <a-steps class="steps" :current="currentTab">
      <a-step title="填写订单信息" />
      <a-step title="确认订单信息" />
      <a-step title="完成" />
    </a-steps>
    <div class="content">
      <step1 v-if="currentTab === 0" @nextStep="nextStep" :form="form"/>
      <step2 v-if="currentTab === 1" @nextStep="nextStep" @prevStep="prevStep" :form="form"/>
      <step3 v-if="currentTab === 2" @prevStep="prevStep" @finish="finish" :form="form"/>
    </div>
  </a-card>
</template>

<script>
import Step1 from './Step1'
import Step2 from './Step2'
import Step3 from './Step3'
export default {
  components: {
    Step1,
    Step2,
    Step3
  },
  data() {
    return {
      form: this.$route.query,
      currentTab: 0,
    };
  },
  methods: {
    nextStep () {
      if (this.currentTab < 2) {
        this.currentTab += 1
      }
    },
    prevStep () {
      if (this.currentTab > 0) {
        this.currentTab -= 1
      }
    },
    finish () {
      this.currentTab = 0
      this.$router.replace({name: 'Home'})
    }
  }
};
</script>
