import feedparser

python_wiki_rss_url = "http://limetok.tistory.com/rss"
test = feedparser.parse( python_wiki_rss_url )

herald_rss_url="http://biz.heraldcorp.com/common_prog/rssdisp.php?ct=010000000000.xml"


herald=feedparser.parse(herald_rss_url)

print(herald.entries[0].title)


#item =feedparser.parse( python_wiki_rss_url )

#print(feed["channel"]["title"])
#print(feed.channel.title)
#print(test.entries[0].title)
#print(test.entries[1].title)