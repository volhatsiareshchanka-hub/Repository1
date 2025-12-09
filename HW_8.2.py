# 8.2 Декоратор проверки прав доступа

def require_role(required_role):
    def decorator(func):
        def wrapper(user, *args, **kwargs):
            if user != required_role:
                print(f"Error: Required role is '{required_role}', current role: 'user'")
                return "Access Denied"
            return func(user, *args, **kwargs)
        return wrapper
    return decorator

user_one = "user"
user_two = "admin"

@require_role("admin")
def admin_test(user, *args):
    print("Running admin test")
    return "Success"

print(admin_test(user_one))
print(admin_test(user_two)) 
