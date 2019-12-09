import request from '@/utils/request'

export function getmap() {
  return request({
    url: '/charts/map',
    method: 'get'
  })
}

export function GetEventType(params) {
  return request({
    url: '/charts/type',
    method: 'get',
    params
  })
}
export function Myget(params) {
  return request({
    url: '/charts/myget',
    method: 'get',
    params
  })
}
