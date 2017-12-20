import random
import string

def code_generator(size=6, chars=string.ascii_lowercase + string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def create_shortcode(instance):
    new_code = code_generator()
    print(instance)
    print(instance.__class__)
    print(instance.__class__.__name__)
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(shortcode = new_code).exists()
    if qs_exists:
        return create_shortcode()
    return new_code
