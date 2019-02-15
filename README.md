# BigQuery-Request

* First, access 

		./build_docker

* Write query in
		
		./data/query.txt

* Copy json file with Google BigQuery credentials in
	
		./data/credentials.json

* If you want to use Docker

	* Build with:

			sudo docker build -t python <name what you want> .
	* Run with:
		
			sudo docker run -ti -v $(pwd)/data:/data <name what you want>

* You can run program without docker with  
		
		python Query.py
