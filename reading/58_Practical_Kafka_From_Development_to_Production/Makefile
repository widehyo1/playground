help: ## Show available commands
	@echo "Available targets:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
	| awk 'BEGIN {FS=":.*?## "}; {printf "  %-15s %s\n", $$1, $$2}'

ConsumerAsync: ## ConsumerAsync
	mvn exec:java -Dexec.mainClass=ConsumerAsync

ConsumerAuto: ## ConsumerAuto
	mvn exec:java -Dexec.mainClass=ConsumerAuto

ConsumerSync: ## ConsumerSync
	mvn exec:java -Dexec.mainClass=ConsumerSync

PeterProducerCallback: ## PeterProducerCallback
	mvn exec:java -Dexec.mainClass=PeterProducerCallback

ProducerAsync: ## ProducerAsync
	mvn exec:java -Dexec.mainClass=ProducerAsync

ProducerFireForgot: ## ProducerFireForgot
	mvn exec:java -Dexec.mainClass=ProducerFireForgot

ProducerSync: ## ProducerSync
	mvn exec:java -Dexec.mainClass=ProducerSync

