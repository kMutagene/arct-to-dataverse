from pyDataverse.api import NativeApi

from pyDataverse.models import Dataverse
from pyDataverse.utils import read_file

from domain import first

BASE_URL = 'http://arc-testing-dataverse.qa.km.k8s.zbmed.de/'
API_TOKEN = '73e11470-ff1c-4aa4-b480-bd59db8b774c'
api = NativeApi(BASE_URL, API_TOKEN)

resp = api.get_info_version()
resp.json()

blocks = api.get_metadatablocks().json()["data"]
for m in blocks: print(m)

study_block = api.get_metadatablock("Studies").json()["data"]

api.get
ds = api.get_dataset_versions("doi:10.5072/FK2/3G5PAI").json()["data"]

citation = ds[0]["metadataBlocks"]["citation"]
studies = ds[0]["metadataBlocks"]["Studies"]

print(citation)

study_fields = study_block["fields"]
study_fields
for f in study_fields.keys():
    print(study_fields[f]["name"])
    print(f'    {study_fields[f]["type"]}')
    print(f'    {study_fields[f]["multiple"]}')

dv = Dataverse()
dv._default_json_format

exp = api.get_dataset_export(export_format="dataverse_json", pid="doi:10.5072/FK2/3G5PAI").json()

exp["datasetVersion"]["metadataBlocks"]["Studies"]
