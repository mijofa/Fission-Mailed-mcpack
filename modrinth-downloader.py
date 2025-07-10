#!/usr/bin/python3
import argparse
import hashlib
import json
import os
import pathlib
import tempfile
import typing
import urllib.parse
import urllib.request
import zipfile

argparser = argparse.ArgumentParser()
argparser.add_argument("project_ids",
                       default=[
                           # Server admin assistance
                           'ducky-updater-rework',
                           # Questcraft compatibility
                           'vivecraft',
                           'simple-voice-chat',
                           'voice-chat-interaction',
                           # General VR improvements
                           'immersivemc',
                           'mc-vr-api',
                           # Nice to have
                           'appleskin',
                           'calm-down-dog',
                           'sleep-warp-updated',
                           # Efficiency optimisation
                           'clumps',
                       ],
                       nargs='*',
                       type=str)
# FIXME: Check if this file already exists **before** we download everything and hardlink the temporary zip
argparser.add_argument("--output-file", type=pathlib.Path, default=pathlib.Path("modrinth-server-pack.zip"))
args = argparser.parse_args()


# NOTE: The square braces being part of the string is important!
#       I think modrinth is abusing query parameters as json-encoded strings
version_search_query = urllib.parse.urlencode({"loaders":'["fabric","minecraft","datapack"]',"game_versions":'["1.21.5","1.21"]'})


def recurse_dependencies(project_id_or_slug: str,
                         _history: typing.Optional[list[str]] = None) -> typing.Generator[dict[str, str | None | dict[str, str]] | bool | int, None, None]:
    if _history is None:
        _history = []
    _history.append(project_id_or_slug)
    project_url: str = urllib.parse.urljoin(base="https://api.modrinth.com/v2/project/",
                                            url=project_id_or_slug + '/')
    try:
        response: urllib.request.http.client.HTTPResponse = urllib.request.urlopen(
            url=(urllib.parse.urljoin(base=project_url + '/',
                                    url="version") +
                                    f'?{version_search_query}'))
    except urllib.error.HTTPError as exc:
        if exc.code != 404: raise
        raise urllib.error.HTTPError(code=exc.code, msg=f"Project '{project_id_or_slug}' not found",
                                     url=exc.url, hdrs=exc.hdrs, fp=exc.fp)
    # FIXME: This type checking is a mess, I eyeballed it from the returned JSON
    data: list[dict[str, str | list[dict[str, str | None | dict[str, str]] | bool | int]]] = json.load(response)
    latest_version: dict[str, str | list[dict[str, str | dict[str, str] | None] | bool | int]] = sorted(data,
                            # Sort by version, and prefer fabric over other loaders.
                            # Then grab the newest
                            key=lambda i: (i['version_number'], "fabric" in i["loaders"]))[-1]
    for file in latest_version["files"]:
        if file['primary'] != True: continue
        if "loaders" not in file: file["loaders"] = latest_version["loaders"]
        yield file
    for dependency in latest_version['dependencies']:
        if dependency['project_id'] not in _history and dependency['dependency_type'] == 'required':
            for dependency_file in recurse_dependencies(dependency['project_id'], _history=_history):
                yield dependency_file

print("Collecting project versions & dependencies...")
filespecs: list[dict[str, str | None | dict[str, str]] | bool | int | list[str]] = {file['url']: file
                                                                                for id in args.project_ids
                                                                                for file in recurse_dependencies(id)}.values()
print("Generating zip file...")
with tempfile.NamedTemporaryFile(dir=os.curdir,
                                    prefix='.', suffix='zip') as output_file:
    with zipfile.ZipFile(output_file,
                            mode='w') as zf:
        for filespec in filespecs:
            if 'fabric' in filespec['loaders']:
                dest = 'mods'
            elif 'datapack' in filespec['loaders']:
                dest = 'world/datapacks'
            elif 'minecraft' in filespec['loaders']:
                dest = 'resourcepacks'
            print(dest, filespec['filename'], sep='/')
            # FIXME: Confirm checksums, we have them in the filespec already.
            resp: urllib.request.http.client.HTTPResponse = urllib.request.urlopen(filespec['url'])
            file_data: bytes = resp.read()
            assert hashlib.sha1(file_data).hexdigest() == filespec['hashes']['sha1'],   "sha1sum mismatch!"
            assert hashlib.sha512(file_data).hexdigest() == filespec['hashes']['sha512'], "sha512sum mismatch!"
            zf.writestr(zinfo_or_arcname=f"{dest}/{filespec['filename']}",
                        data=file_data)

    # Hard link to unhidden destination path before Python deletes the temp file
    os.link(output_file.name, args.output_file)
