<template>
  <v-navigation-drawer
    dark
    app
    clipped
    v-model="visible"
    class="yellow darken-3"
    >
    <v-container grid-list-sm>
      <v-layout row justify-center align-center>
        <v-flex xs12>
          <v-card flat class="yellow darken-3">
            <v-card-title flat>
              <v-container grid-list-sm>
                <v-layout row wrap>
                  <v-flex xs12
                    align-center justify-center text-xs-center>
                    <v-avatar tile="tile" style="cursor: pointer">
                      <img src="../assets/pikachu.svg" alt="avatar" @click.stop="toRoute('/')">
                    </v-avatar>
                  </v-flex>
                  <v-flex xs12 align-center justify-center text-xs-center headline>
                      <div>
                        Pikachu!
                      </div>
                  </v-flex>
                </v-layout>
              </v-container>
            </v-card-title>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
    <v-list>

    <v-list-tile v-for="(item, i) in items" :key="i"  @click.stop="toRoute(item.link)">
      <v-list-tile-action>
        <v-icon>{{ item.icon }}</v-icon>
      </v-list-tile-action>
      <v-list-tile-content>
        <v-list-tile-title>
          {{ item.text }}
        </v-list-tile-title>
      </v-list-tile-content>
    </v-list-tile>

    <v-spacer></v-spacer>
    <v-list-tile >
      <v-list-tile-action>
        <v-icon>copyright</v-icon>
      </v-list-tile-action>
      <v-list-tile-content>
        <v-list-tile-title>
          Copyright {{ year }}
        </v-list-tile-title>
      </v-list-tile-content>
    </v-list-tile>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
export default {
  name: 'Sidebar',
  props: ['visible'],
  data () {
    return {
      items: [
        { icon: 'dashboard', text: 'Home', link: '/' },
        { icon: 'home', text: 'House', link: '/house/' },
        { icon: 'person', text: 'About Us', link: '/about/' }
      ]
    }
  },
  methods: {
    toRoute (rname, rparams = {}, query = {}) {
      this.$router.push({path: rname, params: rparams, query: query})
    }
  },
  computed: {
    year () {
      return new Date().getFullYear()
    }
  }
}
</script>

<style scoped>

</style>
