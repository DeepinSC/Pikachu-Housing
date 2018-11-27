<template>
  <v-card dark class="white--text mt-3" v-if="houses.length > 0">
    <v-card-title primary-title>
      <div class="headline">Your House Suggestions</div>
    </v-card-title>
    <v-card-text>
      <div>Based on your information, our algorithm will suggest best houses to you. Have a try!</div>
    </v-card-text>
    <v-expansion-panel v-if="houses" dark expand>
      <v-expansion-panel-content  class="white--text" v-for="(house,i) in houses" :key="i">
        <div color="green" slot="header">{{house.name}}</div>
        <div>
          <v-card-text>
            <h4>Suggest reasons: <span style="color: yellow">{{house.suggested_reason[0]}}</span> and
              <span style="color: yellow">{{house.suggested_reason[1]}}</span></h4>
            <span>Price: {{house.price}}</span>
            <br>
            <span v-if="house.closest_department">Distance to <span style="color: yellow">{{house.closest_department.name}}</span>:
              {{house.closest_department.distance.toFixed(2)}}km</span>
            <div>{{house.like_count}} users also like this house</div>
            </v-card-text>
          <v-card-actions>
            <v-btn dark :to="'/house/'+house.id"><v-icon>touch_app</v-icon>Have a look</v-btn>
          </v-card-actions>
        </div>
      </v-expansion-panel-content>
    </v-expansion-panel>
    <div v-if="!houses">
      <el-table
        v-loading="true" style="width: 100%" empty-text="Loading">
      </el-table>
    </div>
  </v-card>
</template>

<script>
import { mapState } from 'vuex'
export default {
  name: "HouseSuggestionCard",

  computed: mapState({
    houses: state => state.house.suggestion,
    userDetail: state => state.user.detail,
  }),
  created() {
    this.$store.dispatch('house/getSuggestions')
  },
  data: () => {
    return {
      activeNames: "",
    }
  },
  methods: {
     toRoute (rname, rparams = {}, query = {}) {
      this.$router.push({path: rname, params: rparams, query: query})
    },
  }
}
</script>

<style scoped>
.collapse {
  background-color: #4caf50!important;
}
.el-collapse-item {
  background-color: #4caf50!important;
}
</style>
