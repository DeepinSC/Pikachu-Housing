webpackJsonp([19],{"5IhO":function(e,t){},dyXl:function(e,t,r){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var i=r("NYxO"),l={name:"HouseFilter",created:function(){this.filter=this.getFilterFromURL(this.$router.history.current.query),this.$store.dispatch("provider/getList")},data:function(){return{filter:{price:[0,6e3],department:"",provider:"",like:!1,suggestion:!1},dialog:!1}},computed:Object(i.b)({providers:function(e){return e.provider.list.results},departments:function(e){return e.department.list.results},authenticated:function(e){return-1!==e.user.detail.id}}),methods:{resetFilter:function(){this.toRoute("",{},{}),this.filter={price:[0,6e3],department:"",provider:"",like:!1}},getFilterFromURL:function(e){var t={price:[0,6e3],department:"",provider:"",like:!1,suggestion:!1};return t.price[0]=e.minprice?e.minprice:0,t.price[1]=e.maxprice?e.maxprice:6e3,t.department=e.department?parseInt(e.department):"",t.provider=e.provider?parseInt(e.provider):"",t.like=e.like&&!0,t},submit:function(e){var t={};for(var r in this.$route.query)t[r]=this.$route.query[r];0===e.price[0]&&6e3===e.price[1]||(t.minprice=e.price[0],t.maxprice=e.price[1]),""!==e.department?t.department=e.department:delete t.department,""!==e.provider?t.provider=e.provider:delete t.provider,e.like?t.like=!0:delete t.like,this.toRoute("",{},t),this.dialog=!1},toRoute:function(e){var t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:{},r=arguments.length>2&&void 0!==arguments[2]?arguments[2]:{};this.$router.push({path:e,params:t,query:r})}}},a={render:function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("v-dialog",{attrs:{"max-width":"800px"},model:{value:e.dialog,callback:function(t){e.dialog=t},expression:"dialog"}},[r("v-card-title",{staticClass:"headline orange lighten-2 white--text",attrs:{"primary-title":""}},[e._v("\n        Advanced Filter\n      ")]),e._v(" "),r("v-list",{attrs:{"three-line":"",subheader:""}},[r("v-subheader",[e._v("Properties")]),e._v(" "),r("v-list-tile",{attrs:{avatar:""}},[r("v-list-tile-content",[r("v-list-tile-title",[e._v("Department")]),e._v(" "),r("v-list-tile-sub-title",[e._v("Set the department to get the houses nearest to this department")]),e._v(" "),r("v-list-tile-sub-title",{staticClass:"mt-1"},[r("el-select",{directives:[{name:"show",rawName:"v-show",value:e.departments,expression:"departments"}],attrs:{filterable:"",clearable:"",placeholder:"Choose a department","no-data-text":"No data","no-match-text":"No matching"},model:{value:e.filter.department,callback:function(t){e.$set(e.filter,"department",t)},expression:"filter.department"}},e._l(e.departments,function(e){return r("el-option",{key:e.id,attrs:{label:e.name,value:e.id}})}))],1)],1)],1),e._v(" "),r("v-list-tile",{staticClass:"mb-2",attrs:{avatar:""}},[r("v-list-tile-content",[r("v-list-tile-title",[e._v("Provider")]),e._v(" "),r("v-list-tile-sub-title",[e._v("Set the provider here")]),e._v(" "),r("v-list-tile-sub-title",{staticClass:"mt-1"},[r("el-select",{directives:[{name:"show",rawName:"v-show",value:e.providers,expression:"providers"}],attrs:{filterable:"",clearable:"",placeholder:"Choose a provider","no-data-text":"No data","no-match-text":"No matching"},model:{value:e.filter.provider,callback:function(t){e.$set(e.filter,"provider",t)},expression:"filter.provider"}},e._l(e.providers,function(e){return r("el-option",{key:e.id,attrs:{label:e.name,value:e.id}})}))],1)],1)],1),e._v(" "),r("v-divider"),e._v(" "),r("v-list",{attrs:{"three-line":"",subheader:""}},[r("v-subheader",[e._v("Price")]),e._v(" "),r("v-layout",{attrs:{row:"",wrap:""}},[r("v-flex",{attrs:{xs1:""}},[r("v-text-field",{staticClass:"price-textfield mr-0 slider",attrs:{type:"number",color:"yellow darken-1"},model:{value:e.filter.price[0],callback:function(t){e.$set(e.filter.price,0,t)},expression:"filter.price[0]"}})],1),e._v(" "),r("v-flex",{attrs:{xs10:""}},[r("v-range-slider",{staticClass:"slider",attrs:{max:6e3,min:0,step:10,color:"yellow darken-1"},model:{value:e.filter.price,callback:function(t){e.$set(e.filter,"price",t)},expression:"filter.price"}})],1),e._v(" "),r("v-flex",{attrs:{xs1:""}},[r("v-text-field",{staticClass:"price-textfield ml-0 slider",attrs:{type:"number",color:"yellow darken-1"},model:{value:e.filter.price[1],callback:function(t){e.$set(e.filter.price,1,t)},expression:"filter.price[1]"}})],1)],1)],1),e._v(" "),r("v-divider"),e._v(" "),r("v-list",{directives:[{name:"show",rawName:"v-show",value:e.authenticated,expression:"authenticated"}],attrs:{"three-line":"",subheader:""}},[r("v-subheader",[e._v("General")]),e._v(" "),r("v-list-tile",{attrs:{avatar:""}},[r("v-list-tile-action",[r("v-checkbox",{attrs:{color:"yellow darken-1"},model:{value:e.filter.like,callback:function(t){e.$set(e.filter,"like",t)},expression:"filter.like"}})],1),e._v(" "),r("v-list-tile-content",[r("v-list-tile-title",[e._v("Houses I Like")]),e._v(" "),r("v-list-tile-sub-title",[e._v("The houses marked as liked.")])],1)],1)],1)],1),e._v(" "),r("v-divider"),e._v(" "),r("v-list",{attrs:{"three-line":"",subheader:""}},[r("v-card-actions",[r("v-spacer"),e._v(" "),r("v-btn",{attrs:{color:"blue",flat:""},on:{click:e.resetFilter}},[e._v("Reset")]),e._v(" "),r("v-btn",{attrs:{color:"green",flat:""},on:{click:function(t){e.submit(e.filter)}}},[e._v("Submit")])],1)],1),e._v(" "),r("v-btn",{attrs:{slot:"activator",flat:""},slot:"activator"},[r("v-icon",[e._v("filter")]),e._v("Filter")],1)],1)},staticRenderFns:[]};var s=r("VU/8")(l,a,!1,function(e){r("5IhO")},"data-v-00b0a708",null);t.default=s.exports}});
//# sourceMappingURL=19.2ef43bf2939dbef9ab0f.js.map