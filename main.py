from typing import Dict, List
from common.account import Admin, User
from common.post import Post
import uuid

if __name__ == '__main__':
    admins = {}
    users = {}
    is_login = False
    curr_user_id = ""
    login_user = ""
    login_user_type = ""
    simple_news: Dict[str, Post] = {}
    simple_news_list: List[Post] = []
    promoted_news: Dict[str, Post] = {}
    promoted_news_list: List[Post] = []

    while True:
        cmd=input()
        statements = cmd.split("~")
        if statements[0] == "LOGIN" and is_login == False:
            if statements[1] == "ADMIN":
                user_name = statements[2]
                if user_name in admins:
                    is_login = True
                    login_user = user_name
                    login_user_type = "ADMIN"
                else:
                    print(f'User {user_name} doesn’t exist')
            elif statements[1] == "USER":
                user_name = statements[2]
                if user_name in admins:
                    is_login = True
                    login_user = user_name
                    login_user_type = "USER"
                else:
                    print(f'User {user_name} doesn’t exist')

        elif statements[0] == "SIGNUP":
            if statements[1] == "ADMIN":
                user_name = statements[2]
                if user_name in admins:
                    print(f"Err: User already present with this name")
                else:
                    curr_user_id = uuid.uuid4()
                    new_admin = Admin(curr_user_id,statements[2])
                    admins.update(statements[2], curr_user_id)
            elif statements[1] == "USER":
                user_name = statements[2]
                if user_name in admins:
                    print(f"Err: User already present with this name")
                else:
                    curr_user_id = uuid.uuid4()
                    new_admin = User(curr_user_id,statements[2])
                    users.update(statements[2], curr_user_id)
        
        elif statements[0] == "UPLOAD":
            if login_user_type != "ADMIN":
                print(f'Exception since {statements[3]} is not an admin')
            else:
                post_type = statements[1]
                content = statements[2]
                optional_category = statements[3]
                new_post_id = uuid.uuid4()
                new_post = Post(new_post_id,post_type, content, optional_category)
                if post_type == "NEWS":
                    simple_news.update(new_post_id, new_post)
                    simple_news_list.insert(new_post)
                elif post_type == "PROMOTED_NEWS":
                    promoted_news.update(new_post_id, new_post)
                    promoted_news_list.insert(new_post)
        elif statements[0] == "DELETE":
            if login_user_type != "ADMIN":
                print(f'Exception since {statements[3]} is not an admin')
            else:
                if post_type == "NEWS":
                    simple_news.pop(statements[1])
                elif post_type == "PROMOTED_NEWS":
                    promoted_news.pop(statements[1])

        elif statements[0] == "UPVOTE":
            if post_type == "NEWS":
                curr_post: Post = simple_news.get(statements[1])
                for item in simple_news_list:
                    if item == curr_post:
                        item.add_upvote()
                        simple_news.update(statements[1], item)
            elif post_type == "PROMOTED_NEWS":
                curr_post: Post = promoted_news.get(statements[1])
                for item in promoted_news_list:
                    if item == curr_post:
                        item.add_upvote()
                        promoted_news_list.update(statements[1], item)

        elif statements[0] == "UPVOTE":
            if post_type == "NEWS":
                curr_post: Post = simple_news.get(statements[1])
                for item in simple_news_list:
                    if item == curr_post:
                        item.add_downvote()
                        simple_news.update(statements[1], item)
            elif post_type == "DOWNVOTE":
                curr_post: Post = promoted_news.get(statements[1])
                for item in promoted_news_list:
                    if item == curr_post:
                        item.add_downvote()
                        promoted_news_list.update(statements[1], item)

        elif statements[0] == "FEED":
            if statements[1] == "RECENT":
                for item in promoted_news_list:
                    print(item.get_content())
                for item in simple_news_list:
                    print(item.get_content)
            elif statements[1] == "TRENDING":
                for item in promoted_news_list:
                    print(item.get_content())
                for item in simple_news_list:
                    print(item.get_content)

        else:
            print("Invalid command")



