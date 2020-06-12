<template>
  <v-container>
    <!-- <v-row align="center" justify="center" class="display-1 py-4">Customer Management</v-row> -->
    <v-row>
      <v-col>
        <v-card flat>
          <v-tabs fixed-tabs v-model="tab">
            <v-tab v-for="(op, idx) in operations" :key="idx">{{ op }}</v-tab>
          </v-tabs>
          <v-tabs-items v-model="tab">
            <v-tab-item v-for="(op, idx) in operations" :key="idx">
              <v-card outlined class="my-4 px-4">
                <v-card-title>{{ cardOneTitle[idx] }}</v-card-title>
                <v-form>
                  <v-row>
                    <v-col cols="2">
                      <v-text-field
                        v-model="inputData.id"
                        counter="256"
                        label="Account ID"
                        outlined
                        dense
                      ></v-text-field>
                    </v-col>
                    <v-col cols="2">
                      <v-text-field
                        v-model="inputData.balance"
                        counter="256"
                        label="Account balance"
                        outlined
                        dense
                      ></v-text-field>
                    </v-col>
                    <v-col cols="3">
                      <v-text-field
                        v-model="inputData.openBank"
                        counter="256"
                        label="Account Open bank"
                        outlined
                        dense
                      ></v-text-field>
                    </v-col>
                    <v-col cols="3">
                      <v-menu
                        v-model="tabMenu[idx].menu1"
                        :close-on-content-click="false"
                        transition="scale-transition"
                        offset-y
                      >
                        <template v-slot:activator="{ on, attrs }">
                          <v-text-field
                            v-model="inputData.openDate"
                            label="Account Open Date"
                            outlined
                            dense
                            readonly
                            v-bind="attrs"
                            v-on="on"
                          ></v-text-field>
                        </template>
                        <v-date-picker
                          v-model="inputData.openDate"
                          no-title
                          @input="tabMenu[idx].menu1 = false"
                        ></v-date-picker>
                      </v-menu>
                    </v-col>
                    <v-col cols="2">
                      <v-select
                        label="Account Type"
                        v-model="inputData.type"
                        :items="['Checking', 'Savings']"
                        outlined
                        dense
                      ></v-select>
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-col cols="2">
                      <v-text-field
                        v-model="inputData.customerID"
                        counter="256"
                        label="Customer ID"
                        outlined
                        dense
                      ></v-text-field>
                    </v-col>
                    <v-col cols="2" v-if="inputData.type == 'Checking'">
                      <v-text-field
                        v-model="inputData.checkingAccountCredit"
                        counter="256"
                        label="Credit"
                        outlined
                        dense
                      ></v-text-field>
                    </v-col>
                    <v-col cols="2" v-if="inputData.type == 'Savings'">
                      <v-text-field
                        v-model="inputData.savingsAccountRate"
                        counter="256"
                        label="Rate"
                        outlined
                        dense
                      ></v-text-field>
                    </v-col>
                    <v-col cols="2" v-if="inputData.type == 'Savings'">
                      <v-text-field
                        v-model="inputData.savingsAccountCurrencyType"
                        counter="256"
                        label="Currency Type"
                        outlined
                        dense
                      ></v-text-field>
                    </v-col>
                  </v-row>
                </v-form>
              </v-card>
              <v-card outlined class="my-4 px-4" v-if="idx == 2">
                <v-card-title>更新后的账户信息</v-card-title>
                <v-form>
                  <v-row>
                    <v-col cols="2">
                      <v-text-field
                        v-model="modifyData.id"
                        counter="256"
                        label="Account ID"
                        outlined
                        dense
                      ></v-text-field>
                    </v-col>
                    <v-col cols="2">
                      <v-text-field
                        v-model="modifyData.balance"
                        counter="256"
                        label="Account balance"
                        outlined
                        dense
                      ></v-text-field>
                    </v-col>
                    <v-col cols="3">
                      <v-text-field
                        v-model="modifyData.openBank"
                        counter="256"
                        label="Account Open bank"
                        outlined
                        dense
                      ></v-text-field>
                    </v-col>
                    <v-col cols="3">
                      <v-menu
                        v-model="tabMenu[idx].menu2"
                        :close-on-content-click="false"
                        transition="scale-transition"
                        offset-y
                      >
                        <template v-slot:activator="{ on, attrs }">
                          <v-text-field
                            v-model="modifyData.openDate"
                            label="Account Open Date"
                            readonly
                            outlined
                            dense
                            v-bind="attrs"
                            v-on="on"
                          ></v-text-field>
                        </template>
                        <v-date-picker
                          v-model="modifyData.openDate"
                          no-title
                          @input="tabMenu[idx].menu2 = false"
                        ></v-date-picker>
                      </v-menu>
                    </v-col>
                    <v-col cols="2">
                      <v-select
                        label="Account Type"
                        v-model="modifyData.type"
                        :items="['Checking', 'Savings']"
                        outlined
                        dense
                      ></v-select>
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-col cols="2">
                      <v-text-field
                        v-model="modifyData.customerID"
                        counter="256"
                        label="Customer ID"
                        outlined
                        dense
                      ></v-text-field>
                    </v-col>
                    <v-col cols="2" v-if="modifyData.type == 'Checking'">
                      <v-text-field
                        v-model="modifyData.checkingAccountCredit"
                        counter="256"
                        label="Credit"
                        outlined
                        dense
                      ></v-text-field>
                    </v-col>
                    <v-col cols="2" v-if="modifyData.type == 'Savings'">
                      <v-text-field
                        v-model="modifyData.savingsAccountRate"
                        counter="256"
                        label="Rate"
                        outlined
                        dense
                      ></v-text-field>
                    </v-col>
                    <v-col cols="2" v-if="modifyData.type == 'Savings'">
                      <v-text-field
                        v-model="modifyData.savingsAccountCurrencyType"
                        counter="256"
                        label="Currency Type"
                        outlined
                        dense
                      ></v-text-field>
                    </v-col>
                  </v-row>
                </v-form>
              </v-card>
              <v-card flat class="my-4 px-4">
                <v-row>
                  <v-col cols="2" offset="4">
                    <v-btn :disabled="!commitBtnValid" color="success" @click="commitForm">Commit</v-btn>
                  </v-col>
                  <v-col cols="2">
                    <v-btn :disabled="!resetBtnValid" color="warning" @click="resetForm">Reset</v-btn>
                  </v-col>
                </v-row>
              </v-card>
              <v-divider class="py-2"></v-divider>

              <v-card outlined>
                <v-card-title>{{ cardStatusTitle[idx] }}</v-card-title>
              </v-card>
            </v-tab-item>
          </v-tabs-items>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "AccountManage",

  data: () => ({
    tabMenu: [
      {
        menu1: false,
        menu2: false
      },
      {
        menu1: false,
        menu2: false
      },
      {
        menu1: false,
        menu2: false
      },
      {
        menu1: false,
        menu2: false
      }
    ],
    tab: 0,
    operations: ["Create", "Delete", "Modify", "Search"],
    cardOneTitle: [
      "需要创建的账户的信息",
      "需要删除的账户的信息",
      "更新前的账户信息",
      "需要搜索的账户信息"
    ],
    cardStatusTitle: [
      "创建账户状态",
      "删除账户状态",
      "更新账户状态",
      "搜索账户状态"
    ],
    inputData: {
      id: "",
      balance: "",
      openDate: "",
      type: "",
      checkingAccountCredit: "",
      savingsAccountRate: "",
      savingsAccountCurrencyType: "",
      openBank: "",
      customerID: ""
    },
    modifyData: {
      id: "",
      balance: "",
      openDate: "",
      type: "",
      checkingAccountCredit: "",
      savingsAccountRate: "",
      savingsAccountCurrencyType: "",
      openBank: "",
      customerID: ""
    }
  }),
  computed: {
    formOneEmpty: function() {
      let result = this.inputData["id"].length == 0;
      for (let item in this.inputData) {
        result = result && this.inputData[item].length == 0;
      }
      return result;
    },
    formTwoEmpty: function() {
      let result = this.modifyData["id"].length == 0;
      for (let item in this.modifyData) {
        result = result && this.modifyData[item].length == 0;
      }
      return result;
    },
    checkFormOneCreate: function() {
      let result = true;
      if (this.inputData.type == "Checking") {
        for (let item in this.inputData) {
          if (
            item == "savingsAccountRate" ||
            item == "savingsAccountCurrencyType"
          ) {
            continue;
          }
          result = result && this.inputData[item] != "";
        }
      } else if (this.inputData.type == "Savings") {
        for (let item in this.inputData) {
          if (item == "checkingAccountCredit") {
            continue;
          }
          result = result && this.inputData[item] != "";
        }
      } else {
        result = false;
      }
      return result;
    },
    resetBtnValid: function() {
      let result = false;
      if (this.tab == 2) {
        // if modify
        result = !this.formOneEmpty || !this.formTwoEmpty;
      } else {
        result = !this.formOneEmpty;
      }
      return result;
    },
    commitBtnValid: function() {
      let result = false;
      if (this.tab == 0) {
        // if modify
        result = this.checkFormOneCreate;
      } else if (this.tab == 1) {
        result = !this.formOneEmpty;
      } else if (this.tab == 2) {
        result = !this.formOneEmpty && !this.formTwoEmpty;
      } else {
        result = !this.formOneEmpty;
      }
      return result;
    }
  },
  methods: {
    resetForm: function() {
      for (let item in this.inputData) {
        this.inputData[item] = "";
      }
    },
    commitForm: function() {
      alert(this.checkFormOneCreate);
    }
  }
};
</script>
