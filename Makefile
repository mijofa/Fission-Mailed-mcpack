Fission-Mailed-mcpack.zip: pack.mcmeta pack.png README.rst assets/
	rm $@ || true
	zip -x @.gitignore -r $@ $^

Fission-Mailed-datapack.zip: pack.mcmeta pack.png README.rst data/
	rm $@ || true
	zip -x @.gitignore -r $@ $^

Fission-Mailed-mcpack.mcpack: Fission-Mailed-mcpack.zip
	echo "Not Implemented yet, go investigate https://github.com/Kas-tle/java2bedrock.sh" ; false

all: Fission-Mailed-mcpack.zip Fission-Mailed-datapack.zip

clean:
	rm Fission-Mailed-mcpack.zip Fission-Mailed-datapack.zip
