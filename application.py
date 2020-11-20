from flask import Flask, render_template, request
import boto3
import json


@application.route('/upload', methods=['POST', 'GET'])

# detect the celebrities
def recognize_celebrities():
    file = request.files['file']
    bucket = ''
    
    # create a resource of S3 to use 'Bucket' attribute
    s3_resource = boto3.resource('s3')

    # upload the file as on object using put_object
    s3_resource.Bucket(bucket).put_object(Key=file.filename, Body=file)
    
    Image= {'S3Object': {'Bucket': bucket, 'Name': file.filename}}
    
    # Celebrity Recognition by AWS Rekognition
    client=boto3.client('rekognition')
    response = client.recognize_celebrities(Image={'Bytes': image.read()})

    print('Detected faces for ' + photo)    
    for celebrity in response['CelebrityFaces']:
        print ('Name: ' + celebrity['Name'])
        print ('Id: ' + celebrity['Id'])
        print ('Position:')
        print ('   Left: ' + '{:.2f}'.format(celebrity['Face']['BoundingBox']['Height']))
        print ('   Top: ' + '{:.2f}'.format(celebrity['Face']['BoundingBox']['Top']))
        print ('Info')
        for url in celebrity['Urls']:
            print ('   ' + url)
        print
        
        celeb_count=len(response['CelebrityFaces'])
        print("Celebrities detected: " + str(celeb_count)

    
if __name__ == "__main__":
    application.run()
