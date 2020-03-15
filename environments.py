import os

# for env_var in os.environ.keys():
#     print env_var

print('---------------------------------------')
print('Environment variable names and values :')
for env in sorted(os.environ.items()):
    print(env[0], '-->', env[1])


