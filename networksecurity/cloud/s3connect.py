from s3_syncer import S3Sync  # Assuming your class is saved in s3_sync.py

sync = S3Sync()

local_folder = "C:/Users/Veneel/OneDrive/Documents/GitHub/NetworkSecurity/"  # your local folder path
bucket_url = "s3://networksecurityveneel/"  # your full S3 URL

# ✅ Upload to S3
sync.sync_folder_to_s3(local_folder, bucket_url)

# ✅ Download from S3
sync.sync_folder_from_s3(local_folder, bucket_url)
