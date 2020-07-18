import tweepy
import twitbot


def main():
    api_keys = ('',
                '')
    access_tokens = ('',
                     '')
    api = twitbot.getAPI(api_keys, access_tokens)
    menu = {
        0: 0,
        1: twitbot.followBack,
        2: twitbot.likeRetweet,
        3: twitbot.getFeed
    }
    option = True
    while option:
        try:
            option = int(input(
                'Choose from the following:\n0 to quit\n1 to follow back other users \n\
2 to like and retweet posts\n3 to view your homepage: '))
            if 0 <= option <= 3:
                if option:
                    menu[option](api)
            else:
                print('Invalid choice')
        except ValueError:
            print('Invalid choice')


if __name__ == '__main__':
    main()
