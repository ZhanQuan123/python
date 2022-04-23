

config = {
  'token':'OTY1MTExNDAzNjM3Nzk2OTM0.YlucCQ.bkt7MiQofiPrOI7Q30aDq5JqDNo',
  'prefix':'-'
}










import json

x = json.dumps(config)
y = json.loads(x)


def token():
    return (y['token'])

def prefix():
    return (y['prefix'])