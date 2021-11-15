import bibmanager.bib_manager as bibm
import json
import sys

if __name__ == "__main__":
    bibs = bibm.load()
    keys = [bib.key for bib in bibs]
    titles = [bib.title for bib in bibs]

    output = {'items':[]}

    for key, title  in zip(keys, titles):
        output['items'].append({'subtitle':title, 'uid':key, 'title':key, 'arg':key, 'autocomplete':key, })

    json_dump = json.dumps(output)

    sys.stdout.write(json_dump)


