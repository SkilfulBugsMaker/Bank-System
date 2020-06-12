<template>
  <v-container>
    <!-- <v-row align="center" justify="center" class="display-1 py-4">Customer Management</v-row> -->
    <v-row>
      <v-col>
        <v-card flat>
          <v-tabs fixed-tabs v-model="tabOut">
            <v-tab v-for="(opOut, idxOut) in operationsOut" :key="idxOut">{{ opOut }}</v-tab>
          </v-tabs>
          <v-tabs-items v-model="tabOut">
            <v-tab-item v-for="(opOut, idxOut) in operationsOut" :key="idxOut">
              <v-card flat>
                <v-tabs fixed-tabs v-model="tabIn">
                  <v-tab v-for="(opIn, idxIn) in operationsIn" :key="idxIn">{{ opIn }}</v-tab>
                </v-tabs>
                <v-tabs-items v-model="tabIn">
                  <v-tab-item v-for="(opIn, idxIn) in operationsIn" :key="idxIn">
                    <v-card outlined class="my-4 px-4">
                      <v-card-title>{{ cardTitle[idxOut][idxIn] }}</v-card-title>
                      <v-form>
                        <v-row v-if="idxOut==0">
                          <v-col cols="2">
                            <v-text-field
                              v-model="inputDataLoan.id"
                              counter="256"
                              label="Loan ID"
                              outlined
                              dense
                            ></v-text-field>
                          </v-col>
                          <v-col cols="2">
                            <v-text-field
                              v-model="inputDataLoan.bankName"
                              counter="256"
                              label="Bank Name"
                              outlined
                              dense
                            ></v-text-field>
                          </v-col>
                          <v-col cols="2">
                            <v-text-field
                              v-model="inputDataLoan.money"
                              counter="256"
                              label="Loan Money"
                              outlined
                              dense
                            ></v-text-field>
                          </v-col>
                          <v-col cols="2">
                            <v-text-field
                              v-model="inputDataLoan.customerID"
                              counter="256"
                              label="Customer ID"
                              outlined
                              dense
                            ></v-text-field>
                          </v-col>
                        </v-row>
                        <v-row v-if="idxOut==1">
                          <v-col cols="2">
                            <v-text-field
                              v-model="inputDataLoanPayment.loanID"
                              counter="256"
                              label="Loan ID"
                              outlined
                              dense
                            ></v-text-field>
                          </v-col>
                          <v-col cols="2">
                            <v-text-field
                              v-model="inputDataLoanPayment.loanPaymentID"
                              counter="256"
                              label="Loan Payment ID"
                              outlined
                              dense
                            ></v-text-field>
                          </v-col>
                          <v-col cols="3">
                            <v-text-field
                              v-model="inputDataLoanPayment.money"
                              counter="256"
                              label="Loan Payment Money"
                              outlined
                              dense
                            ></v-text-field>
                          </v-col>
                          <v-col cols="3">
                            <v-menu
                              v-model="menus[idxIn]"
                              :close-on-content-click="false"
                              transition="scale-transition"
                              offset-y
                            >
                              <template v-slot:activator="{ on, attrs }">
                                <v-text-field
                                  v-model="inputDataLoanPayment.date"
                                  label="Loan Payment Date"
                                  readonly
                                  outlined
                                  dense
                                  v-bind="attrs"
                                  v-on="on"
                                ></v-text-field>
                              </template>
                              <v-date-picker
                                v-model="inputDataLoanPayment.date"
                                no-title
                                @input="menus[idxIn] = false"
                              ></v-date-picker>
                            </v-menu>
                          </v-col>
                        </v-row>
                      </v-form>
                    </v-card>
                    <v-card flat class="my-4 px-4">
                      <v-row>
                        <v-col cols="2" offset="4">
                          <v-btn
                            :disabled="!commitBtnValid"
                            color="success"
                            @click="commitForm"
                          >Commit</v-btn>
                        </v-col>
                        <v-col cols="2">
                          <v-btn :disabled="!resetBtnValid" color="warning" @click="resetForm">Reset</v-btn>
                        </v-col>
                      </v-row>
                    </v-card>
                    <v-divider class="py-2"></v-divider>

                    <v-card outlined>
                      <v-card-title>{{ cardStatusTitle[idxOut][idxIn] }}</v-card-title>
                    </v-card>
                  </v-tab-item>
                </v-tabs-items>
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
  name: "LoanManage",

  data: () => ({
    menus: [false, false, false],

    tabOut: 0,
    tabIn: 0,
    operationsOut: ["Loan", "Loan Payment"],
    operationsIn: ["Create", "Delete", "Search"],
    cardTitle: [
      ["需要创建的贷款的信息", "需要删除的贷款的信息", "需要搜索的贷款信息"],
      [
        "需要创建的贷款支付的信息",
        "需要删除的贷款支付的信息",
        "需要搜索的贷款支付信息"
      ]
    ],
    cardStatusTitle: [
      ["创建贷款状态", "删除贷款状态", "搜索贷款状态"],
      ["创建贷款支付状态", "删除贷款支付状态", "搜索贷款支付状态"]
    ],
    inputDataLoan: {
      id: "",
      bankName: "",
      money: "",
      customerID: ""
    },
    inputDataLoanPayment: {
      loanID: "",
      loanPaymentID: "",
      date: "",
      money: ""
    }
  }),
  computed: {
    formLEmpty: function() {
      let result = this.inputDataLoan["id"].length == 0;
      for (let item in this.inputDataLoan) {
        result = result && this.inputDataLoan[item].length == 0;
      }
      return result;
    },
    formLPEmpty: function() {
      let result = this.inputDataLoanPayment["loanID"].length == 0;
      for (let item in this.inputDataLoanPayment) {
        result = result && this.inputDataLoanPayment[item].length == 0;
      }
      return result;
    },
    checkLCreate: function() {
      let result = true;
      for (let item in this.inputDataLoan) {
        result = result && this.inputDataLoan[item].length != 0;
      }
      return result;
    },
    checkLPCreate: function() {
      let result = true;
      for (let item in this.inputDataLoanPayment) {
        result = result && this.inputDataLoanPayment[item].length != 0;
      }
      return result;
    },
    resetBtnValid: function() {
      let result = false;
      if (this.tabOut == 0) {
        result = !this.formLEmpty;
      } else {
        result = !this.formLPEmpty;
      }
      return result;
    },
    commitBtnValid: function() {
      let result = false;
      if (this.tabOut == 0) {
        if (this.tabIn == 0) {
          result = this.checkLCreate;
        } else {
          result = !this.formLEmpty;
        }
      } else {
        if (this.tabIn == 0) {
          result = this.checkLPCreate;
        } else {
          result = !this.formLPEmpty;
        }
      }
      return result;
    }
  },
  methods: {
    resetForm: function() {
      if (this.tabOut == 0) {
        for (let item in this.inputDataLoan) {
          this.inputDataLoan[item] = "";
        }
      } else {
        for (let item in this.inputDataLoanPayment) {
          this.inputDataLoanPayment[item] = "";
        }
      }
    },
    commitForm: function() {
      alert(1);
    }
  }
};
</script>
