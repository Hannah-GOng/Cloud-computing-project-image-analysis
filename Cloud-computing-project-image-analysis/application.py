from flask import Flask, render_template, request
import boto3
import json


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'upload/'

@app.route('/')
def hello_world():
   return 'Add /upload_page to IP address to begin!'

@app.route('/upload_page')
def upload_file():
   return render_template('upload_page.html')

# detect the celebrities
@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():
    if request.method == 'POST':
        file = request.files['file']
        bucket = 'cloud-computing-706-image-analysis'
    
        # create a resource of S3 to use 'Bucket' attribute
        s3_resource = boto3.resource('s3')

        # upload the file as on object using put_object
        s3_resource.Bucket(bucket).put_object(Key=file.filename, Body=file)
        
         # Celebrity Recognition by AWS Rekognition
        client=boto3.client('rekognition', region_name = 'us-east-2')
        response = client.recognize_celebrities(Image = {'S3Object': {'Bucket': bucket, 'Name': file.filename}})
        
        for celebrity in response['CelebrityFaces']:
            name = celebrity['Name']
            Id = celebrity['Id']
            
        return name
    
if __name__ == "__main__":
    app.run(port = 8080, host = '0.0.0.0', debug = True)