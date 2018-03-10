'''from watson_developer_cloud import VisualRecognitionV3\
visual_recognition = VisualRecognitionV3(
    '2016-05-20',
    api_key='988d558c4a7e45a98f2aa9f1d52a66d5be30287d'
)

classify(images_file=None, parameters=None, accept_language=None, images_file_content_type=None, images_filename=None)


api_key = 988d558c4a7e45a98f2aa9f1d52a66d5be30287d
'''
'''
import json
from watson_developer_cloud import VisualRecognitionV3

visual_recognition = VisualRecognitionV3(
    '2016-05-20',
    api_key='988d558c4a7e45a98f2aa9f1d52a66d5be30287d')

with open('./fruitbowl.jpg', 'rb') as images_file:
    classes = visual_recognition.classify(
        images_file,
        parameters=json.dumps({
            'classifier_ids': ['fruits_1462128776','SatelliteModel_6242312846'],
            'threshold': 0.6
        }))
print(json.dumps(classes, indent=2))


prez.jpg
fruitbowl.jpg


###
Daniel
5a4c8718738c1125628198f74376d5ac9d486df8

###
Evan
988d558c4a7e45a98f2aa9f1d52a66d5be30287d
'''
import json
from watson_developer_cloud import VisualRecognitionV3

visual_recognition = VisualRecognitionV3(
    '2016-05-20',
    api_key='5a4c8718738c1125628198f74376d5ac9d486df8')

with open('./pictures/20180310_100553.jpg', 'rb') as images_file:
    faces = visual_recognition.classify(images_file) #parameters=json.dumps({'threshold':0.6}))
print(json.dumps(faces, indent=2))

