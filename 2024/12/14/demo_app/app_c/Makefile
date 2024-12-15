CC=gcc
CXXFLAGS=-Wall -g
SRC_DIR=./src
OBJ_DIR=./obj
INCLUDE=-Iinclude/
SRCS=$(notdir $(wildcard $(SRC_DIR)/*.c))
OBJS=$(SRCS:.c=.o)
OBJECTS=$(patsubst %.o,$(OBJ_DIR)/%.o,$(OBJS))
DEPS=$(SRCS:.c=.o)
LDFLAGS=
TARGET=main.o

all: $(TARGET)

$(TARGET): $(OBJECTS)
	$(CC) $(CXXFLAGS) $^ -o $@ $(LDFLAGS)

$(OBJ_DIR)/%.o: $(SRC_DIR)/%.c
	$(CC) $(CXXFLAGS) $(INCLUDE) -c $< -o $@ -MD $(LDFLAGS)

.PHONY: all clean

clean:
	$(RM) $(OBJECTS) $(DEPS) $(TARGET)

-include $(DEPS)
