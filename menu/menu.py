class Menu(object):
    def __init__(self):
        self.user = input("enter your name: ")
        if self._user_has_account():
            print("Welcome back()".format(self.user))
        else:
            self._prompt_user_for_account()

    def _user_has_account(self):
        Databas.find_one('blog', {'author': self.user}) is not None





    def run_menu(self):
        #User Read or Write blog?
        #if read:
            #list blogs in database
            #allow user to pick one
            #desplay posts
        #if write
            #check if user has blog
            #if they do, prompt to write post
            #if not, prompt to create new blog
        pass
