import os, uuid, sys, random
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient
from azure.core._match_conditions import MatchConditions
from azure.storage.filedatalake._models import ContentSettings


def run():
    storage_account_name = "adls12133"
    file_system = "fs1"
    #folder_name = "dir1"
    credential = DefaultAzureCredential()
    blob_service_client = BlobServiceClient(account_url="{}://{}.blob.core.windows.net".format("https", storage_account_name), credential=credential)

    # folders
    container_client = blob_service_client.get_container_client(file_system)
    folder_name = "dir1"
    folders = []
    directories = []
    i = 0
    folder_list = container_client.walk_blobs(delimiter="/")
    if folder_list:
        for folder in folder_list:
            if folder.name != "_log/" and folder.name != "_logexception/":
                folders.append(folder.name)
                i += 1
                print(f"start------------------{folder.name}")

                blobs = container_client.list_blobs(name_starts_with="dir11")
                print(f"blobs-{blobs}")
                for blob in blobs:
                    print(f"blobsize-{blob.size}")
                    name = blob.name
                    print(f"blobname-{name}")
                    splitted_elements = name.split('/')
                    if '/' in name and len(name.split('/')) > 1:
                        print(f"splitted_elements[1]-{splitted_elements[1]}")
                        if splitted_elements[1] not in directories:
                            directories.append(splitted_elements[1])
                            print(f"added folder-{splitted_elements[1]}")
    print(f"dir-{directories}")

    # my_string1="dir1/dir11"
    # print(my_string1.split("dir1/")[1])

    # my_string="hello python world , i'm a beginner"
    # print(my_string.split("world", 1)[0])

    # lis dirs
    # logging.info(path)
    # recursive = True
    # if not folder_name == '' and not folder_name.endswith('/'):
    #     folder_name += '/'

    # blob_iter = container_client.list_blobs(name_starts_with=folder_name)
    # dirs = []
    # for blob in blob_iter:
    #     relative_dir = os.path.dirname(os.path.relpath(blob.name, folder_name))
    #     print("Rel Dir: " + str(relative_dir))
    #     if relative_dir and (recursive or not '/' in relative_dir) and not relative_dir in dirs:
    #         dirs.append(relative_dir)
    # print(f"dirs-{dirs}")

if __name__ == '__main__':
    run()