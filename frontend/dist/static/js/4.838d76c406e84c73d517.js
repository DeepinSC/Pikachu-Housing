webpackJsonp([4],{"S+Yy":function(e,t,s){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var r=s("NYxO"),a=this,o={name:"HouseList",components:{HouseCreateModal:function(){return s.e(12).then(s.bind(null,"vH1P"))},HouseFilter:function(){return s.e(19).then(s.bind(null,"dyXl"))},HouseSuggestionCard:function(){return s.e(10).then(s.bind(null,"LVGO"))},RoommateCard:function(){return s.e(11).then(s.bind(null,"XIKK"))}},created:function(){var e=this.$route.query;this.$store.dispatch("house/getList",e)},data:function(){return{sortMethods:[{name:"Price Low to High",param:{srule:"price-low-to-high"}},{name:"Price High to Low",param:{srule:"price-high-to-low"}},{name:"Likes High to Low",param:{srule:"like-high-to-low"}},{name:"Likes Low to High",param:{srule:"like-low-to-high"}},{name:"House name A - Z",param:{srule:"name-ascending"}},{name:"House name Z - A",param:{srule:"name-descending"}}],invalidName:"Please Select Your Suite",invalidPrice:9999}},computed:Object(r.b)({totalNums:function(e){return e.house.list.count},houses:function(e){return e.house.list.results},providers:function(e){return e.provider.list.results},departments:function(e){return e.department.list},currentPage:function(){var e=a.$route.query;return e.page?parseInt(e.page):1},authenticated:function(e){return-1!==e.user.detail.id},userDetail:function(e){return e.user.detail},suggestion:function(e){return e.house.suggestion}}),methods:{deleteHouse:function(e){var t=this;this.$store.dispatch("house/deleteHouseObj",e).then(function(){t.$notify({title:"Delete successfully",type:"success",message:"Your chosen house has been deleted."})}),this.$router.push("/")},toRoute:function(e){var t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:{},s=arguments.length>2&&void 0!==arguments[2]?arguments[2]:{};this.$router.push({path:e,params:t,query:s})},handleLike:function(e,t){var s={house_id:e.id,user_id:t.id};this.$store.dispatch("house/likeHouseList",s).then(function(){e.has_liked=!e.has_liked,console.log(e.has_liked,e.like_count),e.has_liked?e.like_count+=1:e.like_count-=1})}}},n={render:function(){var e=this,t=e.$createElement,s=e._self._c||t;return s("v-layout",{attrs:{"justify-center":""}},[s("v-flex",[s("v-container",{attrs:{fluid:"","grid-list-md":""}},[s("v-layout",{attrs:{row:"",wrap:"","justify-space-between":""}},[s("v-flex",{attrs:{md8:"",xs12:""}},[s("el-carousel",{attrs:{type:"card"}},e._l(e.houses,function(t,r){return s("el-carousel-item",{key:r,attrs:{src:t.cover_img}},[s("v-layout",{attrs:{"justify-center":""}},[s("img",{attrs:{src:t.cover_img+t.imgs_url[0]}}),e._v(" "),s("h4",{staticClass:"white--text ml-1 carousel-title"},[e._v(e._s(t.name))])])],1)}))],1),e._v(" "),s("v-flex",{directives:[{name:"show",rawName:"v-show",value:e.$vuetify.breakpoint.mdAndUp,expression:"$vuetify.breakpoint.mdAndUp"}],attrs:{md3:""}},[s("div",{staticClass:"mr-3",staticStyle:{position:"fixed"}},[s("HouseSuggestionCard"),e._v(" "),s("RoommateCard")],1)]),e._v(" "),s("v-flex",{attrs:{md8:""}},[s("v-layout",{attrs:{row:"","justify-space-between":""}},[s("v-flex",{attrs:{md3:""}},[s("h1",[e._v("House list")])]),e._v(" "),s("v-flex",{staticClass:"text-xs-right list-header-bar",attrs:{md5:""}},[s("HouseCreateModal",{directives:[{name:"show",rawName:"v-show",value:e.authenticated,expression:"authenticated"}]}),e._v(" "),s("HouseFilter"),e._v(" "),s("el-dropdown",{attrs:{trigger:"click"}},[s("v-btn",{attrs:{flat:""}},[s("v-icon",[e._v("sort")]),e._v("Sort")],1),e._v(" "),s("el-dropdown-menu",{attrs:{slot:"dropdown"},slot:"dropdown"},e._l(e.sortMethods,function(t,r){return s("div",{key:r},[s("div",{on:{click:function(){return e.toRoute("",{},t.param)}}},[s("el-dropdown-item",[e._v(e._s(t.name))])],1)])}))],1)],1)],1),e._v(" "),s("v-divider")],1),e._v(" "),s("v-flex",{attrs:{md8:""}},[s("v-layout",{attrs:{row:"",wrap:""}},[e._l(e.houses,function(t){return e.houses.length>0?s("v-flex",e._b({key:t.id,attrs:{xs12:"",md12:""}},"v-flex",((r={})["xs"+t.flex]=!0,r),!1),[s("v-hover",{scopedSlots:e._u([{key:"default",fn:function(r){var a=r.hover;return s("v-card",{staticClass:"mt-3",class:"elevation-"+(a?6:2)},[s("v-layout",{attrs:{row:""}},[s("v-flex",{directives:[{name:"show",rawName:"v-show",value:e.$vuetify.breakpoint.mdAndUp,expression:"$vuetify.breakpoint.mdAndUp"}],attrs:{md3:""}},[s("v-card",{attrs:{to:"/house/"+t.id}},[s("v-img",{attrs:{src:t.cover_img+t.imgs_url[0]},on:{click:function(s){s.stopPropagation(),e.$router.push(t.id)}}})],1)],1),e._v(" "),s("v-flex",{attrs:{md9:"",xs12:""}},[s("v-card-title",{staticClass:"pb-2"},[s("div",{staticClass:"headline"},[e._v(e._s(t.name===e.invalidName?"Anonymous house":t.name))]),e._v(" "),s("br")]),e._v(" "),s("v-card-text",{staticClass:"pt-2"},[s("h4",[e._v("Price:\n                            "),t.price!==e.invalidPrice?s("span",{staticStyle:{color:"orange"}},[e._v("$"+e._s(t.price))]):s("span",{staticStyle:{color:"grey"}},[e._v("Unavailable")])]),e._v(" "),t.closest_department?s("div",[s("span",[e._v("Closest Department:\n                              "),t.closest_department?s("span",{staticStyle:{color:"orangered"}},[e._v(e._s(t.closest_department.name))]):e._e()]),e._v(" "),s("br"),e._v(" "),s("span",[e._v("Distance:\n                              "),s("span",{staticStyle:{color:"dodgerblue"}},[e._v(e._s(t.closest_department.distance.toFixed(2))+" km")])])]):e._e(),e._v(" "),s("br"),e._v(" "),s("span",{staticClass:"grey--text"},[e._v("Location: "+e._s(t.location))]),s("br"),e._v(" "),s("span",{staticClass:"grey--text"},[e._v(e._s(t.description.slice(0,200))+"...")])]),e._v(" "),s("v-card-actions",[s("v-btn",{attrs:{flat:"",color:"green",to:"/house/"+t.id}},[s("v-icon",[e._v("details")]),e._v("Detail")],1),e._v(" "),s("div",{directives:[{name:"show",rawName:"v-show",value:e.authenticated,expression:"authenticated"}]},[s("v-btn",{attrs:{flat:"",color:"orange"},on:{click:function(s){e.handleLike(t,e.userDetail)}}},[s("v-icon",[e._v(e._s(t.has_liked?"star":"star_border")+"\n                          ")]),e._v("Likes: "+e._s(t.like_count))],1)],1),e._v(" "),s("div",{directives:[{name:"show",rawName:"v-show",value:e.authenticated,expression:"authenticated"}]},[s("el-popover",{attrs:{trigger:"click",placement:"top"},model:{value:t.popover,callback:function(s){e.$set(t,"popover",s)},expression:"item.popover"}},[s("p",[e._v("Do you want to delete the house? (This operation is irrevocable)")]),e._v(" "),s("div",{staticStyle:{"text-align":"right",margin:"0"}},[s("v-btn",{attrs:{flat:"",color:"green"},on:{click:function(e){t.popover=!1}}},[e._v("Cancel")]),e._v(" "),s("v-btn",{attrs:{flat:"",color:"red"},on:{click:function(s){e.deleteHouse(t.id)}}},[e._v("Delete")])],1),e._v(" "),s("v-btn",{attrs:{slot:"reference",flat:"",color:"red"},slot:"reference"},[s("v-icon",[e._v("close")]),e._v("Delete")],1)],1)],1)],1)],1)],1)],1)}}])})],1):e._e();var r}),e._v(" "),e.houses?e._e():s("v-flex",{attrs:{xs12:"",md12:""}},[s("el-table",{directives:[{name:"loading",rawName:"v-loading",value:!0,expression:"true"}],staticStyle:{width:"100%"},attrs:{"empty-text":"Loading"}})],1)],2)],1)],1),e._v(" "),s("v-flex",{staticClass:"mt-3",attrs:{md12:""}},[s("div",{staticClass:"text-xs-center"},[s("el-pagination",{attrs:{layout:"prev, pager, next",total:e.totalNums,currentPage:this.$route.query.page?parseInt(this.$route.query.page):1},on:{"current-change":function(t){return e.toRoute("",{},{page:t})},"next-click":function(t){return e.toRoute("",{},{page:t})},"prev-click":function(t){return e.toRoute("",{},{page:t})}}})],1)])],1)],1)],1)},staticRenderFns:[]};var i=s("VU/8")(o,n,!1,function(e){s("WThK")},"data-v-62742342",null);t.default=i.exports},WThK:function(e,t){}});
//# sourceMappingURL=4.838d76c406e84c73d517.js.map