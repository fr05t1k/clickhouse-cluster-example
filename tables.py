import requests
with open('ontime.sql') as f:
  table_sql = f.read()
  cluster = [
    {'server': 'ch1-01', 'shard': '1', 'port': '8121'},
    {'server': 'ch1-02', 'shard': '1', 'port': '8122'},
    {'server': 'ch2-01', 'shard': '2', 'port': '8123'},
    {'server': 'ch2-02', 'shard': '2', 'port': '8124'},
  ]
  for server in cluster:
    cluster_table_sql = table_sql % (server['server'], server['shard'])
    for query in cluster_table_sql.split(';'):
      requests.post('http://localhost:%s' % server['port'], query)
