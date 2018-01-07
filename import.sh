for i in *.zip; do 
  echo $i; unzip -cq $i '*.csv' | sed 's/\.00//g' | docker-compose run --rm client clickhouse-client --host=clickhouse1 --query="INSERT INTO ontime FORMAT CSVWithNames"; 
done