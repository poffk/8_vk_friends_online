import vk
from getpass import getpass


APP_ID = 5750748


def get_user_login():
    login = input('Login: ')
    return login


def get_user_password():
    password = getpass()
    return password


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope=2,
    )
    api = vk.API(session)
    online_friends_id = api.friends.getOnline()
    online_friends_names_json = api.users.get(user_ids=online_friends_id)
    return online_friends_names_json


def output_friends_to_console(online_friends_names_json):
    for online_friend_information in online_friends_names_json:
        print('{0} {1}'.format(online_friend_information['last_name'], online_friend_information['first_name']))


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    online_friends_names_json = get_online_friends(login, password)
    output_friends_to_console(online_friends_names_json)
