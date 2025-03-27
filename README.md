# API contracts repository

Repository to store API contracts and generate code from them.

## Local development

Setup virtual environment and install project dependencies:

```bash
python3 -m venv environment ; source ./environment/bin/activate
pip3 install flask flask-restful grpcio grpcio-tools protobuf grpclib
```

Generate python code from proto file:

If you try to generate python code from proto file and you get the following error:
```bash
protoc --proto_path=. --python_out=. --grpc_python_out=. ./api/requests/v1/requests.proto

protoc-gen-grpc_python: program not found or is not executable
Please specify a program using absolute path or make sure the program is available in your PATH system variable
--grpc_python_out: protoc-gen-grpc_python: Plugin failed with status code 1.
```

Instead of using `--grpc_python_out=.` use `--plugin=grpc_python_plugin --python_out=. --grpc_python_out=.`

```bash
protoc -I=. api/requests/v1/requests.proto --plugin=grpc_python_plugin --python_out=. --grpclib_python_out=.
```

Now, lets run server:
```bash
python3 server_test.py
```

In another terminal, lets run client:
```bash
curl http://127.0.0.1:5000/health
```


