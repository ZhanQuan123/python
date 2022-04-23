

config = {
  'token':'OTY1MTExNDAzNjM3Nzk2OTM0.YlucCQ.QpGgMbIwfoRQ2-NM0k5go7IlVPo',
  'prefix':'-',
  'lavalink':{
    'ip':'0.0.0.0',
    'port':'2900',
    'pass':'password'
  }
}










import json

x = json.dumps(config)
y = json.loads(x)


def token():
    return (y['token'])

def prefix():
    return (y['prefix'])


def lavaPass():
    return (y['lavalink.pass'])

def lavaPort():
    return (y['lavalink.port'])

def ip():
    return (y['lavalink.ip'])