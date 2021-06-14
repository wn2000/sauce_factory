define PROJECT_rule
INPUTS_$(1) := $$(shell find recipes/$(1))

out/$(1).uce : $$(INPUTS_$(1))
	./build_uce.sh recipes/$(1) $$@

endef

PRJS := $(patsubst recipes/%, %, $(shell find recipes/* -maxdepth 0 -type d))

all : $(foreach p, $(PRJS), out/$(p).uce)

$(foreach p, $(PRJS), $(eval $(call PROJECT_rule,$(p))))

