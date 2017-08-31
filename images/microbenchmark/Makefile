# verbose flag
BUILD_VERBOSE = $(V)
ifeq ($(BUILD_VERBOSE),1)
  Q =
else
  Q = @
endif

# directory
SRC = .
BIN = /usr/bin

# compiler
CC = gcc

# cflags and source code
CFLAGS += $(DEFS) -Wall -g -O3 -D_GNU_SOURCE
LDFLAGS +=
LIBS    = $(SRC)/bench.c $(SRC)/util.c
TC      = $(SRC)/MWCM.c $(SRC)/MWCL.c \
		  $(SRC)/DWAL.c $(SRC)/DWOL.c \
		  $(SRC)/DWSL.c $(SRC)/MWRM.c \
		  $(SRC)/DWOM.c $(SRC)/MWRL.c \
		  $(SRC)/DRBL.c $(SRC)/DRBM.c \
		  $(SRC)/DRBH.c $(SRC)/MRDL.c \
		  $(SRC)/MRDM.c $(SRC)/MRPM.c \
		  $(SRC)/MRDL_bg.c $(SRC)/DRBL_bg.c \
		  $(SRC)/DRBH_bg.c $(SRC)/MRDM_bg.c \
		  $(SRC)/DRBM_bg.c $(SRC)/MRPM_bg.c \
		  $(SRC)/MWUM.c $(SRC)/MWUL.c \
		  $(SRC)/DWTL.c $(SRC)/MRPH.c \
		  $(SRC)/MRPL.c
DEPS	= $(wildcard $(SRC)/*.h) $(LIBS) $(TC)
BINS	= $(BIN)/fxmark
CPUPOLS = $(SRC)/cpuinfo $(SRC)/cpupol.h $(SRC)/cpupol.py

# tool
CPU_POLICY = $(SRC)/cpu-sequences | $(SRC)/gen_corepolicy

# target
all: $(BINS) $(LIBS) $(TC)

$(BIN)/%: $(SRC)/%.c $(DEPS) $(SRC)/cpupol.h $(SRC)/cpupol.py
	@echo "CC	$@"
	$(Q)$(CC) $< $(CFLAGS) -o $@ $(LIBS) $(TC) $(LDFLAGS)

$(SRC)/cpuinfo:
	$(Q) $(SRC)/set-cpus all > /dev/null
	- $(Q)cp /proc/cpuinfo $@ 

$(SRC)/cpupol.h: $(SRC)/cpuinfo $(SRC)/cpu-sequences $(SRC)/gen_corepolicy
	- $(Q)cat $(SRC)/cpuinfo | $(CPU_POLICY) c  > $@ 2>&1

$(SRC)/cpupol.py: $(SRC)/cpuinfo $(SRC)/cpu-sequences $(SRC)/gen_corepolicy
	- $(Q)cat $(SRC)/cpuinfo | $(CPU_POLICY) py > $@ 2>&1

clean:
	@echo "CLEAN"
	$(Q) rm -rf $(SRC)/*.o $(SRC)/*.pyc $(CPUPOLS) __pycache__

.PHONY: all clean
