import cherrypy
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import urllib3
import json
http = urllib3.PoolManager()

# Use a service account
cred = credentials.Certificate('firebase.json')
firebase_admin.initialize_app(cred)

db = firestore.client()
class Root:
    @cherrypy.expose
    def internal_camera_api(self,url,key,user):
        if key=="UsBdrPXctXpLYTBSQv3zcVFiB7H5WfjjLmtiaYpdJGqxCGPWc27EpVBQnom":
            doc_ref=db.collection(u"pictures").document(url)
            doc_ref.set({
            u'url':url,
            u'user':user
            })
	    return '{"status":"ok"}'
    @cherrypy.expose
    def lib(self,isbn,type):
        if type=="name":
            uri="https://www.googleapis.com/books/v1/volumes?q=isbn:"+isbn

            r = http.request('GET', uri)
            ol=json.loads(r.data)
            s=ol['items']
            z=s[0]['volumeInfo']
            y=z['imageLinks']
            return "<img src="+y['thumbnail']+">"





cherrypy.config.update({'server.socket_host': '0.0.0.0'})
#cherrypy.server.socket_host = 'www.unreached.com'
cherrypy.quickstart(Root())

