## Identifying Satire in News Article Content
##### DS4400 w/ Felix Yang, Ethan Lee, Derek Leung, Chris He

an analysis of TheOnion vs. nottheonion (regular) news articles

### Data
> built from getting top 1000 posts on r/theonion and r/nottheonion and scraping from the urls from the posts using newspaper3k library

articles.csv format:
- title: article's title
- url: url of the article
- subreddit: either from TheOnion or nottheonion (classification)
- text: raw text of the article

### Classification Methods
- decision trees
- support vector machines
- naive bayes
- *add more here*