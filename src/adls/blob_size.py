import os, uuid, sys, random
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient
from azure.core._match_conditions import MatchConditions
from azure.storage.filedatalake._models import ContentSettings


def run():

    storage_account_name = "adls12133"
    file_system = "fs1"
    folder_name = "dir2"
    credential = DefaultAzureCredential()
    blob_service_client = BlobServiceClient(account_url="{}://{}.blob.core.windows.net".format("https", storage_account_name), credential=credential)
    container_client = blob_service_client.get_container_client(file_system)
    blob_list = container_client.list_blobs(name_starts_with=folder_name)
    size = 0
    if blob_list:
        for blob in blob_list:
            size += blob.size
    print(f"size-{size}")


if __name__ == '__main__':
    run()