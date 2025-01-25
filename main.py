import os
from dotenv import load_dotenv
import requests

# Load environment variables
load_dotenv()
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
INSTAGRAM_ACCOUNT_ID = os.getenv("INSTAGRAM_ACCOUNT_ID")

# Base URL for API calls
BASE_URL = "https://graph.facebook.com/v17.0"

def get_account_info():
    """
    Fetch basic information about the Instagram account.
    """
    url = f"{BASE_URL}/{INSTAGRAM_ACCOUNT_ID}"
    params = {
        "fields": "username,followers_count,media_count",
        "access_token": ACCESS_TOKEN,
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        print("Instagram Account Info:")
        print(f"Username: {data.get('username')}")
        print(f"Followers: {data.get('followers_count')}")
        print(f"Media Count: {data.get('media_count')}")
    else:
        print(f"Error fetching account info: {response.status_code}, {response.json()}")


# def get_recent_posts():
#     """
#     Fetch recent posts from the Instagram account.
#     """
#     url = f"{BASE_URL}/{INSTAGRAM_ACCOUNT_ID}/media"
#     params = {
#         "fields": "id,caption,media_type,media_url,permalink",
#         "access_token": ACCESS_TOKEN,
#     }
#     response = requests.get(url, params=params)
#     if response.status_code == 200:
#         data = response.json()
#         print("Recent Posts:")
#         for post in data.get("data", []):
#             print(f"- Post ID: {post['id']}")
#             print(f"  Caption: {post.get('caption', 'No caption')}")
#             print(f"  Type: {post['media_type']}")
#             print(f"  URL: {post['media_url']}")
#             print(f"  Permalink: {post['permalink']}")
#             print()
#     else:
#         print(f"Error fetching posts: {response.status_code}, {response.json()}")
def get_recent_posts():
    """
    Fetch recent posts from the Instagram account.
    Handles both image and video posts.
    """
    url = f"{BASE_URL}/{INSTAGRAM_ACCOUNT_ID}/media"
    params = {
        "fields": "id,caption,media_type,media_url,thumbnail_url,permalink",
        "access_token": ACCESS_TOKEN,
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        print("Recent Posts:")
        for post in data.get("data", []):
            print(f"- Post ID: {post['id']}")
            print(f"  Caption: {post.get('caption', 'No caption')}")
            print(f"  Type: {post['media_type']}")
            if post["media_type"] == "VIDEO":
                print(f"  Thumbnail URL: {post.get('thumbnail_url', 'No thumbnail available')}")
            else:
                print(f"  Media URL: {post.get('media_url', 'No media available')}")
            print(f"  Permalink: {post['permalink']}")
            print()
    else:
        print(f"Error fetching posts: {response.status_code}, {response.json()}")


# def get_post_details(post_id):
#     """
#     Fetch details about a specific post.
#     Args:
#         post_id (str): The ID of the Instagram post.
#     """
#     url = f"{BASE_URL}/{post_id}"
#     params = {
#         "fields": "id,caption,media_type,media_url,comments_count,like_count,permalink",
#         "access_token": ACCESS_TOKEN,
#     }
#     response = requests.get(url, params=params)
#     if response.status_code == 200:
#         data = response.json()
#         print("Post Details:")
#         print(f"ID: {data['id']}")
#         print(f"Caption: {data.get('caption', 'No caption')}")
#         print(f"Type: {data['media_type']}")
#         print(f"Media URL: {data['media_url']}")
#         print(f"Comments: {data['comments_count']}")
#         print(f"Likes: {data['like_count']}")
#         print(f"Permalink: {data['permalink']}")
#     else:
#         print(f"Error fetching post details: {response.status_code}, {response.json()}")
def get_post_details(post_id):
    """
    Fetch details about a specific post.
    Handles both image and video posts.
    Args:
        post_id (str): The ID of the Instagram post.
    """
    url = f"{BASE_URL}/{post_id}"
    params = {
        "fields": "id,caption,media_type,media_url,thumbnail_url,comments_count,like_count,permalink",
        "access_token": ACCESS_TOKEN,
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        print("Post Details:")
        print(f"ID: {data['id']}")
        print(f"Caption: {data.get('caption', 'No caption')}")
        print(f"Type: {data['media_type']}")
        if data["media_type"] == "VIDEO":
            print(f"Thumbnail URL: {data.get('thumbnail_url', 'No thumbnail available')}")
        else:
            print(f"Media URL: {data.get('media_url', 'No media available')}")
        print(f"Comments: {data['comments_count']}")
        print(f"Likes: {data['like_count']}")
        print(f"Permalink: {data['permalink']}")
    else:
        print(f"Error fetching post details: {response.status_code}, {response.json()}")


def get_post_comments(post_id):
    """
    Fetch comments on a specific post.
    Args:
        post_id (str): The ID of the Instagram post.
    """
    url = f"{BASE_URL}/{post_id}/comments"
    params = {
        "fields": "id,text,username",
        "access_token": ACCESS_TOKEN,
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        print("Comments:")
        for comment in data.get("data", []):
            print(f"- {comment['username']}: {comment['text']}")
    else:
        print(f"Error fetching comments: {response.status_code}, {response.json()}")


if __name__ == "__main__":
    print("Choose an operation:")
    print("1. Get account info")
    print("2. Get recent posts")
    print("3. Get post details")
    print("4. Get post comments")

    choice = input("Enter the operation number: ")

    if choice == "1":
        get_account_info()
    elif choice == "2":
        get_recent_posts()
    elif choice == "3":
        post_id = input("Enter the post ID: ")
        get_post_details(post_id)
    elif choice == "4":
        post_id = input("Enter the post ID: ")
        get_post_comments(post_id)
    else:
        print("Invalid choice. Please try again.")
