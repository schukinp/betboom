from selene.api import s, have, browser


class HomePage:
    def open_url(self, url):
        """Open url"""
        browser.open_url(url)

    def check_username_is(self, username):
        """Check name in span.username is correct"""
        username_locator = s('span.username')
        username_locator.should(have.text(username))
