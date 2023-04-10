RESOURCES := $(shell find assets/minecraft/textures/ assets/minecraft/models/ -type f -not -name '.*' -not -name '*~' -print)
Fission-Mailed-mcpack.zip: pack.mcmeta pack.png README.rst $(RESOURCES)
	rm $@ || true
	zip -r $@ $^

LOOT_TABLES := $(shell find data/ -type f -not -name '.*' -not -name '*~' -print)
Fission-Mailed-datapack.zip: pack.mcmeta pack.png README.rst $(LOOT_TABLES)
	rm $@ || true
	zip -r $@ $^

Fission-Mailed-mcpack.mcpack: Fission-Mailed-mcpack.zip
	echo "Not Implemented yet, go investigate https://github.com/Kas-tle/java2bedrock.sh" ; false

all: Fission-Mailed-mcpack.zip Fission-Mailed-datapack.zip

clean:
	rm Fission-Mailed-mcpack.zip
