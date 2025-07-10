#!/usr/bin/python3
import argparse
import hashlib
import re
import os
import pathlib
import tempfile
import urllib.request
import urllib.parse
import zipfile

import bs4

argparser = argparse.ArgumentParser()
argparser.add_argument("pack_ids",
                       default=[
                           'mob_muffler',
                           'gravestones',
                           'item_magnet',
                           'chicken_shedding',
                           'ender_beacons',
                           'paperbark',
                           'mendfinity',
                           'auto-plant_saplings',
                           'plated_elytra',
                           'weakened_bedrock',
                           'elevators',
                           'apiarist_suit',
                           'effective_netherite_armour',
                           'invisible_item_frames',
                           'beehive_lore',
                           'trim_trader',
                           'netherite_shulker_boxes',
                           # Recipe packs
                           'mixed_stone_tools',
                           'zombie_leather',
                           'botanical_replication',
                           'equestrian_craftables',
                           'layers2blocks',
                           'craftable_bell',
                           'bone_black',
                           'sticky_honey_pistons',
                           'further_fermentation',
                           'blasted_ore_blocks',
                           'turtle_boxes',
                           'cobbled_cutting',
                       ],
                       nargs='*',
                       type=str)
# FIXME: Check if this file already exists **before** we download everything and hardlink the temporary zip
argparser.add_argument("--output-file", type=pathlib.Path, default=pathlib.Path("voodoobeard-server-pack.zip"))
args = argparser.parse_args()

required_pack_urls: dict[str, str] = {}

print("Getting adfoc.us links")
with urllib.request.urlopen("https://mc.voodoobeard.com/") as voodoobeard_resp:
    # FIXME: pass the encoding header to decode?
    voodoobeard_data = bs4.BeautifulSoup(voodoobeard_resp.read().decode(), "html.parser")
    all_packs = {pack.select_one('img[id]').get('id'): pack for pack in voodoobeard_data.select('div.card:has(img[id])')}
    for required_pack_id in args.pack_ids:
        assert required_pack_id in all_packs
        pack_advert_url = all_packs[required_pack_id].select_one('a:has(i.fa-download)').get('href')
        assert urllib.parse.urlparse(pack_advert_url).netloc == "adfoc.us"
        pack_advert_request = urllib.request.Request(
            pack_advert_url,
            # NOTE: The referer can be removed, but the removing any of the other headers results in an empty 200 response
            headers={'Referer': 'https://mc.voodoobeard.com/',
                     'Accept': 'text/html',
                     'Accept-Language': 'en-AU,en'})
        with urllib.request.urlopen(pack_advert_request) as pack_advert_response:
            required_pack_urls[required_pack_id], = re.findall("""click_url *= *["'](.*)["'] *;""",
                                                               # FIXME: pass the encoding header to decode?
                                                               pack_advert_response.read().decode())

print("Generating zip file...")
with tempfile.NamedTemporaryFile(dir=os.curdir,
                                    prefix='.', suffix='zip') as output_file:
    with zipfile.ZipFile(output_file,
                            mode='w') as zf:
        for pack_id, url in required_pack_urls.items():
            dest: pathlib.Path = pathlib.Path('world/datapacks') / pathlib.Path(urllib.parse.urlparse(url).path).name
            print(url, '->', dest)
            # FIXME: Confirm checksums, we have them in the filespec already.
            resp: urllib.request.http.client.HTTPResponse = urllib.request.urlopen(url)
            zf.writestr(zinfo_or_arcname=str(dest),
                        data=resp.read())

    # Hard link to unhidden destination path before Python deletes the temp file
    os.link(output_file.name, args.output_file)
