<template>
  <v-dialog
   v-model="dialogView"
   width="500"
  >
    <div slot="activator"><v-icon>exit_to_app</v-icon>Sign in</div>
    <v-card>
      <v-card-title
        class="headline orange lighten-2 white--text"
        primary-title
      >
        Login here!
      </v-card-title>
      <form>
        <v-card-text>
            <v-container grid-list-md>
              <v-layout wrap>
                <v-flex xs12>
                  <v-text-field
                    name="username_or_email"
                    label="* Username or Email"
                    required
                    v-validate="'required'"
                    v-model="input.username_or_email"
                    :error-messages="errors.collect('username_or_email')"
                    data-vv-name="username_or_email"
                  ></v-text-field>
                </v-flex>
                <v-flex xs12>
                  <v-text-field
                    name="password"
                    label="* Password"
                    required
                    v-validate="'required'"
                    v-model="input.password"
                    type="password"
                    :error-messages="errors.collect('password')"
                    data-vv-name="password"
                  ></v-text-field>
                </v-flex>
                <v-flex>
                  <v-list-tile-action>
                     <v-checkbox
                       name="remember"
                       :label="'Remember me?'"
                       v-model="input.remember"
                       :error-messages="errors.collect('remember')"
                       color="orange"
                       data-vv-name="remember"
                      ></v-checkbox>
                  </v-list-tile-action>
                </v-flex>

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
          @click="submit(input)"
        >
          Sign in
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
  name: "LoginModal",
  data: () => {
    return {
      dialogView: false,
      input: {
        username_or_email: '',
        password: '',
        remember: false,
      }
    }
  },
  methods: {
    submit (input) {
      this.$validator.validateAll().then((isvalid) => {
        if(!isvalid) {
          this.$notify({
            title: "Create failed",
            type: "error",
            message: "The input fields are invalid!"
          })
          return
        }
        this.login(input)
        this.dialogView = false
      })
    },

    login: function (input) { // No arrow function here...
      this.$store.dispatch('user/login',input).then(() => {
      })
      let store = this.$store
      let notify = this.$notify
      setTimeout(() => {
        if(!store.state.user.status) {
        this.$notify.error({
          title: "Signin Failed",
          message: "Check your username/password again."
        })
        return
      }
      notify({
        title: "Login successfully",
        type: "success",
        message: "You have login successfully."
      })
      this.$router.push("/")
      window.location.reload()
      },2000)


    }
  }
}
</script>

<style scoped>

</style>
