<template lang="html">
  <v-layout fill-height column class="text-xs-center">
    <section>
      <v-parallax src="https://www.pixelstalk.net/wp-content/uploads/2016/03/Cute-Pikachu-Wallpapers-HD-free-download.png" height=800>
        <v-layout
          align-center
          justify-center
          class="orange--text"
        >
          <v-flex>
            <h1 class="orange--text mb-2 display-3 text-xs-center">Pikachu-Housing</h1>
            <div class="subheading mb-3 text-xs-center">Find your house now</div>
            <movedown>
              <v-btn class="transparent" flat large @click.stop="scrollToNext('features')">
                <v-icon blue>
                  keyboard_arrow_down
                </v-icon>
              </v-btn>
            </movedown>
          </v-flex>
        </v-layout>
      </v-parallax>
    </section>
    <section id="features">
      <vintro></vintro>
      <movedown>
          <v-btn class="transparent" flat large @click.stop="scrollToEnd">
            <v-icon blue>
              keyboard_arrow_down
            </v-icon>
          </v-btn>
        </movedown>
    </section>
    <section id="create">
      <v-parallax src="https://www.50-best.com/images/pokemon_wallpapers/pikachu_face_wallpaper.jpg" height=800>
        <v-layout
          align-center
          justify-center
          class="white--text"
        >
          <v-flex>
            <h1 class="white--text mb-2 display-3 text-s-center">Pikachu-Housing</h1>
            <div class="subheading mb-3 text-xs-center">Let's start now!</div>
            <v-btn dark large color="yellow darken-3"  @click.stop="$router.push('/house/')" >Get Started</v-btn>
          </v-flex>
        </v-layout>
      </v-parallax>
    </section>
  </v-layout>
</template>

<script>
export default {
  name: 'index',
  components: {
    'movedown': () => import('../../components/shared/MoveDown'),
    'vintro': () => import('./Introduction.vue')
  },
  methods: {
    scrollToNext (e) {
      const element = document.getElementById(e)
      const offset = element.getBoundingClientRect().y
      window.scrollTo({'behavior': 'smooth', 'top': offset})
    },
    scrollToEnd () {
      window.scrollTo({'behavior': 'smooth', 'top': document.body.scrollHeight})
    }
  }
}
</script>

<style scoped>

</style>
