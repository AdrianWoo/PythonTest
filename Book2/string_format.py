favorite_laguage = ' Python '
print(favorite_laguage.rstrip()) # 去除后空格
print(favorite_laguage.lstrip()) # 去除前空格
print(favorite_laguage.strip()) # 去除前后空格

nostarch_url = 'https://nostarch.com'
nostarch_url = nostarch_url.removeprefix("https://") # 清楚前缀
print(nostarch_url)