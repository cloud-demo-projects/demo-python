import os, uuid, sys, random
from azure.identity import DefaultAzureCredential
from azure.storage.filedatalake import DataLakeServiceClient
from azure.core._match_conditions import MatchConditions
from azure.storage.filedatalake._models import ContentSettings


def run():
    storage_account_name = "adls12133"
    default_credential = DefaultAzureCredential()
    datalake_client = DataLakeServiceClient(account_url="{}://{}.dfs.core.windows.net".format(
        "https", storage_account_name), credential=default_credential)

    # Get folders
    size = 0
    file_system = "fs1"

    file_system_client = datalake_client.get_file_system_client(file_system)
    for path in file_system_client.get_paths(path="dir1/dir11"):
        size += path.content_length
        print(f"path.content_length-{path.name}{path.content_length}")
    print(f"total size-{size}")



#working backup
# # get folders
#     folders = []
#     i = 0
#     size = 0
#     for file_system in datalake_client.list_file_systems():
#         print(f"container-name:{file_system.name}")
#         file_system_client = datalake_client.get_file_system_client(file_system)
#         for path in file_system_client.get_paths(path="dir1"):
#             print(f"path: {path.is_directory}-{path.content_length}")
#             if path.is_directory:
#                 folder = path.name
#                 # print(f"path: {path}")
#                 print(f"directory: {file_system.name}.{path.name}.{path.content_length}")
#                 folders.append(folder)
#                 i += 1
#             else:
#                 print(f"filepath: {path}.{path.content_length}")
#                 size += path.content_length
#                 print(f"size-{size}")
#     print(f"size-{size}")
#     print(f"folders: {folders}")


            #directory_system_client = file_system_client.get_directory_client(folder)
            #print(f"path_name: {directory_system_client.path_name}")
                # for path in file_system_client.get_paths(folder):
                #     if path.is_directory == False:
                #         print(f"filename: {path_name}")






if __name__ == '__main__':
    run()