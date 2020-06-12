<template>
  <v-app>
    <v-navigation-drawer
      v-model="drawer"
      app
    >
      <v-list dense>
        <v-list-item
            v-for="item in drawerData"
            :key="item.title"
            link
            :to="item.targetPath"
          >
            <v-list-item-icon>
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              <v-list-item-title>{{ item.title }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar
      app
      color="indigo"
      dark
    >
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title>YuxuanGuo's Bank System</v-toolbar-title>
    </v-app-bar>


    <v-content>
      <router-view></router-view>
    </v-content>

    
  </v-app>
</template>

<script>

export default {
  name: 'App',

  // components: {
  //   HelloWorld,
  // },

  data: () => ({
    drawer: null,
    drawerData: [
      {
        title: 'Home',
        icon: 'mdi-home',
        targetPath: '/'
      },
      {
        title: 'Account Management',
        icon: 'mdi-account-cash-outline',
        targetPath: '/account-manage'
      },
      {
        title: 'Business Statistic',
        icon: 'mdi-chart-line',
        targetPath: '/business-statistic'
      },
      {
        title: 'Customer Management',
        icon: 'mdi-account-outline',
        targetPath: '/customer-manage'
      },
      {
        title: 'Loan Management',
        icon: 'mdi-cash-multiple',
        targetPath: '/loan-manage'
      }
    ],
  }),
};
</script>
