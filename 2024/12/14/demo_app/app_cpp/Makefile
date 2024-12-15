CC=g++
CXXFLAGS=-Wall -g
SRC_DIR=./src
OBJ_DIR=./obj
INCLUDE=-Iinclude/
SRCS=$(notdir $(wildcard $(SRC_DIR)/*.cpp))
OBJS=$(SRCS:.cpp=.o)
OBJECTS=$(patsubst %.o,$(OBJ_DIR)/%.o,$(OBJS))
DEPS=$(SRCS:.cpp=.o)
LDFLAGS=
TARGET=main.o

all: $(TARGET)

$(TARGET): $(OBJECTS)
	$(CC) $(CXXFLAGS) $^ -o $@ $(LDFLAGS)

$(OBJ_DIR)/%.o: $(SRC_DIR)/%.cpp
	$(CC) $(CXXFLAGS) $(INCLUDE) -c $< -o $@ -MD $(LDFLAGS)

.PHONY: all clean

clean:
	$(RM) $(OBJECTS) $(DEPS) $(TARGET)

-include $(DEPS)
