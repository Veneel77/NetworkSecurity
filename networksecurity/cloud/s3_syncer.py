import subprocess

class S3Sync:
    def sync_folder_to_s3(self, folder, aws_bucket_url):
        try:
            print(f"Uploading from {folder} to {aws_bucket_url}")
            subprocess.check_call(["aws", "s3", "sync", folder, aws_bucket_url])
        except subprocess.CalledProcessError as e:
            print("Upload failed:", e)

    def sync_folder_from_s3(self, folder, aws_bucket_url):
        try:
            print(f"Downloading from {aws_bucket_url} to {folder}")
            subprocess.check_call(["aws", "s3", "sync", aws_bucket_url, folder])
        except subprocess.CalledProcessError as e:
            print("Download failed:", e)
