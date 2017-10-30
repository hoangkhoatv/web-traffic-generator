clickDepth = 5 # how deep to browse from the rootURL
minWait = 5 # minimum amount of time allowed between HTTP requests
maxWait = 10 # maximum amount of time to wait between HTTP requests
debug = False # set to True to enable useful console output

# use this single item list to test how a site responds to this crawler
# be sure to comment out the list below it.
#rootURLs = ["https://digg.com/"] 

rootURLs = [
	"https://digg.com/",
	"https://www.yahoo.com",
	"https://www.reddit.com",
	"http://www.cnn.com",
	"https://www.facebook.com",
	"http://tuoitre.vn",
	"http://www.ebay.com",
	"https://en.wikipedia.org/wiki/Main_Page",
	"https://austin.craigslist.org/"
	]


# items can be a URL "https://t.co" or simple string to check for "amazon"
blacklist = [
	"https://t.co", 
	"t.umblr.com", 
	"messenger.com", 
	"itunes.apple.com", 
	"l.facebook.com", 
	"bit.ly", 
	"mediawiki", 
	".css", 
	".ico", 
	".xml", 
	"intent/tweet", 
	"twitter.com/share", 
	"signup", 
	"login", 
	"dialog/feed?", 
	".png", 
	".jpg", 
	".json", 
	".svg", 
	".gif", 
	"zendesk",
	"clickserve"
	]  

# must use a valid user agent or sites will hate you
userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) ' \
	'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36' \
	'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36' \
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246' \
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A'

