CXX      := g++
CXXFLAGS := -Wall -Wextra -std=c++17 -Iinclude -g
LDFLAGS  :=

TARGET   := lexico

NOM      := Louvet
PRENOM   := Arthur
RENDU    := $(NOM)-$(PRENOM)

# Cherche tous les .cpp sous src/ (récursif)
SRC := $(shell find src -name '*.cpp')
# Translation src/.../foo.cpp -> obj/.../foo.o
OBJ := $(patsubst src/%.cpp,obj/%.o,$(SRC))

all: $(TARGET)

$(TARGET): $(OBJ)
	$(CXX) $(LDFLAGS) -o $@ $^

# Crée le sous-dossier de obj/ à la volée si besoin
obj/%.o: src/%.cpp
	@mkdir -p $(dir $@)
	$(CXX) $(CXXFLAGS) -c $< -o $@

clean:
	rm -rf obj $(TARGET)

rebuild: clean all