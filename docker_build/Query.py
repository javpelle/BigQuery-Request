from google.cloud import bigquery

def query_to_csv():

	client = bigquery.Client.from_service_account_json('data/credentials.json')
	query = open('data/query.txt', 'r').read()
	query_job = client.query(query)
	data = query_job.to_dataframe()
	
	data.to_csv("data/result.csv", index=False, line_terminator="\r\n")
	print(data)

if __name__== "__main__":
  query_to_csv()
