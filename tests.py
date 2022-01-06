import unittest
import uuid 
from boto_minio_oops_version_final import BotoMinio, STORAGE_SERVICE, ACCESS_KEY, SECRET_KEY
#13 methods
# ping
# buckets exists or not

def create_bucket():
    pass
    # rt bucket_name

def create_bucket_with_folder():
    pass
    # rt bucket_name, path


def delete_bucket():
    pass

def delete_bucket_with_folder():
    pass



class TestBucket(unittest.TestCase):
    def test_create_new_bucket(self):
        """Check if we can create a bucket in mino"""

        minio = BotoMinio(STORAGE_SERVICE, ACCESS_KEY, SECRET_KEY)
        #self.assertTrue(minio.create_new_bucket(str(uuid.uuid4())))

    def test_create_new_bucket_existing_name(self): 
        """Check if we can't create a bucket existing previously in mino"""

        minio = BotoMinio(STORAGE_SERVICE, ACCESS_KEY, SECRET_KEY)    
        self.assertFalse(minio.create_new_bucket('images'))

    def test_del_bucket(self):
        """Check if we can delete a bucket in mino"""

        minio = BotoMinio(STORAGE_SERVICE, ACCESS_KEY, SECRET_KEY)
        #self.assertTrue(minio.del_bucket('mybucket3'))

    def test_del_bucket_not_existing(self): 
        """Check if we can't delete a bucket not existing in mino"""
        minio = BotoMinio(STORAGE_SERVICE, ACCESS_KEY, SECRET_KEY)
        self.assertFalse(minio.del_bucket(str(uuid.uuid4())))

    def test_check_bucket_exist(self):
        """Check if a bucket existing in mino"""
        minio = BotoMinio(STORAGE_SERVICE, ACCESS_KEY, SECRET_KEY)
        self.assertTrue(minio.check_bucket_exist('mybucket'))

    def test_check_bucket_exist_not_existing(self):
        """Check if a bucket not existing in mino"""
        minio = BotoMinio(STORAGE_SERVICE, ACCESS_KEY, SECRET_KEY)
        self.assertFalse(minio.check_bucket_exist(str(uuid.uuid4()))) #not existing

class TestFile(unittest.TestCase):

    def test_upload_text(self):
        """check if we can upload text into minio"""
        minio = BotoMinio(STORAGE_SERVICE, ACCESS_KEY, SECRET_KEY)
        self.assertTrue(minio.post_data('images','testing','test_text.txt'))
    
    def test_upload_text_bucket_not_existing(self):
        """check if we can't upload text into minio bucket not existing"""
        minio = BotoMinio(STORAGE_SERVICE, ACCESS_KEY, SECRET_KEY)
        self.assertFalse(minio.post_data(str(uuid.uuid4()),'testing','test_text.txt'))


    def test_upload_bytes(self):
        """check if we can upload bytes into minio"""
        minio = BotoMinio(STORAGE_SERVICE, ACCESS_KEY, SECRET_KEY)
        self.assertTrue(minio.post_data('images',bytes(10),'test_bytes'))


    def test_upload_bytes_bucket_not_existing(self):
        """check if we can upload bytes into minio"""
        minio = BotoMinio(STORAGE_SERVICE, ACCESS_KEY, SECRET_KEY)
        self.assertFalse(minio.post_data(str(uuid.uuid4()),bytes(10),'test_bytes'))

    def test_upload_text_file(self):
        minio = BotoMinio(STORAGE_SERVICE, ACCESS_KEY, SECRET_KEY)
        self.assertTrue(minio.post_file('images','commands.txt','commands_in_minio'))
    
    def test_upload_text_file_bucket_not_existing(self):
        minio = BotoMinio(STORAGE_SERVICE, ACCESS_KEY, SECRET_KEY)
        self.assertFalse(minio.post_file(str(uuid.uuid4()),'commands.txt','commands_in_minio'))
    
    def test_upload_text_file_object_name_not_given(self):
        minio = BotoMinio(STORAGE_SERVICE, ACCESS_KEY, SECRET_KEY)
        self.assertTrue(minio.post_file('images','commands.txt'))
       
    def test_upload_text_file_file_path_not_existing(self):
        minio = BotoMinio(STORAGE_SERVICE, ACCESS_KEY, SECRET_KEY)
        self.assertFalse(minio.post_file('images',str(uuid.uuid4()),'commands_in_minio'))
       
       
    def test_delete_object(self):
        """check if we can delete object in minio"""
        minio = BotoMinio(STORAGE_SERVICE, ACCESS_KEY, SECRET_KEY)
        self.assertTrue(minio.delete_object_file('images','me/image.png'))

    def test_get_link(self):
       
        minio = BotoMinio(STORAGE_SERVICE, ACCESS_KEY, SECRET_KEY)
        self.assertIsNotNone(minio.get_link('images','me/base64_file',3800))

    def test_get_link_bucket_not_existing(self):

        minio = BotoMinio(STORAGE_SERVICE, ACCESS_KEY, SECRET_KEY)
        self.assertIsNone(minio.get_link(str(uuid.uuid4()),'me/base64_file',3800))

    def test_read_object_content(self):
        pass

    

