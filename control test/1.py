import requests

def email(name_user):
    usernames = requests.get('https://jsonplaceholder.typicode.com/users/', params={'username': name_user})
    user_id = usernames.json()[0]['id']
    posts = requests.get('https://jsonplaceholder.typicode.com/posts', params={'userId': user_id})
    posts_of_user = []
    for i in posts.json():
        posts_of_user.append(i['id'])
    list_of_emails = []
    for elem in posts_of_user:
        comments = requests.get('https://jsonplaceholder.typicode.com/comments', params={'postId' : elem})
        for i in comments.json():
            list_of_emails.append(i['email'])
    return list_of_emails


print(email('Antonette'))
