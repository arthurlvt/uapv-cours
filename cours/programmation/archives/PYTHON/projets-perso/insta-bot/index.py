from instapy import InstaPy
from instapy import smart_run

insta_username = 'arthur_.lvt'
insta_password = 'Insta.Arthur-2'

session = InstaPy(
    username = insta_username,
    password = insta_password,
    headless_browser = False # A modifier pour être invisible (True)
)

with smart_run(session):
    # Le code suivant permet de définir l'algorithme en fonction du nombre d'abonnés
    session.set_relationship_bounds(
        enabled = True,
        delimit_by_numbers = True,
        max_followers = 100000000,
        min_followers = 50,
        min_following = 5
    )

# La ligne suivante va permettre d'éviter les photos avec l'hashtag NSFW
session.set_dont_like(['nsfw'])

# Aimer les posts selon les hashtags
session.like_by_tags(['bot', 'programming', 'instagram', 'car', 'f1', 'f4'], amount = 2)

# Commenter chaque posts liké aléatoirement
session.set_do_comment(enabled = True, percentage = 70)
session.set_comments([
    	u'Ça à l\'air bon ! :heart_eyes:',
		u'Super photo ! :wink:',
		u'Magnifique !! :heart_eyes:',
		media = 'Photo'
])