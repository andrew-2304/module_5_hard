import time
class UrTube:
    def __init__(self, users = None, videos = [], current_user = None):
        if not users:
            self.users = []
        else:
            self.users = users
        self.videos = videos
        self.current_user = current_user

    def log_in(self, nickname, password):
        for user in self.users:
            if nickname == user.nickname and password == user.password:
                self.current_user = user

    def register(self, nickname, password, age):
        for user in self.users:
            if nickname in user.nickname:
                print(f'Пользователь {nickname} уже существует')
                return

        user = User(nickname, password, age)
        self.users.append(user)
        self.log_out()
        self.log_in(user.nickname, user.password)

    def log_out(self):
        self.current_user = None
    def add(self, *args):
        if args not in self.videos:
            for movie in args:
                self.videos.append(movie)
    def get_videos(self, text):
        list_movie = []
        for video in self.videos:
            if text.lower() in video.title.lower():
                list_movie.append(video.title)
        return list_movie

    def watch_video(self, movie):
        if not self.current_user:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return

        for video in self.videos:
            if movie != video.title:
                return

            if video.adult_mode and self.current_user.age < 18:
                print('Вам нет 18 лет, пожалуйста покиньте страницу')
                return

            if video.adult_mode and self.current_user.age < 12:
                print('Вам нет 12 лет, пожалуйста покиньте страницу')
                return

            if not video.adult_mode or video.adult_mode and self.current_user.age >= 18:
                for i in range(video.time_now, video.duration):
                    print(i + 1, end = '')
                    time.sleep(1)
                print('Конец видео')

    def __str__(self):
        return f'{self.videos}'

class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return f'{self.nickname}'

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return f'{self.nickname}'

    def __eq__(self, other):
        return self.nickname == other.nickname

    def __hash__(self):
        return hash(self.password)

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')