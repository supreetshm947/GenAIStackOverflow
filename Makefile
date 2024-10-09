setup_google_cli:
	curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-linux-x86_64.tar.gz
	tar -xf google-cloud-cli-linux-x86_64.tar.gz
	./google-cloud-sdk/install.sh
	./google-cloud-sdk/bin/gcloud init
	./google-cloud-sdk/bin/gcloud auth application-default login
	rm -r google-cloud-cli-linux-x86_64.tar.gz

