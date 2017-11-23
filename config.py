clickDepth = 5 # how deep to browse from the rootURL
minWait = 10 # minimum amount of time allowed between HTTP requests
maxWait = 20 # maximum amount of time to wait between HTTP requests
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
	"https://austin.craigslist.org/",
	"https://world.taobao.com",
	"http://kenh14.vn",
	"https://www.amazon.com",
	"http://kbsworld.kbs.co.kr",
	"https://tiki.vn",
	"http://dangkyhochieu.dientap.cnsc/egov/php/login.php",
	"http://dangkyhochieu.dientap.cnsc/egov/php/create_captcha.php",
	"http://oneshop.dientap.cnsc/index.php"
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
ipList = [
	"192.168.250.247",
	"192.168.250.249",
	"192.168.250.250",
	"192.168.250.251",
	"192.168.250.252",
	"192.168.250.253",
	"192.168.250.254",
	"192.168.220.50",
	"192.168.220.51",
	"192.168.220.52",
	"172.16.20.10",
	"172.16.20.20",
	"172.16.20.21",
	"172.16.20.30"
    ]
urlDKHC = [
	"http://dangkyhochieu.dientap.cnsc/egov/check.html",
	"http://dangkyhochieu.dientap.cnsc/egov/index.html",
	"http://dangkyhochieu.dientap.cnsc/egov/register.html",
	"http://dangkyhochieu.dientap.cnsc/egov/hoidap.html",
	"http://dangkyhochieu.dientap.cnsc/egov/php/login.php",
	"http://dangkyhochieu.dientap.cnsc/egov/php/create_captcha.php",
    ]

urlDNS = [
    'dangkyhochieu.dientap.cnsc',
    'fmc.dientap.cnsc',
    'oneshop.dientap.cnsc',
    'noithat.dientap.cnsc',
    'travelblog.dientap.cnsc'
    ]
ipDNS = [
    '192.168.250.250',
    '192.168.250.240',
    '192.168.250.245',
    '192.168.250.254'
    ]
# must use a valid user agent or sites will hate you
userAgent = ['Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) ',
	'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
	'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246',
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A',
	'Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36',
	'Mozilla/5.0 (CrKey armv7l 1.5.16041) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.0 Safari/537.36',
	'Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Xbox; Xbox One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.10586',
	'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
    ]
urlOneShop = ['http://oneshop.dientap.cnsc',
    'http://oneshop.dientap.cnsc/index.php/rtl-support',
    'http://oneshop.dientap.cnsc/index.php/free-extensions/page-builder',
    'http://oneshop.dientap.cnsc/index.php/free-extensions/easy-slider',
    'http://oneshop.dientap.cnsc/index.php/module-styles',
    'http://oneshop.dientap.cnsc/index.php/layout',
    'http://oneshop.dientap.cnsc/index.php/component/content/article?id=101&amp;Itemid=498',
    'http://oneshop.dientap.cnsc/index.php/free-extensions/form-builder',
    'http://oneshop.dientap.cnsc/index.php/painless-configuration',
    'http://oneshop.dientap.cnsc/index.php/module-styles?tmpl=component&amp;print=1&amp;page=',
    'http://oneshop.dientap.cnsc/index.php/docs-support',
    'http://oneshop.dientap.cnsc/index.php/layout/innerleft--center--right',
    'http://oneshop.dientap.cnsc/index.php/layout/main-content-only',
    'http://oneshop.dientap.cnsc/index.php/free-extensions/form-builder?tmpl=component&amp;print=1&amp;page=',
    'http://oneshop.dientap.cnsc/index.php/free-extensions/image-gallery',
    'http://oneshop.dientap.cnsc/index.php/product-tour?tmpl=component&amp;print=1&amp;page=',
    'http://oneshop.dientap.cnsc/index.php/free-extensions/joomla-management',
    'http://oneshop.dientap.cnsc/index.php/layout/left-center-right',
    'http://oneshop.dientap.cnsc/index.php/menu-styles',
    'http://oneshop.dientap.cnsc/index.php/menu-styles/tree-menu',
    'http://oneshop.dientap.cnsc/index.php/free-extensions/website-mobilizing',
    'http://oneshop.dientap.cnsc/index.php/menu-styles/main-menu',
    'http://oneshop.dientap.cnsc/index.php',
    'http://oneshop.dientap.cnsc/index.php/painless-configuration?tmpl=component&amp;print=1&amp;page=',
    'http://oneshop.dientap.cnsc/index.php/layout/left--innerleft--center',
    'http://oneshop.dientap.cnsc/index.php/layout/main-content-only?tmpl=component&amp;print=1&amp;page=',
    'http://oneshop.dientap.cnsc/index.php/easy-to-start',
    'http://oneshop.dientap.cnsc/index.php/rtl-support?tmpl=component&amp;print=1&amp;page=',
    'http://oneshop.dientap.cnsc/index.php/free-extensions/easy-slider?tmpl=component&amp;print=1&amp;page=',
    'http://oneshop.dientap.cnsc/index.php/layout/left--innerleft--center?tmpl=component&amp;print=1&amp;page=',
    'http://oneshop.dientap.cnsc/index.php/layout/left--center--innerright',
    'http://oneshop.dientap.cnsc/index.php/layout/center--innerright--right',
    'http://oneshop.dientap.cnsc/index.php/free-extensions/image-gallery?tmpl=component&amp;print=1&amp;page=',
    'http://oneshop.dientap.cnsc/index.php/image-gallery',
    'http://oneshop.dientap.cnsc/index.php/layout?tmpl=component&amp;print=1&amp;page=',
    'http://oneshop.dientap.cnsc/index.php/docs-support?tmpl=component&amp;print=1&amp;page=',
    'http://oneshop.dientap.cnsc/index.php/layout/left--center--innerright?tmpl=component&amp;print=1&amp;page=',
    'http://oneshop.dientap.cnsc/index.php/easy-to-start?tmpl=component&amp;print=1&amp;page=',
    'http://oneshop.dientap.cnsc/index.php/free-extensions/website-mobilizing?tmpl=component&amp;print=1&amp;page=',
    'http://oneshop.dientap.cnsc/index.php/layout/center--innerright--right?tmpl=component&amp;print=1&amp;page=',
    'http://oneshop.dientap.cnsc/index.php/menu-styles?tmpl=component&amp;print=1&amp;page=',
    'http://oneshop.dientap.cnsc/index.php/menu-styles/main-menu?tmpl=component&amp;print=1&amp;page=',
    'http://oneshop.dientap.cnsc/index.php/layout/innerleft--center--right?tmpl=component&amp;print=1&amp;page=','http://oneshop.dientap.cnsc/index.php/menu-styles/tree-menu?tmpl=component&amp;print=1&amp;page=','http://oneshop.dientap.cnsc/index.php/layout/left-center-right?tmpl=component&amp;print=1&amp;page=','http://oneshop.dientap.cnsc/index.php/free-extensions/joomla-management?tmpl=component&amp;print=1&amp;page='
    ]

urlNoiThat = [
    'http://noithat.dientap.cnsc',
    'http://noithat.dientap.cnsc/contact.html',
    'http://noithat.dientap.cnsc/index.html',
    'http://noithat.dientap.cnsc/about.html'
    ]
