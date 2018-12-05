#from wordpress_xmlrpc import Client, WordPressPost, WordPressMedia
#from wordpress_xmlrpc.methods.posts import NewPost
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.compat import xmlrpc_client
from wordpress_xmlrpc.methods import media, posts
from wordpress_xmlrpc.methods.posts import NewPost

def post(filename):
    wp = Client('https://doricardo.com/images/xmlrpc.php', 'doricardo', 'Raca@0608')

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

    fonte = open('post.txt','r')
    content = fonte.read()
    post = WordPressPost()
    post.title = "POST COM THUMBNAIL"
    post.content = content
    post.post_status = 'publish'
    post.thumbnail = attachment_id

    wp.call(NewPost(post))

    print("Conteúdo posta com sucesso")

if __name__ == "__main__":
    post('post.txt')
