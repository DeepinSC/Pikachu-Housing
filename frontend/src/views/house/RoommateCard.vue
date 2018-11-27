<template>
  <div>
  <v-card color="orange" class="white--text mt-3" v-if="roommates.length > 0" v-for="roommate in roommates" :key="roommate.id">
    <v-layout row>
      <v-flex>
        <v-card-title primary-title >
          <div>
            <div class="headline">Your Potential Roommate</div>
            <h3>{{roommate.username}}</h3>
            <div>From {{roommate.profile.department.name}} department</div>
            <div>Email: {{roommate.email}}</div>
          </div>
        </v-card-title>
      </v-flex>
    </v-layout>
    <v-divider light></v-divider>
    <v-card-actions class="pa-3">
      <v-btn color="orange" class="white--text" :href="'mailto:' + roommate.email">
        Contact him/her via email
      </v-btn>
    </v-card-actions>
  </v-card>
  </div>
</template>

<script>
import { mapState } from 'vuex'
export default {
  name: "RoommateCard",
  created() {
    this.$store.dispatch('house/getRoommates')
  },
  computed: mapState({
    roommates: state => state.house.roommates,
  }),
}
</script>

<style scoped>

</style>
