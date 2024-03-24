1. Open the `rabbitmq-demo` in Visual Studio Code
1. Open the project in container (`Ctrl+Shift+P` and choose "Remote-Containers: Reopen in container")
1. Make sure both containers (this and RabbitMQ) are connected to `bridge` network.
1. Inspect the RabbitMQ container and get its IP address.
1. Export it as a RABBITMQHOST environment variable `export RABBITMQHOST="172.17.0.5"`.
1. Run the script `python consume.py`.

Expected output is

```
RabbitMQ host: 172.17.0.5
 [*] Waiting for messages. To exit press CTRL+C
 [x] Received b'"{\\"status\\":\\"ACTIVATED\\",\\"id\\":\\"3fdafe7e-3e2a-4ea5-a3ea-49198eef619d\\"}"'
 [x] Received b'"{\\"status\\":\\"ACTIVATED\\",\\"id\\":\\"8f46cbc5-a394-4114-945a-0539a570c1b9\\"}"'
 [x] Received b'"{\\"status\\":\\"ACTIVATED\\",\\"id\\":\\"7d0d2412-60f9-412a-92ea-a8c42e35bbe8\\"}"'
 [x] Received b'"{\\"status\\":\\"ACTIVATED\\",\\"id\\":\\"88948f7f-8ca1-4ad1-90dd-066a6edaad1a\\"}"'
```