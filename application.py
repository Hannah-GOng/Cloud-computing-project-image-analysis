from flask import Flask, render_template, request
import boto3
import json

application = Flask(__name__)

@application.route('/')
def home():
    return "Hello World!"

# detect the celebrities
@application.route('/upload', methods=['POST', 'GET'])
def detect_celebrity():
    if request.method == 'POST':
        file = request.files['file']
        bucket = 'cloud-computing-706-image-analysis'
    
        # create a resource of S3 to use 'Bucket' attribute
        s3_resource = boto3.resource('s3')

        # upload the file as on object using put_object
        s3_resource.Bucket(bucket).put_object(Key=file.filename, Body=file)
    
        # Celebrity Recognition by AWS Rekognition
        client=boto3.client('rekognition')
        response = client.recognize_celebrities(Image= {'S3Object': {'Bucket': bucket, 'Name': file.filename}})

        print('Detected faces for ' + file)    
        for celebrity in response['CelebrityFaces']:
            print ('Name: ' + celebrity['Name'])
            print ('Id: ' + celebrity['Id'])
            print ('Position:')
            print ('   Left: ' + '{:.2f}'.format(celebrity['Face']['BoundingBox']['Height']))
            print ('   Top: ' + '{:.2f}'.format(celebrity['Face']['BoundingBox']['Top']))
            print ('Info')
        
        print("Celebrities detected: " + str(len(response['CelebrityFaces'])))

    
if __name__ == "__main__":
    application.run()