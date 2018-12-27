SWAGGER_CMD=swagger-codegen

SWAGGER_SPEC=swagger/swagger.yml

all: server client doc

server: $(SWAGGER_SPEC)
	mkdir -p $@
	$(SWAGGER_CMD) generate $(SWAGGER_OPTION) -i $(SWAGGER_SPEC) -l python-flask -o $@

client: $(SWAGGER_SPEC)
	mkdir -p $@
	$(SWAGGER_CMD) generate $(SWAGGER_OPTION) -i $(SWAGGER_SPEC) -l python -o $@

doc: $(SWAGGER_SPEC)
	mkdir -p $@
	$(SWAGGER_CMD) generate $(SWAGGER_OPTION) -i $(SWAGGER_SPEC) -l html2 -o $@
