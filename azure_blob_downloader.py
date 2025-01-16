import os
from azure.storage.blob import BlobServiceClient

# Replace with your actual connection string and container name
CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=azchatgpt;AccountKey=inYbI5JwKlhgBFbRoD1HRdal8Ip9J1uq1pa072wrig7YhTSToL7RqxRpgUDkbmMe43v3qzpaizIG+AStlRj04g==;EndpointSuffix=core.windows.net"
CONTAINER_NAME = "text-documents/def.finanze.it"
LOCAL_DOWNLOAD_PATH = "./second"  # Local path to save downloaded files

# Initialize the BlobServiceClient
blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)
container_client = blob_service_client.get_container_client(CONTAINER_NAME)

def download_blob(blob_name):
    """Download a single blob."""
    blob_client = container_client.get_blob_client(blob_name)
    local_file_path = os.path.join(LOCAL_DOWNLOAD_PATH, blob_name)

    # Create local directory if it doesn't exist
    os.makedirs(os.path.dirname(local_file_path), exist_ok=True)

    # Download the blob data to a local file
    with open(local_file_path, "wb") as download_file:
        download_file.write(blob_client.download_blob().readall())
    print(f"Downloaded {blob_name} to {local_file_path}")

def download_multiple_blobs(start_index, end_index):
    """Download multiple blobs based on the index range."""
    for index in range(start_index, end_index, 1000):
        blob_name = f"metadata_{index}.xlsx"
        download_blob(blob_name)

# Download files from file_0 to file_121
download_multiple_blobs(0, 8000)