import praw
import time

redditObject = praw.Reddit(user_agent="undergroundrapbot by Harsha Dodda /u/undergroundrapbot")  # makes a reddit object
redditObject.login()  # if you leave it blank, it'll prompt you for user/pass
    # which is more secure than leaving the info in the function

print("Successfully logged in")

rappers_to_follow = ["cunninlynguists", "mf doom", "doom", "big krit", "mick jenkins", "blu", "deltron", "deltron3030",
    "lushlife", "nujabes", "oddisee", "open mike eagle", "the pro letarians", "quest", "thurz", "vakill"]
# list of the rappers I want to follow on reddit.com/r/hiphopheads

cache = []  # keeps a list of the comments that have already been replied to,
    # so the bot doesn't reply to the same comment multiple times


def runBot():
    print("getting subreddit")
    subreddit = redditObject.get_subreddit("hiphopheads")  # goes into r/hiphopheads
    comments = subreddit.get_comments(limit=100)  # the limit in number of requests is 200 for the praw api
    for comment in comments:  # loop through the comments that the reddit bot found
        comment_text = comment.body.lower()  # takes the comment body and returns it in all lower case letters
        isMatch = any(
            string in comment_text for string in rappers_to_follow)  # returns true if any string in the comment matches
        # any string in the list of rappers I want to follow
        if isMatch and comment.id not in cache:
            comment.reply("Replying to this comment so I can follow one of the rappers you are talking about")
            print("comment id:" + comment.id + "\n")
            print("comment text: \n" + comment_text + "\n")
            cache.append(comment.id)

while True:
    runBot()
    time.sleep(5)
