include .env

export $(shell sed 's/=.*//' .env)

setup_google_cli:
	curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-linux-x86_64.tar.gz
	tar -xf google-cloud-cli-linux-x86_64.tar.gz
	./google-cloud-sdk/install.sh
	./google-cloud-sdk/bin/gcloud init
	./google-cloud-sdk/bin/gcloud auth application-default login
	rm -r google-cloud-cli-linux-x86_64.tar.gz

create_collection:
	@echo "Creating collection in Qdrant..."
	curl -X PUT "http://$(QDRANT_HOST):$(QDRANT_PORT)/collections/$(QDRANT_COLLECTION_NAME)" \
		-H 'Content-Type: application/json' \
		--data-raw '{ "vectors": { "size": $(QDRANT_VECTOR_SIZE), "distance": "$(QDRANT_DISTANCE)" } }'