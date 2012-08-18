from boto.s3.key import Key
from boto import connect_s3
from buddy.utils import datetime_string

def upload_to_s3(file, bucket):
    """ 
    file is the file that is given from request.FILES

    Example:
    upload_to_s3(request.FILES['image'], 'bucket-name')
    """
    filename = datetime_string() + file.name

    conn = connect_s3()
    bucket = conn.create_bucket(bucket)
    k = Key(bucket)
    k.key = filename
    k.content_type = mimetypes.guess_type(filename)[0]
    k.set_contents_from_string(file.read())
    k.set_acl('public-read')

    return filename
