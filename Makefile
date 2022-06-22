clean:
	echo "\n\nCLEANING OUT DOCKER RESOURCES!\n\n"
	- docker ps -aq | xargs docker rm -f
	- docker images -aq | xargs docker rmi -f
	- docker volume ls -q | xargs docker volume rm
	echo "\n\nDESTROYED DOCKER RESOURCES!\n\n"
	- rm -r ./report/data/*
	echo "\n\nDESTROYED EXISTING DATA!\n\n"



docker-base:
	cd ./lib && tar -czh * | \
	docker build -t spacepowermonkey/monkeyfusion -

docker-stocks: docker-base
	cd ./packages/stocks && tar -czh * | \
	docker build -t spacepowermonkey/monkeyfusion-stocks -


report: docker-stocks
	echo "\n\nSTARTING MONKEYFUSION STOCK REPORT\n\n"

	docker run --name mf-stocks \
	--mount type=volume,src=monkeyfusion-data,dst="/data" \
	--mount type=bind,src=$(PWD)/report/config.json,target=/meta/config.json,readonly \
	spacepowermonkey/monkeyfusion-stocks --confdir /meta --config config.json

	echo "\n\n SUCCESS!\n"

