#from wordpress_xmlrpc import Client, WordPressPost, WordPressMedia
#from wordpress_xmlrpc.methods.posts import NewPost
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.compat import xmlrpc_client
from wordpress_xmlrpc.methods import media, posts
from wordpress_xmlrpc.methods.posts import NewPost
import json

def post(filename):
    wp = Client('https://doricardo.com/images/xmlrpc.php', 'user', 'pass')

    # set to the path to your file
    filename = '/path/to/my/post.jpg'
    filename = 'post.jpg'

    # prepare metadata
    data = {
            'name': 'post.jpg',
            'type': 'image/jpeg',  # mimetype
    }

    # read the binary file and let the XMLRPC library encode it into base64
    with open(filename, 'rb') as img:
            data['bits'] = xmlrpc_client.Binary(img.read())
    response = wp.call(media.UploadFile(data))

    #response = {
    #           'id': 100,
    #           'file': 'StoriesBras18-1.jpg',
    #           'url': 'https://i1.wp.com/www.trisportmag.com.br/wp-content/uploads/2018/11/StoriesBras18-1.jpg',
    #           'type': 'image/jpeg'
    #}

    attachment_id = response['id']

    #fonte = open('post.txt','r')
    #content = fonte.read()
    with open('post_model.json') as fonte:
        data = json.load(fonte)
        title = data['title']
        description = data['description']
        urlmedia = data['media']
        category = data['category']
        tags = data['tags']
        print(title + " " + description)

    post = WordPressPost()
    post.title = title
    post.content = description
    post.post_status = 'publish'
    post.thumbnail = attachment_id

    wp.call(NewPost(post))

    print("Conteúdo posta com sucesso")

if __name__ == "__main__":
    post('post.txt')
