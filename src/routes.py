from views import get_all_accounts, login, signup

def add_url_rules(app):
    app.add_url_rule('/accounts', methods=['GET'], view_func=get_all_accounts)
    app.add_url_rule('/login', methods=['POST'], view_func=login)
    app.add_url_rule('/signup', methods=['POST'], view_func=signup)
