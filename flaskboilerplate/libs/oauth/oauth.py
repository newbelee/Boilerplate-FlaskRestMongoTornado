import requests


class OAuth(object):

    endpoint = None

    def __init__(self, endpoint):
        self.endpoint = endpoint

    def verify(self, access_token):
        if self.endpoint is None:
            return True
        r = requests.get(self.endpoint + "?access_token=" + access_token)
        if r.status_code == 200:
            return True
        return False

if __name__ == "__main__":
    oauth = OAuth("http://localhost:9999/api/accesstoken")

    if oauth.verify("YzJlMTE1YmY4NzgxNzZiM2QzNWM5MmU2OWNiZWQ4MGViMmQ1M2Q4YzUxNTQ2NmNjNTc1OTQ2MjY4M2Y0OGNlMQ"):
        print "AccessToken valid"
    else:
        print "AccessToken invalid"