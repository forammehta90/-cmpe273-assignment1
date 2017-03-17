from flask import Flask
from flask import jsonify
from github import Github

import sys
import yaml


app = Flask(__name__)
#print sys.argv[1]

url=[]

url=sys.argv[1].split("/")
print "url:- %s" %url

for x in url:
#	print "x %r" %x
	if 'github' in x:
		user= url[url.index(x)+1]
		repo=url[url.index(x)+2]
#		print "user %s" % user
#		print "repo %s" % repo
		break
 



@app.route("/v1/<variable>.yml")
def hello(variable):
	git=Github().get_user(user).get_repo(repo)
	stream=yaml.load(git.get_file_contents(variable+".yml").content.decode(git.get_contents(variable+".yml").encoding))
#	print "stream %r" % stream
    	return jsonify(stream)

if __name__ == "__main__":
    app.config["url"] = sys.argv[1]
    app.run(debug=True,host='0.0.0.0')
