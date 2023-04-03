1. Open the `rabbitmq-demo` in Visual Studio Code
1. Open the project in container (Ctrl+Shift+P and choose "Remote-Containers: Reopen in container")
1. Log into RabbitMQ Management (RM) at http://localhost:15672/, use `guest` as username and password
1. Make sure both containers (this and RabbitMQ) are connected to `bridge` network.
1. Inspect the RabbitMQ container and copy its IP address.
1. Export it as a RABBITMQHOST environment variable `export RABBITMQHOST="172.17.0.5"`.
1. Run the script `python consume.py`.