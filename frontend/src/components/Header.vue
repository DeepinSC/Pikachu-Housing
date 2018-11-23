<template>
  <v-toolbar app dense fixed dark clipped-left class="yellow darken-3">
    <v-btn dark flat icon @click.stop="onToggle" class="yellow darken-3">
      <v-icon>menu</v-icon>
    </v-btn>

    <v-avatar tile="tile" style="cursor: pointer">
      <img class="ml-3" src="../assets/pikachu.svg" style="height: 30px;width: 30px" @click.stop="toRoute('/')">
    </v-avatar>

    <v-toolbar-title class="mr-5 align-center">
      <div> Pikachu! </div>
    </v-toolbar-title>

    <v-layout row justify-center>
      <v-flex xs12 sm10 style="max-width: 750px">
        <v-text-field
          placeholder="Search house by name here..."
          single-line
          dark
          color="orange darken-3"
          v-model="searchInput"
          append-icon="search"
          @click:append="() => toRoute('/house/',{}, {name: searchInput})"
        ></v-text-field>
      </v-flex>
    </v-layout>

      <v-toolbar-title class="mr-2 align-center">
        <div><v-icon >person</v-icon> {{ user.username }} </div>
      </v-toolbar-title>

      <v-menu transition="slide-y-transition" bottom>
        <v-btn dark icon slot="activator">
          <v-icon>more_vert</v-icon>
        </v-btn>
        <v-list>
          <v-list-tile v-show="user.id === -1" @click="logout">
            <v-list-tile-title><SignUpModal></SignUpModal> </v-list-tile-title>
          </v-list-tile>

          <v-list-tile v-if="user.id !== -1" @click="logout">
            <v-list-tile-title><v-icon>exit_to_app</v-icon> Log Out </v-list-tile-title>
          </v-list-tile>

          <v-list-tile v-else>
            <v-list-tile-title><LoginModal></LoginModal></v-list-tile-title>
          </v-list-tile>

        </v-list>
      </v-menu>

</v-toolbar>
</template>
<script>
import { mapState } from 'vuex'
export default {
  name: 'Header',
  props: ['toggle'],
  created() {
    this.$store.dispatch('user/getUser')
  },
  components: {
    "LoginModal": () => import('./LoginModal.vue'),
    "SignUpModal": () => import('./SignUpModal.vue'),
  },
  computed: mapState({
    user: state => state.user.detail
  }),

  data () {
    return {
      searchInput: '',
    }
  },
  methods: {
    onToggle () {
      this.toggle()
    },
    toRoute (rname, rparams = {}, query = {}) {
      this.$router.push({path: rname, params: rparams, query: query})
    },
    logout () {
      this.$store.dispatch('user/logout').then(() => {
        this.$notify({
          title: "Logout successfully",
          type: "success",
          message: "You have logged out."
        })
      })
    }
  }
}
</script>

<style scoped>

</style>
