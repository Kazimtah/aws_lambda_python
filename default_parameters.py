from datetime import date

def get_weekday():
    """
    Docstring for get_weekday, it doesn't need the parameter, it will just return the days of the week of your local machine.
    """
    return date.today().strftime("%A")

def create_new_post(post, weekday=get_weekday()):
    """
    Docstring for create_new_post
    
    :param post: will take a dictionary as it is paramaters
    :param weekday: which is a default parameters that takes it's value from a function call of get_weekday().
    """
    post_copy = post.copy()
    post_copy['created_on_weekday'] = weekday
    return post_copy

intial_post = {
    'id': 243,
    'author': 'Bodgan'
}

post_weekday = create_new_post(intial_post)
print(post_weekday)