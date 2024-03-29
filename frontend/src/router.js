import Vue from 'vue'
import Router from 'vue-router'
import Login from './views/Login.vue'
import Interview from './views/Interview.vue'
import Performance from './views/Performance.vue'
import InterviewEnd from './views/InterviewEnd.vue'
import Train from './views/Train'
import AdminInstruction from './views/AdminInstruction'
import UserInstruction from './views/UserInstruction'
import ExportExcel from './views/ExportExcel'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
      {
          path:'/',
          redirect:'/login',
      },
      {
          path:'/login',
          name:'login',
          component:Login,
      },
      {
          path:'/interview',
          name:'interview',
          component:Interview,
      },
      {
          path:'/performance',
          name:'performance',
          component:Performance
      },
      {
          path:'/interview_end',
          name:'interview_end',
          component:InterviewEnd
      },
      {
          path:'/train',
          name:'train',
          component:Train
      },
      {
          path:'/admin_instruction',
          name:'admin_instruction',
          component:AdminInstruction
      },
      {
          path:'/user_instruction',
          name:'user_instruction',
          component:UserInstruction
      },
      {
          path:'/export',
          name:'export',
          component:ExportExcel
      },
  ]
})
