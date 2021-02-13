import requests
import json


class Linkedin:
    def __init__(self, organizationID, token):
        self.organizationID = organizationID
        self.token = token
        self.baseurl = "https://api.linkedin.com"

        self.headers = {
            'Content-Type': 'application/json',
            'X-Restli-Protocol-Version': '2.0.0',
            'Authorization': 'Bearer ' + self.token
        }

    def run(self):
        content = "Merhaba, ben robin_scherbotsky. \n #cyberdetails #robin_scherbotsky"
        imagePath = "sqlimother.png"
        check = self.registerImage()
        if check:
            uploadUrl = check[0]
            asset = check[1]
            if self.uploadImage(uploadUrl, imagePath):
                self.sendPostJustText(content)
                # self.sendPostWithImage(asset, content)

    def post(self, path, json):
        return requests.post(self.baseurl + path, headers=self.headers, json=json)

    def convertJson(self, data):
        return json.loads(data)

    def registerImage(self):
        postData = {
            "registerUploadRequest": {
                "owner": "urn:li:organization:" + self.organizationID,
                "recipes": [
                    "urn:li:digitalmediaRecipe:feedshare-image"
                ],
                "serviceRelationships": [
                    {
                        "identifier": "urn:li:userGeneratedContent",
                        "relationshipType": "OWNER"
                    }
                ]
            }
        }

        response = self.post('/v2/assets?action=registerUpload', postData)
        data = self.convertJson(response.content)
        uploadUrl = data['value']['uploadMechanism']['com.linkedin.digitalmedia.uploading.MediaUploadHttpRequest'][
            'uploadUrl']
        asset = data['value']['asset']
        if response.status_code == 200:
            return uploadUrl, asset

    def uploadImage(self, uploadUrl, imagePath):
        headers = {
            'Authorization': 'Bearer ' + self.token
        }
        with open(imagePath, 'rb') as image:
            x = requests.put(uploadUrl, headers=headers, data=image)
            if x.status_code == 201:
                return True

    def sendPostWithImage(self, asset, content):

        postData = {
            "author": "urn:li:organization:" + self.organizationID,
            "lifecycleState": "PUBLISHED",
            "specificContent": {
                "com.linkedin.ugc.ShareContent": {
                    "media": [
                        {
                            "media": asset,
                            "status": "READY",
                            "title": {
                                "attributes": [],
                                "text": ""
                            }
                        }
                    ],
                    "shareCommentary": {
                        "text": content
                    },
                    "shareMediaCategory": "IMAGE"
                }
            },
            "visibility": {
                "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
            }
        }
        self.post('/v2/ugcPosts', postData)

    def sendPostJustText(self, content):

        postData = {
            "author": "urn:li:organization:" + self.organizationID,
            "lifecycleState": "PUBLISHED",
            "specificContent": {
                "com.linkedin.ugc.ShareContent": {
                    "shareCommentary": {
                        "text": content
                    },
                    "shareMediaCategory": "NONE"
                }
            },
            "visibility": {
                "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
            }
        }

        self.post('/v2/ugcPosts', postData)


if __name__ == "__main__":
    organizationID = ''
    token = ''
    app = Linkedin(organizationID, token)
    app.run()
