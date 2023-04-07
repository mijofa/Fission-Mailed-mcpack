RESOURCES := $(shell find assets/minecraft/textures/ assets/minecraft/models/ -not -iname '*~' -print)
Fission-Mailed-mcpack.zip: pack.mcmeta pack.png README.rst $(RESOURCES)
	rm $@ || true
	zip -r $@ $^

Fission-Mailed-mcpack.mcpack: Fission-Mailed-mcpack.zip
	echo "Not Implemented yet, go investigate https://github.com/Kas-tle/java2bedrock.sh" ; false

all: Fission-Mailed-mcpack.zip

clean:
	rm Fission-Mailed-mcpack.zip
