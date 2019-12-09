
import Layout from '@/layout'

const chartsRouter = {
  path: '/charts',
  component: Layout,
  redirect: 'noRedirect',
  name: 'Charts',
  meta: {
    title: '可视化图表',
    icon: 'charts'
  },
  children: [
    {
      path: 'eventtype',
      component: () => import('@/views/charts/EventType'),
      name: 'EventType',
      meta: { title: '问题性质', noCache: true, icon: 'eventtype' }
    },
    {
      path: 'streetevent',
      component: () => import('@/views/charts/StreetEvent'),
      name: 'StreetEvent',
      meta: { title: '街道事件', noCache: true, icon: 'streetevent' }
    },
    {
      path: 'completionstatus',
      component: () => import('@/views/charts/CompletionSituation'),
      name: 'CompletionSituation',
      meta: { title: '结办情况', noCache: true, icon: 'completion' }
    },
    {
      path: 'hotcommunities',
      component: () => import('@/views/charts/HotCommunities'),
      name: 'HotCommunities',
      meta: { title: '热点社区', noCache: true, icon: 'hotcommunities' }
    },
  ]
}

export default chartsRouter
