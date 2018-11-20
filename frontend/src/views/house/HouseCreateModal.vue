<template>
  <v-dialog
   v-model="dialogView"
   width="500"
  >
    <v-btn flat slot="activator"><v-icon>add</v-icon>New House</v-btn>
    <v-card>
      <v-card-title
        class="headline orange lighten-2 white--text"
        primary-title
      >
        Create a new House!
      </v-card-title>

      <form>
        <v-card-text>
            <v-container grid-list-md>
              <v-layout wrap>
                <v-flex xs12>
                  <v-text-field
                    name="name"
                    label="* Name"
                    required
                    v-validate="'required'"
                    v-model="house.name"
                    :error-messages="errors.collect('name')"
                    data-vv-name="name"
                  ></v-text-field>
                </v-flex>
                <v-flex xs12 sm6 md6>
                  <v-text-field
                    name="price"
                    label="* Price"
                    equired
                    v-validate="'required|numeric'"
                    v-model="house.price"
                    :error-messages="errors.collect('price')"
                    data-vv-name="price"
                  ></v-text-field>
                </v-flex>
                <v-flex xs12 sm6 md6>
                  <v-text-field
                    name="location"
                    label="Location"
                    hint="the address of this house"
                    v-model="house.location"
                  ></v-text-field>
                </v-flex>
                <v-flex xs12>
                  <v-text-field
                    name="cover_img"
                    label="Image url"
                    v-model="house.imgs_url"
                    v-validate="'url'"
                    :error-messages="errors.collect('cover_img')"
                    data-vv-name="cover_img"
                  ></v-text-field>
                </v-flex>
                <v-textarea
                  name="description"
                  label="* Description"
                  hint="Hint: the size/service/furniture..."
                  v-validate="'required'"
                  v-model="house.description"
                  required
                  :error-messages="errors.collect('description')"
                  data-vv-name="description"
                ></v-textarea>

              </v-layout>
            </v-container>
        </v-card-text>
      </form>

      <v-divider></v-divider>

      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn
          color="green"
          flat
          @click="submit(house)"
        >
          Submit
        </v-btn>
        <v-btn
          color="primary"
          flat
          @click="dialogView = false"
        >
          Cancel
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>

export default {
  name: "HouseCreateModal",
  data: () => {
    return {
      dialogView: false,
      house: {
        name: '',
        price: 0,
        cover_img: '',
        imgs_url: '',
        location: '',
        description: '',
      }
    }
  },
  methods: {
    submit (house) {
      this.$validator.validateAll().then((isvalid) => {
        if(!isvalid) {
          this.$notify({
            title: "Create failed",
            type: "error",
            message: "The input fields are invalid!"
          })
          return
        }
        this.createHouse(house)
        this.dialogView = false
      })
    },
    createHouse: function (house) { // No arrow function here...
      let splitedURL = house.imgs_url.split('/')
      let originalURL = house.imgs_url
      house.imgs_url = splitedURL[splitedURL.length - 1]
      house.cover_img = originalURL.slice(0, (originalURL.length - house.imgs_url.length))
      house.imgs_url = [splitedURL[splitedURL.length - 1]]

      this.$store.dispatch('house/createHouseObj',house).then(() => {
        this.$notify({
          title: "Create successfully",
          type: "success",
          message: "You have created a new house."
        })
        this.$router.push("house/")
      })
    }
  }
}
</script>

<style scoped>

</style>
