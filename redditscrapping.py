import praw

# Initialize the Reddit API client
reddit = praw.Reddit(
    client_id='Jf3UPD-PHg-O9yNtvXTItQ',
    client_secret='h2R5PwZpc9bfNSxAWwy-0LFhd0wPhQ',
    user_agent='reddit scrapping by MaskedGoats'
)

def scrape_subreddit_posts(subreddit_name, search_query, num_posts=10):
    subreddit = reddit.subreddit(subreddit_name)
    posts = []

    for post in subreddit.search(search_query, sort='new', limit=num_posts):
        posts.append({
            'title': post.title,
            'author': post.author.name,
            'score': post.score,
            'num_comments': post.num_comments,
            'url': post.url,
        })

    return posts

# Example usage
if __name__ == '__main__':
    subreddit_name = 'neurology'  # Change this to the desired subreddit
    search_query = 'women'  # Change this to your specific search query
    num_posts = 5  # Number of posts to scrape

    scraped_posts = scrape_subreddit_posts(subreddit_name, search_query, num_posts)
    for post in scraped_posts:
        print(f"Title: {post['title']}")
        print(f"Author: {post['author']}")
        print(f"Score: {post['score']}")
        print(f"Number of Comments: {post['num_comments']}")
        print(f"URL: {post['url']}")
        print('---')