# Define commands for auto-generating Python proto code
PROTOC=python -m grpc_tools.protoc
PROTO_DIR=protos
PROTO_FILES=$(wildcard $(PROTO_DIR)/*.proto)
OUT_DIR=protos_generated

.PHONY: generate_protos clean_protos
generate_protos: $(PROTO_FILES)
	$(PROTOC) -I$(PROTO_DIR) \
		--python_out=$(OUT_DIR) \
		--pyi_out=$(OUT_DIR) \
		--grpc_python_out=$(OUT_DIR) \
		$(PROTO_FILES)

clean_protos:
	@if exist $(OUT_DIR) ( \
		del /Q $(OUT_DIR)\* \
	)

#