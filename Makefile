clean:
	echo "\n\nCLEANING OUT DOCKER RESOURCES!\n\n"
	- docker ps -aq | xargs docker rm -f
	- docker images -aq | xargs docker rmi -f
	- docker volume ls -q | xargs docker volume rm
	echo "\n\nDESTROYED DOCKER RESOURCES!\n\n"
	- rm -r ./report/data
	echo "\n\nDESTROYED EXISTING DATA!\n\n"



docker-stocks:
	cd ./packages/stocks && tar -czh * | \
	docker build -t spacepowermonkey/monkeyfusion-stocks -


report: docker-stocks
	echo "\n\nSTARTING MONKEYFUSION STOCK REPORT\n\n"

	docker run --name mf-stocks \
	--mount type=volume,src=monkeyfusion-data,dst="/data" \
	spacepowermonkey/monkeyfusion-stocks

	docker cp -a mf-stocks:/data/ ./report/

	echo "\n\n SUCCESS!\n"

