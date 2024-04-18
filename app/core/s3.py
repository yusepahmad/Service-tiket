import os
import  s3fs
import json

from loguru import logger
from dotenv import load_dotenv
import botocore.exceptions

from ..utils.res import Res

load_dotenv()



class S3(Res):
    def __init__(self):
        super().__init__()

    def check(self, file_path):
        client_kwargs = {
            'key': os.getenv('KEY'),
            'secret': os.getenv('SECRET_KEY'),
            'endpoint_url': os.getenv('ENDPOINT_URL'),
            'anon': False
        }
        s3 = s3fs.core.S3FileSystem(**client_kwargs)
        try:
            file_content = s3.cat(file_path)
            response = json.loads(file_content)
            return response
        except botocore.exceptions.ClientError as e:
            print(f"File not found: {e}")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None


    def send_json_s3_v2(self, metadata, path_data_raw, file_name_json):
        client_kwargs = {
            'key': os.getenv('KEY'),
            'secret': os.getenv('SECRET_KEY'),
            'endpoint_url': os.getenv('ENDPOINT_URL'),
            'anon': False
        }
        s3 = s3fs.core.S3FileSystem(**client_kwargs)
        json_s3 = str(path_data_raw)
        json_data = json.dumps(metadata, indent=4, ensure_ascii=False)
        try:
            with s3.open(json_s3, 'w') as s3_file:
                s3_file.write(json_data)
            logger.success(f'File {file_name_json} berhasil diupload ke S3.')
        except Exception as e:
            logger.error(f'Gagal mengunggah file {file_name_json} ke S3: {e}')